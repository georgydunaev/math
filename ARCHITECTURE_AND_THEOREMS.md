# Architecture and Theorems Guide (`math`)

This document summarizes the scope, architectural design, mathematical domains, and open formalization roadmap for the `math` repository.

---

## 1. Repository Overview and Architectural Role

The `math` repository serves as the general-purpose discrete and structural mathematics workspace within `/botworkspace`, bridging pure mathematical exposition, algorithmic reference implementations, and formal verification pipelines in sibling repositories:

| Connected Repository | Mathematical Interface |
|---|---|
| `foundations` | Morse-Kelley (`MK`) and von Neumann-Bernays-Godel (`NBG`) class theory, Dunaev Tagged Ordered Pairs, and `MKTD1-system` / `MKTD2-system` set-theoretic foundations |
| `FirstOrderTheory` | First-order syntax, nested vector induction on terms, Prenex and Skolem normal forms, Hilbert calculi, and ZFC axiom encodings |
| `ProofTheory` | Robinson Arithmetic ($Q$), Peano Arithmetic ($PA$), Gentzen sequent calculus ($LK$), syntactic cut-elimination, Cantor normal form up to $\varepsilon_0$, and Godel's First Incompleteness Theorem |
| `MathLogic` | Propositional tautology checking, Lukasiewicz Hilbert system ($AxK, AxS, AxContra, MP$), Robinson first-order resolution, Knuth-Bendix equational completion, and Herbrand expansion |
| `yoneda_ai` | Finite categories, functors, natural transformations, the Yoneda Lemma ($\mathrm{Nat}(h_A, F) \cong F(A)$), small limits in $\mathbf{Set}$, and adjunctions ($F \dashv G$) |

---

## 2. Core Mathematical Domains and Reference Specifications

### 2.1 Elementary Number Theory and Arithmetic Foundations
- **Euclidean Division and Bezout's Identity**:
  - For all $a, b \in \mathbb{Z}$ with $b > 0$, there exist unique $q, r \in \mathbb{Z}$ such that $a = bq + r$ and $0 \le r < b$.
  - Extended Euclidean algorithm computing $(g, x, y)$ such that $ax + by = g = \gcd(a, b)$.
- **Fundamental Theorem of Arithmetic and Modular Arithmetic**:
  - Prime factorization existence and uniqueness up to permutation of prime factors.
  - Chinese Remainder Theorem ($CRT$) for pairwise coprime moduli $m_1, \dots, m_k$:
    $$\mathbb{Z}/(m_1 \cdots m_k)\mathbb{Z} \cong \mathbb{Z}/m_1\mathbb{Z} \times \cdots \times \mathbb{Z}/m_k\mathbb{Z}$$
  - Euler's totient theorem $a^{\varphi(n)} \equiv 1 \pmod n$ for $\gcd(a, n) = 1$ and Fermat's Little Theorem $a^{p-1} \equiv 1 \pmod p$.

### 2.2 Abstract Algebra (Groups, Rings, Fields)
- **Group Theory**:
  - Group axioms: associativity $(a \cdot b) \cdot c = a \cdot (b \cdot c)$, two-sided identity $e \cdot a = a \cdot e = a$, and two-sided inverses $a \cdot a^{-1} = a^{-1} \cdot a = e$.
  - **Lagrange's Theorem**: For any finite group $G$ and subgroup $H \le G$, $|G| = [G : H] \cdot |H|$.
  - **First Isomorphism Theorem**: For any group homomorphism $\varphi : G \to G'$, $\ker(\varphi) \trianglelefteq G$ and $G / \ker(\varphi) \cong \mathrm{im}(\varphi)$.
- **Ring and Polynomial Theory**:
  - Commutative rings with unity, integral domains, principal ideal domains ($PID$), and Euclidean domains.
  - Polynomial division over fields $F[x]$: for $f, g \in F[x]$ with $g \ne 0$, unique $q, r \in F[x]$ with $f = qg + r$ and $\deg(r) < \deg(g)$ or $r = 0$.

### 2.3 Linear Algebra and Spectral Structure
- **Rank-Nullity Theorem**:
  - For any finite-dimensional vector space $V$ over a field $F$ and linear map $T : V \to W$:
    $$\dim(V) = \dim(\ker(T)) + \dim(\mathrm{im}(T))$$
- **Determinants and Cramer's Rule**:
  - Leibniz alternating multilinear expansion $\det(A) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_{i=1}^n A_{i, \sigma(i)}$, multiplicative law $\det(AB) = \det(A)\det(B)$, and invertibility criterion $A \in \mathrm{GL}_n(F) \iff \det(A) \ne 0$.

### 2.4 Combinatorics and Poset Structure
- **Inclusion-Exclusion Principle**:
  $$\left|\bigcup_{i=1}^n A_i\right| = \sum_{\emptyset \ne I \subseteq \{1,\dots,n\}} (-1)^{|I|-1} \left|\bigcap_{i \in I} A_i\right|$$
- **Knaster-Tarski Fixed-Point Theorem**:
  - Every monotone map $f : L \to L$ on a complete lattice $(L, \le)$ has a complete lattice of fixed points, with least fixed point $\mu f = \bigwedge \{x \in L \mid f(x) \le x\}$ and greatest fixed point $\nu f = \bigvee \{x \in L \mid x \le f(x)\}$.

---

## 3. Unfinished Problems and Development Roadmap (`TODO`)

1. **Exact Rational and Finite-Field Computational Modules (`src/`)**:
   - Implement zero-dependency Python 3 and portable SML'97 modules for exact modular arithmetic, polynomial rings over $\mathbb{Q}$ and $\mathbb{F}_p$, and exact Bareiss/Gaussian elimination.
2. **Formal Proof Scripts (`.v` / `.ML`)**:
   - Add constructive Coq and Standard ML verification scripts for Bezout's identity, the Chinese Remainder Theorem, Lagrange's theorem on finite coset partitions, and the Knaster-Tarski fixed-point theorem.
3. **Unit Test Suite (`tests/`)**:
   - Add automated property and unit tests covering number-theoretic, algebraic, and combinatorial invariants.
