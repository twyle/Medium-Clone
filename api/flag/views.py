# -*- coding: utf-8 -*-
"""This module contains all the routes for flagging articles and flags by moderators."""
from flask import Blueprint, jsonify

flag = Blueprint("flag", __name__)


@flag.route("/", methods=["GET"])
def get_flag():
    """Get a an flag by id."""
    return jsonify({"flag": "one"}), 200
