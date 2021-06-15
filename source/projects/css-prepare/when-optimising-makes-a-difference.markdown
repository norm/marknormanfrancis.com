```
title = "When optimising CSS makes a real difference"
summary = "Given that I've said optimising CSS is slow and dangerous, why bother with it at all?"
published = 2010-03-28T00:36:19Z
origin = "mnf-v1"
type = "article"
series = "css-prepare"
updated = 2021-06-12T08:54:45Z
updated_reason = 'Fixing broken links'
subject = 'projects'
topic = 'css-prepare'
```

I was asked recently why bother with all the effort of optimising CSS.
Admittedly, the gains are not often that great against the much more trivial
act of removing whitespace and comments. If you are comfortable using
shorthands, you are probably already writing fairly well optimised CSS.
Imagine you have written a rule set such as:

    ul,ol,li {margin: 1em 0; padding: 0;}

I could save four bytes on that. But then, so could you if you would just stop
using the space bar so often.

Whilst it can definitely be used to find savings in existing big site-wide
style sheets, that is not where I imagine [CSS Prepare][cp] being used.


## Separation of concerns

In his excellent article [CSS rules of thumb][rt], Mike West writes:

> The general rule of thumb about documenting your code has a corollary:
> *you should use lots of CSS files*. You should be able to pick up a small,
> focused chunk of code, read through it, and understand more or less how it
> fits into the site as a whole.

This applies to practically all computer code, not just CSS. I remember being
taught this for the first time in computer programming classes back in 1987. I
remember consciously realising that this rule had actually saved me time and
effort on a big C project for the first time in 1992.

The “web site performance” obsession with CSS (and JavaScript) minification
has in many ways been a rod for some professional web developers' backs, as
without a proper build process for CSS you can end up working in exactly the
wrong way—in a single, massive stylesheet.

Text editors can lessen this pain, as can CSS-specific tools. But if you are
writing new rule sets into your site’s style sheet (singular) then you have a
problem, as Mike noted:

> If you find yourself sifting through a CSS file, trying to figure out where
> best to stick a new bit of code, you’re simply doing it wrong. The fewer CSS
> files you have, the larger they’ll be, and the more tempted you’ll be to
> simply stick some new rules on the end to save time.


## Inheritance

CSS has a form of inheritance in the cascade (and I don’t just mean the
`inherit` value many properties can be assigned). Take the following CSS:

    ul, ol, li { margin: 0; padding: 0; }
    li { margin-bottom: 0.5em; }

This is equivalent to declaring the `<li>` element’s styles as:

    li { margin: 0 0 0.5em; }

That’s fine, and very useful when it comes to using base stylesheets such as
the [YUI reset][rs]. You can be sure of what you are getting when you are
applying a property to an element that has been previously reset.

The problem comes when you redefine *everything* that is in that base
stylesheet, such as:

    li { list-style: none; }            /* in the YUI reset */
    li { list-style: disc outside; }    /* in your stylesheet */

The first declaration is essentially wasted. And so is the bandwidth used
downloading it, and the computing overhead in every user agent required to
parse it and determine that it does not apply.


## Optimising individual sections of your style sheet

If you could combine the YUI reset with your own base styles, and then apply
optimisation to *just that part*, you would end up with the above example just
being:

    li{list-style:disc outside;}

The optimisation has correctly removed the previous rule which is now
completely redundant. Now, whilst this is also going to occur when you
optimise an entire style sheet which contains both of the above styles, given
my previous [warning about optimising CSS][op], it should be obvious that you
are less likely to have issues occur when you optimise in small chunks, and
more likely to be able to track down the source of the problem if one does
occur.


## Hierarchical style sheets

The command-line script that will come with [CSS Prepare][cp] allows you to
create a hierarchy for your style sheets, to support the creation of
individually optimised sections.

Imagine several short CSS files saved in a tree structure as follows:

    /* in "css/site/first/typography.css" */
        body { font-family: "Palatino", serif; }
    /* in "css/site/second/typography.css" */
        body { font-size: 1.2em; line-height: 1.6; }
    /* in "css/site/typography.css" */
        body { line-height: 1.3; }
    /* in "css/typography.css" */
        body { font-family: "Helvetica", "Arial", sans-serif; }

Running the script with the options to turn on hierarchical file support, and
requesting the optimised output of `site/first/typography.css` would first
combine `css/typography.css`, `css/site/typography.css` and
`css/site/first/typography.css`, as if it were one style sheet like:

    body { font-family: "Helvetica", "Arial", sans-serif; }
    body { line-height: 1.3; }
    body { font-family: "Palatino", serif; }

Then that would be optimised, to generate an output style sheet of:

    body{font-family:"Palatino",serif;line-height:1.3;}

Likewise, requesting `site/second/typography.css` would combine the files
`css/typography.css`, `css/site/typography.css` and
`css/site/second/typography.css` to get:

    body { font-family: "Helvetica", "Arial", sans-serif; }
    body { line-height: 1.3; }
    body { font-size: 1.2em; line-height: 1.6; }

That would be optimised, to generate an output style sheet of (shown as two
lines simply for clarity):

    body{font-family:"Helvetica","Arial",sans-serif;
         font-size:1.2em;line-height:1.6;}

The nesting of the hierarchy is not restricted to just two levels as in this
example. If you work on only one site, you might just use a single directory,
in which you keep your overrides to other sources such as the [YUI reset][rs].

Missing files at any point in the hierarchy are not treated as errors, so even
if you create a seven-level hierarchy, you would not need to create seven
separate style sheets for every section of your site.

This allows you to easily provide default styles for each of the aspects of
your site, and to override them without incurring the unnecessary penalty of
including useless, ignored rule sets in your output style sheets.

Furthermore, by being able to create parent/child relationships between sites
easily by just organising things into subdirectories in the hierarchy, you can
share styles between sites that are closely related, without needing to
excessively copy and paste.


[cp]: https://github.com/norm/CSS-Prepare
[rt]: https://mikewest.org/2010/02/CSS-rules-of-thumb/
[rs]: https://web.archive.org/web/2010033100000/http://developer.yahoo.com/yui/reset/
[op]: /projects/css-prepare/why-optimising-css-is-dangerous
