image_name := deploy-fastapi

install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		python -m textblob.download_corpora
format:
	#format code (black)
	black *.py mylib/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#pytest
	python -m pytest -vv --cov=mylib test_*.py
build:
	#build container
	docker build -t ${image_name} .
run:
	#run docker
	#echo Running ${image_name}:latest
	docker run -p 127.0.0.1:8080:8080 ${image_name}:latest 
deploy:
	#deploy
all: install lint test deploy