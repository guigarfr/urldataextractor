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


class Validator(object):  # pylint: disable=too-few-public-methods
    """Validates data.

    Should raise Validation error if provided value is not valid.
    """

    def validate(self, value):  # pylint: disable=C0321
        """Validates provided value.

        This is the main method of a validator.
        """
        raise NotImplementedError()
