```
title = "Chips for Week 29, 2020"
published = 2020-07-17T17:17:21Z
origin = "mnf"
type = "article"
subject = "weeknotes"
tag = [ "weekchips",]

[twitter]
first_tweet = '1284175370707775488'
last_tweet = '1284175386943852547'
contains_tweet = [
    '1284175370707775488',
    '1284175378551123968',
    '1284175380635688963',
    '1284175382212685824',
    '1284175383538147328',
    '1284175384662220801',
    '1284175385782095878',
    '1284175386943852547',
]
retweets = 0
favourites = 0
```

Another week, another [stack of chips](/2020/06/19/my-week-in-poker-chips).
This week’s chips look like this:

<p class='image'><img src='https://mnf.m17s.net/2020/07/17/EdJOspJWAAoiH6r.jpg' alt=''></p>

I spent Sunday morning going through all of my random todo lists, FIXMEs, entries in Things, and so on, to make a more definitive list of the things I might want to work on, rather than doing just what occurs to me on a given day.

Monday, after a lie-in, I started work on importing my Foursquare checkins to
my website. The code to fetch them was quick to write; the code to filter out
what I didn’t want to import took a while longer. Because it involved looking
at almost every checkin.

Tuesday was another lie-in and more figuring out what checkins to keep.
Finished that by the end of the day, but having a few thousand more entries
did show that [flourish](https://github.com/norm/flourish) would slow down a
lot for generating pages on the fly.

Wednesday, another lie-in and a morning of pottering about to clear my head. I
think best at a whiteboard, not sitting in front of a keyboard, so I did some
standing around. Then cracked on trying to speed flourish up.

Thursday I took the morning off to do some reading, and cook soup. Finished
the speed up work and went back to 4sq, importing images I’d added to a
handful of checkins.

And today I polished that all off and 
[got it committed](https://github.com/norm/marknormanfrancis.com/pull/2),
updated flourish with the 
[speed up](https://github.com/norm/flourish/commit/6a29c68e0afdd24dc4a0c891dd2ff9accece30d5)
and a couple of other bug fixes, then spent the afternoon tracking down 
[why the Atom generator would explode](https://github.com/norm/flourish/commit/e569f027f94003eadaa294cecb1831eb4100dda1).
