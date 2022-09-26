# -*- coding: utf-8 -*-
"""This module declares and registers extensions."""
from flasgger import LazyJSONEncoder, LazyString, Swagger
from flask import request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

cors = CORS()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask Blog.",
        "description": "An application for creating, viewing, editing blog posts.",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "lyceokoth@gmail.com",
            "url": "www.twitter.com/lylethedesigner",
        },
        "termsOfService": "www.twitter.com/deve",
        "version": "1.0",
    },
    "host": LazyString(lambda: request.host),
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "APIKeyHeader": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": 'JWT Authorization header using the Bearer scheme. Example:"Authorization: Bearer {token}"',
        }
    },
}


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}

swagger = Swagger(template=swagger_template, config=swagger_config)


def register_extensions(app):
    """Register the application extensions."""
    cors.init_app(app)
    app.json_encoder = LazyJSONEncoder
    swagger.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
