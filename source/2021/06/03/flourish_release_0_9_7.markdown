```
title = "flourish release 0.9.7"
published = 2021-06-03T08:55:31Z
origin = "github"
type = "release"
package = "flourish"
version = "0.9.7"
pypi_url = "https://pypi.org/project/flourish/0.9.7/"
tag = [ "repo-flourish",]

[release_event]
id = "16625404399"
type = "ReleaseEvent"
public = true
created_at = "2021-06-03T08:55:31Z"

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
url = "https://api.github.com/repos/norm/flourish/releases/44028402"
assets_url = "https://api.github.com/repos/norm/flourish/releases/44028402/assets"
upload_url = "https://uploads.github.com/repos/norm/flourish/releases/44028402/assets{?name,label}"
html_url = "https://github.com/norm/flourish/releases/tag/v0.9.7"
id = 44028402
node_id = "MDc6UmVsZWFzZTQ0MDI4NDAy"
tag_name = "v0.9.7"
target_commitish = "main"
name = "0.9.7"
draft = false
prerelease = false
created_at = "2021-06-03T08:53:04Z"
published_at = "2021-06-03T08:55:30Z"
assets = []
tarball_url = "https://api.github.com/repos/norm/flourish/tarball/v0.9.7"
zipball_url = "https://api.github.com/repos/norm/flourish/zipball/v0.9.7"
body = "## 0.9.7 - 3 June 2021\r\n\r\n#### New\r\n\r\n  * Serve asset files (eg CSS, images, etc) from the source directory\r\n    during live preview.\r\n  * Raising `self.DoNotGenerate` in a generator will stop the current\r\n    page from being generated, without causing any errors.\r\n\r\n#### Other changes\r\n\r\n  * Allow overriding an Atom feed's author and title values.\r\n\r\n#### Bug fixes\r\n\r\n  * Fix wildcard generation of URLs. Some patterns were not matching, for\r\n    example `flourish generate /2021/?` was generating `/2021/index.html` but\r\n    not `/2021/04/21/index.html`, or any source with a slug starting\r\n    `/2021/...`.\r\n  * Stop live preview caching sectile-generated templates, which invalidated\r\n    the point of being able to live preview changes as they are made.\r\n  * An Atom feed without entries will still generate now.\r\n\r\n"
short_description_html = "<h2>0.9.7 - 3 June 2021</h2>\n<h4>New</h4>\n<ul>\n<li>Serve asset files (eg CSS, images, etc) from the source directory<br>\nduring live preview.</li>\n<li>Raising <code>self.DoNotGenerate</code> in a generator will stop the current<br>\npage from being gener…</li>\n</ul>"
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

## 0.9.7 - 3 June 2021

#### New

  * Serve asset files (eg CSS, images, etc) from the source directory
    during live preview.
  * Raising `self.DoNotGenerate` in a generator will stop the current
    page from being generated, without causing any errors.

#### Other changes

  * Allow overriding an Atom feed's author and title values.

#### Bug fixes

  * Fix wildcard generation of URLs. Some patterns were not matching, for
    example `flourish generate /2021/?` was generating `/2021/index.html` but
    not `/2021/04/21/index.html`, or any source with a slug starting
    `/2021/...`.
  * Stop live preview caching sectile-generated templates, which invalidated
    the point of being able to live preview changes as they are made.
  * An Atom feed without entries will still generate now.

