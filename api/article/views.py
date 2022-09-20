# -*- coding: utf-8 -*-
"""This module contains all the article routes."""
from flasgger import swag_from
from flask import Blueprint, jsonify

article = Blueprint("article", __name__)


@swag_from(
    "./docs/create_article.yml", endpoint="article.create_article", methods=["POST"]
)
@article.route("/", methods=["POST"])
def create_article():
    """Create an article."""
    return jsonify({"article": "create an artcile"}), 200


@swag_from("./docs/get_article.yml", endpoint="article.get_article", methods=["GET"])
@article.route("/", methods=["GET"])
def get_article():
    """Get an article by id."""
    return jsonify({"article": "get"}), 200


@swag_from(
    "./docs/update_article.yml", endpoint="article.update_article", methods=["PUT"]
)
@article.route("/", methods=["PUT"])
def update_article():
    """Update the article with given id."""
    return jsonify({"article": "update"}), 200


@swag_from(
    "./docs/delete_article.yml", endpoint="article.delete_article", methods=["DELETE"]
)
@article.route("/", methods=["DELETE"])
def delete_article():
    """Delete the article with given id."""
    return jsonify({"article": "delete"}), 200


@swag_from("./docs/like_article.yml", endpoint="article.like_article", methods=["GET"])
@article.route("/like", methods=["GET"])
def like_article():
    """Like the article with given id."""
    return jsonify({"article": "like"}), 200


@swag_from(
    "./docs/comment_article.yml", endpoint="article.comment_article", methods=["POST"]
)
@article.route("/comment", methods=["POST"])
def comment_article():
    """Comment the article with given id."""
    return jsonify({"article": "comment"}), 200


@swag_from(
    "./docs/get_all_articles.yml", endpoint="article.get_all_articles", methods=["GET"]
)
@article.route("/articles", methods=["GET"])
def get_all_articles():
    """List all articles."""
    return jsonify({"article": "all"}), 200
