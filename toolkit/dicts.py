"""Mapping helpers."""

from __future__ import annotations


def deep_get(mapping, path, default=None):
    """Walk a dotted path through nested dicts and return the value.

    Any missing key, or a non-dict along the way, yields `default`
    rather than raising KeyError.
    """
    current = mapping
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def invert(mapping):
    """Swap keys and values.

    Duplicate values silently overwrite earlier keys, because the result
    is a plain dict.
    """
    return {value: key for key, value in mapping.items()}


def group_by(items, key):
    """Partition items into lists keyed by the result of `key`.

    Groups keep the order the items first appeared, and items inside
    each group keep their original relative order.
    """
    grouped = {}
    for item in items:
        grouped.setdefault(key(item), []).append(item)
    return grouped


def merge(base, override):
    """Recursively merge two mappings, with `override` winning.

    Nested dicts are merged rather than replaced. Neither argument is
    mutated; a new mapping is returned.
    """
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], value)
        else:
            merged[key] = value
    return merged
