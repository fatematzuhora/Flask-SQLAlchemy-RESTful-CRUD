from app import app

from app.models import Author, Book, Category
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


"""
=============
schema classes
=============
"""

class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
        fields = ('id', 'name', 'short_desc') # fields to expose

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)



class AuthorSchema(ma.ModelSchema):
    class Meta:
        model = Author
        fields = ('id', 'name', 'about') # fields to expose

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)



class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book
        fields = ('uuid', 'name', 'tagline', 'short_desc', 'is_published', 'category_id', 'author_id') # fields to expose

book_schema = BookSchema()
books_schema = BookSchema(many=True)