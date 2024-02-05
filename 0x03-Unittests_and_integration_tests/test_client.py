#!/usr/bin/env python3
"""Test that GithubOrgClient.org returns the correct value."""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test the GithubOrgClient class."""

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
        g = GithubOrgClient(org)
        self.assertEqual(g.org, expected)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Test that the GithubOrgClient._public_repos_url returns the correct value."""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://someurl.com"}
            g = GithubOrgClient("google")
            self.assertEqual(g._public_repos_url, "http://someurl.com")

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """Test that the GithubOrgClient.public_repos returns the correct value."""
        payload = [{"name": "google"}]
        mock_get.return_value = payload
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
            return_value="http://someurl.com",
        ) as mock_public:
            g = GithubOrgClient("google")
            self.assertEqual(g.public_repos(), ["google"])
            mock_get.assert_called_once_with("http://someurl.com")
