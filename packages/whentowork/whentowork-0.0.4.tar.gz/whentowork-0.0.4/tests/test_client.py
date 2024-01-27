from unittest import TestCase
import requests

from whentowork.client import Client
from settings import W2W_TOKEN, W2W_HOSTNAME


class TestClient(TestCase):

    def setUp(self):
        self.client = Client(hostname=W2W_HOSTNAME, api_key=W2W_TOKEN)
        self.response = requests.Response()

    def test__update_company(self):
        self.fail()

    def test__update_employees(self):
        self.fail()

    def test__update_positions(self):
        self.fail()

    def test__update_categories(self):
        self.fail()

    def test__add_emp_pos_cat_to_shift(self):
        self.fail()

    def test__add_emp_to_timeoff(self):
        self.fail()

    def test_get_employee_by_id(self):
        self.fail()

    def test_get_position_by_id(self):
        self.fail()

    def test_get_category_by_id(self):
        self.fail()

    def test_get_shifts_by_date(self):
        self.fail()

    def test_get_timeoff_by_date(self):
        self.fail()
