# -*- coding: utf-8 -*-
"""This module contains all the routes used to report offensive reports and articles."""
from flask import Blueprint, jsonify

report = Blueprint("report", __name__)


@report.route("/", methods=["GET"])
def get_report():
    """Get a an report by id."""
    return jsonify({"report": "one"}), 200
