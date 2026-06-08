import pytest
import random

from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_healtcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "all good"}

def test_register_user():
    random_email = f"obizian_{random.randint(1000, 9999)}@test.com"

    payload = {
        "email": random_email,
        "password": "sos1izep3yhah2ahaa"
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == random_email

def test_create_item_permission_denied():
    random_email = f"obizian_{random.randint(1000, 9999)}@test.com"
    client.post("/auth/register", json={"email": random_email, "password": "sos1i3zep3yhah2ahaa"})

    login_response = client.post("/auth/login", data={"username": random_email, "password": "sos1i3zep3yhah2ahaa"})
    token = login_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    item_payload = {
        "item_name": "paw",
        "description": "paw",
        "price": 1,
        "quantity": 10,
        "type": "pawpaw"
    }
    response = client.post("/items/", json=item_payload, headers=headers)

    assert response.status_code == 403