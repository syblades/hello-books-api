# A standard pytest file that holds test configurations and common test helper functions.
# Essentially, this file is run before any other test files. 
# This allows fixtures registered here to be available to any other test file.

import pytest
from app import create_app
from app import db


@pytest.fixture
def app():
    # When tests run this will run & create an app object 
    # uses same create_app function defined in app/__init__.py
    app = create_app({"TESTING": True}) # current implementation of create_app() uses argument to check truthiness

    # designates that the following code should have an application context. 
    # lets various functionality in Flask determine what current running app is. 
    with app.app_context():
        db.create_all() # At start of tests code recreates tables needed for models.
        yield app # The lines after this statement will run after the test using the app has been completed.

    with app.app_context():
        # drop all of the tables, delete any data that was created during the test
        db.drop_all() 


# client fixture will make a test client (object able to simulate a client making HTTP requests)
@pytest.fixture
def client(app):
	return app.test_client()


from app.models.book import Book
# ...

@pytest.fixture
def two_saved_books(app):
    # Arrange
    self_help_book = Book(title="The Ultimate Self Help Book", description="This will TOTALLY change ur lyfe!")
    food_book = Book(title="Food Book", description="A book filled with pics of food and paragraphs that are too long to tell you how to make said food... so original.")

    db.session.add_all([self_help_book, food_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()
