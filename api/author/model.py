# -*- coding: utf-8 -*-
"""This module contains the Author user model."""
from datetime import datetime

from sqlalchemy.dialects.postgresql import ARRAY

from ..extensions import bcrypt, db, ma


class Author(db.Model):
    """The Author Model."""

    __tablename__ = "author"
    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String(100), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    screen_name: str = db.Column(db.String(100), nullable=True)
    email_address: str = db.Column(db.Text, nullable=False)
    profile_picture: str = db.Column(db.String(100), nullable=True)
    password_hash: str = db.Column(db.String(100), nullable=False)
    registered_on: datetime = db.Column(db.DateTime(), default=datetime.utcnow)
    is_active: bool = db.Column(db.Boolean(), default=False)
    is_authenticated: bool = db.Column(db.Boolean(), default=False)
    bio: str = db.Column(db.Text, nullable=True)
    interests: list = db.Column(ARRAY(db.String(100)), nullable=True)
    follows: list = db.Column(ARRAY(db.Integer), nullable=True)
    followers: list = db.Column(ARRAY(db.Integer), nullable=True)

    def create_screen_name(self) -> None:
        """Create a screen name for the user."""
        self.screen_name = f"{self.first_name}_{self.last_name}"

    @property
    def password(self):
        """Raise an exception when password is accessed."""
        raise AttributeError("Password is a write-only field!")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Check if password hash is correct."""
        return bcrypt.check_password_hash(self.password_hash, password)


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
