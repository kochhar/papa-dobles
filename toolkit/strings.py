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

    Text that already fits is returned unchanged. If the marker itself is
    longer than the limit, only a prefix of the marker is kept.
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

    Runs of spaces collapse because the string is split and rejoined,
    which is usually what a title wants.
    """
    return " ".join(word[:1].upper() + word[1:] for word in text.split())


def count_words(text):
    """Count whitespace-separated words.

    Runs of spaces do not produce empty words, and an empty string counts
    as zero.
    """
    return len(text.split())
