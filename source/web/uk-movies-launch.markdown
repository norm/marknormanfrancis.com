```
title = "UK Movies launch"
published = 2005-10-26T23:15:28Z
subtitle = "An informal Yahoo! product launch annoucement."
origin = 'chnet'
origin_url = 'cackhanded.net/web/uk-movies-launch'
type = 'article'
```

This evening we launched the new European Movies design in the UK. This is the
end result of several months of work from the European engineering and web
development teams, developing and integrating a new database and API system.

You can compare the [new site][uk] with the old designs still on the
[German][de], [French][fr], [Spanish][es], [Italian][it] sites.

What's so exciting about this? Well, for me, it means finally being free of a
project that seems to have dragged on for ever (not so much luch for the
primary developer Jon, who is still on it until the other four countries have
launched). Now I can spend some time doing more fun things, such as writing
some perl code to pre-process CSS. Yes, I said that would be fun. Yes, I meant
it.

That's probably only exciting for me. So, instead, let's talk about what's
noteworthy about this site. Well, it's built using web standards, it's pretty
good semantically. One or two presentational classnames, but it's mostly using
contextual CSS selectors, rather than `div` and `span` mania. In our recent
all-hands conference in [Tenerife][t], I gave a presentation about web
development, and two slides showed the before/after of the main navigation —
from a complex table with spacer images, to a simple unordered list (I got a
round of applause for that one, and it's not even my code!).

What else? Well, it nearly validates! For a while it did, but then we put the
adverts in, and that generally causes validation errors. Plus there's one or
two templating bugs we're fixing. Not really exciting news for most
standards-based web developers, I'll admit. But I like to think of it as us
fixing Yahoo! Europe, one web site at a time.

So if that's not too noteworthy, what is? Well, we're trying a new page
scaling technique, based upon the technique we were given to use when
developing the [front page][y]. Up your font size and the page gets wider,
because it's sized using `em` units.

Also, and this is something you would never notice unless you examine the
source closely or are writing a search engine, we're experimenting with
[microformats][uf]. Currently, the "critic's reviews" page of a movie (for
example, the wonderful Joss Whedon's [Serenity][s]) is marked up with
[hReview][hr]. I'm not too happy with the way the microformat works out in
this context, but it's a start, and I'll be looking to see if more things fit,
or if we could suggest and/or help develop some new formats.

So, feel free to check it out. Look up some [premiere photos][pp]. Get some
[movie news][mn]. Find out [what's on in cinemas near you][ny] (well, if
you're based in the UK, anyway). And as any good music compilation will say,
much, much more.


[t]: https://www.flickr.com/photos/mn_francis/sets/1026178/
[de]: https://web.archive.org/web/2005123100000/http://de.movies.yahoo.com/
[es]: https://web.archive.org/web/2005123100000/http://es.movies.yahoo.com/
[fr]: https://web.archive.org/web/2005123100000/http://fr.movies.yahoo.com/
[it]: https://web.archive.org/web/2005123100000/http://it.movies.yahoo.com/
[uk]: https://web.archive.org/web/2005123100000/http://uk.movies.yahoo.com/
[y]: https://web.archive.org/web/2005123100000/http://uk.yahoo.com/
[uf]: http://microformats.org/
[s]: https://web.archive.org/web/2005123100000/http://uk.movies.yahoo.com/s/Serenity/reviews-41366.html
[hr]: http://microformats.org/wiki/hreview
[pp]: https://web.archive.org/web/2005123100000/http://uk.movies.yahoo.com/premiere-photos.html
[mn]: https://web.archive.org/web/2005123100000/http://uk.movies.yahoo.com/movie-news/
[ny]: https://web.archive.org/web/2005123100000/http://uk.movies.yahoo.com/cinemas/
