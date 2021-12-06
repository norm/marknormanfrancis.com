```
title = "Chips for week 48, 2021"
published = 2021-12-06T05:39:00Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 48]
tag = [
    'repo-gifs-cackhanded-net',
    'weekchips',
]
image = 'https://mnf.m17s.net/weeknotes/2021/48/chips.jpg'
summary = """
    Made yet more GIFs. Weeknote also talks about how I measure
    some deadlines, and has a nerdy aside about an aspect of
    the GIF specification.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/weeknotes/2021/48/chips.chips.jpg'

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

<p class='image'><img src='https://mnf.m17s.net/weeknotes/2021/48/chips.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down two goals:

1. GIFs (push dates back) — ✅
1. Updates to this site — ❌


## Update

With my recent spate of bad headaches receeding into the rear-view mirror, I
was feeling like I would once again have the energy to spend at least some
time doing personal projects.

As I have noted many times making GIFs is something I can do without much
energy, so it seemed like a good transitional thing to work on to get my
habits back. I was hoping this would be a gateway drug to doing some bug
fixing and small improvements to this site. But in the end, I only made more
GIFs and one improvement to the GIFs site.

During the week I spent my early mornings adding some more Mitchell and
Webb and Invader Zim GIFs, to push back my looming deadlines. I reserve a
part of my study whiteboards for planning my week's activities, and I keep
tallies and deadlines on it:

<figure>
  <a href='https://mnf.m17s.net/weeknotes/2021/48/whiteboard.jpg'><img src='https://mnf.m17s.net/weeknotes/2021/48/whiteboard.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    Eurovision data outstanding: 50 years in 23 weeks = 2.1 years per week.
    Days until next unscheduled: morning GIF, 39; Invader Zim GIF, 45;
    game shows videos, long overdue.
  </figcaption>
</figure>

Until it becomes a burden instead of something I enjoy, I want to keep
publishing at least one GIF per day. This count helps me know when to start
panicking, especially when I use days of the week thematically rather than
publishing randomly whatever is made, and have at least one subject already
[scheduled][s] through to January 2023.

Over the weekend I added two more episodes of Invader Zim, made a couple of
quality of life changes to the code, and then one big change. I added to the
information on the individual GIF page more about the GIF itself rather than
the original source material. So taking [this morning's GIF][g] as an
example, as well as telling you that it comes from the movie Ghostbusters,
and the character Janine Melnitz appears in it, now you also know the GIF
itself is 480×264 in size, weighing in at 0.87mb, has 36 individual frames
of animation, is using 49 unique colours, and lasts 1.99 seconds.

Nerdy aside: the original configuration said 2 seconds, but an aspect of the
GIF spec means you might not get exactly that. Animation frame delays in
[the GIF89a specification][gif] are measured in hundredths of a second.
When you ask ffmpeg to output 18 frames per second (one every 5.55…
hundredths of a second) it approximates by alternating 5 and 6 hundredths
of a second. This means I often end up with one one-hundredth of a second
missing from my GIFs.


[s]: https://github.com/norm/gifs.cackhanded.net/blob/main/schedule.markdown
[i]: https://github.com/norm/gifs.cackhanded.net/commit/7d509f8810e91f929cbcdf2fbb1c8c3f267f2f71
[g]: https://gifs.cackhanded.net/ghostbusters/oh-really
[gif]: https://www.w3.org/Graphics/GIF/spec-gif89a.txt
