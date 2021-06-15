```
title = "Weeknotes: 2015 Week 0"
summary = "I have long struggled with having too many personal projects, and then never doing anything with any of them. I'm going to try to resolve this. This is the first of my weekly status updates."
published = 2015-02-09T23:04:38Z
updated = 2021-06-12T08:54:45Z
updated_reason = 'Fixing broken links'
origin = "mnf-v1"
type = "article"
subject = "weeknotes"
```

## Where I am

I have long struggled with having too many personal projects, and then never
doing anything with any of them. This site, for example — it is currently
running on a bespoke perl site generator I call `flourish`. This is something
like the fifth or sixth version of the software. Originally, back in 2000, it
was a single script inspired by [blosxom][b] (an old blog system which would
now be called a "static site generator"). Then I made it run server-side,
keeping state in shared memory so I didn't need to use a database. Then I made
it more modular. And so on. The version I am writing this into uses
[CouchDB][c] and [redis][r], because I wanted to play with them. This version
dates from 2011, but I have most of a newer version sitting on my laptop.

Clearly this is all an excuse to avoid writing and publishing to the internet.
Because that's scary, whereas writing code you know nobody else will ever use
isn't.

I have 73 repositories in my Github account, and whilst some are one-off
things that I don't need to touch again, more than half are projects I have
abandoned. Several don't even contain any code, they're just placeholders —
create the repo and then, poof, forgotten.

I have a [Pivotal Tracker][p] dashboard full of ideas, notes, bugs… My
velocity has been 0 for five months. Ignoring "sprints" where I achieved
nothing, my average across 2014 was about 0.8. My best week was mid-year when
I had a week off between jobs and did some hacking on my 
[DVD ripping manager][d]. But I never pushed the results to GitHub.

I've attended many a [/dev/fort][df], where a bunch of people work on a
project for the internet and then I fail to do anything more on them. In fact,
that site (that I "run") currently says the most recent fort was the fifth,
but actually is is the ninth.

I promised about a year ago to do a bit of work on [webkit2png][w], but the
moment I stopped working on the project I was using it for at [GDS][gds]…

The [London Pub Standards][ps] website stopped listing new events at the start
of this year because in 2013 I thought to myself that all of 2014 would be
more than enough to get around to updating the database and code. It wasn't,
but fortunately this is now being updated by other people.

I suffer from a paralysis of action because there are too many things I have
thought of and I want them all equally. Everything makes me feel guilty that
I'm not doing more.

And so I do nothing. 


## Where I will be

This paralysis ends now.

This year, I'm wiping my slate clean. I dumped all of my todos out of Pivotal.
I'm not attending any forts. I'm going to kill all of the empty projects in
Github. I am committing to working on just two things in 2015, and if I fail
I'm giving up on the whole idea of side projects and embracing the sofa sloth
lifestyle.

* *marknormanfrancis.com* — this site, because I want to write more about
  myself and my opinions.
* *usinghtml.org* — a book on writing decent HTML. It's not yet anything, but
  it is definitely one of the many ideas I've let languish (I registered the
  domain *five years ago*).

But I just lied. Technically, it'll be three things, because I'll need some
way of turning words into web pages. And I am *quite fussy* about the state of
my web pages and ownership of my words, so just using Tumblr or Medium isn't
going to cut it.

Yup. I'm going to write another version of `flourish`.

But this one will be properly developed in the open, because I heard somewhere
that that should [make it better][dp]. This will be regularly pushed to
Github. Including a design of how it should work up front, not just writing
code as it occurs to me. Once it is capable of reproducing this site, it'll be
*done* and then I'll be focused on writing words. And every Monday I plan to
be writing up what I achieved in the previous week.

Currently I have a whiteboard full of notes, some experimental [go][go] code
and a desire to use [Make][m] as much as possible when producing the sites —
because why should I write something that deals with tracking dependencies and
file rebuilds when it already exists?

This week's actual notes? I've created the README in [the flourish repo][f].
This time next week I should have some working proof of concept code.


[b]: https://en.wikipedia.org/wiki/Blosxom
[c]: https://couchdb.apache.org
[r]: https://redis.io
[p]: https://www.pivotaltracker.com
[d]: https://github.com/norm/p5-Media
[df]: https://devfort.com
[w]: https://github.com/paulhammond/webkit2png/
[ps]: https://london.pubstandards.com
[gds]: https://www.gov.uk/government/organisations/government-digital-service
[dp]: https://www.gov.uk/guidance/government-design-principles#make-things-open-it-makes-things-better
[go]: https://golang.org
[m]: https://en.wikipedia.org/wiki/Make_(software)
[f]: https://github.com/norm/flourish/
