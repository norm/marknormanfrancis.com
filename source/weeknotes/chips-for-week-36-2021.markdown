```
title = "Chips for week 36, 2021"
published = 2021-09-14T05:22:31Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 36]
tag = [
    'weekchips',
    'repo-gifs-cackhanded-net',
    'repo-hasworn',
    'repo-kitout',
    'repo-marknormanfrancis-com',
]
image = 'https://mnf.m17s.net/weeknotes/2021/36/chips.jpg'
summary = """
    My computer needed a new disk, so naturally I wrote some
    code to reinstall my preferred setup on the new disk.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/weeknotes/2021/36/chips.chips.jpg'
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='https://mnf.m17s.net/weeknotes/2021/36/chips.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down some goals:

1. Get back into the GIFs habit — ❌
1. Write up more about hasworn — ❌
1. Write up taking whiteboard pictures — ❌


## Update

For the first few days, other than posting [my weeknote][w] and fixing a few
small bugs (one in GIFs where a [too-long description][b] stopped the tweet
from sending; one in hasworn where the sites were not building overnight
because I got the [task name wrong][t]; and I copied the [generated site
test][g] from here to GIFs to spot problematic content) I got nothing done.

And then Friday, the disk inside my iMac died. First thing in the morning, and
after unlocking it, I right-clicked on a link in the web page I had left open
as a todo marker. I got the spinning wait beachball. Not unusual, I leave a
lot of stuff open on my iMac and, despite having 32GB of memory, I am often
into using a few gigabytes of swap too. So left it for a minute, expecting
some swapping to occur and then the menu to appear. But it didn't, so I
clicked on the memory usage widget that [iStat Menus][is] provides to see how
badly into swap I was. This is when everything locked solid. No mouse
movement, no screen updates, nada.

Power off, wait, power on. A seemingly endless progress bar of startup. I left
it for a bit, returned maybe ten minutes later, nothing. Tried again and got
the [question mark folder][q]. No usable boot partition.

<figure>
  <a href='https://mnf.m17s.net/weeknotes/2021/36/question-mark.jpg'><img src='https://mnf.m17s.net/weeknotes/2021/36/question-mark.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    sad, unbootable iMac
  </figcaption>
</figure>

So instead of doing anything useful on Friday I instead arranged a replacement
disk with my local service place, took the iMac to them, then stared at the
uninterrupted view of the wall of my study.

<figure>
  <a href='https://mnf.m17s.net/weeknotes/2021/36/no-mac.jpg'><img src='https://mnf.m17s.net/weeknotes/2021/36/no-mac.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    invisible sad, unbootable iMac
  </figcaption>
</figure>

I then spent every spare minute of my weekend on [a new version][k] of an [old
way][s] of setting up a Mac from scratch, and using it to set up my Mac from
scratch. A new version for various reasons, one being to [add tests][a] to it,
because at some point I broke the in-progress version of the old script with
some overly excitable changes and have had a "write tests" todo for years now.

After getting my iMac back, and using said script to help me recreate my
preferred setup, only now (Tuesday morning) am I actually in a position where
I can preview this weeknote locally on my iMac again, before I publish it.


[w]: /weeknotes/chips-for-week-35-2021
[b]: https://github.com/norm/gifs.cackhanded.net/commit/9f0e4941b11bc0373e7120eb0a9f397b13670a9b
[t]: https://github.com/norm/hasworn/commit/a699f182d2b2289f0c8c5c9088a0109b4ba0b3ad
[is]: https://bjango.com/mac/istatmenus/
[q]: https://support.apple.com/en-gb/HT204323
[g]: https://github.com/norm/gifs.cackhanded.net/commit/43ae68f1eb3cfb11f4bfd18b696f83803d943098
[k]: https://github.com/norm/kitout
[s]: https://github.com/norm/suited
[a]: https://github.com/norm/kitout/tree/main/tests
