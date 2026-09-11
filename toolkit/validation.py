"""Cheap format checks. None of them prove a value is real."""

from __future__ import annotations

import re
import uuid

_EMAIL = re.compile(r"^[^@\s]+@[^@\s.]+(\.[^@\s.]+)+$")
_HEX_COLOR = re.compile(r"^#(?:[0-9a-f]{3}|[0-9a-f]{6})$", re.IGNORECASE)


def is_email(value):
    """Report whether value has the shape of an email address.

    Shape only: a local part, one @, and a dotted domain. Whether anything
    answers there is a different question and needs the network.
    """
    return bool(_EMAIL.match(value))


def is_ipv4(value):
    """Report whether value has the shape of a dotted IPv4 address.

    Four decimal octets in 0..255, with no leading zeros. This does
    not check that the address is reachable.
    """
    parts = value.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or (len(part) > 1 and part[0] == "0"):
            return False
        if int(part) > 255:
            return False
    return True


def is_hex_color(value):
    """Report whether value is a #RGB or #RRGGBB colour.

    The leading hash is required and the letters may be either case.
    """
    return bool(_HEX_COLOR.match(value))


def is_uuid(value):
    """Report whether value can be parsed as a UUID.

    Any of the forms accepted by uuid.UUID count; malformed input
    returns False rather than raising.
    """
    try:
        uuid.UUID(value)
    except (ValueError, AttributeError, TypeError):
        return False
    return True
