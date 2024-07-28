#!/usr/bin/env python3
"""Module for testing utils file"""
import utils
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Defining the test utils class"""
    @parameterized.expand([
		({"a": 1}, ("a",), 1),  # (nested_map, path, expected_value)
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
	])
    def test_access_nested_maps(self, nested_map, path, expected):
        """tests the nested map output"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
