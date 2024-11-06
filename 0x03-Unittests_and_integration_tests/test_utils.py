#!/usr/bin/env python3
"""
IIntegration tests using unittest module

Modules imported: utils, unittest, patch,  parameterized,
rrequests, typing

"""
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json
)
from typing import (
    Any,
    Dict,
    Mapping,
    Sequence
)
import requests
import unittest
from unittest.mock import (
    Mock,
    patch
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the mthds in utils module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        (
            {"a": {"b": 2}},
            ("a", "b"),
            2
        )
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any
    ) -> None:
        """Tests the access_nested_map mthd
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, "a"),
        ({"a": 1}, ("a", "b"), KeyError, "b")
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            exception_raised: Exception,
            exception_msg: str
    ) -> None:
        """Test the appr Exception is raised
        """
        with self.assertRaises(exception_raised) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(str(e.exception), exception_msg)


class TestGetJson(unittest.TestCase):
    """Tests the get_json mthd in utils
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(
            self,
            test_url: str,
            test_package: Dict,
            mock_obj: Mock,
    ) -> None:
        """Test get_json
        """
        # Create a response
        mock_obj.return_value.json.return_value = test_package

        # Make a request with the patched method
        resp = get_json(test_url)

        # Test if the patched mthd was called
        mock_obj.assert_called_once_with(test_url)

        # Test if the resp received is the same as the created response
        self.assertEqual(test_package, resp)
