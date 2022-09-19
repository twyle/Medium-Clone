# -*- coding: utf-8 -*-
"""This module contains all the admin routes."""
from flask import Blueprint, jsonify

admin = Blueprint("admin", __name__)


@admin.route("/", methods=["GET"])
def get_admin():
    """Get a an admin by id."""
    return jsonify({"admin": "one"}), 200
