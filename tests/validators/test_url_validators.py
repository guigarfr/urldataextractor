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

from urldataextractor.validators import exceptions
from urldataextractor.validators import url_validators

from .. import test_validator


class UrlValidatorTests(test_validator.ValidatorTestBase, case.TestCase):

    object_class = url_validators.UrlValidator

    def _test_validate_url_exception(self, value):
        super(UrlValidatorTests, self)._test_validate_exception(
            value,
            exceptions.UrlValidationError)

    def test_validate_urlno_scheme(self):
        self._test_validate_url_exception('www.test.com')

    # Http tests

    def test_validate_url__ip(self):
        self.validator.validate('http://192.18.1.1')

    def test_validate_url__ip__invalid_value(self):
        self._test_validate_url_exception('http://256.18.1.1')

    def test_validate_url__ip__invalid_format(self):
        self._test_validate_url_exception('http://255.18.1')

    def test_validate_url__http__no_path(self):
        self.validator.validate('http://www.test.com')

    def test_validate_url__http__path(self):
        self.validator.validate('http://www.test.com/some/path')

    def test_validate_url__http__query(self):
        self.validator.validate('http://www.test.com/some/path?foo=var')

    def test_validate_url__http__named(self):
        self.validator.validate('http://localhost')

    def test_validate_url__http__invalid_scheme_separator(self):
        self._test_validate_url_exception('http:/www.test.com')

    # Ftp Tests

    def test_validate_url__ftp__no_path(self):
        self.validator.validate('ftp://www.test.com')

    def test_validate_url__ftp__path(self):
        self.validator.validate('ftp://www.test.com/some/path')

    def test_validate_url__ftp__query(self):
        self.validator.validate('ftp://www.test.com/some/path?foo=var')

    def test_validate_url__ftp__named(self):
        self.validator.validate('ftp://localhost')
