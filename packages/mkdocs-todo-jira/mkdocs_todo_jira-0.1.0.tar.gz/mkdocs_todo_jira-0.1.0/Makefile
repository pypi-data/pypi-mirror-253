.PHONY: clean build upload deploy help

clean:
	@echo "Cleaning up dist, build, and egg-info directories..."
	rm -rf dist/ build/ *.egg-info ./*.tar.gz ./*.whl

build: clean
	@echo "Building the package..."
	python3 -m build

upload: build
	@echo "Uploading the package to PyPI..."
	python3 -m twine upload dist/*

deploy: upload

help:
	@echo "Makefile commands:"
	@echo "clean - Remove build artifacts"
	@echo "build - Build the package"
	@echo "upload - Upload the package to PyPI"
	@echo "deploy - Alias for upload"
