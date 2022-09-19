# -*- coding: utf-8 -*-
"""This module declares the error handlers."""
from flask import jsonify


def register_error_handlers(app):
    """Register the error hadlers."""
    app.register_error_handler(405, handle_method_not_allowed)


def handle_method_not_allowed(e):
    """Handle all Method Not allowed errors errors."""
    return jsonify({"error": str(e)}), 405
