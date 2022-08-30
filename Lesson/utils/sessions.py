import os
from Lesson.utils.requests_helper import BaseSession


def reqres() -> BaseSession:
    reqres_url = "https://reqres.in/api"
    return BaseSession(base_url=reqres_url)
