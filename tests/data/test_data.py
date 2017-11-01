# -*- coding: utf-8 -*-
"""
   Copyright 2017 Guillermo García

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from __future__ import unicode_literals

from unittest import case

import urldataextractor


class DataClassTests(case.TestCase):
    def setUp(self):
        super(DataClassTests, self).setUp()

    def test_init(self):
        data_object = urldataextractor.Data()

        self.assertTrue(data_object.items.__iter__)
        self.assertListEqual(list(data_object.items), [])

        self.assertTrue(data_object.keys.__iter__)
        self.assertListEqual(list(data_object.keys), [])

        self.assertTrue(data_object.values.__iter__)
        self.assertListEqual(list(data_object.values), [])

        self.assertTrue(data_object.__iter__)
        self.assertSetEqual(set(data_object), set())

    def test_add(self):
        data_object = urldataextractor.Data()
        data_object.add('foo', 'bar')
        self.assertListEqual(list(data_object.items), [('foo', ['bar'])])
        self.assertListEqual(list(data_object.keys), ['foo'])
        self.assertListEqual(list(data_object.values), ['bar'])

    def test_add__multiple(self):
        data_object = urldataextractor.Data()
        data_object.add('foo', 'bar')
        data_object.add('foo', 2)
        data_object.add('bar', {})
        self.assertListEqual(
            list(data_object.items),
            [('foo', ['bar', 2]), ('bar', [{}])],
        )
        self.assertListEqual(list(data_object.keys), ['foo', 'bar'])
        self.assertListEqual(list(data_object.values), ['bar', 2, {}])
