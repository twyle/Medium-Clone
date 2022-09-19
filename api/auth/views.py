# -*- coding: utf-8 -*-
"""This module contains all the authentication, authorization and registration routes."""
from flask import Blueprint, jsonify

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET"])
def get_auth():
    """Get a an auth by id."""
    return jsonify({"auth": "one"}), 200
