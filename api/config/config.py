# -*- coding: utf-8 -*-
"""This module contain the confuguration for the application."""
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration."""

    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Configuration used during development."""

    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    """Configuration used during testing."""

    DEBUG = True
    TESTING = True


class StagingConfig(BaseConfig):
    """Configuration used during staging."""

    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    """Configuration used during production."""

    DEBUG = False
    TESTING = False
