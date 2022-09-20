# -*- coding: utf-8 -*-
"""This module contains all the article routes."""
from flask import Blueprint, jsonify

article = Blueprint("article", __name__)


@article.route("/", methods=["GET"])
def get_article():
    """Get a an article by id."""
    return jsonify({"article": "one"}), 200
