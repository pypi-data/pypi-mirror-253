from typing import List, Optional

import uuid


def remove_trailing_empty_lines(lines):
    while lines and lines[-1].strip() == "":
        lines.pop()
    return lines


def remove_leading_empty_lines(lines):
    while lines and lines[0].strip() == "":
        lines.pop(0)
    return lines


def remove_special_lines(lines, drop_lines: List[str]):
    return [line for line in lines if line.strip() not in drop_lines]


def wrap_content(content_str: str, start_flag: str, end_flag: str) -> str:
    """wrap the content with start flag and end flag"""
    if len(content_str) == 0:
        return f"{start_flag}\n{end_flag}\n"
    else:
        return f"{start_flag}\n{content_str}\n{end_flag}\n"


def generate_random_id(prefix: Optional[str] = None, maximum_length: int = 12) -> str:
    """
    Generate a random ID with optional prefix.

    Args:
        prefix: (Optional[str]) The prefix for the generated ID.
        maximum_length: (int) Desired maximum length for the resulting ID(prefix excluded). Must be between 1 and 32(both inclusive).

    Returns:
        (str) The generated ID.

    Example:

    >>> generate_random_id(prefix="chat", maximum_length=10)
        'chat-bkHjj4wI4S'
    >>> generate_random_id(maximum_length=10)
        'U3WKcV3bTE'
    """
    if not 0 < maximum_length <= 32:
        raise ValueError(f"maximum_length must be between 1 and 32(both inclusive), but got {maximum_length}")

    random_id = uuid.uuid4().hex[:maximum_length]

    if prefix:
        return f"{prefix}-{random_id}"
    return random_id

def get_hash_id(d: dict) -> str:
    """Get a unique hash id for a serializable object
    
    Args:
        obj (Serializable): The object to hash

    Returns:
        str: The unique hash id
    """
    import json
    import hashlib
    json_str = json.dumps(d, sort_keys=True)
    hash_object = hashlib.md5(json_str.encode())
    hash_id = hash_object.hexdigest()
    return hash_id


__all__ = [
    'get_hash_id',
    'wrap_content',
    'generate_random_id',
    'remove_special_lines',
    'remove_leading_empty_lines',
    'remove_trailing_empty_lines',
]
