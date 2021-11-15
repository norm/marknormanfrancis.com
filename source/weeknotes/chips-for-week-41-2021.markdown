```
title = "Chips for week 41, 2021"
published = 2021-10-18T09:16:33Z
updated = 2021-11-15T07:05:06Z
updated_reason = 'Fixing tshirt date typo'
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 41]
tag = [
    'repo-hasworn',
    'weekchips',
]
image = 'https://mnf.m17s.net/weeknotes/2021/41/chips.jpg'
summary = """
  I did a few small bits of work on hasworn, and made a silly video.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/weeknotes/2021/41/chips.chips.jpg'

[twitter]
account = "cackhanded"
contains_tweet = [
    '',
]
retweets = 0
favourites = 0
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='https://mnf.m17s.net/weeknotes/2021/41/chips.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down three goals:

1. Add one season two Ted Lasso episode to GIFs — ❌
1. Start on music library project — ❌
1. Improve using hasworn — ✅


## Update

I started the week with a little housekeeping on the site, publishing
the sad weeknote [summary of the past month][w], then fixing a couple of
tiny bugs in the site. The automatic updates had stopped because of a new
major version of tweepy came out, and I hadn't [pinned the version][p],
and I realised the “quick” publish part of the site generation workflow
wasn't generating all the pages it could due to me getting a
[naming convention wrong][n].

My goals were probably a little ambitious, but I did at least do one.
I spent an hour each morning on a handful of small updates to hasworn:

* fixed a bug where in the year in which a tshirt was first worn,
  the tshirt would [repeatedly be annotated][ra] “first worn”
* improved the hasworn user interface by [styling it][bs],
  [showing previous wearings][sh], and having a page showing
  [all previously worn items][pw] to make it much easier to rewear an item
* added [`<title>` elements][te] to all pages (I used to make websites
  *professionally* donchaknow)
* added count of tshirts [last worn in a year][lw] to the year pages
  (excluding the current year, because by definition…)
* added a [tweetable summary][tw] of a wearing, so I don't have to write
  them by hand
* fixed the homepage to support [low numbers][ln] of wearings (not a problem
  for me now, but I noticed it when testing rewinding time)

And over the weekend I finished something I'd been noodling at on and off
for a couple of months, an [animation][an] of my most-worn tshirts across the
lifetime of my data.

<iframe
    width="560"
    height="315"
    src="https://www.youtube-nocookie.com/embed/ZD1lFO3Z6tU"
    frameborder="0"
    allow="accelerometer; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
></iframe>

This was inspired by not noticing that my long-time most worn tshirt
(previously [Explorer][ex], most worn from 2014-07-28) changed in February to
be [Firewatch][fw] (most worn from 2021-02-04 through today). Also, my first
most worn was [Thunder-King][tk] (starting at a count of 5 wearings, it was
most worn from 2013-10-25 through 2014-07-27).

Although, having said all that I **know** that my actual most worn tshirt is
actually [Hard core pawn][hc] which I wore **a lot** in the 90s and 00s,
before records began. I had far fewer tshirts to choose from, and it
definitely got worn every two or three weeks. Look at the fraying and holes
around the neck, that tshirt **Has. Been. Worn.**


[w]: /weeknotes/chips-for-weeks-37-38-39-40-2021
[p]: https://github.com/norm/marknormanfrancis.com/commit/62d8ae1cf04eec0b9300b2adf6e6f966bb8de7db
[n]: https://github.com/norm/marknormanfrancis.com/commit/f089f6b9861ac893fd4e2beb18fe9c9498b886d8
[ra]: https://github.com/norm/hasworn/commit/3ff91a8c3eb608a473fd17f5c280d54be54c30fc
[bs]: https://github.com/norm/hasworn/commit/843d5996032bd2aa594a556105f913109638d29e
[sh]: https://github.com/norm/hasworn/commit/f68ff70c228a6aae77422e2f9c022f6f3b3857e3
[pw]: https://github.com/norm/hasworn/commit/1e45d47834d404b89fab2107cce76d4b2c02c6c2
[te]: https://github.com/norm/hasworn/commit/37335bd6b02418c8469cb4fae3de11af524f913e
[lw]: https://github.com/norm/hasworn/commit/98b85488902f60deba1ba33efc7594f663ac9280
[tw]: https://github.com/norm/hasworn/commit/d4a67de2555d3c167fbfc48c00afaa84bfd1a145
[ln]: https://github.com/norm/hasworn/commit/48d176de617b3f1d5ea8a7ec1a13fd5cf58013c6
[an]: https://github.com/norm/hasworn/commit/40d286a9a1afc39d692416db814c604fe1b329ea
[ex]: https://norm.hasworn.com/tshirts/explorer
[fw]: https://norm.hasworn.com/tshirts/firewatch
[tk]: https://norm.hasworn.com/tshirts/thunder-king
[hc]: https://norm.hasworn.com/tshirts/hard-core-pawn
