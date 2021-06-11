```
summary = "This week's activities include more bookmarking and a proper start on setting up my laptop's development environment."
title = "Weeknotes: 2015 Week 26"
origin = "mnf-v1"
type = "article"
published = 2015-08-10T10:29:19Z
```

Another week of working on "fun" projects.

## battleschool

I changed my mind about using [battleschool] to set things up on my laptop, so I spent some of the week configuring that for myself. The change of heart came around because it has built-in support for installing software to `/Applications`. I was originally thinking of using [homebrew-cask][cask] to install things, but I hadn't used it before. I found it installs apps somewhere else, then symlinks them to `/Applications` (well, actually it first symlinks to `~/Applications` but you can override that). Unfortunately for me, I am hard-wired now to switch apps with the keyboard (I use [LaunchBar]) and it didn't see the symlinks as apps. There's probably something I could've done to make it work, but I tried battleschool again and had my first app installed in a couple of minutes. Sold.

I've got a good start now on ansible playbooks that set up my laptop the way I like, which I'll be tidying up and publishing to GitHub once I work out how to properly arrange them.

[battleschool]: https://github.com/spencergibb/battleschool/
[cask]: https://github.com/caskroom/homebrew-cask
[LaunchBar]: http://www.obdev.at/launchbar

## More `evocation` work

I added some more niceties to [evocation], including:

* listing all archives of a bookmark, not just the most recent
* button to take a new archive
* button to delete the bookmark
* fetch new bookmarks from Pinboard automatically
* push bookmarks added in `evocation` to Pinboard

and fixed a few more bugs and niggles.

[evocation]: https://github.com/norm/evocation/

## Health

I also spent a couple of days not doing much because I had a bad gout attack and felt very sorry for myself (even though it was entirely my own fault for drinking more soda than I normally do to see if it would bring on an attack… which it did).