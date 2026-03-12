---
title: "Encoding a qubit in an oscillator"
authors:
  - "D. Gottesman"
  - "A. Kitaev"
  - "J. Preskill"
year: 2001
citekey: gottesman2001_encoding
topics:
  - "gkp"
  - "bosonic-codes"
  - "qec"
  - "continuous-variables"
  - "stabilizer-codes"
status: "deep-read"
relevance: 5
doi: "10.1103/PhysRevA.64.012310"
url: "https://www.semanticscholar.org/paper/49325b4d95f0fca3500ca1ce60c712a9ddf8fbfd"
venue: "Physical Review A"
tags: [paper]
---

## Summary

The foundational paper introducing the Gottesman-Kitaev-Preskill (GKP) code, which encodes a finite-dimensional (qubit) code space into the infinite-dimensional Hilbert space of a continuous-variable oscillator. The code exploits the noncommutative geometry of phase space — position $\hat{q}$ and momentum $\hat{p}$ — to protect against small shift errors in both quadratures. In the quantum optics setting, fault-tolerant universal quantum computation can be performed on the encoded subspace using linear optical operations, squeezing, homodyne detection, and photon counting, with nonlinear mode coupling required only for state preparation.

## Key Findings

- A qubit can be encoded into a single oscillator by constructing a code space that is stabilized by displacement operators $e^{2i\sqrt{\pi}\hat{q}}$ and $e^{2i\sqrt{\pi}\hat{p}}$.
- The code corrects any shift error $(\Delta q, \Delta p)$ with $|\Delta q| < \sqrt{\pi}/2$ and $|\Delta p| < \sqrt{\pi}/2$ (the square GKP lattice).
- Fault-tolerant Clifford gates (H, S, CNOT) are implementable with Gaussian operations; non-Clifford gates (e.g., T) require non-Gaussian resources or magic state injection.
- Nonlinear mode coupling (e.g., photon counting or Kerr interaction) is necessary for preparing ideal GKP codewords from scratch.
- Finite-dimensional ($d$-level) analogs protect against errors in amplitude or phase of a $d$-state system.
- Continuous-variable codes establish lower bounds on the quantum capacity of Gaussian quantum channels.

## Methodology

Stabilizer formalism extended to the continuous-variable (CV) setting. The code is defined as the simultaneous +1 eigenspace of the two commuting displacement operators $S_q = e^{2i\sqrt{\pi}\hat{q}}$ and $S_p = e^{-2i\sqrt{\pi}\hat{p}}$. Logical operators are $\bar{X} = e^{i\sqrt{\pi}\hat{q}}$ and $\bar{Z} = e^{i\sqrt{\pi}\hat{p}}$. Error correction is performed by measuring the stabilizers (homodyne detection modulo $\sqrt{\pi}$) and applying the inverse shift. The paper also considers hexagonal and more general symplectic lattice structures.

## Relevance

This is the foundational reference for GKP codes in quantum error correction. It defines the stabilizer group, logical operators, and ideal codewords in position-space eigenstates (superpositions of Dirac combs). The finite-energy approximations (envelope function) and loss-channel analysis build upon the ideal states defined here. The error model characterized in this paper underpins all subsequent work on GKP-based QEC.

## Key Equations / Results

The GKP stabilizers for the square lattice code:
$$S_q = e^{2i\sqrt{\pi}\hat{q}}, \qquad S_p = e^{-2i\sqrt{\pi}\hat{p}}$$

Logical Pauli operators:
$$\bar{X} = e^{i\sqrt{\pi}\hat{q}}, \qquad \bar{Z} = e^{i\sqrt{\pi}\hat{p}}$$

Ideal GKP codewords in position representation (Dirac comb superpositions):
$$|0_L\rangle \propto \sum_{n=-\infty}^{\infty} |2n\sqrt{\pi}\rangle_q, \qquad |1_L\rangle \propto \sum_{n=-\infty}^{\infty} |(2n+1)\sqrt{\pi}\rangle_q$$

Error correction condition: corrects shifts $(\Delta q, \Delta p)$ if $|\Delta q|, |\Delta p| < \sqrt{\pi}/2$.

## Key Quotes

"Quantum error-correcting codes are constructed that embed a finite-dimensional code space in the infinite-dimensional Hilbert space."

## Questions / Critiques

- The ideal codewords have infinite energy (infinite superposition of position eigenstates); practical implementation requires finite-energy approximations (envelope function).
- The paper does not address the pure-loss (photon loss) channel directly — the loss-channel performance is analyzed in Albert 2017.
- Gate set completeness: what exactly is the minimal non-Gaussian resource required? The paper asserts photon counting suffices but does not give a complete circuit construction.

## Related Papers

- albert2017_performance — systematic performance comparison of GKP vs cat/binomial codes under pure-loss channel
- brady2023_advances — comprehensive review of GKP theory and experiment
