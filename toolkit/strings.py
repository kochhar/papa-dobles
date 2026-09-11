"""String helpers."""

from __future__ import annotations

import re

_NOT_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text):
    """Reduce text to lowercase words joined by hyphens.

    Runs of anything that is not a letter or digit become a single hyphen,
    and leading and trailing hyphens are dropped.
    """
    return _NOT_ALNUM.sub("-", text.lower()).strip("-")


def truncate_middle(text, limit, marker="..."):
    """Shorten text to `limit` characters by replacing the middle.

    If the marker itself is longer than the limit, return a prefix of the
    marker. Short text is returned unchanged.
    """
    if len(text) <= limit:
        return text
    keep = limit - len(marker)
    if keep <= 0:
        return marker[:limit]
    head = (keep + 1) // 2
    tail = keep - head
    return text[:head] + marker + (text[len(text) - tail:] if tail else "")


def title_case(text):
    """Capitalise the first letter of each whitespace-separated word.

    Runs of spaces collapse to a single space.
    """
    return " ".join(word[:1].upper() + word[1:] for word in text.split())


def count_words(text):
    """Count whitespace-separated words. Empty text has none."""
    return len(text.split())
