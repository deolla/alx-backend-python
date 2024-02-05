#!/usr/bin/env python3
"""Unit test for utils.access_nested_map."""
import unittest
from parameterized import parameterized
from unittest.mock import patch
import utils
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Create a TestAccessNestedMap class that inherits
    from unittest.TestCase."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        """A method to test that the method returns what it is supposed to."""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, nested_map, path, exceptions):
        """A method to test that the method raises the correct exceptions."""
        with self.assertRaises(KeyError) as context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(f"KeyError('{exceptions}')", repr(context.exception))


class TestGetJson(unittest.TestCase):
    """Create a TestGetJson class that inherits from unittest.TestCase."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, payload):
        """A method to test that the method returns what it is supposed to."""
        pop = {"return_value.json.return_value": payload}
        patches = patch("requests.get", **pop)
        mock = patches.start()
        self.assertEqual(get_json(url), payload)
        mock.asseert_called_once()
        patches.stop()
