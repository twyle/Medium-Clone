# -*- coding: utf-8 -*-
"""This module contains all the routes used to report offensive reports and reports."""
from flasgger import swag_from
from flask import Blueprint, jsonify

report = Blueprint("report", __name__)


@swag_from(
    "./docs/report_author.yml", endpoint="report.report_author", methods=["POST"]
)
@report.route("/author", methods=["POST"])
def report_author():
    """Report Author with given id."""
    return jsonify({"report": "author"}), 200


@swag_from(
    "./docs/report_article.yml", endpoint="report.report_article", methods=["POST"]
)
@report.route("/article", methods=["POST"])
def report_article():
    """Report article with given id."""
    return jsonify({"report": "article"}), 200
