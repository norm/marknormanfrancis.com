```
title = "Finishing the 2020 site restoration"
published = 2021-06-23T13:00:00Z
origin = 'mnf'
type = 'article'
tag = [
    'colophon',
]
summary = """
  A little note to mark the end of the restoration of this site that I
  started a year ago, and the work done to do the final part — restoring
  the handful articles I've written since 2005.
"""

[thumbnail]
200 = 'https://mnf.m17s.net/about/finishing-the-2020-restoration.200.jpg'
```

Back in 2020 I wrote an article about starting a restoration of my website. At
the time I was fairly confident that this would not take more than a few
weeks. And yet, I am writing this summary having finished importing all the
content I wanted before I considered it "done" a whole year later.

I can sense something of a pattern in my meta-posts about my site. The very
first “about this site” page I wrote in 2005 said:

> This site is still under construction, and this page will continue to be
> updated as this site evolves. The styles are still a little rough right now
> as I tie down the code [...]

For the last year I've had a banner on the site that said "Please hold…
rebuild in progress" that linked to [an explanation][rb] as my intention was
to have it done in a few weeks. Two things derailed that entirely. Firstly,
I spent [two weeks][w32] suffering from vertigo and the summer heat, and
then I pivoted almost entirely from writing words and code to making
[YouTube videos][w36] for six months.

## The last imported content

Apart from one or two things that I'm not yet able to import to the site,
the very last thing to import was the original content. I put that off
until the end as I knew it would be mostly manual editing, rather than being
able to write and tweak a script that did it all, and be done.

To start with, I decanted the posts stored in a database backup from the last
version of this site.

<figure>
  <a href='https://mnf.m17s.net/about/marknormanfrancis.com.v2.1024.jpg'><img src='https://mnf.m17s.net/about/marknormanfrancis.com.v2.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    <i>marknormanfrancis.com</i> v2, circa October 2011
  </figcaption>
</figure>

<figure>
  <a href='https://mnf.m17s.net/about/marknormanfrancis.com.v1.1024.jpg'><img src='https://mnf.m17s.net/about/marknormanfrancis.com.v1.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    <i>marknormanfrancis.com</i> v1, circa September 2009
  </figcaption>
</figure>

Some of them were written in Markdown, which made the process of editing them
to work for this site easier. But many were written in a format called
[`textframe`][tf], an old side project of mine to create a
[lightweight markup language][lw] that would support many more HTML elements.
For those I converted the output HTML into Markdown using [markdownify][md],
then compared that to the original source, correcting as necessary.

I then did a pass comparing these restored versions to those recorded in the
[Wayback Machine][wb] for the site, checking links and rewriting them in my
current posts to the Wayback Machine from that period in time if they had
subsequently broken or no longer represented the content I was referring to.

By going back far enough, I then realised that when I moved my content from
being on `cackhanded.net` to `marknormanfrancis.com` I had either missed or
deliberately left out some of my earliest content. So I recovered those from
a much older backup I had kept.

<figure>
  <a href='https://mnf.m17s.net/about/cackhanded.net.v2.1024.jpg'><img src='https://mnf.m17s.net/about/cackhanded.net.v2.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    <i>cackhanded.net</i> v2, circa August 2007
  </figcaption>
</figure>

<figure>
  <a href='https://mnf.m17s.net/about/cackhanded.net.v1.1024.jpg'><img src='https://mnf.m17s.net/about/cackhanded.net.v1.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    <i>cackhanded.net</i> v1, circa November 2005
  </figcaption>
</figure>

A few observations:

  * In 2006, there was a debate in web circles over [microformats][uf]
    (adding richer semantics to the web) versus the Semantic Web.
    Microformats still exists, and has had new content within
    the last year. Semantic Web got wrapped up under another banner
    ("data activity") and was frozen in 2013.
  * In my post [on microformats at Yahoo][pm] I linked to "this year's
    d.Construct" and those links still work **unmodified** because Clearleft
    had the foresight to bake the year in. Nice.
  * In the same post, links to Technorati no longer work (but presumably only
    for anyone in or near the EU, which I am) and redirect to [`/gdpr`][tr].
    That page says "We are working to enhance your experience!" a full three
    years after [GDPR][gdpr] became enforcable. The claim seems unlikely.


[rb]: /about/2020-rebuild
[w32]: /weeknotes/chips-for-week-32-2020
[w36]: /weeknotes/chips-for-week-36-2020
[tf]: https://github.com/norm/textframe
[lw]: https://en.wikipedia.org/wiki/Lightweight_markup_language
[md]: https://pypi.org/project/markdownify/
[wb]: https://web.archive.org
[uf]: /presentations/wsg-london/microformats
[pm]: /yahoo-europe/presenting-microformats
[tr]: https://technorati.com/gdpr
[gdpr]: https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
