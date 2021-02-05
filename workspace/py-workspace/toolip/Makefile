prep-env:
	pip install -r requirements.dev.in
run-tests:
	tox
update-deps:
	pip-compile requirements.in requirements.testing.in -o requirements.txt
