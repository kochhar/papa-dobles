"""Mapping helpers."""

from __future__ import annotations


def deep_get(mapping, path, default=None):
    """Walk a dotted path through nested dicts and return the value.

    Any missing key or non-dict along the way yields `default` rather than
    raising, so callers can treat absence as ordinary.
    """
    current = mapping
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def invert(mapping):
    """Swap keys and values. Later duplicates overwrite earlier ones."""
    return {value: key for key, value in mapping.items()}


def group_by(items, key):
    """Bucket items under the result of `key`, keeping input order in each list."""
    grouped = {}
    for item in items:
        grouped.setdefault(key(item), []).append(item)
    return grouped


def merge(base, override):
    """Recursively merge override into a shallow copy of base.

    Nested dicts are combined rather than replaced. Neither input mapping
    is mutated.
    """
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], value)
        else:
            merged[key] = value
    return merged
