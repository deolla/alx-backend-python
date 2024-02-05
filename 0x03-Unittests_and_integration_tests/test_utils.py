#!/usr/bin/env python3
"""Unit test for utils.access_nested_map."""
import unittest
from parameterized import parameterized
from unittest.mock import patch
import utils
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """Create a TestMemoize class that inherits from unittest.TestCase."""

    def test_memoize(self):
        """A method to test that the method returns what it is supposed to."""

        class TestClass:
            """A class to test the method return value."""

            def a_method(self):
                """A method to test the return value."""
                return 42

            @memoize
            def a_property(self):
                """A method to test the return value."""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock.assert_called_once()
            mock.assert_called_with()
