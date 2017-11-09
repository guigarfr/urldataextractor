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

from urldataextractor import validator

from . import base


class ValidatorTestBase(base.TestObjectBase):

    init_object_on_setup = True
    validator = None

    def setUp(self):
        super(ValidatorTestBase, self).setUp()
        self.validator = self.object

    def _test_validate_exception(self, value, exception):
        with self.assertRaises(exception) as ctx:
            self.validator.validate(value)
        self.assertEqual(ctx.exception.value, value)


class BasicValidatorTests(ValidatorTestBase, case.TestCase):

    object_class = validator.Validator

    def test_validate_value(self):
        validator_object = self.get_test_object()
        with self.assertRaises(NotImplementedError):
            validator_object.validate('foo')
