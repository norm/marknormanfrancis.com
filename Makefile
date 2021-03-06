.PHONY: clean baked_css dev_css generate upload publish stash push rebuild unstash

clean:
	@rm -rf output

baked_css:
	@./script/update_css

dev_css: 
	@./script/reset_css

generate:
	@flourish generate -v

upload:
	@flourish upload

publish: stash push rebuild unstash

stash:
	git stash --include-untracked

push:
	git push origin main

rebuild: clean baked_css upload generate upload dev_css

unstash:
	git stash pop
