web:
	uvicorn src.server:app --port=3000 --workers 5 --reload

test:
	python -m pytest tests/ $(SNAPSHOT_UPDATE)

up:
	docker-compose up -d

start-kafka-email-worker:
	faust -A src.workers.link_scrapper worker --web-port=6066 -l info

create-mongodb-indexes:
	pipenv run python -m scripts.create_indexes_mongodb

.PHONY: autoflake
autoflake:
	pipenv run autoflake -r $(AUTOFLAKE_OPTIONS) --exclude */snapshots --remove-unused-variables --remove-all-unused-imports  **/ | tee autoflake.log
	echo "$(AUTOFLAKE_OPTIONS)" | grep -q -- '--in-place' || ! [ -s autoflake.log ]

.PHONY: isort
isort:
	pipenv run isort ./src --multi-line 3 --trailing-comma --line-width 88 --skip */snapshots $(ISORT_OPTIONS)

.PHONY: black
black:
	pipenv run black ./src --exclude '.*/snapshots' $(BLACK_OPTIONS)

.PHONY: lint
lint: ISORT_OPTIONS := --check-only
lint: BLACK_OPTIONS := --check
lint: autoflake isort black
	pipenv run mypy ./src/*.py --ignore-missing-imports
	pipenv run flake8 ./src

.PHONY: format
format: AUTOFLAKE_OPTIONS := --in-place
format: autoflake isort black

.PHONY: snapshot-update
snapshot-update: SNAPSHOT_UPDATE := --snapshot-update
snapshot-update: test
