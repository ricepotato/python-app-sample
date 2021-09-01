init:
	docker build --no-cache --network host -t python-app-sample:$(shell cat version) . -f ./build/Dockerfile

test:
	PYTHONPATH=$(shell pwd)/src/app coverage run -m pytest src/tests -v --junitxml="unittest.xml"
	coverage report
	coverage html
