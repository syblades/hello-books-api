from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
# provides a way to read env variables
import os


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()
# postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development
# package file that contains alot of the start up code for app
def create_app(test_config=None):
    app = Flask(__name__)

    # if falsy (None/empty) will connect to development database else will connect to test environment
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config["TESTING"] = True # Turns testing mode on
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    # connecting db and migrate to Flask app
    # initializing db oobject
    db.init_app(app)
    # telling migrate how to connect to the db
    migrate.init_app(app, db)

    from app.models.book import Book

    from .routes import books_bp
    app.register_blueprint(books_bp)

		
    return app
