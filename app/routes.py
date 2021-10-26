
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        # uses request.args object to access value of query param
        title_query = request.args.get("title")

        # Decide which conditional branch to take, checks if we got a query param
        if title_query:
            # 'books' stores result of query
            books = Book.query.filter_by(title=title_query)
        else:
            books = Book.query.all()

        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()
        return jsonify(f"Book {new_book.title} successfully created"), 201

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return jsonify("Not found"), 404

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }

    elif request.method == "PUT":
        request_body = request.get_json()

        book.title = request_body["title"]
        book.description = request_body["description"]

        db.session.commit()
        return jsonify(f"Book #{book.id} successfully updated"), 200

    elif request.method == "DELETE":
        # SQLAlchemy's function to tell database to prepare to delete book
        db.session.delete(book)
        db.session.commit()
        return jsonify(f"Book #{book.id} successfully deleted"), 200

