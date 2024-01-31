"""
This module contains utility functions that are used throughout the Grooper
API.
"""

import random
import re
import string
from typing import Any
from typing import List

PrimitiveJSONType = str | int | float | bool | bytes | None
ListJSONType = List[PrimitiveJSONType] | List[dict[str, PrimitiveJSONType]]
JSONType = PrimitiveJSONType | dict[str, PrimitiveJSONType] | ListJSONType


def to_snake_case(name: str) -> str:
    """
    Converts a string from "CamelCase" or "PascalCase" to "snake_case".
    """
    name = re.sub(pattern="(.)([A-Z][a-z]+)", repl=r"\1_\2", string=name)
    return re.sub(pattern="([a-z0-9])([A-Z])", repl=r"\1_\2", string=name).lower()


def snake_to_pascal_case(snake_case_string: str) -> str:
    """
    Converts a string from "snake_case" to "PascalCase"
    """
    # Split the string into individual words
    words: list[str] = snake_case_string.split(sep="_")
    # Capitalize each word and join them together
    pascal_case_string: str = "".join(word.capitalize() for word in words)
    return pascal_case_string


def snake_to_pascal_keys(dictionary: dict) -> dict[str, Any]:
    """
    Updates every key from dictionary from "snake_case" to "PascalCase"
    """
    updated_dictionary: dict[str, str] = {}
    for key, value in dictionary.items():
        updated_key: str = snake_to_pascal_case(snake_case_string=key)
        updated_dictionary[updated_key] = value
    return updated_dictionary
