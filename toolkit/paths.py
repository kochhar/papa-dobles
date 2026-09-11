"""Path string helpers. Nothing here touches the filesystem."""

from __future__ import annotations

import posixpath
import re

_SLASHES = re.compile(r"/+")


def normalize_slashes(path):
    """Rewrite backslashes as slashes and collapse repeated slashes."""
    return _SLASHES.sub("/", path.replace("\\", "/"))


def split_extension(name):
    """Split a path into stem and last suffix, including the leading dot."""
    stem, extension = posixpath.splitext(name)
    return stem, extension


def is_hidden(path):
    """Report whether the final path component starts with a dot."""
    return posixpath.basename(normalize_slashes(path)).startswith(".")


def common_prefix(paths):
    """Return the shared slash-separated prefix of the given paths.

    An empty collection has no prefix. Comparison is after slash
    normalisation, component by component.
    """
    if not paths:
        return ""
    segmented = [normalize_slashes(p).split("/") for p in paths]
    shared = []
    for parts in zip(*segmented):
        if len(set(parts)) != 1:
            break
        shared.append(parts[0])
    return "/".join(shared)
