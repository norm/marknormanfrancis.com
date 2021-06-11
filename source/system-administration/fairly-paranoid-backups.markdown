```
subtitle = "I like to have my data backed up. I don't like people touching it."
title = "Fairly paranoid backups"
origin = "mnf-v1"
type = "article"
fixme = true
published = 2009-10-12T22:34:12Z
```

Backing up your data is never fun, but it is something you have to do. Many people concoct complex plans for backing up their data, but actually doing it rarely happens. Here’s a clue, if you’re not performing backups regularly, you don’t have a backup plan, just a fantasy. As [Jamie Zawinski says](http://www.jwz.org/doc/backups.html), if you don’t backup you should instead “learn not to care about your data.”


I do various things to keep my data safe, but I’d like to tell you about one thing in particular because it is non-trivial to create, but really easy to continue doing once it is setup.


## My requirements


I’m kinda paranoid when it comes to my computers. I don’t like people touching them. Also, I’ve never been that comfortable storing data on other systems, unless it’s already publicly visible data (such as my [photos on Flickr](http://www.flickr.com/photos/mn_francis/) or [code on github](http://github.com/norm/)). For example, I run my own mail server rather than using any hosted solution such as GMail.


That said, I do want to keep an offsite backup of many of my files, plus the data I keep on my own servers. Ooh, tension. A solution to this tension is to keep the data in an encrypted format.


Of course, it’s not always as easy as that. I also want to use a program called [rsnapshot](http://rsnapshot.org/) to keep rolling backups, not just one copy. This program uses [rsync](http://samba.anu.edu.au/rsync/) internally to keep the transfer of new files to a minimum. However, any changes to the original file will cause much, if not all, of the encrypted version to be completely transferred again. Encryption software exists that has been deliberately weakened to minimise data changes, such as [murk](http://murk.sourceforge.net/) or [rsyncrypto](http://sourceforge.net/projects/rsyncrypto/) (obviously, this is better than an unencrypted file, but it is still weaker encryption than you can otherwise achieve).


What I really want is files that are encrypted at destination, not source. The best way of achieving this is to use a file system that keeps data on the disk in an encrypted format.


I toyed with the idea of getting a disk-heavy/CPU light server, such as a [cheap VPS](http://www.lowendbox.com/) or other [low-end server](http://www.lowenddedi.net/) to store my backups, but it still proves to be quite expensive. Plus, I quite like the idea of having slightly more redundancy than that. So I chose to store my data within Amazon’s [elastic compute cloud](http://aws.amazon.com/ec2/) (EC2) infrastructure.


## My solution


In outline, my backup solution is to run rsnapshot on an EC2 instance writing to an encrypted [elastic block store](http://aws.amazon.com/ebs/) (EBS). This allows me to only have the backup server running when it is in use, and to know that my data is pretty much safe from prying eyes, even those that work for Amazon. It also costs less than running a server 24/7, even a remarkably cheap one.


First, I start up an Amazon Machine Image (AMI—the EC2 virtual machines) running Ubuntu Hardy (one of the [official Ubuntu AMI images](http://www.ubuntu.com/ec2)) and reconfigure it to my needs. This includes updating and installing extra software (rsnapshot, support for encrypted filesystems) and replacing the ubuntu account with my own. This running instance I [rebundle as my own image](http://alestic.com/2009/06/ec2-ami-bundle) so that I don’t have to alter the setup of the operating system every time I want to backup files.


Next I create an EBS volume big enough to contain all of the data I need backed up. Since you pay for the space you allocate for an EBS, it would be cheaper to size the disk for exactly the amount of storage needed. However, when you later need to store more, you’ll have to create a second EBS volume and migrate the data across. I chose convenience over cost, so even though my storage needs are around 120GB, I created a 200GB image. I configure the disk as an [encrypted volume](http://groups.google.com/group/ec2ubuntu/web/encrypting-mnt-using-cryptsetup-on-ubuntu-7-10-gutsy-on-amazon-ec2), format it with a new filesystem and mount the disk.


(Note: during this process, what looks like a serious error appears — "[Error inserting padlock\_sha](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/206129)". This can safely be ignored, as it is the software trying to use chips that assist with encryption, which are not available. The encryption still works, however.)


Lastly, I create an rsnapshot configuration file. I store this on the encrypted volume, not for any sense of security, but because it is likely to change over time and I don’t want to have to create a new AMI image every time I alter my backup schedule.


## Passwordless access to remote servers


Whilst rsnapshot can be used to backup remote directories (or databases, entire disks), it does not work unless rsync can connect to the remote machine without being prompted for a password.


It would be foolish of me to allow access to the root account over ssh, so I instead setup a second, [restricted rsync account](http://notes.endnode.se/2009/07/restricted-backups-using-rsync/) on each box which has a [fixed response to ssh connections](http://oei.yungchin.nl/2009/05/07/rsync-fixed-server-side-options/). Further, it has no password and can only be accessed with my [public key](http://sial.org/howto/openssh/publickey-auth/), so only works when I am logged in and have [forwarded my ssh agent](http://unixwiz.net/techtips/ssh-agent-forwarding.html).


## Running my backups


Having setup all of this, my backup procedure is:


1. Run an instance of my personal backup AMI image, and attach the encrypted EBS store.


2. `ssh -A` to the instance, to forward my main computer’s SSH agent details on.


3. Run `sudo rsnapshot /backups/config daily` on the instance.


4. Shut down the instance.




All of which I have wrapped up as [a function in my bash startup](http://github.com/norm/homedir/blob/master/etc/bash/rc/backup) (which links to the current copy from my github homedir project; this is *not usable* as a standalone script that you can copy, as it uses various features found in other parts of my homedir; it is provided as a reference for the entire backup procedure as code).


Yes, the downside of all of this is that my backups have to be run manually. But they happen pretty quickly (it takes less than half an hour to run on most days) and are, apart from issuing one command into a terminal window, entirely automated.


The upside is that my data on Amazon’s disks remains encrypted. Also, my backup server is inaccessible to attackers almost all of the time; and it randomly changes IP address every time I start it up. And as long as I remain confident that no-one has taken my SSH key and Keychain from my laptop and cracked the two different 20+ character passphrases on each, I can be pretty sure no-one can access it even when it is up, but for me access is seamless.


