from unittest import TestCase, mock
import requests

from whentowork.adapter import Adapter
from whentowork.models import Result
from settings import W2W_TOKEN, W2W_HOSTNAME


class TestAdapter(TestCase):
    def setUp(self):
        self.adapter = Adapter(hostname=W2W_HOSTNAME, api_key=W2W_TOKEN)
        self.response = requests.Response()

    def test__do_good_request_returns_result(self):
        self.response.status_code = 200
        self.response._content = "{}".encode()
        with mock.patch("requests.request", return_value=self.response):
            result = self.adapter._do('GET', '')
            self.assertIsInstance(result, Result)

    def test__get(self):
        self.fail()

    def test_get_from_endpoint(self):
        self.fail()
