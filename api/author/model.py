# -*- coding: utf-8 -*-
"""This module contains the Author user model."""
from sqlalchemy.dialects.postgresql import ARRAY

from ..extensions import db, ma
from ..models import User


class Author(User):
    """The Author Model."""

    __tablename__ = "author"
    id: int = db.Column(db.Integer, primary_key=True)
    bio: str = db.Column(db.Text, nullable=True)
    interests: list = db.Column(ARRAY(db.String(100)), nullable=True)
    follows: list = db.Column(ARRAY(db.Integer), nullable=True)
    followers: list = db.Column(ARRAY(db.Integer), nullable=True)


class AuthorSchema(ma.Schema):
    """Show all the author information."""

    class Meta:
        """The fileds to display."""

        fields = (
            "id",
            "first_name",
            "last_name",
            "screen_name",
            "email",
            "date_registered",
            "profile_pic",
            "bio",
        )


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
