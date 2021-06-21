source keys
===========

This documents the standard keys used in sources.

## Flourish baked-in keys 

There are some keys with baked-in meanings for Flourish.

  * **title** — The title of the entry.
  * **published** — The date and time the entry was first published.
  * **updated** — The date and time the content of the entry was last updated.
    Modifying the metadata (eg adding a `subject`) or the formatting
    (eg replacing already formatted HTML with Markdown; rewrapping paragraphs
    to a given line-length) does not count as updating, only making changes
    to the actual content.
  * **previous_slug** — When an entry changes location in the site, adding
    the previous slug to this list will have Flourish redirect the old
    path to the new.

```toml
title = "Chips for week 23, 2021"
published = 2021-06-14T06:03:07Z
previous_slug = [
  '/2021/06/14/chips-for-week-23-2021',
]
```

## Site-specific keys

There are more keys that have specific meanings as used by the `generate.py`
and Sectile templates of this site.

Keys that classify and the content of the entry:

  * **origin** — Where the content came from. The value for this is the
    second Sectile dimension. Some example values:
      * `mnf` for original content on this site
      * `foursquare` for checkins syndicated from Foursquare
      * `instagram` for content originally posted to Instagram
  * **origin_link_text** — Text to use in a link back to the original content.
  * **origin_link_url** — URL pointing to the original content.
  * **type** — What kind of content to expect (ie how to render the page).
    The value for this is the third Sectile dimension. Some example values:
      * `article` for prose
      * `photo` for photographic content with no or minimal description
      * `video` for YouTube videos etc
  * **subject** — The general term to describe the content of the entry.
    Used to construct navigation and index pages.
  * **topic** — A smaller area of the **subject** matter, if needed.
  * **tag** — A list of concepts/subjects that appear in the entry (eg
    keywords, people). A way of linking disparate content together if
    needed.

```toml
origin = "mnf"
type = "article"
subject = "weeknotes"
tag = [ "weekchips", "repo-flourish", "repo-sectile", ]
```

Keys used to enrich the presentation of the entry:

  * **updated_reason** — A free text description of what changed in the
    last update, shown on content pages alongside the updated date.
  * **summary** — A brief synopsis of the content of the entry, suitable
    for adding to index pages that don't include the whole entry.
  * **image** — The primary image for an entry.
  * **thumbnail** — A table containing the URLs of different sizes of
    thumbnails should an index want a smaller version of the primary image.

```toml
image = 'https://mnf.m17s.net/2021/06/14/E30kMQYXoAU19Eg.jpg'
summary = """
  I improved the development experience behind the templating library
  that builds this website, and started restoring the last of the 
  missing content.
"""

[thumbnail]
200 = "https://mnf.m17s.net/2021/06/14/E30kMQYXoAU19Eg.200.jpg"
chips = 'https://mnf.m17s.net/2021/06/14/E30kMQYXoAU19Eg.chips.jpg'
```

  * **twitter** — A table containing information about tweets that
    form, or are part of, the entry.
      * **first_tweet** — The ID of the first tweet that makes this entry,
        if it is a pure Twitter import (as opposed to using a tweet in a
        longer prose article).
      * **last_tweet** — The ID of the last tweet that makes this entry.
        Presence of this turns the entry from an archived tweet (eg a photo
        or short pithy comment) into an archived twitter thread.
      * **contains_tweet** — A list of IDs of tweets that are a part of
        the entry.
      * **retweets** — The total of retweets all of the tweets in this entry
        have received.
      * **favourites** — The total of favourites (likes, hearts, whatever they
        are this week) all of the tweets in this entry have received.

```
[twitter]
contains_tweet = [ "1404318463091478528",]
retweets = 0
favourites = 1
```

### Content-specific keys

Where content is being pulled from a service that provides a lot of data
that we would want stored (as opposed to Twitter, where we look up the
tweets from the IDs as they are used to generate content), that should be
stored in a source-specific table. Some in use, include:

  * **foursquare**
  * **youtube**
