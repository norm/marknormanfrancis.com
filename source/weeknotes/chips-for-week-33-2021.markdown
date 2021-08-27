```
title = "Chips for week 33, 2021"
published = 2021-08-23T06:24:44Z
origin = 'mnf'
type = 'article'
subject = 'weeknotes'
isoweek = [2021, 33]
tag = [
    'repo-hasworn',
    'repo-marknormanfrancis-com',
    'repo-normpress-com',
    'weekchips',
]
image = 'https://mnf.m17s.net/twitter/1429690687486840833/E9dIF0oWQAAL3j6.jpg'
summary = """
  Stopped neglecting weeknotes, didn't break the hasworn chain, set up
  some terraform, wrote words.
"""

[thumbnail]
chips = 'https://mnf.m17s.net/twitter/1429690687486840833/E9dIF0oWQAAL3j6.chips.jpg'
w200 = 'https://mnf.m17s.net/twitter/1429690687486840833/E9dIF0oWQAAL3j6.200.jpg'
w80 = 'https://mnf.m17s.net/twitter/1429690687486840833/E9dIF0oWQAAL3j6.80.jpg'

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

<p class='image'><img src='https://mnf.m17s.net/twitter/1429690687486840833/E9dIF0oWQAAL3j6.jpg' alt=''></p>

## Intention

At the start of the week, I wrote down three goals for myself:

1. restart weeknotes — ✅
1. small improvements to hasworn — ✅
1. setup automated terraform skeleton — ✅


## Update

Started the week by rebasing and rewriting a lot of my untidy,
[piecemeal style commits][p] to hasworn (trying to wrangle Github Actions
into being more useful when building, using, and publishing a Docker image)
into a [neater commit history][n]. Then I wrote up and published the three
weeks of [weeknotes][w] that I had been ignoring.

Then through the week I spent a little bit of time each morning doing
something small to hasworn. Tuesday, a [presentational massage][tue];
Wednesday, added [atom feeds][wed]; Thursday, [iCal feeds][thu]. Small,
achievable bits of work that I can do in half an hour or so. The point is
to keep up the feeling of momentum throughout the week, not just waiting for
the weekend to get back to my own stuff. I'm not [breaking the chain][c].

(For clarity, because I do a four-day week my definition of "the weekend"
includes Friday because it is *my* time — it is not "a day off").

Over the weekend, I got started doing a bunch of reading on how to handle
larger terraform codebases. I've used neat codebases in previous jobs, but my
own use of it has always been a bit slap-dash, and with minimal organisation.
For a couple of years I've wanted to tidy it up and be able to publish as much
of it as I could in the open, alongside/inside the project it controls.

To start with I have experimented with a private repo that has the main code,
the scripts to help me run terraform, and applies any changes via Github
Actions once they are merged to the main branch. Anything that I want open
will be brought in via git submodule, and linked to the right place.

To prove to myself this was going to work, I extracted a small part of my
older terraform and published it in the open. Behold, the wonder that is
[normpress][np]! (A silly waste of a few cents based on an old joke from a
friend, but it amuses me and hopefully him too).

Lastly, I did a few more cosmetic tweaks to hasworn (making 
[`hasworn.com` itself][hw] not a 404, and making an actual 404 for anyone
visiting a broken link on `norm.hasworn.com` (eg. [this isn't a page][not]),
and wrote [a few words][fw] about the history of it too.


[p]: /2021/08/14/github_activity
[n]: /2021/08/16/github_activity
[w]: /weeknotes/
[tue]: /2021/08/17/github_activity
[wed]: /2021/08/18/github_activity
[thu]: /2021/08/19/github_activity
[c]: https://lifehacker.com/jerry-seinfelds-productivity-secret-281626
[np]: https://github.com/norm/normpress.com
[hw]: https://hasworn.com/
[not]: https://norm.hasworn.com/not-a-page
[fw]: /projects/hasworn/rebuilding-hasworn
