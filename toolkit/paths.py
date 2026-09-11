"""Path string helpers. Nothing here touches the filesystem."""

from __future__ import annotations

import posixpath
import re

_SLASHES = re.compile(r"/+")


def normalize_slashes(path):
    """Rewrite a path to use single forward slashes.

    Backslashes become slashes and runs of slashes collapse. The
    filesystem is not consulted.
    """
    return _SLASHES.sub("/", path.replace("\\", "/"))


def split_extension(name):
    """Split a name into stem and extension.

    Only the last suffix is the extension, so file.tar.gz yields
    .gz. A name with no dot returns an empty extension.
    """
    stem, extension = posixpath.splitext(name)
    return stem, extension


def is_hidden(path):
    """Report whether the final path component starts with a dot.

    Slashes are normalized first so a Windows-style path is treated
    the same way.
    """
    return posixpath.basename(normalize_slashes(path)).startswith(".")


def common_prefix(paths):
    """Return the shared slash-separated prefix of `paths`.

    Comparison is by whole components, not characters. An empty
    sequence yields the empty string.
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
