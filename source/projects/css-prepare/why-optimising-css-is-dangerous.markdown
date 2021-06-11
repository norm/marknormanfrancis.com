```
series = "css-prepare"
summary = "An automated tool altering the structure and source order of your\nCSS should fill you with The Fear™. Here's why."
title = "Why optimising CSS is dangerous"
origin = "mnf-v1"
type = "article"
fixme = true
published = 2010-03-27T22:20:50Z
```

One of the basic principles that an effective web developer has to learn is [the cascade](http://www.w3.org/TR/CSS21/cascade.html#cascade) part of cascading style sheets. “So … explain the cascade to me.” is still my favourite question to ask when interviewing candidates for web development jobs (and if you don’t sweat, stammer and fumble your explanation, the chances are you really don’t understand it).


If the idea of letting an automated tool rewrite your CSS and potentially *change the source order* doesn’t doesn’t fill you with The Fear™, then you definitely don’t understand [the cascade](http://www.w3.org/TR/CSS21/cascade.html#cascade) properly.


The last rule of determining how CSS is applied to elements is that if two declarations have equal weight, origin and specificity, then *the last rule wins*.


This is why the following CSS would colour an `<h1>` element blue:



```
h1 { color: red; }
h1 { color: blue; }

```

They are otherwise equal statements, so the last one specified is used to style the element.


## Alphabetical order


Imagine you are using the common technique of using sprited images to provide icons to a list of links to bookmarking sites. Your CSS might look like:



```
#bookmarks .item { 
    background: url(sprite.png)
                no-repeat
                0 0;
}
#bookmarks .delicious {
    background-position: 0 -15px;
}
#bookmarks .pinboard {
    background-position: 0 -45px;
}
#bookmarks .magnolia {
    background-position: 0 -30px;
}

```

Running that code through a CSS optimiser that output the modified rules in *alphabetical order* would give you:



```
#bookmarks .delicious{background-position:0 -15px;}
#bookmarks .item{background:url(sprite.png) no-repeat 0 0;}
#bookmarks .magnolia{background-position:0 -30px;}
#bookmarks .pinboard{background-position:0 -45px;}

```

This would reset the background-position property for the item with the class `delicious`, giving it the wrong part of the sprite image. Of course, this is a slightly contrived example. But it illustrates the dangers of arbitrarily re-ordering code where order is significant.


The real solution is to use `#bookmarks li` instead of `#bookmarks .item` because then the class has greater specificity, regardless of the order it appears in the output style sheet.


## An explicit output order


After optimisation, my [CSS Prepare](http://github.com/norm/CSS-Prepare/) code will group the rule sets in the order elements, then IDs, then classes. And inside of each group, the rule sets are indeed output in alphabetical order. Whilst I could output them randomly, a guaranteed ordering makes testing the code much easier.


If you are writing your CSS well and using specificity meaningfully, this reordering should result in zero actual changes to the rendered document if you were to use [CSS Prepare](http://github.com/norm/CSS-Prepare/). But you should always test the output of any minifier before putting code live. Doubly so something that has the potential to change the meaning of your code.


