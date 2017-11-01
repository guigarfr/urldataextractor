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

from urldataextractor import exceptions


class Url(object):
    """Contains all relevant data extracted from an url

    Url can be loaded in order to extract data from it.
    """
    def __init__(self, url=None):
        if not url:
            raise exceptions.RequiredParameterError()
        self._url = url

    @property
    def url(self):
        """Returns the url address."""
        return self._url

    def load(self):
        """Assigns a new data value to the provided key."""
        self.load_content()
        self.load_data()

    def load_content(self):
        """Loads the content of the url.

        This implementation is dependant on the http
        requests library used by the developer."""
        raise NotImplementedError()

    def load_data(self):
        """Loads relevant data related to the url.

        This data might be a dictionary (json data), or an object.

        This implementation is dependant on the http
        requests library used by the developer."""
        raise NotImplementedError()
