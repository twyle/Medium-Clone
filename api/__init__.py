# -*- coding: utf-8 -*-
"""This package contains all the application code."""
from flask import Flask, jsonify

from .extensions import register_extensions
from .helpers import register_blueprints, register_error_handlers, set_flask_environment


def create_app():
    """Create the flask application."""
    app = Flask(__name__)

    register_error_handlers(app)

    set_flask_environment(app)

    @app.route("/", methods=["GET"])
    def health_check():
        """Check if application is up."""
        return jsonify({"Hello": "From the blog application!"}), 200

    register_extensions(app)
    register_blueprints(app)

    # shell context for flask cli
    app.shell_context_processor({"app": app})
    return app
