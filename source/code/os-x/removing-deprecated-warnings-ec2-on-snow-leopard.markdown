```
title = "Removing the deprecated warnings from EC2 tools on Snow Leopard"
published = 2009-10-16T14:48:12Z
origin = "mnf-v1"
type = "article"
updated = 2021-06-12T08:54:45Z
updated_reason = 'Fixing broken links'
```

One thing about my recent [usage of EC2][fpb] is that the current set of tools
from Amazon come with a slight annoyance on Snow Leopard. Every command causes
a warning message:
"[Deprecated] Xalan: org.apache.xml.res.XMLErrorResources\_en\_US"
to appear, but the command works regardless.

Amazon will fix this soon, I’m sure, but it annoyed me enough to make it go
away. In the absence of any solutions found via Google at the time, I just
altered the `ec2-bin` script to filter out just these error messages, and my
[patch is on github][gh].

As it is more complex than [another solution][sol] that has later appeared on
the Amazon forums, I thought I’d explain a little further.

A simple solution is to redirect the output (which in Unix parlance is
[file descriptor][fd] (fd) 1, commonly referred to as stdout) and error
messages (fd2, stderr) of `ec2-bin` through a grep command to filter the
warning. My problem with this is that any other errors are now appearing on
stdout rather than stderr (this only matters to nerds like me, but not to most
people).

So, I first duplicate the original destinations of stdout and stderr to other,
numbered, file descriptors using the redirections (that’s the `3>&1` bits).
This means anything send to fd3 will appear on what is currently fd1.

Then the Java command is executed, with stderr redirected to stdout and stdout
redirected to fd3 (our previously captured duplicate of stdout). At first
glance, this would seem to imply that errors would also end up going to fd3,
but this is not the case as the redirections happen independently. Then I pipe
the now redirected output, which solely consists of the stderr stream, through
a `grep` command to remove the deprecated warning, and then send that to fd4,
the previously captured duplicate of stderr.

The end result is output appears on stdout, errors appear on stderr and I no
longer have to sit through the same tedious warning over and over. Phew!


[fpb]: /system-administration/fairly-paranoid-backups
[gh]: https://gist.github.com/200283
[sol]: https://forums.aws.amazon.com/message.jspa?messageID=148420#148420
[fd]: https://en.wikipedia.org/wiki/File_descriptor
