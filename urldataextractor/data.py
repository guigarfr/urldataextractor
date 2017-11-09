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
import collections


class Data(collections.defaultdict):
    """Stores data with associated keys.

    It is a collection of keys and values.
    Each key can have multiple values assigned.

    It is an iterator.
    """
    def __init__(self):
        super(Data, self).__init__(list)

    def __iter__(self, *args, **kwargs):
        """ Iterates over data items. """
        for key, list_of_values in self.items:
            for value in list_of_values:
                yield key, value

    @property
    def items(self):
        """Returns an iterator over all pairs of (key, list of values)."""
        return super(Data, self).items()

    @property
    def keys(self):
        """Returns an iterator over all keys."""
        return super(Data, self).keys()

    @property
    def values(self):
        """Returns an iterator over all single values."""
        for value_list in super(Data, self).values():
            for value in value_list:
                yield value

    def add(self, key, value):
        """Assigns a new value to the provided key."""
        self[key].append(value)


class ExtractedData(object):
    """Represents extracted data.

    holds all information extracted from a page.

    Data can be transformed and validated

    Data which could not be transformed or validated
    will be stored as errors.

    It is an iterator.
    """
    def __init__(self):
        self.__values = Data()
        self.__errors = Data()

    @property
    def data(self):
        """Valid data."""
        return self.__values

    @property
    def errors(self):
        """Errors data."""
        return self.__errors

    def add_error(self, key, value):
        """Assigns a new data value to the provided key."""
        self.__errors.add(key, value)

    def add_value(self, key, value):
        """Assigns a new data error to the provided key."""
        self.__values.add(key, value)

    def clear(self):
        """Clears all extracted data."""
        self.__values.clear()
        self.__errors.clear()
