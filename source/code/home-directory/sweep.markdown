```
title = "Cleaning up after Byline"
subtitle = "A script to perform actions on flagged items in Google Reader."
published = 2009-08-30T23:21:51Z
origin = "mnf-v1"
type = "article"
updated = 2021-06-12T08:54:45Z
updated_reason = 'Fixing broken links'
```

I use Google Reader as my feed aggregator. Most of the time I don’t read feeds
sat at my computer, but rather on my iPhone using [Byline][by].

As for the principles of [Inbox Zero][ib0], I abhor dealing with feed items
multiple times. But over the past couple of months I had noticed in myself a
bad habit of marking items as unread after reading them because I wanted to
deal with them in some other way. Of course, I never did get around to doing
so because the items were not differentiated in any way from the rest of the
unread, *new* items.

Once I noticed this behaviour, I started making a mental note whenever I
marked something as unread again. It turns out, this happens for one of only a
few reasons:

* I want to read the article properly later, and I’m currently just scanning
  through my feeds to eliminate the chaff
* I want to bookmark the page in some way, to save it for future reference
* It’s something that requires a computer (a flash video, something I want to
  download, etc.)

Now, Byline does include the star, share and note features of Google Reader
which I could use. Except that I wanted to have five different actions, not
just three.

Thing is, three buttons does not mean that there are three states available to
me, it means there are seven (eight if you count nothing) when you combine the
buttons in various ways.

So what I did was mentally assign a greater meaning to each of the three
states, rather than an action. By combining those, I achieved my required
actions without needing to make myself a manual of which combination achieved
what.

* *starring* an item means “deal with this later”
* *sharing* an item means “some other app will deal with this”
* *noting* an item means bookmarking it (and the text of the note serves as
  description and tags for the bookmark)

So by combining these meanings, I get:

* *star* and *share* means "post this to [instapaper][ip] and I’ll read it
  there"
* *star* and *note* means “bookmark this and flag it for review”
* *share* and *note* means “bookmark this and publish it to a blog”

Taking that logic, I then wrote [a perl script][sw] (that I call sweep, as it
cleans up after me) to carry out those actions for me on any newly marked
items.

Now I sort through my new feed items much more quickly and now regularly
achieve Feed Zero.


[by]: http://www.phantomfish.com/byline.html
[ib0]: https://www.43folders.com/izero
[ip]: https://www.instapaper.com/
[sw]: https://github.com/norm/homedir/blob/8f17b4b4b8444e5a684a60b0f90dd49ab6cf9f2e/bin/sweep
