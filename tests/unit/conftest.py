# -*- coding: utf-8 -*-
"""This module sets up the fixtures that will be used in our testing."""
import pytest

from api import create_app as create_app_


@pytest.fixture
def create_app():
    """Create the app instance."""
    app = create_app_()
    return app


@pytest.fixture
def client():
    """Create the test client."""
    # create_app_().config.from_object(TestingConfig)
    test_client = create_app_().test_client()
    # with create_app_().app_context():
    #     db.drop_all()
    #     db.create_all()

    return test_client
