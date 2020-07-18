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

* Update `SQLALCHEMY_DATABASE_URI` at the `.env` file according to your MySQL database information


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


## API Documentation

#### 1. Create Category

**Request**
```
POST /category
```

**Parameters**
Name|Type|Description|Required
:-:|:-:|:-:|:-:
`name`|`string`|category name|`True`
`short_desc`|`string`|category short description|`False`

**Request Body**
```
{
    "name": "Python",
    "short_desc": "A python programming language blog"
}
```

**Response**
```
{
    "data": {
        "id": 1,
        "name": "Python",
        "short_desc": "A python programming language blog"
    },
    "message": "New Category Created!",
    "status": 201
}
```

#### 2. Category List

**Request**
```
GET /category
```

**Response**
```
{
    "data": [
        {
            "id": 1,
            "name": "Python",
            "short_desc": "A python programming language blog"
        },
        ....
    ],
    "message": "All Categories!",
    "status": 200
}
```

#### 3. Category Detail

**Request**
```
GET /category/:id
```

**Response**
```
{
    "data": {
        "id": 1,
        "name": "Python",
        "short_desc": "A python programming language blog"
    },
    "message": "Category Info!",
    "status": 200
}
```

#### 4. Update Category

**Request**
```
PATCH /category/:id
```

**Parameters**
Name|Type|Description|Required
:-:|:-:|:-:|:-:
`name`|`string`|category name|`False`
`short_desc`|`string`|category short description|`False`

#### 5. Delete Category

**Request**
```
DELETE /category/:id
```

**Response**
```
{
    "message": "Category Deleted!",
    "status": 200
}
```

#### 6. Create Author

**Request**
```
POST /author
```

**Parameters**
Name|Type|Description|Required
:-:|:-:|:-:|:-:
`name`|`string`|author name|`True`
`about`|`string`| short description about author|`False`

**Request Body**
```
{
    "name": "Fatema T. Zuhora",
    "about": "Full Stack Software Engineer"
}
```

**Response**
```
{
    "data": {
        "about": "Full Stack Software Engineer",
        "id": 1,
        "name": "Fatema T. Zuhora"
    },
    "message": "New Author Created!",
    "status": 201
}
```

#### 7. Author List

**Request**
```
GET /author
```

**Response**
```
{
    "data": [
        {
            "about": "Full Stack Software Engineer",
            "id": 1,
            "name": "Fatema T. Zuhora"
        },
        ....
    ],
    "message": "All Authors!",
    "status": 200
}
```

#### 8. Author Detail

**Request**
```
GET /author/:id
```

**Response**
```
{
    "data": {
        "about": "Full Stack Software Engineer",
        "id": 1,
        "name": "Fatema T. Zuhora"
    },
    "message": "Author Info!",
    "status": 200
}
```

#### 9. Update Author

**Request**
```
PATCH /author/:id
```

**Parameters**
Name|Type|Description|Required
:-:|:-:|:-:|:-:
`name`|`string`|author name|`False`
`about`|`string`| short description about author|`False`

#### 10. Delete Author

**Request**
```
DELETE /author/:id
```

**Response**
```
{
    "message": "Author Deleted!",
    "status": 200
}
```

#### 11. Create Book

**Request**
```
POST /book
```

**Parameters**
Name|Type|Description|Required
:-:|:-:|:-:|:-:
`name`|`string`|book name|`True`
`tagline`|`string`|book tagline|`True`
`category_id`|`int`|category id of book|`True`
`author_id`|`int`|author id of book|`True`
`short_desc`|`string`| short description of book|`False`

**Request Body**
```
{
    "name": "Code In Python",
    "tagline": "A python programming language blog!",
    "category_id": 1,
    "author_id": 1
}
```

**Response**
```
{
    "data": {
        "author_id": 1,
        "category_id": 1,
        "is_published": false,
        "name": "Code In Python",
        "short_desc": "",
        "tagline": "A python programming language blog!",
        "uuid": "edf5b0e0-7a3b-4ea6-8890-b6bb84d2318f"
    },
    "message": "New Book Created!",
    "status": 201
}
```

#### 12. Book List

**Request**
```
GET /book
```

**Response**
```
{
    "data": [
        {
            "author_id": 1,
            "category_id": 1,
            "is_published": false,
            "name": "Code In Python",
            "short_desc": "",
            "tagline": "A python programming language blog!",
            "uuid": "edf5b0e0-7a3b-4ea6-8890-b6bb84d2318f"
        },
        ....
    ],
    "message": "All Books!",
    "status": 200
}
```

#### 13. Book Detail

**Request**
```
GET /book/:uuid
```

**Response**
```
{
    "data": {
        "author_id": 1,
        "category_id": 1,
        "is_published": false,
        "name": "Code In Python",
        "short_desc": "",
        "tagline": "A python programming language blog!",
        "uuid": "edf5b0e0-7a3b-4ea6-8890-b6bb84d2318f"
    },
    "message": "Book Info!",
    "status": 200
}
```

#### 14. Update Book

**Request**
```
PATCH /book/:uuid
```

**Parameters**
Name|Type|Description|Required
:-:|:-:|:-:|:-:
`name`|`string`|book name|`False`
`tagline`|`string`|book tagline|`False`
`category_id`|`int`|category id of book|`False`
`author_id`|`int`|author id of book|`False`
`is_published`|`boolean`| status of book|`False`
`short_desc`|`string`| short description of book|`False`

#### 15. Delete Book

**Request**
```
DELETE /book/:uuid
```

**Response**
```
{
    "message": "Book Deleted!",
    "status": 200
}
```