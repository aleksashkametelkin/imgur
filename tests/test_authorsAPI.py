import json
import random

import main as m
from tests.support.assertions import assert_valid_schema
from utils.models import BaseClass

URL = m.TEST_URL


def test_get_list_of_authors():
    response = m.get_list_of_authors()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_list_of_authors.json')


def test_create_author(user: BaseClass):
    # Create POST response to create new User
    payload = m.author_payload()
    response = m.create_author(payload)
    assert response.status_code == 200

    BaseClass.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'author.json')


def test_get_book_by_author_id():
    # Get Author by Author ID
    # API can respond only user ID from 1 to 10
    response = m.get_book_of_author()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'book.json')


def test_get_author_id():
    # Get Author by Author ID
    # API can respond only Author ID from 1 to 10
    response = m.get_author_by_id()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'author.json')


def test_update_author_by_id(user: BaseClass):
    # Update Author's params
    author_id = random.randrange(1, 200)
    payload = {
        "id": author_id,
        "idBook": user.idBook,
        "firstName": f"{user.firstName}",
        "lastName": f"{user.lastName}"
    }
    response = m.update_author(payload)
    assert response.status_code == 200
    author_id_new = response.json()["id"]

    assert BaseClass.id != author_id_new
    BaseClass.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'author.json')


def test_delete_author_by_id():
    # Delete existing activity
    response = m.delete_author()
    assert response.status_code == 200
