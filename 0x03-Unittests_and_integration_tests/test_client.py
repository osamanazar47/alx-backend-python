#!/usr/bin/env python3
"""Module for testing the client.py file"""
import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Difining the class for testing the client file"""
    @parameterized.expand([
		("google", {"login": "google"}),
		("abc", {"login": "abc"}),
	])
    @patch('client.get_json')
    def test_org(self, org: str, exp_result: Dict, mock_g_json: Mock) -> None:
        """for testing the org method"""
        mock_g_json.return_value = exp_result
        client = GithubOrgClient(org)
        result = client.org

        exp_url = f"https://api.github.com/orgs/{org}"
        mock_g_json.assert_called_once_with(exp_url)
        self.assertEqual(result, exp_result)

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json', return_value=[
		{"name": "repo1"},
		{"name": "repo2"},
		{"name": "repo3"},
	])
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """For testiing the public_repos method in client file"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/google/repos"
            client = GithubOrgClient("google")
            result = client.public_repos()

            # Assert that the result matches the expected list of repo names
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Assert that the mocked property was called once
            mock_url.assert_called_once()

            # Assert that the mocked get_json was called once with the correct URL
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")


if __name__ == '__main__':
    unittest.main()
