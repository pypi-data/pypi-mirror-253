# Makefile

help:
	@echo "Usage:"
	@echo "    make <command>"
	@echo ""
	@echo "Commands:"
	@echo "    help          Show this message"
	@echo "    build         Build package"
	@echo "    testpypi      Upload package to TestPyPi"
	@echo "    pypi          Upload package to PyPi"
	@echo "    install-test  Install from TestPyPi"

build:
	python3 -m build

testpypi:
	twine upload --repository pypitest dist/*

pypi:
	twine upload --repository pypi dist/*

install-test:
	python3 -m pip install --index-url https://test.pypi.org/simple/ thoplw

clean:
	rm -rf dist `find -type d | grep __pycache__`

# vim: noexpandtab tabstop=4 shiftwidth=4
