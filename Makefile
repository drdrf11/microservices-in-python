install:
	#install commands
format:
	#format code (black)
lint:
	#flake8 or #pylint
test:
	#pytest
deploy:
	#deploy
all: install lint test deploy