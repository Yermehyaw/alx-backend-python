#!/usr/bin/env python3
"""
IIntegration tests using unittest module

Modules imported: utils, unittest, parameterized, typong

"""
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Any,
    Mapping,
    Sequence
)
import unittest


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
