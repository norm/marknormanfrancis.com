```
title = "Chips for week 11, 2021"
published = 2021-03-22T10:24:59Z
origin = "twitter-cackhanded"
type = "tweet"
original_url = "https://twitter.com/cackhanded/status/1373943783667208193"
twitter_account = "cackhanded"
tweet_id = "1373943783667208193"
retweets = 0
favourites = 1
tag = [ "weekchips",]
```

Another week, and I’m back to
[stacking chips](/2020/06/19/my-week-in-poker-chips).
Last week’s [chips][m] looked like this:

<p class='image'><img src='http://mnf.m17s.net/2021/03/22/ExE6lKxXAAY1xEU.jpg' alt=''></p>

## Reflection

It's been [six months](/2020/08/22/chips-for-week-34-2020) since my last
[#weekchips](/tags/weekchips/) post, during which time I was basically doing
one of two things on any given day: nothing, or editing video.

Okay, that's not entirely true, but for more weeks than not I would've had a
stack of white or pink chips and nothing else. That wouldn't have been
interesting so I didn't bother with the chips, and the knock-on effect from
that was that I also didn't bother writing anything.

And that was a mistake.

For one thing, I've learned some things about editing videos, and using tools
to overlay content. Nothing groundbreaking, but I could've been writing about
my discoveries. Or about the many tricks I've been employing to make my videos
less boring, or smoother to watch from a non-livestream perspective. I'm
hoping to fix that with my next game, and to write up at least a few
paragraphs on anything new in each video as it is published, rather than me
trying to retrospectively remember what I could possibly write about for each
now-published video.

## Update

This past week I've been preparing for Eurovision.

Specifically I've been going through previous Eurovision contests to collate
the acts and scores, to create a [repository of Eurovision data][ed] that I
can then use to start to add historical information to
[the site promoting][drink] my live Eurovision Drinking Game twitter
experience.

As the most error-prone part was going to be going through hundreds of
scoring data points, I've written a script to [fetch that][f] and create
the data files for any given show. I then go through each by hand, add the
artists/singers and try to find some basic information about each (name,
dates of birth/death, country they are from).

I've also added [a set of tests][t] to ensure the data makes sense and no
artists, singers, or songs are accidentally duplicated or reusing IDs (I'm
using slugs made from their names, so there's a likely chance of some
accidental duplication).

So far I've worked through [1956 to 1969][pr6]. One of my goals for week 12 is
to bring that up to at least 1989.

And I finished making more [Innerspace GIFs][isg] for [Simon Willison][sw] that will
be published once per week on my [gifs site][gifs] over the next few months.


[drink]: http://eurovisiondrinking.com
[ed]: https://github.com/norm/eurovision_data
[f]: https://github.com/norm/eurovision_data/blob/main/fetch_scoreboard.py
[gifs]: https://gifs.cackhanded.net
[isg]: https://github.com/norm/gifs.cackhanded.net/commit/703f33a5ede6c99c33b5403661fdb7710ab8e754
[m]: /2020/08/22/my-weekchips-markers
[pr6]: https://github.com/norm/eurovision_data/pull/6
[sw]: https://twitter.com/simonw/status/1367836107199553541
[t]: https://github.com/norm/eurovision_data/blob/main/test_integrity.py
