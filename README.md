# Knot Theory and Recursion: Computing d-Invariants of 2-Bridge Links

A computational mathematics project developed as part of the
**Mathematical Programming** module at the **University of Bristol**.
The project translates recursive definitions from knot theory into
Python algorithms for computing and investigating the **d-invariants of
2-bridge links** (S(p,q)).

## Project Overview

The notebook develops a recursive implementation for calculating the
d-invariant associated with a 2-bridge link (S(p,q)). It then builds on
this implementation to:

-   compute individual components (d(S(p,q),i));
-   generate the complete list of d-invariants for a given (S(p,q));
-   test the modulo behaviour specified by the recursive definition;
-   compare d-invariants for selected pairs of 2-bridge links; and
-   computationally investigate whether d-invariants completely
    distinguish between 2-bridge links.

The project combines mathematical reasoning with recursion, exact
rational arithmetic, memoisation, dictionary-based caching and automated
testing.

## Mathematical Definition

The implementation is based on three recursive rules supplied in the
project:

1.  For any (q) and (i),

    `d(S(1,q),i) = 0`

2.  Values of (q) and (i) can be reduced modulo (p):

    `d(S(p,q),i) = d(S(p,q mod p), i mod p)`

3.  When (p \> q \> 0), the d-invariant is calculated recursively using
    the stated recurrence relation from the project.

The notebook uses the example (d(S(9,7))) to test the implementation.

## Implementation

### `d_S(p, q, i)`

The core recursive function computes the (i)-th component of the
d-invariant of (S(p,q)).

Python's `Fraction` class is used instead of floating-point arithmetic
so that the calculations retain exact rational values.

Memoisation is incorporated through a dictionary cache. Previously
computed `(p, q, i)` values can therefore be reused instead of
recalculated during later recursive calls.

### `D_S(p, q)`

The function

``` python
D_S(p, q)
```

returns the complete d-invariant as a list by evaluating `d_S(p, q, i)`
for every index from `0` to `p - 1`.

For example:

``` python
print(D_S(9, 7))
```

is used to reproduce and test the example supplied in the project.

### Modulo-rule testing

The notebook defines `check_modulo_rule(p, q, k)` to test
computationally that indices equivalent modulo (p) produce the same
d-invariant value.

Assertions are used so that a violation of the expected property is
automatically flagged.

### Comparing 2-bridge links

Selected examples are compared by computing their complete d-invariant
lists. The notebook investigates how known relationships between
(S(p,q_1)) and (S(p,q_2)) are reflected computationally in their
d-invariants.

### Searching for duplicate invariants

The function

``` python
is_distinguished(max_p)
```

systematically computes d-invariants for values satisfying

``` text
2 <= p < max_p
1 <= q < p
```

and stores previously encountered invariant lists in a dictionary.

If the same computed invariant is encountered again, the program reports
the corresponding `(p, q)` pairs. This provides a computational method
for investigating whether the calculated d-invariants uniquely
distinguish the links in the tested collection.

The notebook demonstrates this search for collections with bounds of 100
and 200.

## Computational Efficiency

The recursive calculation can repeatedly encounter the same subproblems.
To reduce redundant computation, the implementation uses
**memoisation**.

This substantially improves the practicality of the larger searches,
although the notebook notes that calculations for values of (p) above
approximately 200 can still take several minutes.

This part of the project demonstrates the connection between a
mathematical recursive definition and an important programming
technique: caching previously computed results to improve algorithmic
efficiency.

## Technologies and Techniques

-   **Python**
-   **Jupyter Notebook**
-   Recursive algorithms
-   Memoisation
-   Dictionaries and tuple keys
-   Exact rational arithmetic with `fractions.Fraction`
-   Modular arithmetic
-   Assertions and automated validation
-   Systematic parameter testing

## Repository Structure

``` text
Python-Portfolio/
└── Knot Theory Group Project.ipynb
```

The Jupyter notebook contains the mathematical explanation, Python
implementation and testing used throughout the project.

## Running the Project

Clone the repository and open the notebook in Jupyter Notebook,
JupyterLab or VS Code with Jupyter support.

A typical setup is:

``` bash
git clone <repository-url>
cd Python-Portfolio
python -m venv .venv
source .venv/bin/activate
pip install jupyter
jupyter notebook
```

Then open the knot theory notebook and run the cells in order.

The mathematical calculations themselves rely only on Python's
standard-library `fractions` module.

## Skills Demonstrated

This project demonstrates the ability to:

-   translate abstract mathematical definitions into executable
    algorithms;
-   design and implement recursive Python functions;
-   improve recursive algorithms using memoisation and caching;
-   work with exact rational arithmetic rather than numerical
    approximations;
-   use modular arithmetic programmatically;
-   validate mathematical properties using assertions;
-   design systematic computational experiments; and
-   communicate mathematical reasoning alongside code.

## Academic Context

This was a **University of Bristol Mathematical Programming project**
focused on knot theory, recursion and computational mathematics.

The repository is intended to demonstrate both the mathematical
reasoning behind the problem and the programming techniques used to
investigate it computationally.
