import requests

from schemas.reqres import create, register, single_user, list_user
from Lesson.utils.sessions import reqres
from pytest_voluptuous import S


def test_create():
    users = {
        "name": "Bohdan",
        "job": "QA"
    }
    response = reqres().post('/users', data=users)
    assert response.json()["name"] == 'Bohdan'
    assert response.json()["job"] == 'QA'
    assert response.status_code == 201
    assert S(create) == response.json()


def test_register():
    users = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = reqres().post('/register', data=users)
    assert response.json()["id"] == 4
    assert response.json()["token"] == 'QpwL5tke4Pnpja7X4'
    assert response.status_code == 200
    assert S(register) == response.json()


def test_single_user():
    response = reqres().get('/users/3')

    assert response.json()["data"]["id"] == 3
    assert response.json()["data"]["avatar"] == "https://reqres.in/img/faces/3-image.jpg"
    assert response.status_code == 200
    assert S(single_user) == response.json()


def test_list_user():
    page = 2
    response = reqres().get('/users', params={'page': page})
    assert len(response.json()["data"]) == 6
    assert response.json()["total"] == 12
    assert response.json()["total_pages"] == page
    assert response.json()["data"][0]['id'] == 7
    assert response.json()["data"][0]['avatar'] == 'https://reqres.in/img/faces/7-image.jpg'
    assert response.status_code == 200
    assert S(list_user) == response.json()


def test_delete_user():
    response = reqres().delete('/users/3')

    assert response.status_code == 204



