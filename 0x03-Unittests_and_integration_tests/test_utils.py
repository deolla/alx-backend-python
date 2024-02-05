#!/usr/bin/env python3
"""Unit test for utils.access_nested_map."""
import unittest
from parameterized import parameterized
import utils


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

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        """Raise Expection Message"""
        with self.assertRaises(KeyError) as context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_exception_message)


if __name__== "__main__":
    unittest.main()
