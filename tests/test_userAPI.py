import main as m
import random
import json
from tests.support.validate import User
from conftest import http_session

from faker import Faker
from tests.support.assertions import assert_valid_schema

f = Faker()
URL = m.TEST_URL


def test_get_list_of_users(http_session):
    response = m.get_list_of_users()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_list_of_users.json')


def test_create_user(http_session, user: User):
    # Create POST response to create new User
    payload = m.user_payload()
    response = m.create_user(payload)
    assert response.status_code == 200

    User.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'user.json')


def test_get_user_by_id(http_session):
    # Get User by User ID
    # API can respond only user ID from 1 to 10
    response = m.get_user_by_id()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'user.json')


def test_update_user_by_id(http_session, user: User):
    # Update User's params
    user_id = random.randrange(100, 1000)
    payload = {
        "id": user_id,
        "userName": f"{f.name()}",
        "password": f"{f.password()}"
    }
    response = m.update_user(payload)
    assert response.status_code == 200
    user_id_new = response.json()["id"]

    assert User.id != user_id_new
    User.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'user.json')


def test_delete_user(http_session):
    response = m.delete_user()
    assert response.status_code == 200
