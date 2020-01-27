from app import app

from app.models import Book, Category
from flask_marshmallow import Marshmallow


ma = Marshmallow(app)


# schema
class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
        fields = ('id', 'name', 'short_desc') # fields to expose


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)




class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book
        fields = ('id', 'name', 'tagline', 'short_desc', 'is_published', 'category_id') # fields to expose


book_schema = BookSchema()
books_schema = BookSchema(many=True)