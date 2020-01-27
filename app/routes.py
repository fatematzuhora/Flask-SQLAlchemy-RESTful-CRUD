from app import app, db

from app.models import Book, Category
from app.schema import book_schema, books_schema, category_schema, categories_schema

from flask import request, jsonify, make_response

from config import Config




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
        'message': 'Category Created!',
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
endpoints for Book CRUD
===========================
"""
