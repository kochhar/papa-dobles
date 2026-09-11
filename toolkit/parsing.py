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

    Surrounding whitespace on keys, values, and the whole text is
    ignored. A token with no equals sign is an error.
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
    """Parse a single CSV record into a list of fields.

    Quoted commas stay inside their field, using the stdlib csv reader.
    """
    return next(csv.reader([line]))


def parse_duration(text):
    """Parse a compact duration such as 1h30m into a number of seconds.

    Units are h, m, and s, and they may be chained. The whole string
    must be consumed; anything leftover is an error.
    """
    cleaned = text.strip().lower()
    matches = _DURATION.findall(cleaned)
    if not matches or "".join(a + b for a, b in matches) != cleaned:
        raise ValueError("not a duration: {!r}".format(text))
    return sum(int(amount) * _UNITS[unit] for amount, unit in matches)


def parse_bool(text):
    """Parse a truthy or falsey word into a bool.

    Accepts 1/true/yes/on and 0/false/no/off, ignoring case and
    surrounding space. Anything else raises ValueError.
    """
    cleaned = text.strip().lower()
    if cleaned in _TRUE:
        return True
    if cleaned in _FALSE:
        return False
    raise ValueError("not a boolean: {!r}".format(text))
