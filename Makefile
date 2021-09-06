.PHONY: clean baked_css dev_css generate upload publish stash push rebuild unstash

clean:
	@rm -rf output

baked_css:
	@./script/update_css

dev_css: 
	@./script/reset_css

diff_generate:
	@./script/diff_generate

generate:
	@flourish generate -v

upload:
	@flourish upload --invalidate --max-invalidations 50

publish: stash push rebuild unstash

stash:
	git stash --include-untracked

push:
	git push origin main

rebuild: clean baked_css upload generate upload dev_css

test:
	@./script/test_generated_site

diff_test:
	@./script/test_generated_site diff

unstash:
	git stash pop
