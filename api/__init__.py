# -*- coding: utf-8 -*-
"""This package contains all the application code."""
from flask import Flask, jsonify

from .helpers.error_handlers import register_error_handlers
from .helpers.helpers import set_flask_environment


def create_app():
    """Create the flask application."""
    app = Flask(__name__)

    register_error_handlers(app)

    set_flask_environment(app)

    @app.route("/", methods=["GET"])
    def health_check():
        """Check if application is up."""
        return jsonify({"Hello": "From the blog application!"}), 200

    # shell context for flask cli
    app.shell_context_processor({"app": app})
    return app
