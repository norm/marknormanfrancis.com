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