"""Numeric helpers."""

from __future__ import annotations


def clamp(value, low, high):
    """Return value confined to the inclusive range low..high.

    Raises ValueError if the bounds are the wrong way round, which is
    otherwise a silent way to get the wrong answer.
    """
    if low > high:
        raise ValueError("low must not exceed high")
    return max(low, min(value, high))


def mean(values):
    """Return the arithmetic mean. Raise ValueError on an empty sequence."""
    if not values:
        raise ValueError("mean of no values")
    return sum(values) / len(values)


def median(values):
    """Return the median of `values`.

    An odd-length sequence yields the middle element after sorting; an
    even-length one averages the central pair. Raise ValueError if empty.
    """
    if not values:
        raise ValueError("median of no values")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def percentile(values, q):
    """Return the nearest-rank percentile of `values` at fraction `q`.

    `q` must lie in 0..1 inclusive. Raise ValueError if the sequence is
    empty or `q` is out of range.
    """
    if not values:
        raise ValueError("percentile of no values")
    if not 0.0 <= q <= 1.0:
        raise ValueError("q must be between 0 and 1")
    ordered = sorted(values)
    rank = int(round(q * (len(ordered) - 1)))
    return ordered[rank]
