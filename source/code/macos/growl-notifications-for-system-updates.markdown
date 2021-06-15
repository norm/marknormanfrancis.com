```
title = "Growl notifications for system updates"
summary = """
I wrote a little shell script wrapper around softwareupdate which pops up a
Growl notification when there are new updates available for your computer.
"""
published = 2010-02-27T02:24:07Z
updated = 2021-06-12T08:54:45Z
updated_reason = 'Fixing broken links'
origin = "mnf-v1"
type = "article"
subject = 'code'
topic = 'macos'
previous_slug = [
    '/code/os-x/growl-notifications-for-system-updates',
]
```

Apple’s Software Update will run automatically, but only from an account which
has “Allow user to administer this computer” set. Running it manually from a
normal account will bring up an authorisation prompt, so it seems Apple
consider this to be a UI no-no to do automatically. As a consequence, any Mac
which is almost always used from a normal account will not get updates unless
that user is vigilant in checking manually.

I don’t give my primary account admin rights, as I consider this to be bad
form. I am not vigilant. In fact I am terribly forgetful. My Macs often
languish without updates for weeks, unless I catch a comment via some blog or
other.

Now, Software Update can also be run from the command-line. The command line
`softwareupdate -l` will list available updates, for example. However, doing
that in a normal account still brings up the authorisation window.

OS X is built on Unix. Unix allows you to run software automatically. Or, more
importantly, allows other accounts to run software automatically. Running that
command on your administrator account doesn’t bring up a prompt and does
successfully list outstanding software updates. Hurrah! So we can wire this up
into cron (or launchd if you’re perverse like that) to get notifications.


## Notifications should be for exceptions

Thing is, I like my notifications only when there’s actually something I need
to know and `softwareupdate -l` will still produce output when there’s no
updates. Also, apparently Apple counts the situation where there are no new
software updates as an actual error—the text “No new software” is output to
`stderr` when you are up to date. The correct behaviour, in my view, would be
total silence. I’ve said “list the updates available”; if there aren’t any, it
should be listing nothing. And Apple see fit to provide a copyright notice in
the output as well, which is oh so useful.

<div class='screen'>
  <img src='http://farm5.static.flickr.com/4065/4390574761_f4678f9d6f_o.png'>
  <em>Growl notification</em>
</div>

So I wrote a little [shell script wrapper][wr] around `softwareupdate` which
pops up a [Growl][gr] notification when there are new updates available for
your computer.

The script is available as a [gist on github][wr] if you want to look at it. If you want to use it yourself, keep on reading…


## Getting the script

First, you’ll need to log into an account that can run `sudo`. By default,
that’s any account with the ability to administer the computer. Open up
Terminal.app and enter the following commands to install the script:

1. `curl -L http://bit.ly/checksoftwareupdate -o checksoftwareupdate`
2. `chmod 755 checksoftwareupdate`
3. `sudo mv checksoftwareupdate /usr/bin`

As a quick aside—if you’re thinking "`/usr/bin` is not the right place for
it", you’re right. If you’re not thinking that, then happily ignore the next
paragraph.

The right place is `/usr/local/bin`. The problem is that `cron` has a
purposefully restricted environment, and the default `PATH` is just
`/usr/bin:/bin`. Whilst it is possible to alter that, it is beyond the scope
of what I want to write about here.


## Getting `growlnotify`

The script relies upon `growlnotify`, which is found in the Extras folder of
the Growl disk image. Download the latest version of [Growl][gr], mount the
disk image and run:

`sudo cp /Volumes/Growl-1.2/Extras/growlnotify /usr/bin`

If you look carefully the path does include the current version of Growl. If
1.2 is not the latest version when you do this, you will need to adapt
`/Volumes/Growl-1.2` suitably.


## Using the script

To use the script, it needs to be put into `cron`. The following commands are
very simple ways of creating a `cron` entry. Run *one* of the following
commands, depending on how often you want to check for updates.

*Be warned*: these commands *will overwrite* any existing crontab file. I assume that if you have used cron already, you know what you’re doing (so go do it).

* to check for updates *daily*:   
 `echo "00 12 * * * checksoftwareupdate" | crontab -`
* to check for updates *weekly*:   
 `echo "00 12 * * 1 checksoftwareupdate" | crontab -`
* to check for updates *monthly*:   
 `echo "00 12 1 * * checksoftwareupdate" | crontab -`

Once you’ve done that, you will get a Growl notification if, and only if, you have new updates available to be installed on your computer.


[wr]: https://gist.github.com/norm/314043
[gr]: https://growl.github.io/growl/
