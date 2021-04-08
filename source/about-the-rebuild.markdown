```
title = 'About the rebuild'
noindex = true
page_class = 'about article'
```

# About the rebuild

[![Sketches of how to do CSS on a whiteboard](https://mnf.m17s.net/2012/07/31/dropping-a-css-knowledge-bomb-on-rujmah.jpg)][img] Hello world.

Again.

I'm rebuilding my site.

Take a moment to look at the previous version of it in the
[wayback machine][wb]. Note two things:

1. I hadn't posted anything since August 2015. And I'm writing this in June 2020,
    almost five years later.

2. I had had this idea to collect things such as tweets, Foursquare checkins,
   instagram posts, etc that otherwise end up invisible and unfindable on the
   web. That part I hadn't continued with since 2011.

Also, the site has been offline most of this year
after I shut down the host that was serving it.

Now, with time on my hands
and more importantly some degree of motivation
(completely missing for most of the Covid-19 lockdown)
I'm going to reimplement my site.

I still like the idea of collecting some of those things,
but definitely not all.

And I have more words to write.


## public todo list for shaming me later


* Site mechanism:
  * ✅ <del>build it with (new) [flourish][fl]</del> 
    (and use it as an opportunity to improve that as you find rough edges)
  * ❌ document the rebuild well for future-norm and other curious people

* Old posts:
  * ❌ restore (some of) the old posts from the database backup
  * ❌ restore even older posts not in that database, but in archives

* Instagram:
  * ✅ <del>write a script to create pages for instagram posts
    taken from my downloaded archive</del>
  * ❌ improve the presentation
  * ❌ include a link to the original (unfiltered, uncropped) image if
    it exists 

* Twitter: (I'm not going to import every single tweet)
  * ✅ <del>write [a script to import a tweet or tweet thread][tw] given a tweet ID</del>
  * ✅ <del>write [a script to find previous threads][find] in case they're interesting</del>
  * ✅ <del>import tweets from my [`@norms_ps4`][ps4] account</del>

* Other data:
  * ✅ <del>write a script to import my YouTube videos</del>
  * ✅ <del>write a script to import my GIFs</del>
  * ❌ write a script to import public github activity
  * ❌ write a script to import tshirt wearings
  * ❌ write a script to import/easily add movie watching
  * ❌ write a script to import/easily add bookmarks

* ❌ Then do everything else...
  * ✅ <del>Add SSL</del>
  * ✅ <del>Add logging to the S3 bucket/cloudfront</del>
  * ❌ Analyse said logs
  * ❌ New post on the minimum amount of terraform needed to get a static site
    on S3 with SSL behind CloudFront

[fl]: https://github.com/norm/flourish
[wb]: https://web.archive.org/web/20180823220441/http://marknormanfrancis.com/
[img]: /2012/07/31/dropping-a-css-knowledge-bomb-on-rujmah
[tw]: https://github.com/norm/marknormanfrancis.com/blob/master/script/add_tweets
[find]: https://github.com/norm/marknormanfrancis.com/blob/master/script/find_tweets
[ps4]: https://twitter.com/norms_ps4
