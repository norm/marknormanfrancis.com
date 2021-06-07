```
published = 2021-06-07T09:57:14Z
type = 'article'
title = 'My potted history of making GIFs'
thread = 'making-gifs'
```

The original idea behind my [GIFs site][gifs] was that there were a bunch of
GIFs I wanted to use that were bad quality — low resolution, had janky
animation (low frames per second, or just slow sampling of the original
source), and often did not capture what I thought of as the right part. As I
used a specific GIF that wasn't good enough, or when I couldn't find what I
wanted at all, I would make my own.

But this was when I was making each one by hand using [GIF Brewery][brew].
There was a significant time cost to each, and it was harder than I liked to
save the config and reuse it again later if I wanted to tweak the GIF.
In 2014 I made and published just 18 GIFs. I did one more at a friend's
request in 2015. The inertia behind making a new GIF meant I just stopped.

<figure>
  <a href='https://gifs.cackhanded.net/babylon-5/war-without-end-ii/wrong-tool'>
  <img src="https://mnf.m17s.net/2021/06/07/wrong_tool.png" alt="Zathras telling Ivanova “This is wrong tool”" width="480" height="270"></a>
  <figcaption>
    Zathras telling Ivanova “This is wrong tool” — 
    <a href='https://gifs.cackhanded.net/babylon-5/war-without-end-ii/wrong-tool'>Babylon 5</a>
  </figcaption>
</figure>

But for a long time, I had a note in [Things][th] to investigate using
command-line tools to make GIFs. I knew it could be done, I just needed
some time on my hands to see what was involved, and how easy it would be
to put together a script to make GIFs.

## Automating things

Last June I had a moment of clarity. Flourish, my [website generator][fl], can
use a [TOML][toml] file as the source of a webpage. That TOML file can contain
extra keys that Flourish doesn't use without problems. I could keep the
configuration for the GIF in the same definition file as the website uses. All
I needed was to work out the command-line GIF generation and I should be able
to make and remake GIFs to my heart's content.

I found an article on the GIPHY engineering blog on
[making GIFs with FFmpeg][ff], which was very helpful as the basis of my
script. I had expected FFmpeg to be the basis of things, but I hadn't used
it much and had been confounded by trying to work out how to use filters.
Mostly, I'd just used it to convert and trim video.

More articles and forum posts helps solidify it in my head, especially a post
on [high-quality GIFs][hq], and I had the basis of making GIFs repeatedly. A
bit of work, and [in July last year][wk312020] I republished the site with
newly automated GIF making potentials, and fulfilled an old promise by making
a huge swathe of GIFs from [Lilo & Stitch][ls]. What would've taken me weeks
of effort in GIF Brewery now took me two afternoons. The hard part is getting
the timing of the GIF and the captions right. Changing my mind about the font
to use in the captions was a matter of a quick search and replace, then typing
`make` and waiting a few minutes.

<figure>
  <a href='https://gifs.cackhanded.net/screenrant-pitch-meetings/super-easy'>
  <img src="https://mnf.m17s.net/2021/06/07/super_easy_45.png" alt="A script writer saying “Super easy, barely an inconvenience”" width="480" height="270"></a>
  <figcaption>
    ”…super easy…” — 
    <a href='https://gifs.cackhanded.net/screenrant-pitch-meetings/super-easy'>Screenrant’s Pitch Meetings</a>
  </figcaption>
</figure>


## Getting to the one-a-day habit

I started by publishing the GIFs as soon as they were done. For example,
all of [Shatner of the Mount][SHATNER] published on 
[July 30th, 2020][20200730], the aforementioned Lilo & Stitch across three
days following that.

As it sunk in that I could make a GIF in mere minutes, I started doing one as
part of my morning routine. I kept that going, [mostly][mostly], throughout
2020. But around Christmas I took a break.

The longer I left it, the harder it became to get back into the habit
of making one a day. To crack this, I sat down and worked through
[Ghostbusters][gb] from start to finish, making the GIF each time I got to
a part of the film I had made a todo about. By the end I had
[48 new GIFs][48new]. I altered the GIFs site to not publish anything dated in
the future and queued up these new GIFs on Mondays throughout the rest of the
year.

Then I did [the Five Levels of Drinking][5levels], [Horizon Zero Dawn][hzd],
[Ted Lasso][tl] (nearly 200 of them, I might have a problem), and more.

I find it easier to sit down for a protracted period of time, go through the
video and make draft entries for each GIF with just rough timings, then go
back and polish the timings, then set the options to tweak colours, sizes,
compression, etc. to make it as small as I'd like.

And, well, here we are. I have a [git repository][repo] containing the
configuration to make 698 GIFs (as of 7th June, 2021). I have queued
posts through the year with only 36 days currently missing content,
and 112 as-yet unscheduled Ted Lasso GIFs.

<figure>
  <a href='https://gifs.cackhanded.net/ted-lasso/the-diamond-dogs/barbecue-sauce'>
  <img src="https://mnf.m17s.net/2021/06/07/barbecue_sauce_24.png" alt="Ted Lasso saying to himself “Barbecue sauce”" width="400" height="225"></a>
  <figcaption>
    “Barbecue sauce” — 
    <a href='https://gifs.cackhanded.net/ted-lasso/the-diamond-dogs/barbecue-sauce'>Ted Lasso</a>
  </figcaption>
</figure>



[gifs]: https://gifs.cackhanded.net
[brew]: https://gfycat.com/gifbrewery
[th]: https://culturedcode.com/things/
[fl]: https://github.com/norm/flourish
[toml]: https://toml.io/

[ff]: https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/
[hq]: http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html
[repo]: https://github.com/norm/gifs.cackhanded.net
[wk312020]: /2020/07/31/chips-for-week-31-2020
[ls]: https://gifs.cackhanded.net/lilo-and-stitch/
[SHATNER]: https://gifs.cackhanded.net/shatner-of-the-mount/
[20200730]: https://gifs.cackhanded.net/2020/07/
[mostly]: https://gifs.cackhanded.net/aliens/mostly

[gb]: https://gifs.cackhanded.net/ghostbusters/
[48new]: https://github.com/norm/gifs.cackhanded.net/commit/f1f3570baaef6af0eae1f0cbdd1e4a2a156f8b7d
[5levels]: https://gifs.cackhanded.net/larry-miller/5-levels-of-drinking/
[tl]: https://gifs.cackhanded.net/ted-lasso/
[hzd]: https://gifs.cackhanded.net/horizon-zero-dawn/
