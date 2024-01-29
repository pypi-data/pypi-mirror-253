from typing import Collection


def to_sorted_list_str(snippet_list: Collection) -> str:
    """Convert a collection of snippets to a sorted list of strings.

    Args:
        snippet_list (Collection): The collection of snippets.

    Returns:
        (str) The string representation of the sorted list of snippets.
    """
    s = ""
    for i, snippet in enumerate(snippet_list):
        s += f"{i + 1}. {snippet}\n"
    return s


__all__ = [
    'to_sorted_list_str',
]
