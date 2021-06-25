```
title = "Working with the History API"
published = 2012-07-12T09:39:00Z
origin = "artfinder"
origin_url = "artfindertech.wordpress.com/2012/07/12/working-with-the-history-api/"
origin_note = "An article I wrote for the now-retired Artfinder tech blog while I was working there."
type = 'article'
subject = 'web'
repost = true
tag = ['history-api',]
thread = 'artfinder-history-api'
todo = ['embedded-photo',]
```

<a href='/2012/06/22/the-history-api-yay'>
![The History API](https://mnf.m17s.net/web/history-api.jpg)
</a>

On the surface, the History API as specified in HTML5 should be trivial to use
for anyone with half-decent JavaScript skills. There is one of two methods to
call (`history.pushState` or `history.replaceState`) and one event to listen
for (`onpopstate`). Everything else is Your Website specific. And yet, there
are still plenty of things to confuse and frustrate developers.

This article shares our observations from working with it.


## A brief introduction to the History API

Firstly, you should check that the History API is actually available in the
browser.

    if ( window.history && history.pushState ) {
        // you must be this tall to ride
    }

Then you can add state when something happens on your page.

    function update_page () {
        var state = { 'stuff': [ 1, 2, 3 ] },
            title = 'More stuff',
            new_url = $(this).attr('href');
     
        history.pushState(state, title, new_url);
    }

    $('a.pushstateify').on('click', update_page);


Having provided a (fairly useless, admittedly) new state, you can now listen
for changes to the page state and update it as necessary.

    function handle_browser_navigate (jq_ev) {
        var event = jq_ev.originalEvent,
            new_state = event.state;

        // do stuff with the new state here
    }

    $(window).on('popstate', handle_browser_navigate);

So far, pretty easy.


### The conceptual problem with popstate

With the terms “push” and “pop”, the History API invites you to think of it as
a [stack][s]. You push new entries to the top of the stack as the user does
things. Then you get items popped off the stack as they press the back button.
Except … traditionally popping an item removes it from the stack.

Imagine that the user has navigated to a page, then triggered `pushState`
three times. The user holds the back button until a menu of all history items
appear, and they choose to go back two steps, not one. You do not get two
`popstate` events, only one containing the first state that was pushed. Then
they press the browser’s forward button. You get another `popstate` event,
this time with the second state that was pushed. Nothing is being “popped”
from the ”stack”.

Don’t mistake `popstate` for simply user has pressed back button. It is
actually a `newstate` event.

Further, if you don’t install a `popstate` handler, what happens when the user
presses their back button? **Absolutely nothing**. You have to write code to
handle the `popstate` events or their experience is broken.


### The browser problem with popstate

Further confusing the meaning of “pop”, the `popstate` event is also fired on
the initial page load, but without any state. This means you need to deal with
receiving `popstate` events that don’t contain a state.

    if ( event.state ) {
        // do stuff with the new state here
    }

### The original state problem with popstate

Imagine that the user has navigated to a page, triggered `pushState` once and
then press the browser’s back button. You will get a `popstate` event
**that doesn’t contain a state object**. So, technically, you can’t just
ignore a popstate event without state as it could be the event that says “put
the page back to it’s initial state”.


## How we use the History API on Artfinder

We use the History API along with some animation on the artwork page (eg.
[Marilyn by Andy Warhol][m]). Navigating to the next or previous work in the
current “stream” of art (such as all works by an artist, works in a gallery,
works in an event) slides the work into the centre, then updates the page
details.

### Fixing the initial state problem

After the check to see if the History API is available, the first thing we do
is store the state of the page by calling `history.replaceState` before
binding to the `popstate` events. Then we can safely ignore any events without
a state, and still handle when the user navigates back to the original URL.

### What is stored in the state object

Before animating, we fetch the new state from the server. This contains the
HTML for the new work of art and the previous/next links, the new page title,
and the new URL. This is then augmented with the direction of the animation
and a counter to say how many times we have animated.

The direction is added so we know whether to animate to the left or to the
right when getting a `popstate` event. The counter also tells us whether the
`popstate` is for one step backwards/forwards (which means we can animate the
slide across) or for more (in which case we fade out and back in).

### Repeatedly pressing the browser buttons

The one downside to performing an animation when the browser’s back/forward
button is pressed is that it takes time. More time than it takes for the user
to press the button again.

In the event of a `popstate` event firing whilst the previous is still being
dealt with, we turn off animations and reset the state of the page. It is
possible with repeated button presses in short succession for the `popstate`
events to collide and the final state of the page to be incorrect. This is
something we consider acceptable as a simple reload will fix it, but if you
are storing data more sensitive than a picture of a work of art you might want
to spend more time trying to deal with this eventuality.



[s]: https://web.archive.org/web/20120827010522/http://en.wikipedia.org/wiki/Stack_(abstract_data_type)
[m]: https://web.archive.org/web/20120827010522/http://www.artfinder.com/work/marilyn-andy-warhol/
