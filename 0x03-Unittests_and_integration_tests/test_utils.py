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
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exceptions):
        """A method to test that the method raises the correct exceptions."""
        with self.assertRaises(KeyError) as context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(f"KeyError('{exceptions}')", repr(context.exception))
