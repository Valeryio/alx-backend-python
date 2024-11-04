#!/usr/bin/env python3

"""This module contains all the unittests used for
the utils.py module
"""

import utils
import unittest
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
