```
tweet_id = "1386543537479634944"
type = "tweet"
title = "Chips for week 16, 2021"
published = 2021-04-26T04:51:54Z
retweets = 0
favourites = 0
source = "twitter"
twitter_account = "cackhanded"
source_url = "https://twitter.com/cackhanded/status/1386543537479634944"
tag = [ "weekchips",]
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='http://mnf.m17s.net/2021/04/26/Ez39_ZXWUAYEAe2.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down four goals for the week:

1. Increase Ezio content buffer — ✅
1. Improve publishing — ✅
1. Fix 404s, implement 301s — both ✅ and ❌
1. Add more old content — ❌

I also added a "stretch goal" of adding more Eurovision data, which once
again I ignored.


## Update

The very first thing I did last week was the [weekchips write up][wc]. The
second thing was go back to bed, because I lucked out in the
[side-effects][se] lottery with my AstraZeneca vaccination:

> Side effects may include:
> 
> * a sore arm ✅
> * a headache ✅
> * feeling tired ✅
> * flu-like symptoms ✅
> 
> Heavy sigh.

But then I woke up Tuesday morning feeling normal again, so I only had a
24-hour reaction to it. Tuesday I cracked on improving the publishing on
this site, which meant more automatic publishing. I already collect videos
that I publish on YouTube overnight, and GIFs that I publish on that site,
and I'd like to do this with tweets. But I don't want to archive every
single tweet, that seems overkill.

I started with a script that autopublishes [based on hashtag][ht], and the
first two hashtags I've identified are [#itsy][itsy] and [#roxy][roxy], our
cats.

I added a script that autopublishes [based on likes][lik]. Not by anyone, only
those liked by me using a secondary twitter account ([@mnfpublishing][mnfp])
to mark tweets and threads that I would like to archive.

Now, when I import a tweet I try to use the text of the tweet as the title
of the post. When it is a thread, such as [my trip to the hospital][surg])
or just a long tweet, that might not be practical so I arbitrarily decided
to cut at ten words. If the first tweet has more, the post ends up titled
"Undefined (timestamp)".

I wanted to catch these and other errors before automatically pushing new
content to the site. For example, last week I went looking through the logs
for 404 errors on the site and found a lot of links to date-based archives
such as `/2021/4/` instead of `/2021/04`, which I traced that back to the
[archive index][arc] page. And although I've now [fixed that bug][flb] in
Flourish, having a brake to make sure it doesn't reoccur is a good idea. Plus
it gives me a place to inspect for any other problems later.

I did then spend a lot of wasted time debugging that brake, as you can
see in [Tuesday's activity][tues]. To summarise, I was looking for broken
links in the generated content using `ag -l /...././`. And it took me *far
too long* to realise that for whatever reason, the `-l` flag to `ag` wasn't
reporting filenames. In the end I replaced the silver searcher with ripgrep,
and [now it works][check].

Wednesday I finished off chapter 5 of my [Ezio content][ez], so (for now) I am
running with a two week buffer. I hope to extend that, as occasional pain in
my wrists makes it difficult to hold a PS4 controller for long, and I'm trying
to keep to a two videos per week routine. I have 14 in the pocket from
[Horizon Zero Dawn][hzd] so in the worst case I don't have to make a video for
seven weeks, but now I've started releasing Assassin's Creed II I'd like to
keep to one of each per week.

I also [switched my support scripts][subs] to expect `.srt` format subtitles
instead of `.sbv`, as I discussed in [last week's update][wc], tidied up a
few other uncommitted changes, and made sure I had backups of important files
such as the Davinci Resolve project database.

To further illustrate that whilst I might plan out my week, I don't feel
[beholden to the plan][bc], on Thuesday and Friday I ignored my goals beyond [one quick change][oqc] to fix the archive page causing 404s.

Instead I spent some time reading and testing how to index the content of my
site using [xapian][xp] so I could add a decent search experience. I have it
working on the command-line, and am now building a web interface to the search
results.

And then on Sunday, it was the [perfect date][pd].


[wc]: /2021/04/19/chips-for-week-15-2021
[se]: https://twitter.com/cackhanded/status/1384105759403765763
[hzd]: https://www.youtube.com/playlist?list=PL0lW90IMJShJZkfyJEZtyWArFJXCJ2U1Z
[ez]: https://www.youtube.com/playlist?list=PL0lW90IMJShLky0HULzKr1rtkjrreblW-
[ht]: https://github.com/norm/marknormanfrancis.com/commit/3a1e9d0e10d005728ee9bdb5a2093a7d516f2280
[itsy]: /tags/itsy/
[roxy]: /tags/roxy/
[lik]: https://github.com/norm/marknormanfrancis.com/commit/07ae99a4e3ed7461b0b2f12825683f8e0eae055a
[mnfp]: https://twitter.com/mnfpublishing
[surg]: /2019/06/23/off-to-the-hospital
[arc]: /archives
[flb]: https://github.com/norm/flourish/commit/772b881c9121900c912745481208972b9961ee91
[tues]: https://marknormanfrancis.com/2021/04/20/github_activity
[check]: https://github.com/norm/marknormanfrancis.com/commit/849dbde19643c6f1b2654e7612282971aa08725c
[subs]: https://github.com/norm/game_shows_support/commit/739b4581b319c2efd770c1d3d99ddc297ba2feed
[bc]: https://gifs.cackhanded.net/airplane/hes-in-charge
[oqc]: https://github.com/norm/marknormanfrancis.com/commit/129c570d708a0770359c566c55fb091447078f74
[xp]: https://xapian.org
[pd]: https://gifs.cackhanded.net/tags/perfect-date/
