all:
	python ${PWD}/ppb/main.py

testall:
	py.test --maxfail=1 --showlocals  --duration=3 -v --clearcache  -s

initvenv:
	pip install -r requirements.txt


