#!/usr/bin/env python3
"""Module for testing utils file"""
import utils
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """Defining the test utils class"""
    @parameterized.expand([
		({"a": 1}, ("a",), 1),  # (nested_map, path, expected_value)
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
	])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
