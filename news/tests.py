from django.test import TestCase

# Create your tests here.
import unittest
import json
from django.test import Client


class NewsTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/news/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context is a list
        json_checker = json.loads(response.content)
        self.assertIsInstance(json_checker,list)


class QueryTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/news/',{'query': "bitcoin"})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context is a list
        json_checker = json.loads(response.content)
        # print(json_checker)
        self.assertIsInstance(json_checker,list)