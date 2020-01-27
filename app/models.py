from app import db
import datetime


# models
class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    short_desc = db.Column(db.String(255))

    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    # books = db.relationship(Book, backref='category', lazy=True)


    def __init__(self, name, short_desc):
        self.name = name
        self.short_desc = short_desc
    



class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    tagline = db.Column(db.String(255), nullable=False)
    short_desc = db.Column(db.Text())
    is_published = db.Column(db.Boolean(), nullable=False, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    

    def __init__(self, name, tagline, short_desc, category_id):
        self.name = name
        self.tagline = tagline
        self.short_desc = short_desc
        self.category_id = category_id
