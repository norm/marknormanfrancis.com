```
title = "Chips for week 14, 2021"
published = 2021-04-12T04:42:00Z
origin = "twitter-cackhanded"
type = "tweet"
original_url = "https://twitter.com/cackhanded/status/1381467616422854656"
twitter_account = "cackhanded"
tweet_id = "1381467616422854656"
retweets = 0
favourites = 2
tag = [ "weekchips",]
```

Another week, and I’m still [stacking chips][chips]. Last week’s
[chips][markers] looked like this:

[chips]: /2020/06/19/my-week-in-poker-chips
[markers]: /2020/08/22/my-weekchips-markers

<p class='image'><img src='http://mnf.m17s.net/2021/04/12/Eyv1dwZWYAQAUcl.jpg' alt=''></p>


## Reflection

At the start of the week, I wrote my high-level goals down:

1. Increase [Ezio Collection content][ezio] buffer
1. Create at least one post or video about how I make [Game Shows][gs] content
1. Import more content into this site
1. Add more Eurovision data

Well, I didn't touch the last one with a bargepole, once again. But I did
complete the other three. Not bad for a shorter bank holiday week.

## Update

I started the week by deciding how to pull in content from my
[home-made, artisinal GIFs][gifs] site. Sources of content in [Flourish][fl]
were very much one-to-one, one source file for one piece of content. I could
either pull in the GIFs and create one new file for each, … or …

For an entirely unrelated reason I had [previously added a CSV file][csv] of
all of the GIFs on the site. Well, if Flourish could understand a CSV file
as being a collection of sources, not one source, I could use that directly.

Despite being the only author of Flourish, it is something I've been working
on for years, and then only sporadically. The [first][first] commit of this
current version (long story, I'll tell you some other time) was made in 2016.
I do not hold it in my head, like you might a codebase that is your day job.
Whenever I add more to it, I often have to read back my own code, tests, and
the documentation to remember how it works before I can get started. Kids, it
is rarely a bad idea to add tests and documentation to your side projects,
even if you're the only one using them.

But that said, I was very confident there was nothing inherently stopping me
from making one file act as multiple sources. And by Wednesday morning I'd
added [CSV rows as source files][csvdiff] and [released][v095] version
`0.9.5` and started writing an import script to pull the GIFs CSV, and the 
template changes to have them appear in the site.

Feeling like a change of pace, I spent a day putting together the raw and the
cooked footage of the “Terror of the Sun” mission from [chapter 54][ch54] of
Horizon Zero Dawn. I'd made a couple of structural changes to the game's
cinematic footage when putting this video together, and wanted to talk about
it. But also it served as an excuse to watch that sequence again, as it is one
of my favourite moments in the game.

Until this week I had [just one][bts] behind the scenes video, illustrating
how I edit the branching conversations to alter and hopefully improve the
structure, and eliminate all the timewasting parts. I spent most of the time
in making that video figuring out how to make the timeline animation (I ended
up writing a bunch of numbers on a piece of A3 paper for the maths). That just
used game audio, there was no commentary.

I've been nervous about making more behind the scenes videos as it would
definitely involve some narration on my part, and like most people I don't
like hearing my recorded voice. But I felt I had been putting it off for too
long (months) and if I didn't do something soon, I never would. And I did
really want to talk about this scene now it had been published. So I recorded
myself talking about the video, with the pauses, umms, errs and all, typed it
up, and then rerecorded it. And ended up [sounding a bit lifeless][bts2]. My
best “NPR podcast” voice as my friend Worm put it. Hopefully that's broken my
nervousness and the next one will sound better.

After hitting publish on that, I finished the work of [pulling in GIFs][pull]
to this site.

Then I spent Friday writing a [script to import GitHub activity][gh] into this
site. And here's Friday's [GitHub activity][fri] preserved and published, as
an example. It can be a bit noisy, but it is part of my collecting stuff from
elsewhere to preserve approach, and I can't imagine anyone but me would bother
reading it anyway.

And Saturday morning I indulged myself by starting to make some Babylon 5 GIFs
(having just finished [rewatching the best of it][bab5]). Even in the HD
remastered version, there's a lot of visual noise in the video. And if there's
something that bumps up the file size of a GIF it is lots of rapid changes. So
I added the option to [use a denoise filter][dn] to my script that makes GIFs.
Another project where I have documentation and tests to reduce the struggle
to remember how it works later.


[ezio]: https://www.youtube.com/watch?v=RLUAJTX6Zxg&list=PL0lW90IMJShKw_Ut0omr_Lz4z51LbMbGg
[gs]: https://www.youtube.com/channel/UCI0KNfM-b2vXKPY4QwJ0_oQ
[gifs]: https://gifs.cackhanded.net/
[fl]: https://github.com/norm/flourish
[csv]: https://github.com/norm/gifs.cackhanded.net/commit/14690142d9ad54c84b2bcad612c31ddfeb3c5d5f
[first]: https://github.com/norm/flourish/commit/d2e81c4a982e49ff78c60a31c32fb47f27ce7858
[csvdiff]: https://github.com/norm/flourish/compare/23cd4e4fb79d35678dd0700a8a31f26776dc7221..c92a398083914f25df4998ff8e8334b7ed26de1e
[v095]: https://github.com/norm/flourish/releases/tag/v0.9.5
[ch54]: https://www.youtube.com/watch?v=xF2poDHo0hA
[bts]: https://www.youtube.com/watch?v=pJ3I97zJZS4
[bts2]: https://www.youtube.com/watch?v=t65w8tDQn-g
[pull]: https://github.com/norm/marknormanfrancis.com/commit/7a0603424090514362f01b4fbdc1f4eb21cb55e1
[gh]: https://github.com/norm/marknormanfrancis.com/blob/main/script/add_github_events
[fri]: /2021/04/09/github_activity
[bab5]: https://twitter.com/cackhanded/status/1380871626871431169
[dn]: https://github.com/norm/gifs.cackhanded.net/commit/fe8ed67b4d50c27836f7a98790a3f8126ea7d39f