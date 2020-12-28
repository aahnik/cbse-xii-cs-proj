hi:
	@cat Makefile

pypi:
	python3 -m pip install --upgrade pip
	python3 -m pip install setuptools wheel twine
	rm -rf __pycache__
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf build dist *.egg-info

documentation:
	pdoc3 --force --html --config show_source_code=False -o docs marksman
	mv docs/marksman/*.html docs
	rmdir docs/marksman

	

