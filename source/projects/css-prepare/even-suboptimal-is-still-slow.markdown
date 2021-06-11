```
subtitle = "Well, it is when you've got fourteen thousand properties to sort through"
title = "Even suboptimal CSS optimising is still too slow"
origin = "mnf-v1"
type = "article"
fixme = true
published = 2010-03-19T00:28:37Z
```

In my last post "[suboptimal CSS parsing](/projects/css-prepare/suboptimal-css-optimising)", I talked about how much faster it was to compare the savings to be made by taking rule sets with properties in common (sharing a `margin: 0;` rule, for example) rather than doing an exhaustive tree search to find the shortest, most perfect solution. It was what you might call a “quick and dirty” solution.


Quick, not so much.


## Testing


So, as part of my [CSS pre-processor](http://github.com/norm/CSS-Prepare/) project I have [a few tests](http://github.com/norm/CSS-Prepare/tree/master/p5-CSS-Prepare/t/) written to ensure both that I am correctly parsing CSS and that when I recombine it I am achieving the smallest output. These generally work on tiny fragments of CSS, that test individual features. For example, testing that a shorthand of `margin: 5px 0px;` is being correctly interpreted as if it were the longer declaration block:



```
margin-top: 5px;
margin-right: 0;
margin-bottom: 5px;
margin-left: 0;

```

This makes sure I am determining the intent correctly. I can also test that given such a block, I do output it in the correct shorthand form.


Having got to a state where I support most of [CSS 2.1](http://www.w3.org/TR/CSS21/) (the parts I’m missing at the time of writing this are support for @media blocks, @import rules and anything I’ve stupidly missed whilst working my way through the specification), I am starting to write tests for longer blocks of CSS to test the optimising code rather than the parsing/output.


To aid this, and to find any parsing problems I still have by using real world CSS and not sterile laboratory code, I made a start on the command line script which will take a bunch of CSS fragments and concatenate and minify them into one output file.


I asked a few of the web developers I worked with whilst I was at Yahoo! if they could give me some complex CSS to test this with. [Mike West](http://mikewest.org/) was very helpful in pointing me towards a *massive* stylesheet that his current employer [sueddeutsche.de](http://www.sueddeutsche.de/) has.


After fixing a few bugs and edge cases that this stylesheet brought up (such as not interpreting [an empty block](http://github.com/norm/CSS-Prepare/commit/e0da0314b4b478f2d9ca5fc62e5ae110e7cc8106) as being part of the selector), my code will now successfully parse it. And try to optimise it. For all I know it will too, if I let it run for long enough. After eight hours of running I got bored (especially as I hadn’t put in any feedback so I had no idea how close to completion it was) and killed it.


This stylesheet has 13,954 selector/property pairs. And the way the code I described before works, every time I combine something I have to recalculate the next possible saving. That, again, is a *lot* of calculations.


Now, the way I am designing my code to be used, this is not a scenario you would actually hit. You are supposed to use the code to *create* the very large single stylesheet from many smaller files, which are optimised in isolation as you go along.


(I’ll explain this design, and why it’s important, in more detail in a later post. And in the code’s documentation, once I get around to writing that too.)


That said, this scenario is bound to crop up. And I don’t want anyone bad-mouthing my code because “it never returns anything”. So I’ve implemented a threshold, and if the stylesheet has more than that threshold’s worth of properties, a third, even more suboptimal (subsuboptimal?) optimisation algorithm is used.


All this does is group every pair by the selector, and then combine any selectors which have matching properties. This will miss many of the optimisations that could be had by taking apart a declaration block with many properties and combining those individual properties with other blocks instead. However, it will still create a significant saving in most large stylesheets.


Like last time, this suboptimal strategy runs in a tiny fraction (at least one ten-thousandth) of the time, and that against a time that wasn’t even a completed run against the stylesheet.


## A working example


The [sueddeutsche.de](http://www.sueddeutsche.de/) stylesheet I mentioned before is 231,641 bytes. There are around 300 comments, and plenty of both horizontal and vertical whitespace that can be trimmed. I ran this through both the [YUI compressor](http://developer.yahoo.com/yui/compressor/) and my code, to compare.


(If you examine the source to the CSS part of the YUI compressor it is quite simple, just a handful of regular expressions. It trims all excess whitespace; *adds* semicolons where they are missing at the end of declaration blocks; removes any units on zero-length values; shortens `rgb()` colour values to hex notation; and shortens 6-character hex colours to 3-character where possible.)


YUI gives a compressed version of 189,217 bytes, making it nearly 82% of the size, a saving of nearly one fifth. It also takes around two seconds to run on my MacBook Pro.


My version (which admittedly may still have problems, so this is only a rough guide to the savings possible) comes out at 160,321 bytes, making it under 70% of the size, a saving of over one quarter and nearly one third. This takes around four seconds.


And this is just the even quicker, even dirtier method. Imagine how much bandwidth could be saved by leaving computers crunching CSS—it could probably total a few megabytes per CPU year!


