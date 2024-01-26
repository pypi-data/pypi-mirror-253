from fastapi.testclient import TestClient
from fsapp.base import app
from fsapp.core.config import settings

client = TestClient(app)


def test_main_page():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': f"Hello {settings.required.instance}"}


test_main_page()