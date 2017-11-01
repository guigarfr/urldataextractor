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


class ExtractionError(Exception):
    """Error during the data extraction. Applies to `SimpleExtractor`."""


class RequiredParameterError(Exception):
    """Called a method without a required parameter."""


class UrlDataExtractorException(Exception):
    """Generic url data extractor exception."""


class ValidationError(Exception):
    """Validation error."""
