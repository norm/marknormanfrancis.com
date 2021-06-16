```
title = "flourish release 0.10.1"
published = 2021-06-15T14:26:16Z
origin = "github"
type = "release"
package = "flourish"
version = "0.10.1"
pypi_url = "https://pypi.org/project/flourish/0.10.1/"
tag = [ "repo-flourish",]

[release_event]
id = "16787278372"
type = "ReleaseEvent"
public = true
created_at = "2021-06-15T14:26:16Z"

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
url = "https://api.github.com/repos/norm/flourish/releases/44650656"
assets_url = "https://api.github.com/repos/norm/flourish/releases/44650656/assets"
upload_url = "https://uploads.github.com/repos/norm/flourish/releases/44650656/assets{?name,label}"
html_url = "https://github.com/norm/flourish/releases/tag/v0.10.1"
id = 44650656
node_id = "MDc6UmVsZWFzZTQ0NjUwNjU2"
tag_name = "v0.10.1"
target_commitish = "main"
name = "0.10.1"
draft = false
prerelease = false
created_at = "2021-06-15T14:25:05Z"
published_at = "2021-06-15T14:26:16Z"
assets = []
tarball_url = "https://api.github.com/repos/norm/flourish/tarball/v0.10.1"
zipball_url = "https://api.github.com/repos/norm/flourish/zipball/v0.10.1"
body = "## 0.10.1 - 15 Jun 2021\r\n\r\n#### New\r\n\r\n  * Permanent (301) redirects from an old slug to a new location can be kept\r\n    in the `_site.toml`:\r\n\r\n        [permanent_redirects]\r\n        \"/index.php\" = \"/\"\r\n\r\n    and in an individual source:\r\n\r\n        previous_slug = ['/page']\r\n\r\n\r\n#### Bug fixes\r\n\r\n  * Stop reusing previously generated files in the live preview.\r\n  * Use backwards-compatible importlib_resources for older pythons, and\r\n    test that part of the code.\r\n"
short_description_html = "<h2>0.10.1 - 15 Jun 2021</h2>\n<h4>New</h4>\n<ul>\n<li>\n<p>Permanent (301) redirects from an old slug to a new location can be kept<br>\nin the <code>_site.toml</code>:</p>\n<pre><code>[permanent_redirects]\n\"/index.php\" = \"/\"\n</code></pre>\n<p>and in an individual source:</p>\n<pre><code>previou…</code></pre>\n</li>\n</ul>"
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

## 0.10.1 - 15 Jun 2021

#### New

  * Permanent (301) redirects from an old slug to a new location can be kept
    in the `_site.toml`:

        [permanent_redirects]
        "/index.php" = "/"

    and in an individual source:

        previous_slug = ['/page']


#### Bug fixes

  * Stop reusing previously generated files in the live preview.
  * Use backwards-compatible importlib_resources for older pythons, and
    test that part of the code.
