from unittest import TestCase
from whentowork.client import Client
from settings import W2W_TOKEN, W2W_HOSTNAME


class TestEmployee(TestCase):

    def setUp(self):
        self.client = Client(hostname=W2W_HOSTNAME, api_key=W2W_TOKEN)
        self.employee = self.client.employees[0]

    def test_name(self):
        self.fail()
