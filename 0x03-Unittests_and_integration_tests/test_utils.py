#!/usr/bin/env python3

"""This module contains all the unittests used for
the utils.py module
"""

import utils
import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """This class is the test class of the utils
    module
    """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """This function tests the access_nested_map
        method of the module
        """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """This method tests the exceptions of the access_nested_map_exception
        """
        if expected is not None:
            with self.assertRaises(expected):
                result = utils.access_nested_map(nested_map, path)



class TestGetJson(unittest.TestCase):
    """This class is the test class of the utils
    class"""

    @patch("requests.get")
    def test_get_json(self, mock_get):
        """Patch function to test"""
        mock_get.side_effect = [
                unittest.mock.Mock(json=lambda: {"payload": True}),
                unittest.mock.Mock(json=lambda: {"payload": False})
                                   ]

        result = utils.get_json("http://example.com")
        self.assertEqual(result, {'payload': True})

        result = utils.get_json("http://holberton.io")
        self.assertEqual(result, {'payload': False})

        mock_get.assert_any_call("http://example.com")
        mock_get.assert_any_call("http://holberton.io")
