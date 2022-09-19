# -*- coding: utf-8 -*-
"""This module declares and registers extensions."""
from flask_cors import CORS

cors = CORS()


def register_extensions(app):
    """Register the application extensions."""
    cors.init_app(app)
