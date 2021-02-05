prep-env:
	pip install -r requirements.dev.in
run-tests:
	docker-compose -f docker-compose.testing.yml build 
	docker-compose -f docker-compose.testing.yml up

update-deps:
	pip-compile requirements.in requirements.testing.in -o requirements.txt


format:
	black armon tests
	flake8 armon tests
	mypy armon tests
