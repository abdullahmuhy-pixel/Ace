"""Compact builder for topic notes, used by the law, education, humanities and health courses."""


def N(ov, kt, ex, fm, steps, we, cm, rw, es, rc, fl='Key points'):
    """we = (problem, [steps], answer, check)."""
    assert len(ex) == 3 and len(cm) >= 3 and len(rc) >= 3 and len(we) == 4 and len(steps) >= 3
    return {'overview': ov, 'key_terms': kt, 'explanation': ex, 'formulas_label': fl, 'formulas': fm, 'steps': steps,
            'worked_example': {'problem': we[0], 'steps': we[1], 'answer': we[2], 'check': we[3]},
            'mistakes': cm, 'real_world': rw, 'exam_strategy': es, 'recap': rc}


def module(title, topics, overview, key_terms, explanation, quick_facts):
    assert len(explanation) == 3
    return {'title': title, 'topics': topics, 'overview': overview, 'key_terms': key_terms, 'explanation': explanation, 'quick_facts': quick_facts}
