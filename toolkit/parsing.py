"""Parsers for the small formats that turn up in configuration."""

from __future__ import annotations

import csv
import re

_DURATION = re.compile(r"(\d+)([hms])")
_UNITS = {"h": 3600, "m": 60, "s": 1}
_TRUE = {"1", "true", "yes", "on"}
_FALSE = {"0", "false", "no", "off"}


def parse_key_values(text):
    """Parse a comma-separated list of key=value pairs.

    Surrounding space around keys, values, and pairs is ignored. A token
    with no equals sign is a ValueError, not a flag.
    """
    pairs = {}
    for item in text.split(","):
        item = item.strip()
        if not item:
            continue
        key, separator, value = item.partition("=")
        if not separator:
            raise ValueError("not a key=value pair: {!r}".format(item))
        pairs[key.strip()] = value.strip()
    return pairs


def parse_csv_line(line):
    """Parse a single CSV record, honouring quoted commas.

    Uses the stdlib csv reader so a field like "b,c" stays one column.
    """
    return next(csv.reader([line]))


def parse_duration(text):
    """Turn a duration such as 1h30m into a number of seconds.

    Accepted units are h, m and s, in any combination. The whole string
    must be consumed; leftover junk is a ValueError.
    """
    cleaned = text.strip().lower()
    matches = _DURATION.findall(cleaned)
    if not matches or "".join(a + b for a, b in matches) != cleaned:
        raise ValueError("not a duration: {!r}".format(text))
    return sum(int(amount) * _UNITS[unit] for amount, unit in matches)


def parse_bool(text):
    """Parse a common truthy or falsey word, ignoring case and space.

    True for 1/true/yes/on, False for 0/false/no/off. Anything else
    raises ValueError rather than guessing.
    """
    cleaned = text.strip().lower()
    if cleaned in _TRUE:
        return True
    if cleaned in _FALSE:
        return False
    raise ValueError("not a boolean: {!r}".format(text))
