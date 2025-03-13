.PHONY: lint format install

# Directories containing Python files
SRC_DIRS=model

# Install required tools
install:
	pip install flake8 black isort

# Install project dependencies from requirements.txt
install-model-requirements:
	pip install -r ./model/requirements.txt

# Run linting (flake8) on all Python files
lint:
	flake8 $(SRC_DIRS) --max-line-length=100

# Format code using black and isort
format:
	black $(SRC_DIRS)
	isort $(SRC_DIRS)

# Run both linting and formatting
check: lint format

# Build Docker Image inside ./model
build:
	cd model && docker build -t loan_prediction .
