#!/usr/bin/python3

import os

from flask import Flask, redirect, url_for

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://webaccess:cs160mysql@localhost:3306/RESMGTDB"
    app.config['SQLALCHEMY_TRACK_MODOFOCATIONS'] = False

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    from . import db
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.db_session.remove()
    db.init_db()

    from . import manager
    app.register_blueprint(manager.bp)

    from . import customer
    app.register_blueprint(customer.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    return app

