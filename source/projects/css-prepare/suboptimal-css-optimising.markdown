```
summary = "When optimising CSS, there is the right way and then there's the\ncorrect way."
title = "Suboptimal CSS optimising"
origin = "mnf-v1"
type = "article"
fixme = true
published = 2010-03-14T11:43:20Z
```

Recently, I have been working on a personal project, writing code to [pre-process CSS](http://github.com/norm/CSS-Prepare/). Yes, plenty of those exist already, but I want to reinvent the wheel to see if I can make it rounder. Or at least, rounder for me.


For one thing, I want to write actual CSS, not some [crazy nonsense like Sass](http://sass-lang.com/) (“Sass does away with the unnecessary brackets and semicolons of CSS”—unnecessary as long as you’re willing to change the syntax and make vertical whitespace significant). But I digress.


As part of this project, I’m writing some code to optimise CSS when a processed stylesheet is output. All of the usual stuff such as using shorthands, minimising whitespace, removing comments.


But here’s one little trick: CSS can also be re-arranged if you are careful. As a simple, fairly obvious example:



```
div { margin: 0; }
li { margin: 0; }
div { padding: 0; }

```

Because of the cascade, both rule sets that target `div` are used when calculating the layout. So, this could also be written:



```
div { margin: 0; padding: 0; }
li { margin: 0; }

```

But equally, this could be written by combining the selectors to make just one `margin: 0;` rule set:



```
div, li { margin: 0; }
div { padding: 0; }

```

The only question is which way produces the smallest output (it’s the latter, as repeating `margin: 0;` is longer than repeating `div`).


## Optimising the “correct” way


As you can see, there are three routes to choose from when adding a new declaration whilst trying to optimise the size of your CSS. The selector can be added to an existing declaration block which contains only that declaration (exact matches for both the property and value being set), or the declaration can be added to a rule set which contains only that selector, or the declaration can be added as a new rule set.


Applying this logic to the above example, we have the following steps to determine the shortest output:


1. add `div { margin: 0; }` as a new rule set


2. try adding `li` to the selector of the rule set, then:


	1. add `div { padding: 0; }` as a new rule set, because it cannot be added to the existing rule set, nor by adding `div` to the selector of an existing `padding: 0;` declaration.
	
	
	2. calculate the length of the result
3. try adding `li { margin: 0; }` as a new rule set, then:


	1. add `padding: 0;` as a new declaration in the `div` declaration block.
	
	
	2. calculate the length of that result
	
	
	3. add `div { padding: 0; }` as a new rule set
	
	
	4. calculate the length of that result


Of the three results, 3.2 is the smallest. This is pretty easy to calculate. The problem comes that, as you add more rules, things start to slow down dramatically. How slow? Well, in a test stylesheet with only *twenty-six* declarations, it took my MacBook Pro nearly four hours. The mathematically inclined amongst you, gentle readers, will know why.


Although my description above has three outcomes for each new declaration, the code I was running was a simple if/else branch which automatically encompassed adding a new rule set because of the data structure being used.


So, for the first declaration, two outcomes had to be calculated. For the second, four outcomes. For the third, eight outcomes. And so on. For all twenty-six declarations, the total number of calculations performed a smidgen over *sixty-seven million* outcomes had to be calculated.


After four hours, the resulting stylesheet was as short as it could be. The code found a combination that I hadn’t seen when writing the test to determine if it had produced the smallest possible stylesheet, so was actually smaller than I predicted by ten bytes. But it’s a little too slow, given it took me only five minutes to optimise it by hand.


Sure there are code optimisations I could then make, such as bailing out of a calculation branch if you are already larger than the smallest result found so far. But that’s not going to save all that much processing time.


## Optimising the faster way


So I needed a quicker method if this code was ever to be used on stylesheets for large sites that commonly have hundreds, if not thousands, of declarations.


The method I’ve adopted is to group the stylesheet by the declarations, so for the example above, I would have an array like so:


* `margin: 0;`


	+ `div`
	
	
	+ `li`
* `padding: 0;`


	+ `div`


If multiple declarations share selectors (like `div` in this example) I calculate if combining them would be a saving over the automatic saving from having multiple selectors on the declaration. If it is shorter, I rearrange the data structure to reflect this.


So, still using the same example, were it to be shorter, there would be a new "`margin: 0; padding: 0;`" declaration in the data structure.


Once there are no more savings to be made that way, the structure is ready to be assembled into a stylesheet and output.


## Optimising the right way


I ran this new code against the same test stylesheet with 26 declarations. It found the same result, and took less time. I say “less time”, what I mean is less than a second, which is about one fifty-thousandth of the original time.


I knew that the branching version would be prohibitively slow when I wrote it, but I was curious if it could find something smaller than my fast method, in order to improve my code.


It’s possible that on large stylesheets the slower, rigorous version would find savings that the quicker method might not. But I’m not willing to wait over a trillion years for my computer to calculate the outcome in order to find out.


