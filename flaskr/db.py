import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    # g is special object unique for each request
    if 'db' not in g:
        # sqlite3.connect => establish connections to the file pointed at 
        # by the DATABASE configuration key
        g.db = sqlite3.connect(
            # current_app => special obj points to flask app
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row tells connection to return rows behave like dicts
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        # checks if connection was created
        db.close()