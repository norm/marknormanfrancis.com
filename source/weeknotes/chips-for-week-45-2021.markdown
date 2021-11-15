```
title = "Chips for week 45, 2021"
published = 2021-11-15T06:33:13Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 45]
tag = [
    'repo-gifs-cackhanded-net',
    'weekchips',
]
image = 'https://mnf.m17s.net/weeknotes/2021/45/chips.jpg'
summary = """
    A low effort week, just some small fixes and improvements to GIFs,
    and another episode of Ted Lasso.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/weeknotes/2021/45/chips.chips.jpg'

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

<p class='image'><img src='https://mnf.m17s.net/weeknotes/2021/45/chips.jpg' alt=''></p>

## Intention

[Last week's note][lw] said:

> Headaches and migraines kicking off all week, so a lot of my energy got
> reserved for work.

This was still happening on the Monday morning as I was writing that weeknote.
I wasn't feeling particularly upbeat, so when planning for this week, I
anticipated another week of struggle so gave myself only these two pessimistic
goals:

1. Whatever — ⏩
1. More GIFs? — ✅


## Update

I got nothing done during the week, and I was really struggling to concentrate
at work. The weekend rolled around and I managed to have some occasional brain
time and did [a bunch of small fixes and improvements][sm] to the GIFs site,
and GIFed up [another episode of Ted Lasso][tl].

One particular GIF had me investigating how to eliminate camera shake with
ffmpeg, as some of the more egregiously shakicam footage used on TV at times
can cause me to abandon a GIF because the constant motion leaves the output
too bloated, sometimes more than three times as big as a comparable but
statically shot scene. I've tried this before using the "virtual tripod" mode
but that seems to only work well within a single shot — in a section of video
with two camera angles, one is stabilised but the other swings around wildly,
worse than before. Some more reading led me to the option `smoothing=0` for
the stabilise transformation, which is "a special case where a static camera
is simulated" and this works out much better for my needs. Not perfectly
still footage, but enough shake removed to keep the GIFs small enough.
So now I have an option to [stabilise video][vs] if needed.

Quite a small week in terms of achievement, but honestly feels bigger because
of the inability to think for half of it.


[lw]: /weeknotes/chips-for-week-44-2021
[sm]: /2021/11/14/github_activity
[tl]: https://github.com/norm/gifs.cackhanded.net/commit/4b2aace76f5b36d221bc91d404551a68c76be777
[vs]: https://github.com/norm/gifs.cackhanded.net/commit/16232689a7a7ce6cae7508db1ee3bb95e161b885
