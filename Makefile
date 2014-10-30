all:
	python ${PWD}/ppb/main.py mandatory_positional_arg

test:
	py.test -c ressources/conf/pytest.ini --maxfail=1 --showlocals  --duration=3 -v  -s

initvenv:
	pip install -r requirements.txt


