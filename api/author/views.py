# -*- coding: utf-8 -*-
"""This module contains all the author routes."""
from flask import Blueprint, jsonify

author = Blueprint("author", __name__)


@author.route("/", methods=["GET"])
def get_author():
    """Get a an author by id."""
    return jsonify({"author": "one"}), 200
