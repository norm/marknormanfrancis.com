```
title = 'Rebuilding hasworn'
published = 2021-08-22T10:28:25Z
subject = 'projects'
topic = 'hasworn'
thread = 'hasworn'
origin = 'mnf'
type = 'article'
tag = [
    'repo-hasworn',
]

image = 'https://mnf.m17s.net/projects/hasworn/2021-08-22.hasworn.1024.jpg'

[thumbnail]
480 = 'https://mnf.m17s.net/projects/hasworn/2021-08-22.hasworn.480.jpg'
200 = 'https://mnf.m17s.net/projects/hasworn/2021-08-22.hasworn.200.jpg'
```

<img src='https://mnf.m17s.net/projects/hasworn/2021-08-22.hasworn.480.jpg'
width='480' height='300' alt=''> This is the first [in a series of
articles][th] about `hasworn` — the site I run to catalogue which tshirt I
wear on any given day. The project is open-source and [published on
Github][gh], and my wearings can be found at [norm.hasworn.com][nhw].

[th]: /threads/hasworn
[gh]: https://github.com/norm/hasworn/
[nhw]: https://norm.hasworn.com/


## In the beginning…

On the 31st of May, 2011 I registered a domain `hasworn.com`, with the idea
of using it to track things I had worn. Specifically, my tshirt collection.

On the 3rd of September, 2012 I tracked my first tshirt. I did this by posting an
image of it to Instagram. Over the next couple of years I posted more
tshirt images as I wore them. As any individual tshirt came around again,
I would sometimes post to it to Twitter, including the link to the original Instagram post.

On the 16th of July, 2015, I started building a django website to track
tshirt wearings, but only four days later I got bogged down in trying to
support logging into it from twitter, and let that code lapse.

On the 9th of May, 2018, **seven years** after registering the domain,
I started a new django project, and focused on just enough database to
log wearings. I posted a link to my log publicly the [next evening][t].

[t]: https://twitter.com/cackhanded/status/994678595124686848

I did some more work on it over the new few weeks. Later, I started adding
the code to support images in the app (rather than hard-coded image
locations) I broke something, and managed to `git rebase` myself into a
mess. I stopped working on the app, but continued adding wearing
information into the database.

## And now…

<figure>
  <a href='https://mnf.m17s.net/projects/hasworn/2021-08-22.hasworn.1024.jpg'><img src='https://mnf.m17s.net/projects/hasworn/2021-08-22.hasworn.480.jpg' 
    width='480' height='300' alt=''></a>
  <figcaption>
    <a href='https://norm.hasworn.com/'><i>norm.hasworn.com</i></a> v2, August 2021
  </figcaption>
</figure>

Over the past month, I've been rebuilding it from scratch, this time trying to
lay a solid foundation for being able to work on it piecemeal. As I'm no
longer unemployed, for any of my side projects need to see further development
they need to be in a position where I can do small things in the odd bits of
time I have, rather than expecting to power through them in my time off.

It's in a position where I can develop it locally, commit my changes and
push them to Github, and the production site will be automatically redeployed.
This was half of my previous problem stalling work on hasworn; I had a mess
of half-deployed code and too many manual steps.

Now it's in quite a good state, with a few caveats:

* the site is still norm-only; it does support multiple users, but
  there's no way to register new ones without my intervention
* the site only supports the clothing logged to be tshirts
* the design is based around ideally one thing per day

If you're someone who already meticulously notes the tshirts you wear on a
daily basis, or want to become someone who does that, and don't mind doing it
in public,
<a href='https://twitter.com/intent/tweet?text=@cackhanded+I+would+like+to+use+hasworn+pls'>let me know</a>.
