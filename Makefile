.PHONY: clean
test: up
	docker-compose exec app pytest --disable-warnings -s

.PHONY: up
up:
	docker-compose up -d
