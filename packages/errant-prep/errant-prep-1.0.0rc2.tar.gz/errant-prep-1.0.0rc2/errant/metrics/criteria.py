from __future__ import annotations


def computeFScore(tp: int, fp: int, fn: int, beta: float = 0.5) -> tuple:
    """
    Compute the F-score given the TP, FP, and FN counts.
    :param tp: The number of true positives.
    :param fp: The number of false positives.
    :param fn: The number of false negatives.
    :param beta: The beta value for the F-score.
    :return: The precision, recall, and F-score.
    """
    p = float(tp) / (tp + fp) if fp else 1.0
    r = float(tp) / (tp + fn) if fn else 1.0
    f = float((1 + (beta**2)) * p * r) / (((beta**2) * p) + r) if p + r else 0.0
    return round(p, 4), round(r, 4), round(f, 4)
