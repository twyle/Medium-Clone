# -*- coding: utf-8 -*-
"""This package contains all the application code."""
from flask import Flask, jsonify


def create_app():
    """Create the flask application."""
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def health_check():
        """Check if application is up."""
        return jsonify({"Hello": "From the blog application!"}), 200

    # shell context for flask cli
    app.shell_context_processor({"app": app})
    return app
