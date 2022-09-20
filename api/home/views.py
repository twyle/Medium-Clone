# -*- coding: utf-8 -*-
"""This module contains the home route."""
from flask import Blueprint, jsonify

home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
def get_home():
    """Get a an home by id."""
    return jsonify({"home": "one"}), 200
