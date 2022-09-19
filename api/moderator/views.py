# -*- coding: utf-8 -*-
"""This module contains all the content and moderator moderation routes."""
from flask import Blueprint, jsonify

moderator = Blueprint("moderator", __name__)


@moderator.route("/", methods=["GET"])
def get_moderator():
    """Get a an moderator by id."""
    return jsonify({"moderator": "one"}), 200
