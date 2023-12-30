install:
	# install requirements
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	# format
	black *.py models/*.py tests/*.py
lint:
	# lint
	pylint --disable=R,C *.py models/*py tests/*.py
test:
	# test
	python -m pytest -vv --cov=tests/test_*.py
build:
	# builds docker 
run:
	# runs
deploy:
	# deploys
all: install format lint test build run deploy
