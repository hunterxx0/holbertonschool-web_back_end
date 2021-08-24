#!/usr/bin/env python3
"""
Unit test for Client.
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
from urllib.error import HTTPError

class TestGithubOrgClient(unittest.TestCase):
    """
    Unit test CLass for GithubOrgClient.
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mck):
        """
        Test that the method returns what it is supposed to.
        """
        mck.return_value = {"payload": True}
        clt = GithubOrgClient(org)
        self.assertEqual(clt.org, mck.return_value)
        mck.assert_called_once()

    def test_public_repos_url(self):
        """
        Test that the method returns what it is supposed to.
        """
        payl = {"payload": True}
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value=payl):
            res = GithubOrgClient("google")
            self.assertEqual(res._public_repos_url, payl)

    @patch('client.get_json', return_value=[{"name": "facebook"}])
    def test_org(self, mck):
        """
        Test that the method returns what it is supposed to.
        """
        ret = "https://api.github.com/orgs/facebook/repos"
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value=ret) as pub:
            clt = GithubOrgClient("facebook")
            res = clt.public_repos()
            self.assertEqual(res, ['facebook'])
            pub.assert_called_once()
            mck.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, lic, res):
        """
        Test that the method returns what it is supposed to.
        """
        self.assertEqual(GithubOrgClient.has_license(repo, lic), res)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Unit test CLass for GithubOrgClient using fixtures.
    """
    @classmethod
    def setUpClass(cls):
        """
        setUpClass
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that the method returns what it is supposed to.
        """
        clt = GithubOrgClient("repo")
        self.assertEqual(clt.org, self.org_payload)
        self.assertEqual(clt.repos_payload, self.repos_payload)
        self.assertEqual(clt.public_repos(), self.expected_repos)
        self.assertEqual(clt.public_repos("apache-2.0"), self.apache2_repos)
