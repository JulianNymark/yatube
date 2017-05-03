docker-run: docker-image
	docker stop -t 1 yatube || true # stop yatube if already running
	docker run --name yatube -d -p 80:80 --rm yatube

docker-image: docker-context/Dockerfile
	docker build -t yatube docker-context

bash:
	docker exec -it yatube /bin/bash
