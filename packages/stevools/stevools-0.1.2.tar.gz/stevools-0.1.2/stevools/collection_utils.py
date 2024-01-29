from typing import Collection


def is_empty_collection(collection: Collection) -> bool:
    return collection is None or len(collection) == 0


__all__ = [
    'is_empty_collection',
]
