test:
	/home/andrea/.virtualenvs/spec-py/bin/pytest -v tests.py

clean:
	find . -iname '*.pyc' -delete
