#!/usr/bin/env python3
""" unittests client module
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value=org_payload)
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, org_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch(
        'client.GithubOrgClient.org',
        new_callable=PropertyMock,
        return_value=org_payload
    )
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url returns correct value"""
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, org_payload["repos_url"])

    @patch('client.get_json', return_value=repos_payload)
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock,
        return_value="https://api.github.com/orgs/google/repos"
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct value"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), expected_repos)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos"
        )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct value"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(org_payload, repos_payload, expected_repos, apache2_repos)]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get"""
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.get_side_effect)
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patcher"""
        cls.get_patcher.stop()

    @staticmethod
    def get_side_effect(url):
        """Side effect method to mock requests.get().json()"""
        if url == "https://api.github.com/orgs/google":
            return Mock(**{"json.return_value": org_payload})
        elif url == "https://api.github.com/orgs/google/repos":
            return Mock(**{"json.return_value": repos_payload})
        return Mock(**{"json.return_value": {}})

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos with integration"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
