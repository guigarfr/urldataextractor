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

from urldataextractor import data as data_extractor_data
from urldataextractor import exceptions
from urldataextractor import url as data_extractor_url


class DataExtractor(object):
    """Extracts data from specific type of urls.

    Extracts data from an Url using different `SimpleExtractor`.
    """

    extractors = None

    def __init__(self):
        self.extractors = self.extractors or []

    def extract_data(self, url):
        self.validate_url(url)
        self._extract_data(url)

    def validate_url(self, url):
        """Validates the url is valid for this extractor.

        Validates that the extractor is capable of extracting
        data for this kind of url (site, path, format...).

        Raises ValidationError
        """
        raise NotImplementedError()

    def _extract_data(self, url):
        source_url = data_extractor_url.Url(url)
        obtained_data = data_extractor_data.Data()

        for extractor in self.extractors:

            for key, value in extractor.extract(source_url):

                try:
                    extractor.validate_raw(value)
                except exceptions.ValidationError:
                    obtained_data.add_error(key, value)
                    continue

                try:
                    transformed_value = extractor.transform(value)
                except Exception:
                    obtained_data.add_error(key, value)
                    continue

                try:
                    extractor.validate_raw(transformed_value)
                except exceptions.ValidationError:
                    obtained_data.add_error(key, value)
                    continue

                obtained_data.add(extractor.key, value)
