"""Tests for ping views."""
from http import HTTPStatus

from flask import url_for


def test_ping(client):
    """Test for ping endpoint."""
    response = client.get(url_for("ping.main"))
    assert response.status_code == HTTPStatus.OK


#import pytest
#from app import create_app


#@pytest.fixture
#def client():
#    app = create_app()
#    app.config["TESTING"] = True
#    with app.test_client() as client:
#        yield client


#def test_square(client):
#    rv = client.get("/ping/")
#    assert 200 == rv.status_code