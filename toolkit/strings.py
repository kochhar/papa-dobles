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
    if len(text) <= limit:
        return text
    keep = limit - len(marker)
    if keep <= 0:
        return marker[:limit]
    head = (keep + 1) // 2
    tail = keep - head
    return text[:head] + marker + (text[len(text) - tail:] if tail else "")


def title_case(text):
    return " ".join(word[:1].upper() + word[1:] for word in text.split())


def count_words(text):
    return len(text.split())
