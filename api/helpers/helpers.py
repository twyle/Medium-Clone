# -*- coding: utf-8 -*-
"""This module declares the application helpers."""
import os

from ..admin.views import admin
from ..article.views import article
from ..auth.views import auth
from ..author.views import author
from ..email.views import mail
from ..flag.views import flag
from ..home.views import home
from ..moderator.views import moderator
from ..report.views import report
from ..suspend.views import suspend


def set_flask_environment(app) -> str:
    """Set the flask development environment.

    Parameters
    ----------
    app: flask.Flask
        The flask application object

    Raises
    ------
    KeyError
        If the FLASK_ENV environment variable is not set.

    Returns
    -------
    str:
        Flask operating environment i.e development
    """
    try:
        if os.environ["FLASK_ENV"] == "production":  # pragma: no cover
            app.config.from_object("api.config.config.ProductionConfig")
        elif os.environ["FLASK_ENV"] == "development":  # pragma: no cover
            app.config.from_object("api.config.config.DevelopmentConfig")
        elif os.environ["FLASK_ENV"] == "test":
            app.config.from_object("api.config.config.TestingConfig")
        elif os.environ["FLASK_ENV"] == "stage":
            app.config.from_object("api.config.config.StagingConfig")
    except KeyError:
        app.config.from_object("api.config.config.DevelopmentConfig")
        return "development"

    return os.environ["FLASK_ENV"]


def register_blueprints(app):
    """Register the application blueprints."""
    app.register_blueprint(admin, url_prefix="/api/v1/admin")
    app.register_blueprint(auth, url_prefix="/api/v1/auth")
    app.register_blueprint(article, url_prefix="/api/v1/article")
    app.register_blueprint(author, url_prefix="/api/v1/author")
    app.register_blueprint(mail, url_prefix="/api/v1/mail")
    app.register_blueprint(flag, url_prefix="/api/v1/flag")
    app.register_blueprint(home, url_prefix="/api/v1/home")
    app.register_blueprint(moderator, url_prefix="/api/v1/moderator")
    app.register_blueprint(report, url_prefix="/api/v1/report")
    app.register_blueprint(suspend, url_prefix="/api/v1/suspend")
