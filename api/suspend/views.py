# -*- coding: utf-8 -*-
"""This module contains all the routes used to suspend articles and suspends."""
from flasgger import swag_from
from flask import Blueprint, jsonify

suspend = Blueprint("suspend", __name__)


@swag_from(
    "./docs/suspend_author.yml", endpoint="suspend.suspend_author", methods=["POST"]
)
@suspend.route("/author", methods=["POST"])
def suspend_author():
    """Suspend Author with given id."""
    return jsonify({"suspend": "author"}), 200


@swag_from(
    "./docs/suspend_article.yml", endpoint="suspend.suspend_article", methods=["POST"]
)
@suspend.route("/article", methods=["POST"])
def suspend_article():
    """Suspend article with given id."""
    return jsonify({"suspend": "article"}), 200
