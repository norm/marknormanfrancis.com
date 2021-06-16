```
title = "flourish release 0.9.6"
published = 2021-04-22T04:59:48Z
origin = "github"
type = "release"
package = "flourish"
version = "0.9.6"
pypi_url = "https://pypi.org/project/flourish/0.9.6/"
tag = [ "repo-flourish",]

[release_event]
id = "16039242779"
type = "ReleaseEvent"
public = true
created_at = "2021-04-22T04:59:48Z"

[release_event.actor]
id = 32136
login = "norm"
display_login = "norm"
gravatar_id = ""
url = "https://api.github.com/users/norm"
avatar_url = "https://avatars.githubusercontent.com/u/32136?"

[release_event.repo]
id = 73727
name = "norm/flourish"
url = "https://api.github.com/repos/norm/flourish"

[release_event.payload]
action = "published"

[release_event.payload.release]
url = "https://api.github.com/repos/norm/flourish/releases/41816827"
assets_url = "https://api.github.com/repos/norm/flourish/releases/41816827/assets"
upload_url = "https://uploads.github.com/repos/norm/flourish/releases/41816827/assets{?name,label}"
html_url = "https://github.com/norm/flourish/releases/tag/v0.9.6"
id = 41816827
node_id = "MDc6UmVsZWFzZTQxODE2ODI3"
tag_name = "v0.9.6"
target_commitish = "main"
name = "0.9.6"
draft = false
prerelease = false
created_at = "2021-04-22T04:56:35Z"
published_at = "2021-04-22T04:59:48Z"
assets = []
tarball_url = "https://api.github.com/repos/norm/flourish/tarball/v0.9.6"
zipball_url = "https://api.github.com/repos/norm/flourish/zipball/v0.9.6"
body = "## 0.9.6 - 22 April 2021\r\n\r\n#### Bug fixes\r\n\r\n  * Months and days in date-based path segments are treated as\r\n    2-character segments, so now 4th June 2016 is generated\r\n    as `/2016/06/04` not `/2016/6/4`.\r\n"

[release_event.payload.release.author]
login = "norm"
id = 32136
node_id = "MDQ6VXNlcjMyMTM2"
avatar_url = "https://avatars.githubusercontent.com/u/32136?v=4"
gravatar_id = ""
url = "https://api.github.com/users/norm"
html_url = "https://github.com/norm"
followers_url = "https://api.github.com/users/norm/followers"
following_url = "https://api.github.com/users/norm/following{/other_user}"
gists_url = "https://api.github.com/users/norm/gists{/gist_id}"
starred_url = "https://api.github.com/users/norm/starred{/owner}{/repo}"
subscriptions_url = "https://api.github.com/users/norm/subscriptions"
organizations_url = "https://api.github.com/users/norm/orgs"
repos_url = "https://api.github.com/users/norm/repos"
events_url = "https://api.github.com/users/norm/events{/privacy}"
received_events_url = "https://api.github.com/users/norm/received_events"
type = "User"
site_admin = false
```

## 0.9.6 - 22 April 2021

#### Bug fixes

  * Months and days in date-based path segments are treated as
    2-character segments, so now 4th June 2016 is generated
    as `/2016/06/04` not `/2016/6/4`.
