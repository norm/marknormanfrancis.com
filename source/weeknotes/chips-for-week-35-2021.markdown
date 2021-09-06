```
title = "Chips for week 35, 2021"
published = 2021-09-06T07:16:27Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 35]
tag = [
    'repo-hasworn',
    'repo-marknormanfrancis-com',
    'weekchips',
]
image = 'https://mnf.m17s.net/twitter/1434777176117755908/E-laObwX0AAW-uP.jpg'
summary = """
  Took photos of a whiteboard, published some words, did a little work
  on my tshirt collector.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/twitter/1434777176117755908/E-laObwX0AAW-uP.chips.jpg'
w200 = 'https://mnf.m17s.net/twitter/1434777176117755908/E-laObwX0AAW-uP.200.jpg'
w80 = 'https://mnf.m17s.net/twitter/1434777176117755908/E-laObwX0AAW-uP.80.jpg'

[twitter]
account = "cackhanded"
contains_tweet = [
    '1434777176117755908',
]
retweets = 0
favourites = 0
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='https://mnf.m17s.net/twitter/1434777176117755908/E-laObwX0AAW-uP.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down three goals:

1. Practice using overhead camera to get clear whiteboard photos — ✅
1. Write up hasworn — ⏩
1. Make GIFs — ❌


## Update

Perhaps a little overambitious when I only have one day and some odd hours
here and there to set myself three goals. But they're not concrete goals, just
things that at the start of the week I felt I should make some progress on.

Monday mornings are for writing the weeknote, and getting my brain back in
"work" mode. [Tuesday][tm] and [Thursday][ts] mornings I spent a tiny amount
of time implementing two Atom feeds. I haven't yet linked to them in any way
other than the autodiscovery links, but they are at [`/index.atom`][a] for
just the new articles, and [`/firehose.atom`][f]. Not much work, but then I've
still feeling the pain of gout.

Friday morning I spent working on taking and refining photos of a whiteboard,
for a post was writing explaining how I mostly use [static pages][s] on
`hasworn`. A [little Twitter thread][th] introduces my whiteboard diagrams,
and I'll be writing more about that and committing the code soon. Along with a
couple more articles about `hasworn`.

As part of the article, I tidied up some of the [images presentation][i]
and added some basic support for marking posts as [being in a "thread"][t].

Alas, I made zero GIFs, because over the weekend I went off book and did some
more work on `hasworn`. [Saturday][st] I added a couple of redirects,
highlighting when a tshirt is first/last worn on the year pages, and included
the images in the CSV export (mostly so I can more easily reuse them in
development). [Sunday][sn] I did most of the work to add celery, so I can
rebuild the static pages asynchronously when using the django interface, and
overnight so the "last worn yesterday"s update.


[tm]: /2021/08/31/github_activity
[ts]: /2021/09/02/github_activity
[a]: /index.atom
[f]: /firehose.atom
[i]: https://github.com/norm/marknormanfrancis.com/commit/3bfb08652c15f24882bc92cd4e686e5c4c754a13
[t]: https://github.com/norm/marknormanfrancis.com/commit/1821bed5495f37c2f3a9c88ae23389dcaa98e7e3
[s]: /projects/hasworn/the-static-pages-of-hasworn
[th]: https://twitter.com/cackhanded/status/1433838682499334147
[st]: /2021/09/04/github_activity
[sn]: /2021/09/05/github_activity

