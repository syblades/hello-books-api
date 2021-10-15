# routes.py = file where we define our endpoints

from flask import Blueprint
# We need to import our dependencies. Python supports comma-separated importing.
# # jsonify is a Flask utility function that turns its argument into JSON. 
# use jsonify to turn a list of book dictionaries into a Response object.
from flask import Blueprint, jsonify 


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
] 

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)


@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }



# "hello_world" = first argument is a string to be used to identify Blueprint from Flask server logs (in terminal)
# "__name__" = second argument is almost always "__name__" which blueprint uses to figure out aspects of routing.
hello_world_bp = Blueprint("hello_world", __name__)

# "@blueprint_name.route(...)" = decorator transforms the function that follows into an endpoint
# use ".route()" instance method from Blueprint instance
@hello_world_bp.route("/hello-world", methods=["GET"]) 

# function will execute whenever a request that matches the decorator is received
def say_hello_world():
    # must define a response body to return. 
    my_beautiful_response_body = "Hello, World!"
    # For each endpoint, we must return the HTTP response.
    return my_beautiful_response_body

@hello_world_bp.route("/hello/JSON", methods=["GET"]) 
def say_hello_json():
    return {
        "name": "Harry Potter",
        "message": "Wingardium Leviosa",
        "hobbies": ["Smashing Demintours", "Dating Ming Lee", "Being a bad-ass"]
    }


@hello_world_bp.route("/broken-endpoint", methods=["GET"])
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body
