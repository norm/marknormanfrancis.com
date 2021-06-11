```
subtitle = "An Applescript for setting my away status."
title = "Going away"
origin = "mnf-v1"
type = "article"
fixme = true
published = 2006-09-21T07:50:00Z
```

So, recently I wrote about [my lovely new mobile](/gadgets/nokia-n80-review). One thing about it that’s not so lovely is the lack of support in [Salling Clicker](http://www.salling.com/Clicker/mac/) for third generation Series 60 phones.


I became very used to just being able to walk away from my Mac and having several things automatically happen, including the screensaver starting (so no-one can monkey with my computer), iTunes pausing and Adium setting an “away” status. Now, not so much.


So, I wrote myself a little bit of AppleScript magic, and using [Quicksilver](http://quicksilver.blacktree.com/) bound it as a trigger to Command-Escape. Now things happen nearly automatically—I just have to remember to bosh that key combination as I walk away.


The only problem I have with it currently is detecting when I’ve really returned. I’m just testing for the screen saver going away, but that also happens if someone presses a key or moves the mouse. I don’t yet know how to detect that I really have unlocked the computer. But it’s a good start.


If you’d like to use it, either [grab the compiled version](http://bumph.cackhanded.net/lock_screen.scpt), or copy and paste the code below into script editor and save it somewhere useful on your machine.



```
-- no point doing anything if the screensaver is already running
tell application "System Events"
    set screen\_saver to (exists process "ScreenSaverEngine")
end tell
if screen\_saver then
    return
end if

-- first off, start the screensaver 
-- (everything else can happen after this, so we can be confident of starting 
-- the script and just walking away)
tell application "SEC Helper"
    start screensaver
end tell

-- capture the current state of the computer, for restoration later
set screen\_saver to true
tell application "Adium"
    set status\_message to (my status message)
    set status\_type to (my status type)
end tell

-- capture the current state of iTunes
set itunes\_playing to false
tell application "SEC Helper"
    set itunes\_running to check application availability "iTunes"
end tell
if itunes\_running then
    tell application "iTunes"
        if player state is playing then
            set itunes\_playing to true
            pause
        end if
    end tell
end if

-- set the "away" status in Adium, but only if you are signed in and available
tell application "Adium"
    if status\_type is available then
        set my status type to away
        set my status message to "Not at my computer"
    end if
end tell

-- now loop, until the screensaver has finished (user has returned)
repeat while screen\_saver
    delay 5
    tell application "System Events"
        set test\_ss to (exists process "ScreenSaverEngine")
        if test\_ss is false then
            set screen\_saver to false
        end if
    end tell
end repeat

-- restore Adium's state
tell application "Adium"
    set my status type to status\_type
    try
        set my status message to (status\_message)
    on error
        set my status message to ""
    end try
end tell

-- restore iTunes if it was paused
if itunes\_playing then
    tell application "iTunes"
        play
    end tell
end if

```

