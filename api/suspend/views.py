# -*- coding: utf-8 -*-
"""This module contains all the routes used to suspend articles and suspends."""
from flask import Blueprint, jsonify

suspend = Blueprint("suspend", __name__)


@suspend.route("/", methods=["GET"])
def get_suspend():
    """Get a an suspend by id."""
    return jsonify({"suspend": "one"}), 200
