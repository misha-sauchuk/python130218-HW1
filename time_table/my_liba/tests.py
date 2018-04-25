from django.test import TestCase, client
from .views import books
from unittest.mock import patch
# Create your tests here.
import unittest

unittest.TestCase

class MyTestCase(unittest.TestCase):
    def test_ok(self):
        return True

    def test_error(self):
        result = sum([1,4])
        self.assertNotEquals(result,6)

    def test_invalid_paran(self):
        self.assertRaises(TypeError, sum, ['abass', 1])


class ListViewTestCase(TestCase):

    @patch('liba.views.Books')
    def test_get_ok(self):
        request = None
        view = books(request)
        response = view.get(request)
        self.assertEqual(response.status_code, 200)