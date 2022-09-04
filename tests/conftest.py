import os

import pytest
from dotenv import load_dotenv

from Lesson.utils.requests_helper import BaseSession


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


@pytest.fixture(scope='session')
def demoqa() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    with BaseSession(base_url=demo_url) as session:
        yield session


@pytest.fixture(scope='session')
def demoqa_authorized() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    aut_cookie_name = 'NOPCOMMERCE.AUTH'
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    with BaseSession(base_url=demo_url) as session:
        response = session.post('/login',
                                data={'email': login, 'password': password},
                                allow_redirects=False
                                )
        auth_cookie_value = response.cookies.get(aut_cookie_name)
        session.cookies.set(aut_cookie_name, auth_cookie_value)
        yield session



