from flask import Flask

# package file that contains alot of the start up code for app

def create_app(test_config=None):
    app = Flask(__name__)

    # importing hello_world_bp into this module so we may use it in the next line
    from .routes import hello_world_bp 
    # use app's pre-defined function "register_blueprint()"to register hello_world_bp Blueprint
    app.register_blueprint(hello_world_bp) 

    from .routes import books_bp
    app.register_blueprint(books_bp)
    
    return app

