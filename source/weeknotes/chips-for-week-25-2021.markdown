```
title = "Chips for week 25, 2021"
published = 2021-06-28T06:05:41Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 25]
tag = [
    'weekchips',
    'repo-marknormanfrancis-com',
]
image = 'https://mnf.m17s.net/twitter/1409392539203952641/E48rCPYXMAAm0Je.jpg'
summary = """
  I reworked a lot of the data format behind the content of the site to
  support the new homepage layout, then launched the new home.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/twitter/1409392539203952641/E48rCPYXMAAm0Je.chips.jpg'
w200 = 'https://mnf.m17s.net/twitter/1409392539203952641/E48rCPYXMAAm0Je.200.jpg'
w80 = 'https://mnf.m17s.net/twitter/1409392539203952641/E48rCPYXMAAm0Je.80.jpg'

[twitter]
account = "cackhanded"
contains_tweet = [
    '1409392539203952641',
]
retweets = 0
favourites = 0
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='https://mnf.m17s.net/twitter/1409392539203952641/E48rCPYXMAAm0Je.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down one goal:

1. Finish rebuild and improve site as desired — ✅


## Update

And that's pretty much what I did for the first half of the week, starting
with a sketched out homepage that features the things I'm actually doing
(GIFs, YouTube videos, code and weeknotes, occasional words, pictures of my
cats) and then working backwards to make the content fit this.

For example, I altered the structure of much of my imported data, such as
[YouTube][yt] videos and [tweets][tw], wrote a script to produce
[thumbnail images][tn], and relocated my [weeknotes][wn] then added
[summaries and images to them][wns]. And more besides, check the full
[day's activity][gh].

The last thing was to turn the "rebuilding" message into [an article][rb], and
[launch the homepage][hp]. And then [write that up][ab] (forgetting that the
date I started writing it was not the date I finished, oh well). For the write
up I wanted to include screenshots of what the site used to look like, so I
wrote a [script to pull down copies][ar] from the [Wayback Machine][wb],
(I'm also keeping those archives in this repo, just in case).

Having launched the new page, I got an immediate bug report for a small bit of
wonk in the latest Chrome, and [fixed it][bf]. Topped off the week by
[adding a bit more fancy][fa] to my [weeknotes index page][wni].

And, as the chips show, I also spent a fair amount of the week on "tidying",
because we've got our first overnight visitor in a year and a half and the
guest bedroom had become the storage closet.


[yt]: https://github.com/norm/marknormanfrancis.com/commit/438c28db03bc6f032ffe8f25c34004375ce7d7f4
[tw]: https://github.com/norm/marknormanfrancis.com/commit/9c52ab3795c8707b7fb192b0a80e886f38eaf947
[tn]: https://github.com/norm/marknormanfrancis.com/commit/5093dcc13cacb004bd07d58ffa8521c5a2b86f10
[wn]: https://github.com/norm/marknormanfrancis.com/commit/bda797af61be974741dfadd2b6527c607e547830
[wns]: https://github.com/norm/marknormanfrancis.com/commit/bbd142f31023b893880f78bf205f1ff1339b6b6f
[gh]: /2021/06/24/github_activity

[rb]: https://github.com/norm/marknormanfrancis.com/commit/feff86f85e7caadc908ad0229e3c1b0f1efeca71
[hp]: https://twitter.com/cackhanded/status/1408008442921598977

[ab]: /about/finishing-the-2020-restoration
[ar]: https://github.com/norm/marknormanfrancis.com/commit/9ee7b3fb44154685bd9ff5ea0edcde06d40d35ab#diff-7d8103e4a11f6f76962211bff78fd22f7991db446ac7dcf27f39d3e3d45f6701
[wb]: https://web.archive.org

[bf]: https://github.com/norm/marknormanfrancis.com/commit/8f04283a1da93aa62523090e99d350839b6cdde1
[fa]: https://github.com/norm/marknormanfrancis.com/commit/0eda9b16bb74ea2288430cd1dd7644e94120c34b
[wni]: /weeknotes/
