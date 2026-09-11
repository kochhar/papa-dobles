"""Parsers for the small formats that turn up in configuration."""

from __future__ import annotations

import csv
import re

_DURATION = re.compile(r"(\d+)([hms])")
_UNITS = {"h": 3600, "m": 60, "s": 1}
_TRUE = {"1", "true", "yes", "on"}
_FALSE = {"0", "false", "no", "off"}


def parse_key_values(text):
    """Parse a comma-separated list of key=value pairs into a dict.

    Surrounding space around keys, values, and pairs is ignored. A token
    with no equals sign is an error.
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
    """Split a single CSV record, honouring quoted commas."""
    return next(csv.reader([line]))


def parse_duration(text):
    """Turn a compound duration such as 1h30m into a number of seconds.

    Units are h, m, and s. Case and surrounding space are ignored; anything
    that is not a run of those tokens is refused.
    """
    cleaned = text.strip().lower()
    matches = _DURATION.findall(cleaned)
    if not matches or "".join(a + b for a, b in matches) != cleaned:
        raise ValueError("not a duration: {!r}".format(text))
    return sum(int(amount) * _UNITS[unit] for amount, unit in matches)


def parse_bool(text):
    """Parse a common truthy or falsey word into a bool.

    Accepts 1/0, true/false, yes/no, and on/off, ignoring case and
    surrounding space. Anything else is an error.
    """
    cleaned = text.strip().lower()
    if cleaned in _TRUE:
        return True
    if cleaned in _FALSE:
        return False
    raise ValueError("not a boolean: {!r}".format(text))
