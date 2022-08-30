import requests
from pytest_voluptuous import S
from voluptuous import Schema, Any, ALLOW_EXTRA,PREVENT_EXTRA

from Lesson.schemas.facts import facts
from Lesson.utils.sessions import reqres


def test_facts_count():
    limit = 2
    response = requests.get("https://catfact.ninja/facts", params={'limit': limit})
    assert len(response.json()['data']) == limit


def test_facts_count_v2():
    limit = 2
    response = reqres().get("/facts", params={"limit": limit})
    assert len(response.json()['data']) == limit


def test_fact_schema_validation():
    limit = 2
    schema = Schema({
        'current_page': int,
        'data': [
            {
                'fact': str,
                'length': int
            }
        ],
        'first_page_url': str,
        'from': int,
        'last_page': int,
        'last_page_url': str,
        'links': [
            {
                'url': Any(None, str),
                'label': str,
                'active': bool
            }
        ],
        'next_page_url': str,
        'path': str,
        'per_page': str,
        'prev_page_url': Any(None, str),
        'to': int,
        'total': int
    })

    response = requests.get("https://catfact.ninja/facts", params={'limit': limit})

    assert S(schema) == response.json()
    assert response.status_code == 200


def test_fact_schema_validation_short():
    limit = 2

    response = requests.get("https://catfact.ninja/facts", params={'limit': limit})

    assert S(facts) == response.json()
    assert response.status_code == 200




def test_fact_schema_validation_short3():
    response = requests.get("https://catfact.ninja/fact")

    assert isinstance(response.json()['fact'], str)
    assert isinstance(response.json()['length'], int)


def test_fact_schema_validation1():
    limit = 3
    schema = Schema({
        'current_page': int,
        'data': [
            {
                'fact': str,
                'length': int
            }
        ],
        'first_page_url': str,
        'from': int,
        'last_page': int,
        'last_page_url': str,
        'links': [
            {
                'url': Any(None, str),
                'label': str,
                'active': bool
            }
        ],
        'next_page_url': int,
        'path': str,
        'per_page': str,
        'prev_page_url': Any(None, str),
        'to': int,
        'total': int
    })

    response = requests.get("https://catfact.ninja/facts", params={limit})

    assert S(schema) == response.json()


def test_fact_schema_validation_extra():
    limit = 3
    schema = Schema({
        'current_page': int,
        'data': [
            {
                'fact': str,
                'length': int
            }
        ]
    },
        extra=PREVENT_EXTRA,
        required=True
    )

    response = requests.get("https://catfact.ninja/facts", params={'limit': limit})

    assert S(schema) == response.json()
