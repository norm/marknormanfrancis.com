from datetime import timedelta
import os
import time

from django.utils.text import slugify
import pytz
import toml
import tweepy

from lib import update_content, strip_trailing_hashtags, strip_links
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

    def create_source_from_tweet(self, id, extra):
        tweets = self.get_tweets_from_id(id, extra)

        try:
            created = extra['published']
        except KeyError:
            created = timestamped(tweets[0].created_at)

        updated = timestamped(tweets[-1].created_at)
        date = created.strftime('%Y/%m/%d')

        body = ''

        # FIXME retweets
        # FIXME attached images/video
        # FIXME add original data as attachment

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
                title = 'Tweet at %s' % created.strftime('%H:%M:%S').lower()
            # zero words and it's also not a good title
            if len(title.split()) == 0:
                title = 'Untitled tweet at %s' % \
                    created.strftime('%H:%M:%S').lower()
                tags.add('fixme')
        slug = slugify(title)

        tags.update(
            slugify(word[1:].lower())
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
            if text == title:
                tweets[0].full_text = ''
            if text == '':
                tweets[0].full_text = ''
            try:
                _ = tweets[0].quoted_status
                tweets[0].full_text = ' '
            except AttributeError:
                pass

        previous_time = created
        for tweet in tweets:
            time = timestamped(tweet.created_at)
            if time - previous_time > timedelta(hours=1):
                body += timestamp_header(time, previous_time)
            previous_time = time
            body += self.tweet_to_markdown(tweet, date)

        retweets = 0
        favourites = 0
        for tweet in tweets:
            retweets += int(tweet.retweet_count)
            favourites += int(tweet.favorite_count)
            if 'hashtags' in tweet.entities:
                for tag in tweet.entities['hashtags']:
                    tags.add(slugify(tag['text']))

        if 'remove_tags' in extra:
            for tag in extra['remove_tags']:
                tags.remove(tag)

        post = {
            'tweet_id': tweets[-1].id_str,
            'type': 'tweet',
            'title': title,
            'published': created,
            'retweets': retweets,
            'favourites': favourites,
            'source': 'twitter',
            'twitter_account': tweets[-1].author.screen_name,
            'source_url': 'https://twitter.com/%s/status/%s' % (
                tweets[-1].author.screen_name,
                tweets[-1].id_str,
            ),
            'tag': sorted(tags),
        }

        if created != updated:
            post['updated'] = updated
        if len(tweets) > 1:
            post['thread_tweet_ids'] = sorted([
                tweet.id
                for tweet in tweets
            ])

        output = '```\n%s```\n\n%s' % (toml.dumps(post), body)
        output_file = 'source/%s/%s.markdown' % (date, slug)
        update_content(output_file, output)

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
                        slugify(section['text'])
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
                    print('++', destination)
                markdown += "<p class='image'><img src='%s' alt=''></p>\n\n" % (
                    'http://%s/%s' % (BUCKET, destination)
                )

        return markdown


