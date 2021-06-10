```
tweet_id = "1384000122728550408"
type = "tweet"
title = "Chips for week 15, 2021"
published = 2021-04-19T04:25:17Z
retweets = 0
favourites = 0
source = "twitter"
twitter_account = "cackhanded"
source_url = "https://twitter.com/cackhanded/status/1384000122728550408"
tag = [ "weekchips",]
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='http://mnf.m17s.net/2021/04/19/EzT0xCXUYAIrl8W.jpg' alt=''></p>

## Reflection

At the start of the week, I wrote my high-level goals down:

1. More Eurovision data — ❌
1. Another Ezio chapter — ✅
1. Analyse weblogs — ✅
1. Improve publishing — ❌

Once again, I have avoided adding anything to my Eurovision data collection
(and now it is drawing perilously close, so that'll end either with a mad
scramble, or me punting it to 2022 and beyond).

I finished another Ezio chapter, and have a second almost finished apart from
adding music to the last 20 minutes.

And I started performing some analysis on the raw logs I get from Amazon
CloudFront.

Two for four, not bad.

And, as the picture illustrates, I've had my first AstraZeneca Covid-19
vaccination. Pretty happy about that, can't lie.

## Update

I spent Monday putting together the rough cut of the next Ezio chapter. This
is a quicker pass where I go through the raw footage, find any sections (a
full run-through of a mission) or elements (a musical sting or loop, a second
attempt at a particular part of a mission) I am likely to use, and put them
onto a timeline in the right order. Then started looking into tools that
could be used to make reports from web logs (instead of the now much more
common practice of using JavaScript and trying to determine everything about
everyone).

Tuesday morning I started polishing up the footage, cutting between sections
so it looks seamless, making notes of anything that might need recapturing,
and what database entries to add to the end of the video. In the afternoon, I
wrote some code to pull down logs, filter them for useful content, and query
them for the most common 404 pages (which was my immediate need, and why I'm
doing this in the first place).

Wednesday I puttered around the house in the morning, then crashed out after
lunch and snoozed the day away.

Thursday and Friday basically video editing, polishing any cuts between
footage, adding music, creating the audio for the database entries, making
thumbnails, all the little tasks that take [the other 80% of the time][pp];
and having a solid *my word I am dumb* moment.

As I [wrote on Twitter][dumb], in six months of making gaming videos, I’ve
been making sure each video has decent, hand-edited captions on YouTube. I
extract the audio from the final footage and [run it through][cap] Amazon’s
transcriber. This gives me captions that aren't exactly great, but manually
correcting something is quicker than typing everything from scratch. As an
example, look at the [raw captions][raw] for Chapter 54 of my Horizon Zero
Dawn content. It is a little eager to find words in sound effects, so there's
a lot of single entries with "what", "get", "okay", and my favourite "Q."

I would then watch the video back whilst manually correcting words, and adding
anything missing. See the [intermediate step][prep] for the same chapter,
where I've removed many spurious entries, corrected spellings, and combined
entries where there is a pause but it looks unnatural (well, to me) to have it
as two captions not one that just stays on screen longer.

Once that was done, I would finally upload it to YouTube and use their
captioning interface to double-check everything in place, and to adjust 
timings as necessary. See the [finalised content][cooked] for the same
chapter, it is mostly timing changes.

Several times I’ve idly thought there must be a macOS program that edits
subtitles against a video source. Easier to drag things around, edit, and
create/delete individual entries when it is in context as an actual caption
rather than a text editor and video player side-by-side. I’d search, but I
wouldn’t find anything.

On Thursday, more than six months after publishing my first video that had
captions, it occurred to me. I can do it in [Davinci Resolve][dvr]. The video
editing suite I’ve been using all this time. It can be used to make, edit, and
export subtitles. I had been *so focused* on the solution being a dedicated
subtitle tool, I had neglected to think wider, to think "I wonder if the video
editor can do subtitles, makes sense that it could, right?". It can.

A deluxe, premium, gold-plated, high-end, top of the range, select, leather
trimmed, five-star, luxurious, Tesco's finest of a facepalm moment.

So I spent Friday learning how to update captions on my next two videos using
a native macOS interface that certainly has it's quirks but is so much easier
and quicker than trying to use YouTube's controls. A small downside is that
I've been working with `.sbv` format captions until now, but Resolve wants to
use `.srt` format, so I'll need to update my tooling a smidge.

Then I spent my weekend mornings making a whole bunch of [Miss Congeniality
GIFs][mc] for my site, ready for the perfect date.


[pp]: https://en.wikipedia.org/wiki/Pareto_principle
[dumb]: https://twitter.com/cackhanded/status/1382729678256013313
[cap]: https://github.com/norm/game_shows_support/blob/main/bin/captions
[raw]: https://github.com/norm/game_shows_support/commit/755bdabdb0562c6b2f607e959ef6f6a4179c6085
[prep]: https://github.com/norm/game_shows_support/commit/0f3acb6dfa6918cce27f7c0c7c7883c9d3d77c45
[cooked]: https://github.com/norm/game_shows_support/commit/e4a0ac3e547210c15f9817dee47de5323c52f417
[dvr]: https://www.blackmagicdesign.com/products/davinciresolve/
[mc]: https://github.com/norm/gifs.cackhanded.net/commit/4c9998b4bf4b2a650fae4f7a10b3fdfa9d334e8c
