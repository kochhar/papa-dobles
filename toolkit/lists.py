"""Sequence helpers."""

from __future__ import annotations


def chunk(items, size):
    """Split items into consecutive lists of at most `size` elements.

    The final chunk is short rather than padded. Raises ValueError if size
    is not positive, because an empty chunk would loop forever.
    """
    if size < 1:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]


def flatten(nested):
    """Collapse one level of nesting into a single list.

    Deeper structure is left alone; only the outermost groups are joined.
    """
    return [item for group in nested for item in group]


def dedupe(items):
    """Return items with later duplicates removed.

    The first occurrence of each value is kept, so input order is
    preserved for the values that remain.
    """
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def partition(items, predicate):
    """Split items into those that satisfy `predicate` and those that do not.

    Both halves keep the original relative order of their items.
    """
    matching = []
    rest = []
    for item in items:
        (matching if predicate(item) else rest).append(item)
    return matching, rest
