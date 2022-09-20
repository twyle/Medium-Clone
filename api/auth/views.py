# -*- coding: utf-8 -*-
"""This module contains all the authentication, authorization and registration routes."""
from flasgger import swag_from
from flask import Blueprint, jsonify

auth = Blueprint("auth", __name__)


@swag_from(
    "./docs/register_admin.yml", endpoint="auth.register_admin", methods=["POST"]
)
@auth.route("/register/admin", methods=["POST"])
def register_admin():
    """Register an admin."""
    return jsonify({"auth": "register admin"}), 200


@swag_from(
    "./docs/register_author.yml", endpoint="auth.register_author", methods=["POST"]
)
@auth.route("/register/author", methods=["POST"])
def register_author():
    """Register an author."""
    return jsonify({"auth": "register author"}), 200


@swag_from(
    "./docs/register_moderator.yml",
    endpoint="auth.register_moderator",
    methods=["POST"],
)
@auth.route("/register/moderator", methods=["POST"])
def register_moderator():
    """Register a moderator."""
    return jsonify({"auth": "register moderator"}), 200


@auth.route("/reset_password", methods=["POST"])
@swag_from(
    "./docs/password_reset.yml", endpoint="auth.reset_password", methods=["POST"]
)
def reset_password():
    """Reset admin password."""
    return jsonify({"auth": "reset password"}), 200
