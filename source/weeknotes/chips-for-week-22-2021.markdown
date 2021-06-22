```
title = "Chips for week 22, 2021"
published = 2021-06-07T10:30:54Z
origin = "mnf"
type = "article"
subject = "weeknotes"
image = "https://mnf.m17s.net/2021/06/07/E3ReV5eXoAArHxg.jpg"
tag = [ "weekchips",]
previous_slug = [
    '/2021/06/07/chips-for-week-22-2021',
]
summary = """
  I made my GIFs site better by fixing as many navigation bugs as I could
  find, and added many Atom feeds. And made some GIFs.
"""

[twitter]
contains_tweet = [
    '1401849138761850883',
]
retweets = 0
favourites = 1

[thumbnail]
chips = "https://mnf.m17s.net/2021/06/07/E3ReV5eXoAArHxg.chips.jpg"
w200 = "https://mnf.m17s.net/2021/06/07/E3ReV5eXoAArHxg.200.jpg"
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='https://mnf.m17s.net/2021/06/07/E3ReV5eXoAArHxg.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down five high level goals:

1. Improve flourish live preview — ✅
1. Fix bugs in gifs.cackhanded.net navigation — ✅
1. Add all the Atom feeds to gifs.cackhanded.net — ✅
1. Improve older GIFs — ❌
1. Add 1 year of Eurovision data — ❌


## Update

As I've gone through a mental transition of making GIFs occasionally to
[publishing at least one every day][gif-history], that site has become harder
to navigate to find everything. Plus I'd noted a few problems where the index
pages were not listing all (or any!) of the GIFs correctly. So this week I
fixed all of the bugs I could find, added by-year and by-month navigation,
added [Atom feeds][feeds] almost everywhere, and a [404 page][404] using one
of many [candidates][404cd] at [random][404cm]. But because the site is
static, this happens [every hour][hr] not every time you refresh the page.

As part of this, I fixed a couple of page generation bugs in [Flourish][fl]
(it's hard to preview the bug fixes when your previewer doesn't even know to
regenerate the page you're previewing) and released [version 0.9.7][v097]
on Thursday.

Plus, to stay on-brand, I added [twelve more GIFs][mwgifs] to my site's
backlog and once again did **not** add any more years of Eurovision data to
[my collection][evd].

[gif-history]: /2021/06/07/history-of-my-gifs-site
[feeds]: https://gifs.cackhanded.net/feeds
[404]: https://gifs.cackhanded.net/404
[404cm]: https://github.com/norm/gifs.cackhanded.net/commit/f8e42ad6ad883b876cf678712a9dcebad67c9e60
[404cd]: https://gifs.cackhanded.net/tags/404-page-candidate/
[hr]: https://github.com/norm/gifs.cackhanded.net/commit/ed8c110aad88779b47cc88b01f6005d81206a9b6

[fl]: https://github.com/norm/flourish
[v097]: https://github.com/norm/flourish/releases/tag/v0.9.7
[mwgifs]: https://github.com/norm/gifs.cackhanded.net/compare/d6a5653b98ebe07ac9d281941bc258fc6b512522..625b7b296082a0bc42b099f4457b633a8a1dc9dd
[evd]: https://github.com/norm/eurovision_data
