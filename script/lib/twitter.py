from datetime import timedelta
import os
import time

from django.utils.text import slugify
import pytz
import toml
import tweepy

from lib import (
    get_body_from_markdown,
    strip_links,
    strip_trailing_hashtags,
    update_content,
    tagify,
    make_thumbnail,
)
from lib.bucket import Bucket

BUCKET = 'mnf.m17s.net'


def escape_newlines(text):
    text = text.replace('\n', '  \n')       # preserve newlines as <br>s
    text = text.replace('  \n  \n', '\n\n') # return to paragraphs
    return text


def timestamped(stamp):
    if not stamp.tzinfo:
        stamp = pytz.timezone('UTC').localize(stamp)
    return stamp


def timestamp_header(now, previous):
    # FIXME 25th, 7pm
    if now.year != previous.year:
        return '## %s\n\n' % now.strftime('%A %-d %B %Y, %H:%M')
    elif now.month != previous.month:
        return '## %s\n\n' % now.strftime('%A %-d %B, %H:%M')
    elif now.day != previous.day:
        return '## %s\n\n' % now.strftime('%A %-d, %H:%M')
    else:
        return '## %s\n\n' % now.strftime('%H:%M')


class Twitter:
    def __init__(self):
        auth = tweepy.OAuthHandler(
            os.environ['CONSUMER_KEY'],
            os.environ['CONSUMER_SECRET'],
        )
        auth.set_access_token(
            os.environ['ACCESS_TOKEN'],
            os.environ['ACCESS_TOKEN_SECRET'],
        )
        self._api = tweepy.API(auth)
        self.bucket = Bucket(BUCKET)

    def user_timeline(self, *args, **kwargs):
        return self._api.user_timeline(*args, **kwargs, tweet_mode='extended')

    def get_favourites_for(self, screen_name, tweet_mode='extended'):
        return self._api.favorites(screen_name=screen_name)

    def create_source_from_tweet(self, id, extra={}):
        tweets = self.get_tweets_from_id(id, extra)

        try:
            created = extra['published']
        except KeyError:
            created = timestamped(tweets[0].created_at)

        updated = timestamped(tweets[-1].created_at)
        date = created.strftime('%Y/%m/%d')

        # FIXME retweets
        # FIXME attached images/video
        # FIXME add original data as attachment

        body = ''
        content = 'tweet'
        tags = set()
        if 'tag' in extra:
            for tag in extra['tag']:
                tags.add(tag)

        if 'title' in extra:
            title = extra['title']
        else:
            title = tweets[-1].full_text
            title = strip_links(title)
            title = strip_trailing_hashtags(title)
            # more than about 10 words and it's not a good title
            if len(title.split()) > 10:
                title = 'Undefined %s' % created.strftime('%H:%M:%S').lower()
            # zero words and it's also not a good title
            if len(title.split()) == 0:
                title = 'Untitled tweet at %s' % \
                    created.strftime('%H:%M:%S').lower()
                tags.add('fixme')

        output_file = 'source/%s/%s.markdown' % (date, slugify(title))
        if 'slug' in extra:
            output_file = 'source/%s.markdown' % extra['slug']

        tags.update(
            tagify(word[1:])
                for word in title.split()
                    if word.startswith('#')
        )
        if 'tags' in extra:
            for tag in extra['tags']:
                tags.add(tag)

        if len(tweets) == 1:
            # strip text before converting to Markdown if the title and
            # the body will match, so there's no unnecessary repetition,
            # except if it is a quoted tweet (we still want the quote to appear)
            text = strip_trailing_hashtags(strip_links(tweets[0].full_text))
            if 'ignore_body' in extra:
                tweets[0].full_text = ''
            if text == title:
                tweets[0].full_text = ''
            if text == '':
                tweets[0].full_text = ''
            try:
                _ = tweets[0].quoted_status
                tweets[0].full_text = ' '
            except AttributeError:
                pass

            # is it a photo?
            if 'type' in extra and extra['type'] == 'photo':
                content = 'photo'
            else:
                if 'media' in tweets[0].entities and len(text.split()) < 10:
                    content = 'photo'
        else:
            content = 'thread'

        previous_time = created
        images_dir = 'twitter/%s' % tweets[0].id_str

        for tweet in tweets:
            time = timestamped(tweet.created_at)
            if time - previous_time > timedelta(hours=1):
                body += timestamp_header(time, previous_time)
            previous_time = time
            body += self.tweet_to_markdown(tweet, images_dir)

        if 'edited_body' in extra and extra['edited_body']:
            body = get_body_from_markdown(output_file)

        retweets = 0
        favourites = 0
        for tweet in tweets:
            retweets += int(tweet.retweet_count)
            favourites += int(tweet.favorite_count)
            if 'hashtags' in tweet.entities:
                for tag in tweet.entities['hashtags']:
                    tags.add(tagify(tag['text']))

        if 'remove_tags' in extra:
            for tag in extra['remove_tags']:
                tags.remove(tag)

        post = {
            'title': title,
            'published': created,
            'origin': 'twitter-%s' % tweets[-1].author.screen_name,
            'type': content,
        }

        if content == 'photo':
            photo = tweets[0].extended_entities['media'][0]['media_url_https']
            filename, _ = os.path.splitext(os.path.basename(photo))
            post['image'] = 'https://%s/%s/%s.jpg' % (
                self.bucket.bucket_name,
                images_dir,
                filename,
            )
            new, thumb = make_thumbnail(
                    photo,
                    200,
                    '%s/%s' % (images_dir, filename),
                    self.bucket,
                )
            if 'thumbnail' in extra:
                post['thumbnail'] = extra['thumbnail']
            else:
                post['thumbnail'] = {}
            post['thumbnail']['w200'] = thumb
            if new:
                print('++', thumb)

        if tags:
            post['tag'] = sorted(tags)
        post['twitter'] = {
                'account': tweets[0].author.screen_name,
                'first_tweet': tweets[0].id_str,
                'retweets': retweets,
                'favourites': favourites,
            }

        if created != updated and updated - created > timedelta(hours=1):
            post['updated'] = updated
        if len(tweets) > 1:
            sorted_tweets = sorted([
                tweet.id_str
                    for tweet in tweets
            ])
            if len(sorted_tweets) > 2:
                post['twitter']['contains_tweet'] = sorted_tweets
            post['twitter']['last_tweet'] = sorted_tweets[-1]

        output = '```\n%s```\n\n%s' % (toml.dumps(post), body)
        update_content(output_file, output)
        return post

    def get_tweet(self, id):
        return self._api.get_status(id, tweet_mode='extended')

    def get_tweets_from_id(self, id, extra):
        tweets = []
        while True:
            try:
                tweet = self.get_tweet(id)
                break
            except tweepy.error.RateLimitError:
                print('   hit rate limit, sleeping')
                # FIXME use the rate limit endpoint to work out how long to sleep
                time.sleep(60)
        tweets.insert(0, tweet)
        in_reply_to = tweet.in_reply_to_screen_name
        original_author = tweet.author.screen_name

        while in_reply_to == original_author:
            tweet = self.get_tweet(tweet.in_reply_to_status_id)
            tweets.insert(0, tweet)
            if 'stop_at' in extra and extra['stop_at'] == tweet.id_str:
                break
            in_reply_to = tweet.in_reply_to_screen_name
        return tweets


    def tweet_to_markdown(self, tweet, image_subdir):
        sections = []
        markdown = ''

        if 'urls' in tweet.entities:
            for url in tweet.entities['urls']:
                sections.append(url)
        if 'user_mentions' in tweet.entities:
            for mention in tweet.entities['user_mentions']:
                sections.append(mention)
        if 'hashtags' in tweet.entities:
            for tag in tweet.entities['hashtags']:
                sections.append(tag)

        quote = None

        # tweepy really tries my patience at times,
        # some parts are subscriptable while others are not
        try:
            quote_url = tweet.quoted_status_permalink['expanded']
            quote = '> %s\n> \n> — %s [`@%s`](%s) %s\n\n' % (
                tweet.quoted_status.full_text,
                tweet.quoted_status.user.name,
                tweet.quoted_status.user.screen_name,
                tweet.quoted_status_permalink['expanded'],
                tweet.quoted_status.created_at,
            )
        except AttributeError:
            quote_url = None
            quote = ''
            pass

        text_from = 0
        if tweet.full_text:
            for section in sorted(sections, key=lambda s: s['indices'][0]):
                start = section['indices'][0]
                markdown += escape_newlines(tweet.full_text[text_from:start])
                if 'screen_name' in section:
                    # ignore @blah at the very start of a tweet
                    # it's almost certainly not helpful
                    if section['indices'][0] != 0:
                        markdown += '[`@%s`](%s)' % (
                            section['screen_name'],
                            'https://twitter.com/%s' % section['screen_name'],
                        )
                if 'display_url' in section:
                    if section['expanded_url'] == quote_url:
                        if tweet.display_text_range[1] <= section['indices'][1]:
                            # makes this a quote tweet, not just a link to a tweet
                            # quoted tweet text comes before the tweet text
                            markdown = quote + markdown
                        else:
                            markdown += '\n\n' + quote
                    else:
                        markdown += '[`%s`](%s)' % (
                            section['display_url'],
                            section['expanded_url']
                        )
                if 'text' in section:
                    markdown += '[#%s](/tags/%s/)' % (
                        section['text'],
                        tagify(section['text'])
                    )
                text_from = section['indices'][1]
            if text_from < tweet.display_text_range[1]:
                markdown += escape_newlines(tweet.full_text[text_from:tweet.display_text_range[1]])
            markdown += '\n\n'

        if 'media' in tweet.entities:
            for media in tweet.extended_entities['media']:
                destination = '%s/%s' % (
                    image_subdir,
                    os.path.basename(media['media_url_https']),
                )
                uploaded = self.bucket.upload_file(
                    media['media_url_https'],
                    destination,
                    check_digest = False,
                )
                if uploaded:
                    print('++ https://%s/%s' % (BUCKET, destination))
                markdown += "<p class='image'><img src='%s' alt=''></p>\n\n" % (
                    'https://%s/%s' % (BUCKET, destination)
                )

        return markdown


