"""Path string helpers. Nothing here touches the filesystem."""

from __future__ import annotations

import posixpath
import re

_SLASHES = re.compile(r"/+")


def normalize_slashes(path):
    return _SLASHES.sub("/", path.replace("\\", "/"))


def split_extension(name):
    stem, extension = posixpath.splitext(name)
    return stem, extension


def is_hidden(path):
    return posixpath.basename(normalize_slashes(path)).startswith(".")


def common_prefix(paths):
    if not paths:
        return ""
    segmented = [normalize_slashes(p).split("/") for p in paths]
    shared = []
    for parts in zip(*segmented):
        if len(set(parts)) != 1:
            break
        shared.append(parts[0])
    return "/".join(shared)
