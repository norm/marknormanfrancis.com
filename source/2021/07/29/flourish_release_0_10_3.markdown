```
title = "flourish release 0.10.3"
published = 2021-07-29T06:01:25Z
origin = "github"
type = "release"
package = "flourish"
version = "0.10.3"
pypi_url = "https://pypi.org/project/flourish/0.10.3/"
tag = [ "repo-flourish",]

[release_event]
id = "17349035580"
type = "ReleaseEvent"
public = true
created_at = "2021-07-29T06:01:25Z"

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
url = "https://api.github.com/repos/norm/flourish/releases/46951258"
assets_url = "https://api.github.com/repos/norm/flourish/releases/46951258/assets"
upload_url = "https://uploads.github.com/repos/norm/flourish/releases/46951258/assets{?name,label}"
html_url = "https://github.com/norm/flourish/releases/tag/v0.10.3"
id = 46951258
node_id = "MDc6UmVsZWFzZTQ2OTUxMjU4"
tag_name = "v0.10.3"
target_commitish = "main"
name = "0.10.3"
draft = false
prerelease = false
created_at = "2021-07-29T06:00:23Z"
published_at = "2021-07-29T06:01:24Z"
assets = []
tarball_url = "https://api.github.com/repos/norm/flourish/tarball/v0.10.3"
zipball_url = "https://api.github.com/repos/norm/flourish/zipball/v0.10.3"
body = "## 0.10.3 - 29 Jul 2021\r\n\r\n#### New\r\n\r\n  * The preview server can now serve your custom 404 page.\r\n  * Adds an option `--max-invalidations` to control how many paths to\r\n    invalidate in CloudFront when uploading. Too many paths will end up being\r\n    charged. A large site being entirely rebuilt repeatedly can cost more in\r\n    invalidation charges than it would in the edge recaching content from S3.\r\n    Defaults to 100 paths. If this is set too low and a lot of paths need to\r\n    be invalidated, the entire site will be invalidated (`/*`).\r\n\r\n#### Other changes\r\n\r\n  * Turn on the Flask debugger in the live preview server. This provides more\r\n    information when the page fails to generate, and means automatic reloading\r\n    when `generate.py` is changed.\r\n"
short_description_html = "<h2>0.10.3 - 29 Jul 2021</h2>\n<h4>New</h4>\n<ul>\n<li>The preview server can now serve your custom 404 page.</li>\n<li>Adds an option <code>--max-invalidations</code> to control how many paths to<br>\ninvalidate in CloudFront when uploading. Too many pa…</li>\n</ul>"
is_short_description_html_truncated = true

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

## 0.10.3 - 29 Jul 2021

#### New

  * The preview server can now serve your custom 404 page.
  * Adds an option `--max-invalidations` to control how many paths to
    invalidate in CloudFront when uploading. Too many paths will end up being
    charged. A large site being entirely rebuilt repeatedly can cost more in
    invalidation charges than it would in the edge recaching content from S3.
    Defaults to 100 paths. If this is set too low and a lot of paths need to
    be invalidated, the entire site will be invalidated (`/*`).

#### Other changes

  * Turn on the Flask debugger in the live preview server. This provides more
    information when the page fails to generate, and means automatic reloading
    when `generate.py` is changed.
