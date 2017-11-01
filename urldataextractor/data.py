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


class Data(object):
    """Represents extracted data.

    holds all information extracted from a page.

    Data can be transformed and validated

    It is a collection of keys and values.
    Each key can have multiple values assigned.

    It is an iterator.
    """
    def __init__(self):
        self.__values = collections.defaultdict(list)
        self.__errors = collections.defaultdict(list)

    def __iter__(self):
        return self.__values.__iter__()

    def __next__(self):
        return self.__values.items()

    @property
    def errors(self):
        """Iterates over data items.

        Data items are tuples formed by a key and list of values.
        """
        return self.__errors.items()

    @property
    def items(self):
        """Iterates over data items.

        Data items are tuples formed by a key and list of values.
        """
        return self.__values.items()

    @property
    def keys(self):
        """Iterates over data keys."""
        return self.__values.keys()

    @property
    def values(self):
        """Iterates over data values."""
        for list_of_values in self.__values.values():
            for value in list_of_values:
                yield value

    def add(self, key, value):
        """Assigns a new data value to the provided key."""
        self.__values[key].append(value)

    def add_error(self, key, value):
        """Assigns a new data value to the provided key."""
        self.__errors[key].append(value)

    def get(self, key):
        """Obtains all data values assigned to the provided key."""
        return self.__values[key]
