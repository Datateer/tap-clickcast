"""Tests standard tap features using the built-in SDK tests library."""

import json
from tap_clickcast.streams import EmployersStream
from tap_clickcast.tap import TapClickcast

SAMPLE_CONFIG = {"partner_token": "testing"}


class FakeResponse(object):
    def __init__(self, response_body: str):
        self.response_body = response_body

    def json(self):
        return json.loads(self.response_body)


def build_basic_response(current_page, page_count=6):
    response_string = (
        "{"
        '  "count": 526,'
        f'  "num_pages": {page_count},'
        f'  "page": {current_page},'
        '  "results": ['
        "    {"
        '      "employer_id": 4508,'
        '      "employer_name": "2020 Companies"'
        "    },"
        "    {"
        '        "employer_id": 5287,'
        '        "employer_name": "2020 Companies - Jobcase"'
        "    }"
        "  ]"
        "}"
    )
    return FakeResponse(response_string)


BASE_CLIENT = EmployersStream(TapClickcast(SAMPLE_CONFIG))


def test_get_current_page_returns_current_page():
    res = build_basic_response(2)
    actual = BASE_CLIENT.get_current_page(res)
    assert actual == 2


def test_get_page_count_returns_page_count():
    res = build_basic_response(2)
    actual = BASE_CLIENT.get_page_count(res)
    assert actual == 6


def test_get_next_page_token_returns_next_page():
    res = build_basic_response(2)
    actual = BASE_CLIENT.get_next_page_token(res, None)
    assert actual == 3


def test_get_next_page_token_returns_none_if_on_last_page():
    res = build_basic_response(6)
    actual = BASE_CLIENT.get_next_page_token(res, None)
    assert actual is None


def test_get_next_page_token_returns_none_if_only_one_page():
    res = build_basic_response(1, page_count=1)
    actual = BASE_CLIENT.get_next_page_token(res, None)
    assert actual is None
