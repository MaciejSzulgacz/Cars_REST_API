# Microservice with REST API #

### Introduction ###

In order to use all the functionalities of the application, please send some sample data 
with POST /cars with body {"make": "Opel", "model": "Ampera"} and POST /rate with body 
{"rate": 5, "car_id": 1}.

### Technology stack ###

Python 3.8.10, Django, Docker, Git

### Requirements ###

* Python 3.8.10
* Unoccupied port 8000

### Prepare virtualenv (Linux) ###

* Prepare directory for virtual env (on the root of project):
	`mkdir venv`
* Prepare virtual env module:
	`sudo apt-get install python3-venv`
* Create venv:
	`python3 -m venv ./venv/`
* Checkout to venv:
	`source venv/bin/activate`
* Install requirements:
	`pip install -r requirements.txt`
* Check requirements:
	`pip list`

### Run application locally ###

* Source the virtual environment:
    `source ./vevn/bin/activate`
* Make migrations:
	`python3 manage.py migrate`
* Run flask application:
    `python3 manage.py runserver`