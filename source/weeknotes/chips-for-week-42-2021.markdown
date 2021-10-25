```
title = "Chips for week 42, 2021"
published = 2021-10-25T04:37:19Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 42]
tag = [
    'repo-gifs-cackhanded-net',
    'repo-hasworn',
    'repo-marknormanfrancis-com',
    'weekchips',
]
image = 'https://mnf.m17s.net/weeknotes/2021/42/chips.jpg'
summary = """
    Fixed some small bugs, did some unfinished work, felt queasy.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/weeknotes/2021/42/chips.chips.jpg'

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

<p class='image'><img src='https://mnf.m17s.net/weeknotes/2021/42/chips.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down three goals:

1. Fix annoying bugs in site — ✅
1. Fix Galaxy Quest todo (and double check if there are GIFs to be made) — ✅
1. Start music library work — ❌


## Update

A quiet week with only a few small bits of progress, and a lot of nausea
caused by [new glasses][ng].

I started the week by finishing up and committing a couple of bits I had
already started last week for [that week's goal][lw] of improving hasworn —
I added [more description to the Atom feed][at], and
[included the number of times worn][ca] in the calendar feed. I changed the
logic around average days between wearings to consistently choose
[five days][fd] as the minimum threshold before using it, included a summary
[of the newest shirts in the homepage][hp], and linked the homepage
summaries to their [relevant all tshirts page][al].

Tuesday I fixed some bugs in this site, that importing from my GIFs site
when two GIFs on the same day had the same title, one would
[override the other][mg], and the presentation of the latest entries on the
[weeknotes summary page][ws] was not great [at narrow widths][nw].

I also pulled a note I had left myself and then accidentally committed
to the [Galaxy Quest GIFs summary page][gq]. Given the file is Markdown,
that was one big todo I left lying around.

I then spent the rest of the week's mornings working on two things. First,
adding the prescriptions I get [from the optician][op] as I find it
interesting how it changes over time. And second, doing some more work on the
script to automatically crop and blanch a whiteboard diagram (as first seen in
my recent post on [hasworn's static pages][sp]), to include cropping using
[fiducial markers][fd]. Over the weekend I started to write some tests so I can
publish it as a standalone script. Expect to see that appear on GitHub in the
next couple of weeks.


[ng]: https://twitter.com/cackhanded/status/1451115658364825602
[lw]: /weeknotes/chips-for-week-41-2021
[at]: https://github.com/norm/hasworn/commit/ecb237211e8c6cd8571715b229f03cf7ca1b7a64
[ca]: https://github.com/norm/hasworn/commit/860429a8d30818d15abd43a56defbc0143d53856
[fd]: https://github.com/norm/hasworn/commit/bea39293a0c8b6add6ce3d78328866b038709a4a
[hp]: https://github.com/norm/hasworn/commit/fe044a3f3a7d514c455aeb51f36a491bb77f57b3
[al]: https://github.com/norm/hasworn/commit/5a19a19680bce783f154a398ef9fe60d5746d8e7
[mg]: https://github.com/norm/marknormanfrancis.com/commit/997e76afa9dff7e8455686f73175ead476ba7397
[ws]: /weeknotes/
[nw]: https://github.com/norm/marknormanfrancis.com/commit/d6c1f110af448f9ff4ce5af57d4d1ea40778ddd2
[gq]: https://github.com/norm/gifs.cackhanded.net/commit/dc9546b01f8b2e5a97e648a4cb23db5c582c5ba2
[op]: https://github.com/norm/marknormanfrancis.com/commit/56b800e9eaf7b92a70f909d69e98a0e5bc26a4df
[sp]: /projects/hasworn/the-static-pages-of-hasworn
[fd]: https://en.wikipedia.org/wiki/Fiducial_marker
