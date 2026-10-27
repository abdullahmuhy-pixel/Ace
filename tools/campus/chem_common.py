"""Shared constants for the General Chemistry course (IUPAC standard atomic weights, rounded as in most first-year data sheets)."""
import math
AW = {'H': 1.008, 'C': 12.01, 'N': 14.01, 'O': 16.00, 'Na': 22.99, 'Mg': 24.31, 'S': 32.06, 'Cl': 35.45, 'K': 39.10, 'Ca': 40.08, 'Fe': 55.85, 'Cu': 63.55, 'Zn': 65.38, 'Ag': 107.87}
NA = 6.022e23
R = 8.314


def M(formula):
    """Molar mass from a dict like {'C': 6, 'H': 12, 'O': 6}."""
    return sum(AW[e] * n for e, n in formula.items())


def r(x, d):
    return round(x + 0.0, d)


pH = lambda h: -math.log10(h)
