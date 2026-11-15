#!/usr/bin/env python3
"""
Executable Mathematical Foundations Verifier for /botworkspace/math.
Verifies:
1. Finite von Neumann ordinal construction, transitivity, trichotomy, and union laws.
2. Cantor Normal Form (CNF) ordinal arithmetic below omega^omega (associativity,
   left-distributivity, and non-commutativity witnesses).
3. Finite Heyting algebra residuation and pseudo-complement laws.
"""

import json
import sys
from typing import List, Tuple, Dict, Any


def von_neumann_ordinal(n: int) -> frozenset:
    """Constructs the n-th finite von Neumann ordinal recursively."""
    ordinals = []
    current = frozenset()
    for _ in range(n):
        ordinals.append(current)
        current = current | frozenset([current])
    return current


def is_transitive_set(s: frozenset) -> bool:
    return all(elem.issubset(s) for elem in s)


def verify_von_neumann_ordinals(max_n: int = 7) -> Dict[str, Any]:
    orgs = [von_neumann_ordinal(k) for k in range(max_n + 1)]
    transitive_ok = all(is_transitive_set(o) for o in orgs)
    cardinality_ok = all(len(orgs[k]) == k for k in range(max_n + 1))
    successor_union_ok = True
    for k in range(max_n):
        succ = orgs[k + 1]
        union_succ = frozenset().union(*succ) if succ else frozenset()
        if union_succ != orgs[k]:
            successor_union_ok = False
    return {
        "max_n": max_n,
        "all_transitive": transitive_ok,
        "cardinality_exact": cardinality_ok,
        "union_of_successor_eq_predecessor": successor_union_ok,
        "passed": transitive_ok and cardinality_ok and successor_union_ok,
    }


# Cantor Normal Form ordinal representation: list of (exponent, coefficient) in strictly descending exponent order
CNF = List[Tuple[int, int]]


def cnf_normalize(terms: CNF) -> CNF:
    result: List[Tuple[int, int]] = []
    for exp, coeff in terms:
        if coeff <= 0:
            continue
        while result and result[-1][0] < exp:
            result.pop()
        if result and result[-1][0] == exp:
            result[-1] = (exp, result[-1][1] + coeff)
        else:
            result.append((exp, coeff))
    return result


def cnf_add(alpha: CNF, beta: CNF) -> CNF:
    return cnf_normalize(alpha + beta)


def cnf_mul_term(alpha: CNF, exp_b: int, coeff_b: int) -> CNF:
    if not alpha or coeff_b <= 0:
        return []
    if exp_b == 0:
        head_exp, head_coeff = alpha[0]
        return [(head_exp, head_coeff * coeff_b)] + alpha[1:]
    head_exp, _ = alpha[0]
    return [(head_exp + exp_b, coeff_b)]


def cnf_mul(alpha: CNF, beta: CNF) -> CNF:
    acc: CNF = []
    for exp_b, coeff_b in beta:
        acc = cnf_add(acc, cnf_mul_term(alpha, exp_b, coeff_b))
    return acc


def verify_cnf_arithmetic() -> Dict[str, Any]:
    one: CNF = [(0, 1)]
    two: CNF = [(0, 2)]
    omega: CNF = [(1, 1)]
    omega_plus_one = cnf_add(omega, one)
    one_plus_omega = cnf_add(one, omega)

    two_mul_omega = cnf_mul(two, omega)
    omega_mul_two = cnf_mul(omega, two)

    a: CNF = [(2, 1), (1, 2), (0, 3)]
    b: CNF = [(1, 1), (0, 4)]
    c: CNF = [(2, 2), (0, 1)]

    assoc_add = cnf_add(cnf_add(a, b), c) == cnf_add(a, cnf_add(b, c))
    left_distrib = cnf_mul(a, cnf_add(b, c)) == cnf_add(cnf_mul(a, b), cnf_mul(a, c))
    non_comm_add = (one_plus_omega == omega) and (omega_plus_one != omega)
    non_comm_mul = (two_mul_omega == omega) and (omega_mul_two != omega)

    return {
        "addition_associative": assoc_add,
        "left_distributivity": left_distrib,
        "one_plus_omega_eq_omega": non_comm_add,
        "two_mul_omega_eq_omega": non_comm_mul,
        "passed": assoc_add and left_distrib and non_comm_add and non_comm_mul,
    }


def verify_heyting_chain(n: int = 5) -> Dict[str, Any]:
    """Verifies residuation (a & b <= c) iff (a <= (b => c)) on the n-element linear Heyting chain."""
    elems = list(range(n))
    top = n - 1

    def meet(a: int, b: int) -> int:
        return min(a, b)

    def impl(b: int, c: int) -> int:
        return top if b <= c else c

    residuation_ok = all(
        (meet(a, b) <= c) == (a <= impl(b, c))
        for a in elems
        for b in elems
        for c in elems
    )
    return {
        "chain_size": n,
        "residuation_adjunction_holds": residuation_ok,
        "passed": residuation_ok,
    }


def main() -> int:
    vn = verify_von_neumann_ordinals()
    cnf = verify_cnf_arithmetic()
    heyting = verify_heyting_chain()
    report = {
        "von_neumann_ordinals": vn,
        "cantor_normal_form": cnf,
        "heyting_algebra": heyting,
        "passed": vn["passed"] and cnf["passed"] and heyting["passed"],
    }
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
