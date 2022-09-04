import os
from Lesson.utils.requests_helper import BaseSession
from dotenv import load_dotenv


def reqres() -> BaseSession:
    reqres_url = "https://reqres.in/api"  # os.getenv('cats_api')
    return BaseSession(base_url=reqres_url)


def cats() -> BaseSession:
    cats_url = os.getenv('cats_api')
    return BaseSession(base_url=cats_url)


def demoqa() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    return BaseSession(base_url=demo_url)
