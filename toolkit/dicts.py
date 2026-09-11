"""Mapping helpers."""

from __future__ import annotations


def deep_get(mapping, path, default=None):
    """Walk a dotted path of keys and return the nested value.

    Return `default` as soon as a step is missing or lands on a non-dict.
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
    """Partition items into lists keyed by the result of `key`.

    Group order and item order inside each group follow the input.
    """
    grouped = {}
    for item in items:
        grouped.setdefault(key(item), []).append(item)
    return grouped


def merge(base, override):
    """Return a new dict with override layered onto base.

    Nested dicts are merged recursively; everything else is replaced.
    Neither input is mutated.
    """
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], value)
        else:
            merged[key] = value
    return merged
