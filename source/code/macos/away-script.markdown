```
title = "Going away"
subtitle = "An Applescript for setting my away status."
published = 2006-09-21T15:50:54Z
updated = 2021-06-12T08:54:45Z
updated_reason = 'Fixing broken links'
origin = "chnet"
origin_url = 'cackhanded.net/mac/away_script'
type = "article"
subject = 'code'
topic = 'macos'
previous_slug = [
    '/code/os-x/away-script',
]
```

So, recently I wrote about [my lovely new mobile][mb]. One thing about it that’s not so lovelœy is the lack of support in [Salling Clicker][sc] for third generation Series 60 phones.

I became very used to just being able to walk away from my Mac and having
several things automatically happen, including the screensaver starting (so
no-one can monkey with my computer), iTunes pausing and Adium setting an
“away” status. Now, not so much.

So, I wrote myself a little bit of AppleScript magic, and using
[Quicksilver][qs] bound it as a trigger to Command-Escape. Now things happen
nearly automatically—I just have to remember to bosh that key combination as I
walk away.

The only problem I have with it currently is detecting when I’ve really
returned. I’m just testing for the screen saver going away, but that also
happens if someone presses a key or moves the mouse. I don’t yet know how to
detect that I really have unlocked the computer. But it’s a good start.


If you’d like to use it, either <del>grab the compiled version</del>, or copy
and paste the code below into script editor and save it somewhere useful on
your machine.

    -- no point doing anything if the screensaver is already running
    tell application "System Events"
        set screen_saver to (exists process "ScreenSaverEngine")
    end tell
    if screen_saver then
        return
    end if

    -- first off, start the screensaver 
    -- (everything else can happen after this, so we can be confident of starting 
    -- the script and just walking away)
    tell application "SEC Helper"
        start screensaver
    end tell

    -- capture the current state of the computer, for restoration later
    set screen_saver to true
    tell application "Adium"
        set status_message to (my status message)
        set status_type to (my status type)
    end tell

    -- capture the current state of iTunes
    set itunes_playing to false
    tell application "SEC Helper"
        set itunes_running to check application availability "iTunes"
    end tell
    if itunes_running then
        tell application "iTunes"
            if player state is playing then
                set itunes_playing to true
                pause
            end if
        end tell
    end if

    -- set the "away" status in Adium, but only if you are signed in and available
    tell application "Adium"
        if status_type is available then
            set my status type to away
            set my status message to "Not at my computer"
        end if
    end tell

    -- now loop, until the screensaver has finished (user has returned)
    repeat while screen_saver
        delay 5
        tell application "System Events"
            set test_ss to (exists process "ScreenSaverEngine")
            if test_ss is false then
                set screen_saver to false
            end if
        end tell
    end repeat

    -- restore Adium's state
    tell application "Adium"
        set my status type to status_type
        try
            set my status message to (status_message)
        on error
            set my status message to ""
        end try
    end tell

    -- restore iTunes if it was paused
    if itunes_playing then
        tell application "iTunes"
            play
        end tell
    end if


[mb]: /gadgets/mobile-phone/nokia-n80-review
[sc]: https://web.archive.org/web/2006123100000/http://www.salling.com/Clicker/mac/
[qs]: https://web.archive.org/web/2006123100000/http://quicksilver.blacktree.com/
