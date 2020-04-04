from flask import g, current_app
from flask_pymongo import PyMongo

def init_app(app):
    # Close the MongoDB connection after each request
    app.teardown_appcontext(close_client)

def get_client():
    if 'db_client' not in g:
        g.db_client = PyMongo(
            app = current_app,
            uri = current_app.config['MONGO_URL'],
            username = current_app.config['MONGO_USER'],
            password = current_app.config['MONGO_PASS']
        )
    return g.db_client.db

def close_client(app):
    db = g.pop('db_client', None)

    if db:
        db.cx.close()
