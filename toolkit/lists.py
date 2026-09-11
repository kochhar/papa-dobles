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

    Deeper structure is left intact; this is not a recursive flatten.
    """
    return [item for group in nested for item in group]


def dedupe(items):
    """Return items with later duplicates removed.

    First occurrence wins, so the original order of unique values is kept.
    """
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def partition(items, predicate):
    """Split items into those that satisfy `predicate` and the rest.

    Order is preserved in both halves, matching the original sequence.
    """
    matching = []
    rest = []
    for item in items:
        (matching if predicate(item) else rest).append(item)
    return matching, rest
