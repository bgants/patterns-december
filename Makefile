install:
	# install requirements
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	# format
	# black *.py models/test_*.py patterns/test_*.py
lint:
	# lint
	# pylint --disable=R,C *.py models/test_*.py patterns/test_*.py
test:
	# test
	# python -m pytest -vv --cov=models models/test_*.py -cov=patterns patterns/test_*.py --cov=main test_*py
build:
	# builds docker 
run:
	# runs
deploy:
	# deploys
all: install format lint test build run deploy
