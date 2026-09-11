"""Mapping helpers."""

from __future__ import annotations


def deep_get(mapping, path, default=None):
    current = mapping
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def invert(mapping):
    return {value: key for key, value in mapping.items()}


def group_by(items, key):
    grouped = {}
    for item in items:
        grouped.setdefault(key(item), []).append(item)
    return grouped


def merge(base, override):
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], value)
        else:
            merged[key] = value
    return merged
