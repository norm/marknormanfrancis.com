```
summary = "Learning a new programming language isn't easy, but I'm making myself do it anyway."
title = "Weeknotes: 2015 Week 1"
origin = "mnf-v1"
type = "article"
published = 2015-02-16T23:25:46Z
updated = 2015-02-17T08:49:48Z
```

First week, I feel like I achieved very little. All I have to show to you is [three new commits][log] to the `flourish` repo, the end result of which looks like "my first go program". Which, to be fair to me, it is. 

I'm an old skool Perl programmer. In my first job after dropping out of university I was doing sysadmin things, help desk things and writing C software that interrogated printers to find out how many pages a print job had used to charge students automatically. My boss dug out some old terminals and a Spiderport (device that turned one Ethernet port into many serial ports) to use as print queue displays and tasked me with writing something to update those. After nearly two weeks of bashing my head against buffering problems, our [head of networking][abs] threw a Perl book at me and suggested I give that a go. Two days later I had it working.

That was two decades ago. I've been writing Perl ever since. I've also learnt other things along the way, such as PHP and python and pretend to have picked up ruby. But when I did something for myself, it is in Perl. I know my way around it way more than any other programming language. And whilst it is definitely showing its age, it still works and has a huge collection of well tested libraries, which, with [`cpanm`][cpanm], are easy to install.

Now, technically `flourish` is just for myself. I have no reasonable expectation of anyone else ever using it, except out of curiosity or to troll me. But I'm not going into this with the attitude that this is just another thing I bosh together and forget about.

So I chose [go][go]. Because as an end user, go means all you have to worry about is downloading the right binary. No mucking about with `pip`, `gem`, `cpanm`, `npm` or the rest. And because it is compiled and not interpreted, it is fast. Another static generator written in go is [hugo][hugo], which claims millisecond build times.

## Stack Overflow driven development

The problem with choosing a language I've never used before is just that. I've never used it before. I have *literally* no idea how to do anything. I know exactly how `flourish` should work, but I can't just start writing it as I could in Perl.

I have a go book, and their website, but I've always found I learn best by diving in the deep end and reading the books later once I have a handle on a language. So I'm at that amazingly frustrating stage where I know *what* the code should be doing but not *how* to make it do that in go. I could do it in Perl quite easily. But instead I sit and stare at my text editor and feel its emptiness mocking me.

Now, this is much easier to address in the time when Stack Overflow exists. I can Google pretty much any programming problem and get at an example. Many are even not entirely wrong. Read it, digest it, paraphrase it (paracode it?) and get something working. In a year I'll probably shudder at the code I'm writing now if I'm still writing go. But code working now trumps future perfection that I can't use.

So this week I've gone from 0 lines of go ever written to a couple of hundred. Most of them were wrong, and only the successful stuff survived rebasing and were committed. 

But … and this is the important part … I've written some code. I can scan a content directory for JSON files, find them and read them in. And I can even put comments into them and not care about trailing commas causing syntax errors.

## Inspiration

Also of note, it's quite exciting that I wrote [a bit of a moan at myself][w0] and somehow spurred at least two people into action too — both [Neil Kimmett][nk] and [Ann Carrier][pd] made similar statements on their blogs about getting back into doing things.

## Other bits and pieces

I also realised this week that there's another side project I am going to have to work on this year, but it's not much work and it's for a good cause. I'll have to do a bit more work on [boozehound][bh], which powers [eurovisiondrinking.com][edw] and [@eurovisiondrink][edt] before May 23. Only [95 days to go][days]!

## Next week

My aim for the next weeknotes entry is to have `flourish` aggregating and writing out a complete collection of all the JSON it finds, and creating a Makefile include that will in some manner describe build dependencies. If only I could find that on Stack Overflow.


[log]:https://github.com/norm/flourish/compare/week/2015/0...week/2015/1
[abs]:https://twitter.com/abs0
[cpanm]:https://github.com/miyagawa/cpanminus
[go]:http://golang.org
[hugo]:http://gohugo.io
[nk]:http://kimmett.me/2015/02/11/working-on-side-projects.html
[pd]:http://www.pixeldiva.co.uk/blog/category/blogging-like-its-2000
[w0]:http://marknormanfrancis.com/weeknotes/2015-week-zero
[bh]:https://github.com/norm/boozehound
[edw]:http://eurovisiondrinking.com
[edt]:https://twitter.com/eurovisiondrink
[days]:https://twitter.com/eurovisiondrink/status/567347180156227584