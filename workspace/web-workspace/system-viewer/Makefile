prep-env:
	sudo cp -R volumes/* /var/lib/docker/volumes/
	sudo chown -R 472:472 /var/lib.docker/volumes/system-viewer_grafana-storage/_data

build-dev:
	docker-compose -f docker-compose.dev.yml build

run-dev: build-dev
	docker-compose -f docker-compose.dev.yml up

build: 
	docker-compose build

run: build
	docker-compose up

build-deploy:
	docker build -t ophirt/sv-backend backend
	docker build -t ophirt/sv-frontend frontend

deploy: build-deploy
	docker push ophirt/sv-backend
	docker push ophirt/sv-frontend

