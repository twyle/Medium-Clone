# -*- coding: utf-8 -*-
"""This module contains all the email sending routes."""
from flask import Blueprint, jsonify

email = Blueprint("email", __name__)


@email.route("/", methods=["GET"])
def get_email():
    """Get a an email by id."""
    return jsonify({"email": "one"}), 200
