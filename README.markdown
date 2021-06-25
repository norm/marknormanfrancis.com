source for marknormanfrancis.com
================================

This is the source text, scripts, and configuration to build 
[my site][mnf] with [flourish][fl].

[mnf]: http://marknormanfrancis.com
[fl]: https://flourish.readthedocs.io


## import scripts

* [add_instagram][insta]

  Add a TOML source file for every instagram photo in an instagram data
  export. Uploads the images to S3.

* [find_tweets][find]

  Find tweets that match given criteria (eg. a number of likes/retweets, has
  a photo, etc) from a twitter data export.

* [add_tweets][tweets]

  Add a TOML source file for every tweet listed in `data/tweet_ids.toml`.

Run them with `honcho run script/...` to use environment variables from 
`.env`. Can be run repeatedly to refresh TOML (eg to update the likes
on a tweet).

[insta]: script/add_instagram
[find]: script/find_interesting_tweets
[tweets]: script/add_tweets


### Fetching archives

I included four screengrabs of previous iterations of this site in the
post on [finishing the 2020 restoration][rest]. These were fetched
from the [Wayback Machine][wm] using the script [get_archive][ga]:

    # fetch a site's homepage at a point in time
    script/get_archive 20111031 marknormanfrancis.com

    # fetch a post/file from a site at a point in time
    script/get_archive 20210531 marknormanfrancis.com /about-the-rebuild

The first argument is the date. This can as general as a year (`2021`), or as
specific as a day and time (`20210509021558`). The Wayback Machine will
redirect generic dates to the **next** available backup (eg. on my site,
`2020` fetches `20210128020922`, but `20200601` fetches `20200615174443`).

The script fetches the page and linked assets (images, CSS, JS), and
removes the toolbar inserted by the Wayback Machine.

[rest]: https://marknormanfrancis.com/about/finishing-the-2020-restoration
[wm]: https://web.archive.org/
[ga]: script/get_archive
