"""Mapping helpers."""

from __future__ import annotations


def deep_get(mapping, path, default=None):
    """Walk a dotted path through nested dicts and return the value.

    Any missing key, or a non-dict along the way, yields `default` rather
    than raising, so callers can treat absence uniformly.
    """
    current = mapping
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def invert(mapping):
    """Swap keys and values.

    Duplicate values overwrite earlier ones, so the last key that mapped
    to a given value is the one that survives.
    """
    return {value: key for key, value in mapping.items()}


def group_by(items, key):
    """Partition items into lists keyed by `key(item)`.

    Groups and the items inside them keep first-seen order; no sorting is
    applied.
    """
    grouped = {}
    for item in items:
        grouped.setdefault(key(item), []).append(item)
    return grouped


def merge(base, override):
    """Return a new dict with override layered onto base.

    Nested dicts are merged recursively; every other value is replaced.
    Neither argument is mutated.
    """
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], value)
        else:
            merged[key] = value
    return merged
