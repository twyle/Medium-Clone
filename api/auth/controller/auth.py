# -*- coding: utf-8 -*-
"""This module contains all the bussiness logic for authentication and authorization."""
import re

from flask import current_app, jsonify

from ...author import Author, author_schema


def is_user_name_valid(first_name: str, last_name: str):
    """Check if the user name is valid."""
    if not first_name or not last_name:
        raise ValueError("The first name or last must be provided.")
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("The first name or last name must be string")
    if (
        len(first_name) >= current_app.config["NAME_MAX_LENGTH"]
        or len(last_name) >= current_app.config["NAME_MAX_LENGTH"]  # noqa: W503
    ):
        raise ValueError(
            f'The first name or last name must be than {current_app.config["NAME_MAX_LENGTH"]}'
        )
    if (
        len(first_name) <= current_app.config["NAME_MIN_LENGTH"]
        or len(last_name) <= current_app.config["NAME_MIN_LENGTH"]  # noqa: W503
    ):
        raise ValueError(
            f'The first name or last name must be more than {current_app.config["NAME_MIN_LENGTH"]}'
        )


def validate_name(author_data: dict):
    """Validate the validity of the first and last name."""
    if "First Name" not in author_data.keys():
        raise ValueError("The First Name must be provided")
    if "Last Name" not in author_data.keys():
        raise ValueError("The Last Name must be provided")
    if not author_data["First Name"]:
        raise ValueError("The First Name must be provided")
    if not author_data["Last Name"]:
        raise ValueError("The Last Name must be provided")
    is_user_name_valid(author_data["First Name"], author_data["Last Name"])


def author_with_email_exists(author_email: str) -> bool:
    """Check if the author with the given email exists."""
    if not author_email:
        raise ValueError("The author_email has to be provided.")
    if not isinstance(author_email, str):
        raise ValueError("The author_email has to be a string")
    if Author.query.filter_by(email_address=author_email).first():
        raise ValueError(f"The email address {author_email} is already in use!")


def validate_email_address(author_data: dict):
    """Check that the email address format is valid."""
    if "Email Address" not in author_data.keys():
        raise ValueError("The Emai address must be provide!")
    if not author_data["Email Address"]:
        raise ValueError("The Emai address must be provide!")
    if not isinstance(author_data["Email Address"], str):
        raise ValueError("The email address must be a string")
    author_with_email_exists(author_data["Email Address"])
    #  Regular expression for validating an Email
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    if not re.fullmatch(regex, author_data["Email Address"]):
        raise ValueError("Invalid email address format!")


def validate_nickname(author_data: dict):
    """Validate the nicknae."""
    if "Nickname" in author_data.keys():
        if not author_data["Nickname"]:
            raise ValueError("The nickname cannot be an empty string!")
        if not isinstance(author_data["Nickname"], str):
            raise TypeError("The password must be a string!")


def validate_password(author_data: dict):
    """Validate the password."""
    if "Password" not in author_data.keys():
        raise ValueError("The password must be provided!")
    if not author_data["Password"]:
        raise ValueError("The password must be provided!")


def validate_bio(author_data: dict):
    """Validate the bio."""
    if "Bio" in author_data.keys():
        if not author_data["Bio"]:
            raise ValueError("The Bio cannot be an empty string")
        if not isinstance(author_data["Bio"], str):
            raise TypeError("The author bio has to be as string")


def create_author(author_data: dict, profile_pic):
    """Handle the post request to create a new author."""
    if not author_data:
        raise ValueError("The authors data must be provided!")
    if not isinstance(author_data, dict):
        raise ValueError("The author data must be a dictionary!")
    valid_keys = [
        "First Name",
        "Last Name",
        "Email Address",
        "Bio",
        "Nickname",
        "Password",
    ]
    for key in author_data.keys():
        if key not in valid_keys:
            print(key)
            raise ValueError(f"The only valid keys are {valid_keys}")
    validate_name(author_data)
    validate_email_address(author_data)
    validate_nickname(author_data)
    validate_password(author_data)
    validate_bio(author_data)

    author = Author(
        first_name=author_data["First Name"],
        last_name=author_data["Last Name"],
        email_address=author_data["Email Address"],
        password=author_data["Password"],
    )

    print(profile_pic)

    return author_schema.dumps(author), 201


def handle_create_author(author_data: dict, profile_pic):
    """Handle the post request to create a new author."""
    try:
        author = create_author(author_data, profile_pic)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    else:
        return author
