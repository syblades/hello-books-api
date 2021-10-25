from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
# postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development
# package file that contains alot of the start up code for app
def create_app(test_config=None):
    app = Flask(__name__)
    
    # db config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    
    # connecting db and migrate to Flask app
    # initializing db oobject
    db.init_app(app)
    # telling migrate how to connect to the db
    migrate.init_app(app, db)
    from app.models.book import Book

    from .routes import books_bp
    app.register_blueprint(books_bp)

		
    return app
