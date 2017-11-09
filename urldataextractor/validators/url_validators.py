# encoding: utf-8
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

from six.moves import urllib_parse

from urldataextractor import validator
from urldataextractor.validators import exceptions

import validators


class SchemeValidator(validator.Validator):
    """Validates if provided value is an URI with a scheme.

    :raises: NoSchemeValidationError
    """

    def validate(self, value):
        parsed_url = urllib_parse.urlparse(value)

        if not parsed_url.scheme:
            raise exceptions.NoSchemeValidationError(value)


class UrlValidator(SchemeValidator):
    """Validates provided value is an url.

    :raises: NoSchemeValidationError
    :raises: UrlValidationError
    """

    def validate(self, value):
        if not validators.url(value):
            raise exceptions.UrlValidationError(value)
