#!/usr/bin/env python3
"""Unit test for utils.access_nested_map."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
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

    @patch("requests.get")
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        # Mock the 'get' method to return a Mock object with a 'json' method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        requests_get_mock = Mock(return_value=mock_response)

        # Patch the 'requests.get' method with the mock
        with patch("requests.get", requests_get_mock):
            result = utils.get_json(test_url)

        # Assertions
        requests_get_mock.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
