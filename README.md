# Flask-SQLAlchemy-RESTful-CRUD
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) [![MIT license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD)

Simple RESTful CRUD API application using [Flask](http://flask.pocoo.org) & [SQLAlchemy](http://www.sqlalchemy.org), and connecting the both using [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) library.

In this application we are connecting a MySQL database in a python flask file in which there are THREE tables Category, Author, and Books. The Book table contains One-to-Many relationship with Categories and Authors. We use to add a new category, author, book in the database, retrieve them. And later we can update and delete from the database.



## Getting started
* At first you'll need to get the source code of the project. Do this by cloning the [Flask-SQLAlchemy-RESTful-CRUD repository](https://github.com/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD).
```
$ git clone https://github.com/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD.git
$ cd Flask-SQLAlchemy-RESTful-CRUD
```

* Create a virtual environment for this project and install dependencies
```
$ virtualenv .venv
```

* Activate the virtual environment
```
$ source .venv/bin/activate
```

* Install the dependencies
```
$ pip install -r requirements.txt
```

* Create a environment file and configure it
```
$ touch .env
```

#### Sample .env File
```
SECRET_KEY="w&8s%5^5vuhy2-gvkyi=gg4e*tso*51mb$l!=%o(@$a2tmq6o+Flask-SQLAlchemy-RESTful-CRUD"
DEBUG=TRUE
SQLALCHEMY_DATABASE_URI="mysql://YOUR_DB_USER_NAME:YOUR_DB_PASS@localhost:3306/YOUR_DB_NAME"
SQLALCHEMY_TRACK_MODIFICATIONS=FALSE
```



## Running the App

#### 1) With Database Migration

```
$ export FLASK_APP=app.py
$ flask db init
```

* Create a migration file for all tables
```
$ flask db migrate -m tables
```

* Upgrade the database with migration file
```
$ flask db upgrade
```

* Run the app
```
$ flask run
```

And finally, the application will run on the following URL: http://127.0.0.1:5000


#### 2) Without Migration

* Simply run the following command, it will create database tables and run the project on the following URL: http://0.0.0.0:8087
* And the DEBUG mode will be ON

```
$ python app.py
```

If you want to change the PORT go to the [app.py](https://github.com/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD/blob/master/app.py) file and edit on the following line of code.
```
app.run(host='0.0.0.0', port=8087, debug=True)
```