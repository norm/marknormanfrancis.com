```
summary = "This week's activities are about bending computers to my will."
title = "Weeknotes: 2015 Week 27"
origin = "mnf-v1"
type = "article"
published = 2015-08-17T15:13:59Z
```

A quiet week with only a small amount of computing, as it was mostly occupied by having the house repainted and moving furniture around and around.

## Bending computers to my will

As I [mentioned last week][w26], I started using [battleschool] to set up my computer. But I quickly became frustrated with the idea of having *one* setup control only *one* computer for *one* user. I have multiple computers, and I do want them set up in different ways with different software. So I wrote a wrapper around battleschool, called [bend].

Instead of creating the `config.yml` file and running `battle`, you would create files for things that apply to every computer/user, and more specific files for hosts and users. Then running `bend` creates the merged configuration and runs `battle` for you. It is also opinionated in the same way I am that config files live in `~/etc/thing` not `~/.thing` (at least by default). You can see [my setup on GitHub] for an example of how to use bend.

Why bend? Well, because it bends my computers to my will, but also partly because I name my computers after nicknames for being lefthanded (southpaw, etc), so it amuses me to setup my laptop by typing the command "[bend sinister]".

[w26]: /weeknotes/2015-week-twenty-six
[battleschool]: https://github.com/spencergibb/battleschool/
[bend]: https://github.com/norm/bend
[my setup on GitHub]: https://github.com/norm/bend-configuration
[bend sinister]: https://en.wikipedia.org/wiki/Bend_(heraldry)#bend_sinister