"""Path string helpers. Nothing here touches the filesystem."""

from __future__ import annotations

import posixpath
import re

_SLASHES = re.compile(r"/+")


def normalize_slashes(path):
    """Rewrite a path with forward slashes and no repeated separators.

    Backslashes become slashes first so Windows-style paths collapse the
    same way. The filesystem is never consulted.
    """
    return _SLASHES.sub("/", path.replace("\\", "/"))


def split_extension(name):
    """Split a name into stem and the last extension.

    Only the final suffix is the extension, so file.tar.gz yields
    ('file.tar', '.gz'). A name with no dot returns an empty extension.
    """
    stem, extension = posixpath.splitext(name)
    return stem, extension


def is_hidden(path):
    """Report whether the basename starts with a dot.

    Slashes are normalised first so a Windows-style path still hides
    correctly. Parent directories are ignored.
    """
    return posixpath.basename(normalize_slashes(path)).startswith(".")


def common_prefix(paths):
    """Return the shared directory prefix of the given paths.

    Each path is slash-normalised and compared segment by segment. An
    empty input, or paths with nothing in common, yields the empty string.
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
