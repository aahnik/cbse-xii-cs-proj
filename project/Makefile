hi:
	@cat Makefile

pypi:
	python3 -m pip install --upgrade pip
	python3 -m pip install setuptools wheel twine
	rm -rf __pycache__
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf build dist *.egg-info

docu:
	pdoc3 --force --html --config show_source_code=False -o ~/temp marksman



