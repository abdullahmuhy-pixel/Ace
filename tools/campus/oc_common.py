"""Shared helpers for the Organic Chemistry course: formulas, molar masses, degrees of unsaturation, isomer counts."""
import re
from chem_common import AW, M, r, pH

AW = dict(AW, Br=79.90, I=126.90, F=19.00)


def formula(s):
    """'C2H6O' -> {'C': 2, 'H': 6, 'O': 1}."""
    out = {}
    for el, n in re.findall(r'([A-Z][a-z]?)(\d*)', s):
        out[el] = out.get(el, 0) + (int(n) if n else 1)
    return out


def mass(s):
    return sum(AW[e] * n for e, n in formula(s).items())


def dou(s):
    """Degrees of unsaturation (rings + pi bonds): (2C + 2 + N - H - X)/2."""
    f = formula(s)
    x = sum(f.get(h, 0) for h in ('F', 'Cl', 'Br', 'I'))
    return (2 * f.get('C', 0) + 2 + f.get('N', 0) - f.get('H', 0) - x) / 2


ALKANE_ISOMERS = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 9, 8: 18}
try:  # recount the alkane skeletons as carbon trees with valence at most 4, when networkx is available
    import networkx as nx
    for _n in range(4, 9):
        assert sum(1 for t in nx.nonisomorphic_trees(_n) if max(dict(t.degree()).values()) <= 4) == ALKANE_ISOMERS[_n]
except ImportError:
    pass


def nmr_mult(n):
    """n + 1 rule: number of peaks for a proton with n equivalent neighbours."""
    return n + 1
