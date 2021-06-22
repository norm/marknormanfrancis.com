```
title = "Chips for week 24, 2021"
published = 2021-06-21T06:31:40Z
origin = "mnf"
type = "article"
subject = "weeknotes"
tag = [ "weekchips", "repo-flourish", "repo-marknormanfrancis-com", ]
image = "https://mnf.m17s.net/twitter/1406862363383537665/E4Yt2rdWUAYyf4a.jpg"
summary = """
  A couple of bug fixes to Flourish, a buncha work integrating my oldest
  content, and some ongoing improvements to this site.
"""

[thumbnail]
chips = "https://mnf.m17s.net/twitter/1406862363383537665/E4Yt2rdWUAYyf4a.chips.jpg"
w200 = "https://mnf.m17s.net/twitter/1406862363383537665/E4Yt2rdWUAYyf4a.200.jpg"

[twitter]
account = "cackhanded"
first_tweet = "1406862363383537665"
retweets = 0
favourites = 1
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='https://mnf.m17s.net/2021/06/21/E4Yt2rdWUAYyf4a.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down four high level goals:

1. Finish restoring old content — ✅
1. Improve MNF presentation — ⏩
1. Improve MNF navigation — ⏩
1. Add 1 year of Eurovision data — ❌


## Update

I started off the week by fixing that the [flourish release v0.10.0][v0100]
had broken my ability to publish, by inadvertently introducing code that only
worked on python 3.9 (what I develop under on my Mac), while I was deploying
with 3.7. That part of the code had no tests, which is why the build had
passed.

Quickly fixed my ability to publish Monday morning, and then added tests and
made the Flourish code [backwards-compatible][v0101] on Tuesday. Then half an
hour later released [a bug fix][v0102] for a new feature that was added along
with the fix.

[v0100]: /2021/06/11/flourish_release_0_10_0
[v0101]: /2021/06/15/flourish_release_0_10_1
[v0102]: /2021/06/15/flourish_release_0_10_2

Having added the ability to redirect URLs in Flourish, I could finish
reintegrating the content from older versions of this site, and from its
precursor. I started my blog on `cackhanded.net` but less than a year later
moved to `marknormanfrancis.com`. I vaguely recall that I wanted to keep my
words separate from all of the other projects (that I never did, apart from
[gifs][gifs] now). Whatever my reasoning was in 2006, I do prefer this domain
so it stays here.

[gifs]: https://gifs.cackhanded.net/

After adding [the old content][old] to the site, my attention moved to the
(long) list of things I wanted to add or improve about the site. The
presentation is lacking, as the index pages including the homepage were simply
functional lists of links so I could navigate around when developing the site.
I'm not a designer so it's never going to be a beautiful sight (site), but
even with that, I had done little other than choose colours and fonts and made
a bunch of links in the header.

I started with the 404 page, it being the only error page Amazon S3 will
serve, and made sure I could preview it properly by having the Flourish [live
preview use it][404s]. You can see it by deliberately breaking the URL on the
site, or by visiting it [in its published location][404] where it will be
served as `200 OK` (as the not found page was actually found). It mildly
annoys me that there's no way to have a 404 page without having be an actual
page.

(The insistence on using the right HTTP status codes when I was working at
GDS on [the launch of GOV.UK][gov] was how our team ended up owning
custom-made ["HTTP enforcement squad"][es] tshirts.)

Ended the week working on making an actual homepage, and retrofitting the
metadata and images I need into existing content for them to appear correctly.
This will drag into next week where I'll have only one goal: to finish this.


[old]: https://github.com/norm/marknormanfrancis.com/pull/70
[404s]: https://github.com/norm/flourish/commit/2c81ec27f8d0e868337d336f85b9a7019f06e378
[404]: https://marknormanfrancis.com/404
[gov]: https://gds.blog.gov.uk/2012/10/16/gov-uk-the-start/
[es]: https://www.flickr.com/photos/mn_francis/8279823923/
