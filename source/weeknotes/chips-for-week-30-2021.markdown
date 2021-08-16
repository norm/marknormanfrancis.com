```
title = "Chips for week 30, 2021"
published = 2021-08-16T09:21:34Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
tag = [
    'weekchips',
    'repo-flourish',
    'repo-hasworn',
]
image = 'https://mnf.m17s.net/twitter/1427198114801324032/E85tHOtWQAI5DiX.jpg'
summary = """
  A lot of activity on hasworn, and a new version of flourish.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/twitter/1427198114801324032/E85tHOtWQAI5DiX.chips.jpg'
w200 = 'https://mnf.m17s.net/twitter/1427198114801324032/E85tHOtWQAI5DiX.200.jpg'
w80 = 'https://mnf.m17s.net/twitter/1427198114801324032/E85tHOtWQAI5DiX.80.jpg'

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

<p class='image'><img src='https://mnf.m17s.net/twitter/1427198114801324032/E85tHOtWQAI5DiX.jpg' alt=''></p>

## Intention

At the start of the week, I kept the same two goals from [last week][lw]:

1. Rebuild hasworn so it is easily updated — ✅
1. Get back to gaming videos — ❌


## Update

As you can see if you look at the Github activity logs throughout the week
([Monday][m], [Tuesday][tu], [Wednesday][w], [Thursday][th], [Saturday][sa],
[Sunday][su]) there was a lot of bitty activity on hasworn.

I like to publish neat, atomic, reasonably documented commits to git
repositories, but the activity when I'm developing is much more like you
see in the links above. Tiny commits, no explanations, frequent use of
"fixup" (and not even proper fixups, just a commit with "fixup" as the title)
and so on. Generally that would be what my code would look like locally,
and then it would get rebased, tidied, and documented before pushing.

However, rather than trying to finagle my local changes to a remote server, I
just relied on Github deploying my changes as I experimented. Then on the
[following Monday morning][m2] I rebased and rewrote the commits and force
pushed that to be the new history of the repository. Not great behaviour in a
collaborative environment, but then I'm the only one working on this codebase.

By the end of the week I had improved hasworn so it was serving the site
on HTTPS, and building the user site with a full list of all tshirts worn
by year, and showing a summary of the most worn tshirts on the homepage.

I also took a moment to release [a new version of flourish][0103] so I could
ensure I wasn't [spending too much money on CloudFront][cf].


[lw]: /weeknotes/chips-for-week-29-2021
[ac]: https://marknormanfrancis.com/2021/08/02/github_activity
[m]: /2021/07/26/github_activity
[tu]: /2021/07/27/github_activity
[w]: /2021/07/28/github_activity
[th]: /2021/07/29/github_activity
[sa]: /2021/07/31/github_activity
[su]: /2021/08/01/github_activity
[m2]: /2021/08/02/github_activity
[0103]: https://github.com/norm/flourish/releases/tag/v0.10.3
[cf]: https://github.com/norm/flourish/commit/92b9a30b1d23208c99f5f5e84705b564778b41e0
