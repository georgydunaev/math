# Mathematical Foundations and Executable Lattice/Ordinal Index

- **Repository**: `math` (`/botworkspace/math`)
- **Primary Branch**: `main`
- **Remotes**: `gitlab`, `github`

---

## 1. Purpose and Architectural Scope

The `math` repository provides self-contained mathematical reference notes and executable verification routines for foundational set theory, finite von Neumann ordinals, Cantor Normal Form (`CNF`) ordinal arithmetic, and finite distributive/Heyting algebra structures aligned with the `MKTD1` (`MKTD1-theory`) and `MKTD2` (`MKTD2-theory`) foundational ecosystem.

| File | Role and Mathematical Scope |
| :--- | :--- |
| [README.md](file:///botworkspace/math/README.md) | Repository overview and entry point. |
| [ARCHITECTURE_AND_INDEX.md](file:///botworkspace/math/ARCHITECTURE_AND_INDEX.md) | Architectural index and mathematical verification summary. |
| [math_foundations_verifier.py](file:///botworkspace/math/math_foundations_verifier.py) | Executable verifier for finite von Neumann ordinals (transitivity, strict membership well-ordering, union/successor identities), Cantor Normal Form ordinal addition and multiplication (non-commutativity witnesses `1 + omega = omega != omega + 1` and `2 * omega = omega != omega * 2`), and finite Heyting/Boolean algebra residuation laws. |

---

## 2. Verified Mathematical Structures

### 2.1 Finite von Neumann Ordinals
- Each finite ordinal $n$ is constructed recursively as $0 = \emptyset$ and $S(n) = n \cup \{n\} = \{0, 1, \dots, n-1\}$.
- Verified properties:
  1. **Transitivity**: Every element $x \in \alpha$ satisfies $x \subseteq \alpha$.
  2. **Trichotomy of Membership**: For all $x, y \in \alpha$, exactly one of $x \in y$, $x = y$, or $y \in x$ holds.
  3. **Limit/Successor Union Law**: $\bigcup S(\alpha) = \alpha$.

### 2.2 Cantor Normal Form (`CNF`) Ordinal Arithmetic up to $\omega^\omega$
- Every ordinal $0 < \alpha < \omega^\omega$ has a unique representation $\alpha = \omega^{e_1}\cdot c_1 + \omega^{e_2}\cdot c_2 + \dots + \omega^{e_k}\cdot c_k$ with $e_1 > e_2 > \dots > e_k \ge 0$ and $c_i \in \mathbb{N}_{>0}$.
- Verifies associativity of ordinal addition $(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)$, left-distributivity $\alpha \cdot (\beta + \gamma) = \alpha \cdot \beta + \alpha \cdot \gamma$, and non-commutativity of both addition and multiplication at $\omega$.

### 2.3 Finite Heyting Algebra Residuation
- Verifies the adjunction $(a \wedge b) \le c \iff a \le (b \Rightarrow c)$ across finite divisor/subset lattices, connecting constructive intuitionistic implication (`MKTD2-theory`) with classical Boolean algebras (`MKTD1-theory`).

---

## 3. Verification Command

```bash
python3 /botworkspace/math/math_foundations_verifier.py
```
