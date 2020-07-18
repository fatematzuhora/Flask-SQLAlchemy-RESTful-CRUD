from app import db
from sqlalchemy_utils import ChoiceType

from uuid import uuid4
import datetime, enum

# method to generate uuid
def generate_uuid():
    return str(uuid4())

# enum choice class for is_published field in book model
class BookIsPublishedEnum(enum.Enum):
    yes = True
    no = False


"""
=============
model classes
=============
"""
# See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
# for details on the column types.

class Book(db.Model):
    __tablename__ = "books"

    uuid = db.Column(db.String(255), nullable=False, unique=True, default=generate_uuid, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    tagline = db.Column(db.String(255), nullable=False)
    short_desc = db.Column(db.Text())
    is_published = db.Column(
        db.Boolean(),
        ChoiceType(BookIsPublishedEnum),
        default=False,
        nullable=False
    )
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    

    def __init__(self, name, tagline, short_desc, category_id, author_id):
        self.name = name
        self.tagline = tagline
        self.short_desc = short_desc
        self.category_id = category_id
        self.author_id = author_id



class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    short_desc = db.Column(db.String(255))

    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    books = db.relationship(Book, backref='category', lazy=True)


    def __init__(self, name, short_desc):
        self.name = name
        self.short_desc = short_desc



class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    about = db.Column(db.Text())

    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    books = db.relationship(Book, backref='author', lazy=True)


    def __init__(self, name, about):
        self.name = name
        self.about = about
