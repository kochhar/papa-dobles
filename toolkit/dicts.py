"""Mapping helpers."""

from __future__ import annotations


def deep_get(mapping, path, default=None):
    """Walk a dotted path of keys and return the nested value.

    Return `default` as soon as a step is missing or is not a dict, so
    a partial walk never raises.
    """
    current = mapping
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def invert(mapping):
    """Swap keys and values. Duplicate values keep only the last key."""
    return {value: key for key, value in mapping.items()}


def group_by(items, key):
    """Bucket items under the result of `key`, preserving input order."""
    grouped = {}
    for item in items:
        grouped.setdefault(key(item), []).append(item)
    return grouped


def merge(base, override):
    """Recursively merge two mappings without mutating either.

    Nested dicts are combined; any other overlapping value is taken from
    `override`.
    """
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], value)
        else:
            merged[key] = value
    return merged
