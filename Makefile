.PHONY: publish

publish: stash push rebuild unstash

stash:
	git stash --include-untracked

push:
	git push origin main

rebuild:
	./script/rebuild

unstash:
	git stash pop
