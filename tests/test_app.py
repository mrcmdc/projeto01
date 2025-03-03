from http import HTTPStatus

from fastapi.testclient import TestClient

from projeto01.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    with TestClient(app) as client:
        response = client.get('/')
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'Hello': 'World'}
