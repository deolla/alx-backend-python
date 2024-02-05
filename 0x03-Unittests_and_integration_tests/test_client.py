#!/usr/bin/env python3
"""Test that GithubOrgClient.org returns the correct value."""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """This class test the GithubOrgClient class."""

    @parameterized.expand(
        [
            ("google", {"google": True}),
            ("abc", {"abc": False}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org, expected, mock_get):
        """Test that the GithubOrgClient.org returns the correct value."""
        mock_get.return_value = expected
        pop = GithubOrgClient(org)
        self.assertEqual(pop.org, expected)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Test the GithubOrgClient._public_repos_url returns expected value."""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://someurl.com"}
            pop = GithubOrgClient("google")
            self.assertEqual(pop._public_repos_url, "http://someurl.com")

    @patch("client.get_json")
    def test_public_repos(self, mock_find):
        """Test public_repos method."""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_find.return_value = json_payload

        with patch(
            "client.GithubOrgClient._public_repos_url", new_callable=PropertyMock
        ) as mock_public:

            mock_public.return_value = "hello/world"
            pop = GithubOrgClient("test")
            result = pop.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_find.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """unit-test for GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD,
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """Integration test for GithubOrgClient class."""

        @classmethod
        def setUpClass(cls):
            """setUpClass method."""
            cls.get_patcher = patch("requests.get", side_effect=cls.get_side_effect)
            cls.mock_get = cls.get_patcher.start()

        @classmethod
        def tearDownClass(cls):
            """tearDownClass method."""
            cls.get_patcher.stop()

        @staticmethod
        def get_side_effect(url):
            """get_side_effect method."""
            if url == "https://api.github.com/orgs/google":
                return Mock(json=Mock(return_value=TestGithubOrgClient.org_payload))
            if url == "https://api.github.com/orgs/google/repos":
                return Mock(json=Mock(return_value=TestGithubOrgClient.repos_payload))

        def test_public_repos(self):
            """Integration tests for public_repos method."""
            test_class = GithubOrgClient("google")

            self.assertEqual(test_class.org, self.org_payload)
            self.assertEqual(test_class.repos_payload, self.repos_payload)
            self.assertEqual(test_class.public_repos(), self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.mock.assert_called()

        def test_public_repos_with_license(self):
            """Integration tests for public_repos method."""
            test_class = GithubOrgClient("google")

            self.assertEqual(test_class.public_repos(), self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.assertEqual(test_class.public_repos("apache-2.0"), self.apache2_repos)
            self.mock.assert_called()
