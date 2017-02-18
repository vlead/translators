# -*- coding: utf-8 -*-
import os
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin

# Need to change the root PYTHONPATH during runtime
from dev_code.runtime.rest.api import api
# from runtime.rest import api

# Need to change the root PYTHONPATH during runtime
from dev_code.runtime.config import flask_app_config as config
# from runtime.config import flask_app_config as config


def configure_logging():
    from logging import handlers, Formatter
    formatter = Formatter('%(asctime)s: %(levelname)s: %(filename)s:'
                          ' %(funcName)s():%(lineno)d: %(message)s')

    pass


def configure_error_handlers():
    pass


def configure_system():
    pass


def create_app(config):
    # initialise app
    app = Flask(__name__,
                static_folder="",
                template_folder="")
    app.config.from_object(config)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(api)
    # configure_logging()
    # configure_error_handlers()
    # configure_system()

    return app

if __name__ == "__main__":
    app = create_app(config)
    app.run(debug=True, host='0.0.0.0', threaded=True)
