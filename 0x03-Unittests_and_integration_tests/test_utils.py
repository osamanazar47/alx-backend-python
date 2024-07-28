#!/usr/bin/env python3
"""Module for testing utils file"""
from unittest.mock import patch, Mock
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

    @parameterized.expand([
		({}, ("a",)),
		({"a": 1}, ("a", "b"))
	])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         ) -> None:
        """"Tests `access_nested_map`'s error handling"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Defining class for testin the getjson method in utils.py"""
    @parameterized.expand([
		("http://example.com", {"payload": True}),
		("http://holberton.io", {"payload": False}),
	])
    def test_get_json(self, url: str, res: Dict) -> None:
        """for testing the fuction output"""
        mock_res = Mock()
        mock_res.json.return_value = res
        with patch('utils.requests.get', return_value=mock_res) as mock_get:
            self.assertEqual(utils.get_json(url), res)
            mock_get.assert_called_once_with(url)

class TestMemoize(unittest.TestCase):
    """Defining class for testing the memoize method in utils.py"""
    def test_memoize(self) -> None:
        """for testing the memoize method"""
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_a_method:
            result1 = instance.a_property
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_a_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
