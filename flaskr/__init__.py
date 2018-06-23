# this file has two duties:
# 1. contain application factory
# 2. tells python flaskr directory should be treated as package
import os

from flask import Flask

# create_app is app factory function
# test_config can be passed to the factory
def create_app(test_config=None):
    # create and configure the app
    # create the flask instance
    # __name__ => name of current python module

    # instance_relative_config=True => config files are relative to instance folder
    # instance folder located outside flaskr package, can hold local data
    # that should not be commited to version control (config secrets/db file)
    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_mapping() => sets default config app will use
    # dev should be overridden when deploying
    # DATABASE => path where SQLite db file will be saved
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # overrides the default config with values taken from config.py
        # ie when deploying, can be used to set real SECRET_KEY 
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        # os.makedirs() => ensures app.instance_path exists
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    # creates connection between URL /hello and a function 
    # that returns a response
    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    return app