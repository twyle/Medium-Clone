# -*- coding: utf-8 -*-
"""Export all the extensions."""
from .extensions import bcrypt, cors, db, ma, migrate, register_extensions, swagger

__all__ = ["cors", "swagger", "db", "ma", "migrate", "register_extensions", "bcrypt"]
