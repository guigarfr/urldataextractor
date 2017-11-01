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
import re

from urldataextractor import exceptions


class SimpleExtractor(object):
    """Extracts data from an url."""

    transformers = None
    raw_validators = None
    validators = None

    def __init__(self, key=None):
        if not key:
            raise exceptions.RequiredParameterError()

        self.key = key
        self.raw_validators = self.raw_validators or []
        self.transformers = self.transformers or []
        self.validators = self.validators or []

    def get_source(self, url):
        raise NotImplementedError("You should implement this method")

    def extract(self, url):
        for value in self.extract_from_source(self.get_source(url)):
            yield value

    def extract_from_source(self, source):
        """Can be an iterator."""
        raise NotImplementedError("You should implement this method")

    def transform(self, data):
        transformed_data = data
        for transformer in self.transformers:
            transformed_data = transformer(transformed_data)

    def validate_raw(self, data):
        for validator in self.raw_validators:
            validator.validate(data)

    def validate(self, transformed_data):
        for validator in self.validators:
            validator.validate(transformed_data)


class SimpleTextExtractor(SimpleExtractor):

    def extract_from_source(self, source):
        return super(SimpleTextExtractor, self).extract_from_source(source)

    def get_source(self, url):
        return url.text


class SimpleDataExtractor(SimpleExtractor):

    path = None

    def __init__(self, key=None):
        if not self.path:
            raise NotImplementedError(
                "You should specify a path to the element to be extracted"
            )

        super(SimpleDataExtractor, self).__init__(key=key)

    def extract_from_source(self, source):
        obtained_data = source
        for item in self.path:

            if hasattr(obtained_data, item):
                # Object
                try:
                    obtained_data = getattr(obtained_data, item)
                except (AttributeError, IndexError):
                    raise exceptions.ExtractionError(
                        "Unable to get attribute {}".format(
                            item
                        )
                    )

            if hasattr(obtained_data, '__getitem__'):
                # Dictionary, list...
                obtained_data = obtained_data.__getitem__(item)

    def get_source(self, url):
        return url.data


class SimpleRegexExtractor(SimpleTextExtractor):
    regex = None

    def __init__(self, key=None):
        if not self.regex:
            raise NotImplementedError("You should specify a regex")

        super(SimpleRegexExtractor, self).__init__(key=key)

    def extract_from_source(self, source):
        for match in re.findall(self.regex, source):
            yield match
