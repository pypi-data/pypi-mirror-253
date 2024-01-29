'''This module contains classes that are useful for working with the StatsAPI'''

import re
import requests
from mlb.statsapi.settings import TIMEOUT
from mlb.statsapi import auth

class ExtendedDictionary(dict):
    """
    A wrapper for a dictionary with extended functionality
    """

    def get(self, key, default=None):
        """
        This is a recursive version of the standard dict().get() method. You can access
        nested dictionaries' values with the syntax in the example below:

        >> test_case = ExtendedDictionary({"foo": {"bar": "baz"}})
        >> test_case.get("foo")
        {"bar": "baz"}
        >> test_case.get("foo.bar")
        'baz'
        >> test_case.get("foo.abc", "default_value")
        'default_value'
        """
        if not isinstance(key, str) or len(key.split(".")) == 1:
            return super().get(key, default)

        keys = key.split(".")
        output = self

        for item in keys:
            if not isinstance(output, dict):
                return default
            output = output.get(item, {})

        if output == {}:
            return default

        return output

def endpoint_factory(endpoint, section=None, return_object_type=ExtendedDictionary):
    """
    A factory for simple endpoints that we want to follow all the same flow and 
    return either a list of dictionaries or dictionary type object
    """
    base_path_params = re.findall("{(.+?)}", endpoint)

    def inner(**kwargs):
        path_params = {}
        for param in base_path_params:
            if not param in kwargs:
                raise ValueError(f"key word argument '{param}' is required")
            path_params[param] = kwargs.pop(param)
        if "game_pk" in kwargs:
            kwargs["gamePk"] = kwargs.pop("game_pk")
        response = requests.get(
            endpoint.format(**path_params),
            headers = auth.get_headers(),
            timeout = TIMEOUT,
            params = kwargs,
        )

        response.raise_for_status()
        output = response.json()

        if isinstance(output, dict) and section:
            output = ExtendedDictionary(output).get(section)
        if isinstance(output, list):
            if issubclass(return_object_type, list):
                return return_object_type(output)
            return [return_object_type(item) for item in output]
        return return_object_type(output)

    return inner