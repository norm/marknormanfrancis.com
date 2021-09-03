```
title = 'The static pages of hasworn'
published = 2021-09-03T10:43:56Z
origin = 'mnf'
type = 'article'
subject = 'projects'
topic = 'hasworn'
image = 'https://mnf.m17s.net/projects/hasworn/the-static-pages-of-hasworn.jpg'
tag = [
    'repo-hasworn',
]

[thumbnail]
200 = 'https://mnf.m17s.net/projects/hasworn/the-static-pages-of-hasworn.jpg'
```

## High level

At its core, hasworn is a fairly simple django CRUD application. It has a very
light data model (people, items of clothing, when people have worn said
clothing). It is running on a t3.micro AWS EC2 instance, using docker-compose
to connect postgres to django, and nginx as a webserver and reverse proxy.
Not an unusual pattern.

However, when you are browsing [norm.hasworn.com][nhw], you are looking at
static generated pages, being served directly by nginx. There is no hit to the
database.

<figure>
  <img src='https://mnf.m17s.net/projects/hasworn/the-static-pages-of-hasworn.jpg' 
    width='800' height='450' alt=''></a>
  <figcaption>
    the moving parts of hasworn
  </figcaption>
</figure>

From one perspective, not hitting the database every time a page is served
reduces the CPU requirements, which enables me to run this site on the
smallest instances, costing me very little. As a side project, I really don't
want to be spending vast sums when I don't need to.

But that way of describing it is arse-backwards. I didn't choose to do it this
way to save money. I can run it on a cheap server **because** I chose to do it
this way up front.


## Why static pages

Essentially, this is a very slowly changing site. Unless there's a new user
adding in a lot of historical wearings, on any average day each user would add
one wearing (maybe a small handful if they were logging everything they wore
and I had bothered to add types of clothing beyond tshirts; ten or so if they
were fancy and changed for dinner).

Anyone requesting my hasworn summary page between the time I update it in the
morning and the following morning should get the exact same page. Nothing has
changed.

There is no need to query the database for the twelve most recently worn
tshirts again. There is no need to recompute the average time between wearings
of all of the tshirts and order that by the shortest value (a complete scan of
every registered wearing, more than 3,000 database rows as I write this).
There is no need to recalculate which tshirts I have worn the most often.
Those numbers **do not** change until I put more information into the
database.

Therefore the HTML does not change, either. So I can cache the result of
generating the page. And what is the easiest cache to use? The filesystem. I
don't need another service running, another thing to have to configure and
monitor. A server reboot doesn't empty the cache. And it is more than fast
enough for my needs. Plus, the server has around a quarter of a gigabyte of
RAM free, so many thousands of pages can end up fully cached in memory.

The individual wearer homepage (eg [mine][nhw]) takes between 1.5 and 2.2
seconds to generate on a quiescent server. It takes nginx less than 50
milliseconds to serve that HTML. Nginx can serve the page more than three
hundred times in the same period that it takes django to generate the page
from scratch. And far more than that when the server is busier and the page
generation would take logner.

Is it more effort to write the code to create static pages and save them to
disk than it would be to serve the page from django? Yes, but it wasn't
substantially more effort than it would have been to add the same pages to
django instead.


