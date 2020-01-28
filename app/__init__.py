from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# app config file
from config import Config

# create the application instance
app = Flask(__name__)
app.config.from_object(Config)

# create the application database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models