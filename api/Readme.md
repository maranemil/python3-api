# API build from scratch


Step 1: run_migration

~~~shell
	python3 ./migrations/migration_1.py
~~~

Step 2: install uvicorn and start server

~~~shell
sudo apt install uvicorn -y
~~~
~~~shell
uvicorn main:run --reload --host 0.0.0.0 --port 8888
~~~


Step 3: user register

~~~shell
PATHURL="http://0.0.0.0:8888/api/register?email=test4@test.de&password=test"
curl -v  $PATHURL
~~~

Step 3: User login and token creation

~~~shell
PATHURL="http://0.0.0.0:8888/api/login"
curl -vvv POST -d '{"email":"test4@test.de","password":"test"}' $PATHURL 
~~~