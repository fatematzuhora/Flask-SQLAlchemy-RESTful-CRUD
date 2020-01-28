# Flask-SQLAlchemy-RESTful-CRUD
[![Build Status](https://travis-ci.org/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD.svg?branch=master)](https://travis-ci.org/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

Simple RESTful CRUD API application using [Flask](http://flask.pocoo.org) & [SQLAlchemy](http://www.sqlalchemy.org), and connecting the both using [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) library.



### Getting started
At first you'll need to get the source code of the project. Do this by cloning the Flask-SQLAlchemy-RESTful-CRUD repository.

```
# get the project code
$ git clone https://github.com/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD.git
$ cd Flask-SQLAlchemy-RESTful-CRUD
```

Create a virtual environment for this project and install dependencies
```
# create a virtualenv in which we can install the dependencies
$ virtualenv .venv
$ source .venv/bin/activate
```

```
pip install -r requirements.txt
```

### Running the App

```
$ python app.py
```



# Sample .env File
```
SECRET_KEY="w&8s%5^5vuhy2-gvkyi=gg4e*tso*51mb$l!=%o(@$a2tmq6o+Flask-SQLAlchemy-CRUD-RESTful-API"
DEBUG=TRUE
SQLALCHEMY_DATABASE_URI="mysql://root:1234567890@localhost:3306/flask"
SQLALCHEMY_TRACK_MODIFICATIONS=FALSE
```