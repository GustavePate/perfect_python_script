all:
	./bin/perfect_python_script_launcher.sh mandatory_argument

test:
	py.test -c ressources/conf/pytest.ini  --showlocals  --duration=3 -v  -s --confpath=${PWD}/ressources/conf/conf.json

initvenv:
	pip install -r requirements.txt


