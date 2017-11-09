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
        data_object = urldataextractor.ExtractedData()

        self.assertTrue(data_object.data.items.__iter__)
        self.assertListEqual(list(data_object.data.items), [])

        self.assertTrue(data_object.data.keys.__iter__)
        self.assertListEqual(list(data_object.data.keys), [])

        self.assertTrue(data_object.data.__iter__)
        self.assertListEqual(list(data_object.data), [])

    def test_add(self):
        data_object = urldataextractor.ExtractedData()
        data_object.add_value('foo', 'bar')

        self.assertListEqual(list(data_object.data.items), [('foo', ['bar'])])
        self.assertListEqual(list(data_object.data.keys), ['foo'])
        self.assertListEqual(list(data_object.data.values), ['bar'])
        self.assertListEqual(list(data_object.data), [('foo', 'bar')])

        self.assertListEqual(list(data_object.errors.items), [])
        self.assertListEqual(list(data_object.errors.keys), [])
        self.assertListEqual(list(data_object.errors.values), [])
        self.assertListEqual(list(data_object.errors), list(data_object.errors.values))

    def test_add_value__multiple(self):
        data_object = urldataextractor.ExtractedData()
        data_object.add_value('foo', 'bar')
        data_object.add_value('foo', 2)
        data_object.add_value('bar', {})

        self.assertListEqual(
            list(data_object.data.items),
            [('foo', ['bar', 2]), ('bar', [{}])],
        )
        self.assertListEqual(list(data_object.data.keys), ['foo', 'bar'])
        self.assertListEqual(list(data_object.data.values), ['bar', 2, {}])
        self.assertListEqual(list(data_object.data), [('foo', 'bar'), ('foo', 2), ('bar', {})])

        self.assertListEqual(list(data_object.errors.items), [])
        self.assertListEqual(list(data_object.errors.keys), [])
        self.assertListEqual(list(data_object.errors.values), [])
        self.assertListEqual(list(data_object.errors), [])

    def test_add_error(self):
        data_object = urldataextractor.ExtractedData()
        data_object.add_error('foo', 'bar')

        self.assertListEqual(list(data_object.data.items), [])
        self.assertListEqual(list(data_object.data.keys), [])
        self.assertListEqual(list(data_object.data.values), [])
        self.assertListEqual(list(data_object.data), [])

        self.assertListEqual(list(data_object.errors.items), [('foo', ['bar'])])
        self.assertListEqual(list(data_object.errors.keys), ['foo'])
        self.assertListEqual(list(data_object.errors.values), ['bar'])
        self.assertListEqual(list(data_object.errors), [('foo', 'bar')])

    def test_add_error__multiple(self):
        data_object = urldataextractor.ExtractedData()
        data_object.add_error('foo', 'bar')
        data_object.add_error('foo', 2)
        data_object.add_error('bar', {})

        self.assertListEqual(list(data_object.data.items), [])
        self.assertListEqual(list(data_object.data.keys), [])
        self.assertListEqual(list(data_object.data.values), [])
        self.assertListEqual(list(data_object.data), [])

        self.assertListEqual(
            list(data_object.errors.items),
            [('foo', ['bar', 2]), ('bar', [{}])],
        )
        self.assertListEqual(list(data_object.errors.keys), ['foo', 'bar'])
        self.assertListEqual(list(data_object.errors.values), ['bar', 2, {}])
        self.assertListEqual(list(data_object.errors), [('foo', 'bar'), ('foo', 2), ('bar', {})])
