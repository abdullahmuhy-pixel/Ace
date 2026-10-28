"""Shared helpers for Ace Campus course sources.
Every maths question can carry `ans` (a SymPy expression or number). The checker parses each displayed option,
asserts the marked option equals `ans` and that no other option does. Needs SymPy: set PYTHONPATH to a SymPy checkout
(see tools/campus/README.md)."""
import re
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

x, y, t, h, n, a, b, k, r, u, C = sp.symbols('x y t h n a b k r u C')
SUP = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-', 'ⁿ': 'n', 'ˣ': 'x'}
TR = standard_transformations + (implicit_multiplication_application, convert_xor)
LOC = {'e': sp.E, 'pi': sp.pi, 'x': x, 'y': y, 't': t, 'h': h, 'n': n, 'a': a, 'b': b, 'k': k, 'r': r, 'u': u, 'C': C,
       'ln': sp.log, 'log': sp.log, 'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'sec': sp.sec, 'csc': sp.csc, 'cot': sp.cot,
       'sqrt': sp.sqrt, 'arctan': sp.atan, 'arcsin': sp.asin, 'oo': sp.oo, 'E': sp.E}


def to_sym(s):
    """Parse a displayed answer such as '3x² − 2', 'e^(2x)', '√(x + 1)', '−1/2', '∞' into SymPy."""
    s = re.sub(r'^[a-zA-Z](\([a-z]\))? = ', '', str(s).strip())
    s = re.sub(r'\s*%$', '', s)
    s = re.sub(r'\s+(years?|minutes?|words?|days?|weeks?|students?|participants?|per unit|units?|billion|million|hours?|marks?|K|J|kJ|kJ/mol|L|mL|mol|kPa|Pa|g|kg|mol/L|g/mol|N|kN|W|kW|Hz|N m|N·m|kg m/s|kg·m/s|N s|N·s|rad/s|rad/s²|V|kV|mV|A|mA|Ω|kΩ|μF|nF|pF|μC|nC|T|mT|μT|Wb|H|mH|ms|V/m|N/C|eV)$', '', s)
    if s in ('∞', '+∞'): return sp.oo
    if s == '−∞': return -sp.oo
    s = s.replace('−', '-').replace('×', '*').replace('÷', '/').replace('·', '*').replace('π', 'pi').replace('∞', 'oo')
    s = re.sub(r'\s+(cm|m|km|s|kg|g)(\b|[²³])[\w²³/]*$', '', s)
    FN = r'(sin|cos|tan|sec|csc|cot|ln)'
    s = re.sub(FN + r'([²³])\s?([a-z]|\([^()]*\))', lambda m: '(' + m.group(1) + '(' + m.group(3) + '))' + m.group(2), s)
    s = re.sub(r'\b' + FN + r' (\d+|[a-z])\b', r'\1(\2)', s)
    s = re.sub(r'√\(', 'sqrt(', s)
    s = re.sub(r'√(\d+|[a-z])', r'sqrt(\1)', s)
    s = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿˣ]+)', lambda m: '**(' + ''.join(SUP[c] for c in m.group(1)) + ')', s)
    s = s.replace('^', '**')
    s = re.sub(r'\+ ?C$', '', s).strip()
    s = s.replace('sin**(2)', 'sin(x)**2') if 'sin**(2)x' in s else s
    return parse_expr(s, local_dict=LOC, transformations=TR)


def to_val(s):
    """Like to_sym, but also reads matrices '[1 2 ; 3 4]', column vectors '(1, 2, 3)' and lists of values '2 and 5'."""
    s = str(s).strip()
    s = re.sub(r'^(λ|[a-zA-Z](\([a-z]\))?) = ', '', s)
    m = re.fullmatch(r'\[(.*)\]', s)
    if m and (';' in m.group(1) or re.search(r'[\d)]\s+[−\-\d(]', m.group(1))):
        rows = [r.split() for r in m.group(1).split(';')]
        return sp.Matrix([[to_sym(x) for x in r] for r in rows])
    m = re.fullmatch(r'\((.*)\)', s)
    if m and ',' in m.group(1) and not re.search(r'[a-z]\(', s):
        return sp.Matrix([to_sym(x) for x in m.group(1).split(',')])
    if ' and ' in s:
        return tuple(sorted((to_sym(re.sub(r'^(λ|[a-z]) = ', '', x.strip())) for x in s.split(' and ')), key=lambda v: float(v)))
    return to_sym(s)


def same_any(p, q):
    if isinstance(p, sp.MatrixBase) or isinstance(q, sp.MatrixBase):
        if not (isinstance(p, sp.MatrixBase) and isinstance(q, sp.MatrixBase)) or p.shape != q.shape: return False
        return all(same(x, y) for x, y in zip(p, q))
    if isinstance(p, tuple) or isinstance(q, tuple):
        if not (isinstance(p, tuple) and isinstance(q, tuple)) or len(p) != len(q): return False
        return all(same(x, y) for x, y in zip(p, q))
    return same(p, q)


def same(p, q):
    if p in (sp.oo, -sp.oo) or q in (sp.oo, -sp.oo): return p == q
    try:
        d = sp.simplify(sp.nsimplify(p) - sp.nsimplify(q)) if not (p.free_symbols or q.free_symbols) else sp.simplify(p - q)
        if d == 0: return True
        if not d.free_symbols: return abs(float(d)) < 1e-9
        # numeric spot checks for stubborn identities
        import random
        syms = sorted(d.free_symbols, key=str)
        for _ in range(6):
            vals = {s_: random.uniform(0.3, 1.7) for s_ in syms}
            if abs(complex(d.evalf(subs=vals))) > 1e-8: return False
        return True
    except Exception:
        return False


def Q(topic, q, o, a, e, ans=None, num=False):
    """One MCQ. `ans` turns on the SymPy check; `num=True` compares numerically within 0.005 (rounded answers)."""
    d = {'type': 'mcq', 'reviewed': True, 'topic': topic, 'q': q, 'o': o, 'a': a, 'e': e}
    if ans is not None: d['_ans'] = ans; d['_num'] = num
    return d


def check_questions(qs, where):
    probs = []
    for q in qs:
        if '_ans' not in q: continue
        ans = q['_ans']
        if isinstance(ans, (list, tuple)) and not isinstance(ans, sp.MatrixBase): ans = tuple(sorted((sp.sympify(v) for v in ans), key=lambda v: float(v)))
        elif not isinstance(ans, sp.MatrixBase): ans = sp.sympify(ans)
        vals = []
        for o in q['o']:
            try: vals.append(to_val(o))
            except Exception: vals.append(None)
        if vals[q['a']] is None:
            probs.append(f'{where}: cannot parse the marked answer of "{q["q"][:60]}"'); continue
        def eq(v):
            if v is None: return False
            if q['_num']:
                try: return abs(float(v) - float(ans)) < 0.005
                except Exception: return False
            return same_any(v, ans)
        ok = [eq(v) for v in vals]
        if not ok[q['a']]: probs.append(f'{where}: marked answer {q["o"][q["a"]]!r} != {ans} in "{q["q"][:70]}"')
        others = [q['o'][i] for i, v in enumerate(ok) if v and i != q['a']]
        if others: probs.append(f'{where}: distractor {others} also equals the answer in "{q["q"][:70]}"')
    return probs


def strip(q):
    return {k: v for k, v in q.items() if not k.startswith('_')}
