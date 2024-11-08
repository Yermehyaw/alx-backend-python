#!/usr/bin/env python3
"""
Integration tests using unittest module

Modules imported: utils, unittest, patch,  parameterized,
requests, typing

"""
from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import (
    Mock,
    patch
)


class TestGithubOrgClient(unittest.TestCase):
    """Tests the mthds in the GithubOrg class in client.py"""
    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json')
    def test_org(self, org: str, mocked: Mock) -> None:
        """Test the org method"""
        # configure mock acting on utils.get_json(imported mthd used by org)
        mocked.return_value = {'org': org}

        # Create a client from the cls where org is defined
        client = GithubOrgClient(org)
        ret = client.org  # to call the mocked get_json defined therein

        mocked.assert_called_once_with(
            client.ORG_URL.format(org=client._org_name)
        )
        self.assertEqual({'org': org}, ret)
