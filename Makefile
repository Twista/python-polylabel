help: ## list available targets (this page)
	 @awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

_clean::
	rm -rf dist/*

_pack::
	python3 setup.py sdist bdist_wheel


_check::
	twine check dist/*

_upload::
	twine upload dist/*

test: ## run tests
	python3 tests.py
dist: _clean _pack ## create dist package in dist/ folder
publish: _check _upload ## check dist via twine and upload to pypi
