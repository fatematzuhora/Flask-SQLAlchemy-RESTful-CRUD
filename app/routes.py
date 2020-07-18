from app import app, db

from app.models import Author, Book, Category
from app.schema import author_schema, authors_schema, book_schema, books_schema, category_schema, categories_schema

from flask import request, jsonify, make_response


"""
===========================
endpoints for Category CRUD
===========================
"""

# endpoint to CREATE category
@app.route("/category", methods=["POST"])
def create_category():

    name = request.json['name']

    if 'short_desc' in request.json:
        short_desc = request.json['short_desc']
    else:
        short_desc = ""

    new_category = Category(name, short_desc)

    db.session.add(new_category)
    db.session.commit()

    result = category_schema.dump(new_category)

    data = {
        'message': 'New Category Created!',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET all categories
@app.route("/category", methods=["GET"])
def get_categories():

    all_categories = Category.query.all()
    result = categories_schema.dump(all_categories)

    data = {
        'message': 'All Categories!',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET category detail by id
@app.route("/category/<int:id>", methods=["GET"])
def get_category(id):

    category = Category.query.get(id)

    if(category):
        result = category_schema.dump(category)
        data = {
            'message': 'Category Info!',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'Invalid Category ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to UPDATE category
@app.route("/category/<int:id>", methods=["PATCH"])
def update_category(id):

    category = Category.query.get(id)

    if(category):
        if 'name' in request.json:
            category.name = request.json['name']
        if 'short_desc' in request.json:
            category.short_desc = request.json['short_desc']

        db.session.commit()
        result = category_schema.dump(category)
        
        data = {
            'message': 'Category Info Edited!',
            'status': 200,
            'data': result
        }

    else:
        data = {
            'message': 'Invalid Category ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to DELETE category
@app.route("/category/<int:id>", methods=["DELETE"])
def delete_category(id):

    category = Category.query.get(id)

    if(category):
        db.session.delete(category)
        db.session.commit()

        data = {
            'message': 'Category Deleted!',
            'status': 200
        }
    else:
        data = {
            'message': 'Invalid Category ID!',
            'status': 200
        }
    return make_response(jsonify(data))




"""
===========================
endpoints for Author CRUD
===========================
"""

# endpoint to CREATE author
@app.route("/author", methods=["POST"])
def create_author():

    name = request.json['name']

    if 'about' in request.json:
        about = request.json['about']
    else:
        about = ""

    new_author = Author(name, about)

    db.session.add(new_author)
    db.session.commit()

    result = author_schema.dump(new_author)

    data = {
        'message': 'New Author Created!',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET all authors
@app.route("/author", methods=["GET"])
def get_authors():

    all_author = Author.query.all()
    result = authors_schema.dump(all_author)

    data = {
        'message': 'All Authors!',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET author detail by id
@app.route("/author/<int:id>", methods=["GET"])
def get_author(id):

    author = Author.query.get(id)

    if(author):
        result = author_schema.dump(author)
        data = {
            'message': 'Author Info!',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'Invalid Author ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to UPDATE author
@app.route("/author/<int:id>", methods=["PATCH"])
def update_author(id):

    author = Author.query.get(id)

    if(author):
        if 'name' in request.json:
            author.name = request.json['name']
        if 'about' in request.json:
            author.about = request.json['about']

        db.session.commit()
        result = author_schema.dump(author)
        
        data = {
            'message': 'Author Info Edited!',
            'status': 200,
            'data': result
        }

    else:
        data = {
            'message': 'Invalid Author ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to DELETE author
@app.route("/author/<int:id>", methods=["DELETE"])
def delete_author(id):

    author = Author.query.get(id)

    if(author):
        db.session.delete(author)
        db.session.commit()

        data = {
            'message': 'Author Deleted!',
            'status': 200
        }
    else:
        data = {
            'message': 'Invalid Author ID!',
            'status': 200
        }
    return make_response(jsonify(data))




"""
===========================
endpoints for Book CRUD
===========================
"""

# endpoint to CREATE book
@app.route("/book", methods=["POST"])
def create_book():

    name = request.json['name']
    tagline = request.json['tagline']
    category_id = request.json['category_id']
    author_id = request.json['author_id']

    if 'short_desc' in request.json:
        short_desc = request.json['short_desc']
    else:
        short_desc = ""

    new_book = Book(name, tagline, short_desc, category_id, author_id)

    db.session.add(new_book)
    db.session.commit()

    result = book_schema.dump(new_book)

    data = {
        'message': 'New Book Created!',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET all books
@app.route("/book", methods=["GET"])
def get_books():

    all_book = Book.query.all()
    result = books_schema.dump(all_book)

    data = {
        'message': 'All Books!',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET book detail by uuid
@app.route("/book/<path:uuid>", methods=["GET"])
def get_book(uuid):

    book = Book.query.get(uuid)

    if(book):
        result = book_schema.dump(book)
        data = {
            'message': 'Book Info!',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'Invalid Book ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to UPDATE book
@app.route("/book/<path:uuid>", methods=["PATCH"])
def update_book(uuid):

    book = Book.query.get(uuid)

    if(book):
        if 'name' in request.json:
            book.name = request.json['name']
        if 'short_desc' in request.json:
            book.short_desc = request.json['short_desc']
        if 'tagline' in request.json:
            book.tagline = request.json['tagline']
        if 'is_published' in request.json:
            book.is_published = request.json['is_published']
        if 'category_id' in request.json:
            book.category_id = request.json['category_id']
        if 'author_id' in request.json:
            book.author_id = request.json['author_id']

        db.session.commit()
        result = book_schema.dump(book)
        
        data = {
            'message': 'Book Info Edited!',
            'status': 200,
            'data': result
        }

    else:
        data = {
            'message': 'Invalid Book ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to DELETE author
@app.route("/book/<path:uuid>", methods=["DELETE"])
def delete_book(uuid):

    book = Book.query.get(uuid)

    if(book):
        db.session.delete(book)
        db.session.commit()

        data = {
            'message': 'Book Deleted!',
            'status': 200
        }
    else:
        data = {
            'message': 'Invalid Book ID!',
            'status': 200
        }
    return make_response(jsonify(data))
