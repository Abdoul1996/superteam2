from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound
from . import db
from . import error_handlers

DEFAULTS = {
    'result_count': 20,
}


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(error_handlers.blueprint)

    CORS(app, resources={r"/*": {"origins": app.config['CORS']}})
    db.init_app(app)

    @app.route('/', methods=['GET'])
    @app.route('/books', methods=['GET'])
    def getBooks():
        """
        Retreive listing of available book records 
        ---
        query_parameters:
            p: Pagination page to return
            c: Number of results per page
        response:
            200: Returns a list of book records
        """
        page = request.args.get('p', 1)
        count = request.args.get('c', DEFAULTS['result_count'])
        mongo = db.get_client()

        return "Need Implementation"

    @app.route('/book/<isbn>', methods=['GET'])
    def getBook(isbn):
        """
        Retrieve a single book record by it's ISBN 
        ---
        path_parameters:
              isbn:
        response:
            200: Returns a single book record

        """
        if isbn:
            # Fetch document by 'isbn'
            mongo = db.get_client()

            return "Need Implementation"
        else:
            # Return ID missing error
            raise BadRequest

    @app.route('/book', methods=['PUT'])
    def createBook():
        """Create a book record 
        ---
        body_parameters:
            isbn: integer
            title: string
            author: string
            publication_year: string
            image_url_s: string
            image_url_m: string
            image_url_l: string
        response:
            200: Created Ok
        """
        return "Need Implementation"

    return app