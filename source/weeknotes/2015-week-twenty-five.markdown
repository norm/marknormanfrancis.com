```
summary = "This week's activities include more bookmarks, redis pubsub to slack and some ansible roles."
title = "Weeknotes: 2015 Week 25"
origin = "mnf-v1"
type = "article"
published = 2015-08-03T11:10:16Z
```

Another week of working on "fun" projects.

## My bookmarking app `evocation`

Continuing on from last week, I fixed a couple of niggles, added better behaviour for adding new bookmarks with just the URL, added a differentiation between "production" and "development" (so I could run it for real on my laptop with my actual bookmarks without trashing them whenever I made a change). And, most importantly, made it look like a real thing rather than a bunch of placeholders.

![evocation preview](https://raw.githubusercontent.com/norm/evocation/64a97daf768670348bb666f000e7a4cbf830f2d9/evocation.png)

## pubsub-to-slack

As part of getting `evocation` running for reals, I wanted to know when new things were added in the background. I added the [publication of new bookmarks and archives][pub] to [redis pubsub][pubsub]. Then I made a little python script to [republish those into Slack][slack].

This means that I don't have to complicate `evocation` by having it know how to publish to Slack. Also if I think of other things I might want to do when a bookmark is added (eg also tell me via IRC, print it out, update a tally, etc) I don't need to add any more code to `evocation` in order to have that work.

[pub]: https://github.com/norm/evocation/commit/7dbd96403971d7510db6872080c7d6f38c0c12ed
[pubsub]: http://redis.io/topics/pubsub
[slack]: https://github.com/norm/slack-tools#pubsub-to-slack

## Setting up `*.dev` on my laptop

When I was working at [GDS][gds] I used [boxen][boxen] to setup my laptop. At my previous job I also used it, but much more half-heartedly. When you're not dealing with the many repositories, software requirements and personal options of a huge organisation, boxen really feels like too much.

Firstly, unless you [tell it otherwise][nope], you get a lot of stuff you may not need. Definitely not in my case.

Secondly, in order to do *anything*, you really need to know [Puppet][puppet]. If you work in a big organisation that uses boxen well (or you [follow one on github][gds-boxen]) then someone has probably done what you want, and you can just use their code. But if you don't or you're doing something new, and you don't know puppet, well… good luck with that. I just don't want to learn an obscure dialect of a tool I otherwise don't use to do something that I consider to be as simple as "run this script".

So I looked for alternatives for automatic OS X laptop setup. And then gave up, and started using ansible instead. I found ansible much more lightweight and easy to learn (although there's a tool built on top of ansible called [battleschool][battleschool] I didn't like how it decided to do things).

I'm writing a little script to set my Mac up how I like, but it's very basic so far. It will rely on roles, so here's two that fulfilled my need for the week, which was to have anything `.dev` resolve to localhost, so I could have my bookmarks on `bookmarks.dev` rather than `localhost:5000`. If I do any more work on the script, I'll write more about it later.

* [ansible-role-osx-dnsmasq][dnsmasq]
* [ansible-role-osx-nginx][nginx]


[gds]: https://www.gov.uk/government/organisations/government-digital-service
[boxen]: https://boxen.github.com
[nope]: https://github.com/norm/boxen/commit/e897c35d6dcd225863fd1e43b9f353af6781d117
[puppet]: https://en.wikipedia.org/wiki/Puppet_(software)
[gds-boxen]: https://github.com/alphagov/gds-boxen
[battleschool]: https://github.com/spencergibb/battleschool/
[dnsmasq]: https://github.com/norm/ansible-role-osx-dnsmasq
[nginx]: https://github.com/norm/ansible-role-osx-nginx