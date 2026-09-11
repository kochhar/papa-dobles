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
    """Return the arithmetic mean of `values`.

    Raises ValueError on an empty sequence, because there is no sensible
    average of nothing.
    """
    if not values:
        raise ValueError("mean of no values")
    return sum(values) / len(values)


def median(values):
    """Return the median of `values`.

    An odd-length sequence yields the middle element after sorting; an
    even-length one averages the two central elements. Raises ValueError
    if there are no values.
    """
    if not values:
        raise ValueError("median of no values")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def percentile(values, q):
    """Return the nearest-rank value at quantile `q` in [0, 1].

    Raises ValueError if `values` is empty or `q` is outside that range.
    Ties go to the rounded rank, not to interpolation.
    """
    if not values:
        raise ValueError("percentile of no values")
    if not 0.0 <= q <= 1.0:
        raise ValueError("q must be between 0 and 1")
    ordered = sorted(values)
    rank = int(round(q * (len(ordered) - 1)))
    return ordered[rank]
