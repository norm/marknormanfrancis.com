```
title = "Weeknotes: 2015 Week 24"
summary = "This week's activities include bookmarks, pagination and Slack."
published = 2015-07-27T13:30:54Z
updated = 2021-06-12T08:54:45Z
updated_reason = 'Fixing broken links'
origin = "mnf-v1"
type = "article"
subject = "weeknotes"
```

This past week I've been doing some more not-my-objectives programming, to
scratch some of my itches.


## Bookmarks

I have a [Pinboard][pinboard] account, but I don't habitually use it. I think
most often because when I go looking for something, I can't find it from the
title or tags and really need to search across the full text of the page.

Now, Pinboard does offer archiving, which brings with it searching against
[the full text of the page][pinboardfts], but that does require a yearly
payment. Not that I'm against paying for services I use (quite the opposite)
but I just don't use Pinboard enough to justify the extra cost. Which is
probably a vicious circle, I'll admit.

I've been trying [Stache][s] recently to solve this, and whilst I have enjoyed
the simplicity of it, I've also been frustrated by the same simplicity. And by
it not syncing correctly (I have no idea if it's the app or iCloud at fault).
And by the app not syncing the full text anyway (between OS X and iOS this
does makes sense, I don't want many megabytes downloading to my phone, but
between my two Macs this would be ideal). And finally, the lack of updates
makes me wonder if it's just another piece of abandonware.

Anyway, if I'm going use abandonware, I might as well be the one abandoning
it. Then I only have myself to blame. So I started work on a django app for
bookmarks, called [evocation][e]. Currently it supports adding bookmarks, and
will then archive the bookmark permanently and take a screengrab of it. It
will [search using xapian][search], but only against the title, short
description and URL for now. And it can import from Pinboard (so I had
something to work with).


## Better pagination of large sets

When you have thousands of bookmarks (4,563 currently), pagination is
essential. The [pagination example][pagination] in the django documentation is
terrible. And I don't just mean in the markup it uses. It presents as:

<pre><code>Previous  Page 12 of 229  Next</code></pre>

Yeah, I can hack the URL, but that's tedious.

So I [added better pagination][pagination_commit] by using a python package
called [django-concertina][pypi_concertina]. Which I also [wrote][concertina].
It is based upon how we used to build navigation at Yahoo. Probably around
2006–7, a few of us designed and added what we called "bell curve" navigation
links to several Yahoo sites.

The idea is that you provide several points of entry into the pagination, not
just first/last/next/previous. Links cluster around the current page you're
on, but also move out further to the edges in larger increments (so, like a
bell curve around your current position). It presents as:

<pre><code>1 .. 5 .. 10 11 <em>12</em> 13 14 .. 30 .. 50 .. 80 .. 110 .. 160
.. 229</code></pre>

This means your users can explore and drill down to specific things more
quickly. It also has the benefit of making your results pages (and therefore
the content pages they link to) much more discoverable by search engines as
they will go much deeper through your indexes.


## Slack

> Is it weird that I have my own Pivotal Tracker that is integrated with my
> own Slack for the personal code that I write by myself? — [me][tweet]

I also started using [Pivotal Tracker][pivotal] again to keep track of things.
And pushing them into my own [Slack]. So when I write and commit code, I'm
immediately told that I've written and committed it.

Using the Github-to-Slack integration requires granting Slack write access to
your repos, both public and private. This skeeved me out a little, so I wrote
a [little python][slack-tools] to more easily add the unauthed version of the
integration to my repositories.

 
[s]: http://getstache.com
[e]: https://github.com/norm/evocation
[search]: https://github.com/norm/evocation/commit/832eb2db961fb79da678c4be884dfa850afb3dec
[pinboard]: https://pinboard.in
[pinboardfts]: https://pinboard.in/faq/#search_scope
[pagination]: https://docs.djangoproject.com/en/1.8/topics/pagination/#using-paginator-in-a-view
[pagination_commit]: https://github.com/norm/evocation/commit/14225bc5a9d1321e6f1fbc212e4ee8266b21899c
[pypi_concertina]: https://pypi.python.org/pypi/django-concertina/
[concertina]: https://github.com/norm/django-concertina
[pivotal]: http://pivotaltracker.com
[slack]: https://slack.com
[tweet]: https://twitter.com/cackhanded/status/624525203398389760
[slack-tools]: https://github.com/norm/slack-tools
