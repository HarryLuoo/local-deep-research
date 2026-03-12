---
title: "Quantum error mitigation"
authors:
  - "Zhenyu Cai"
  - "Ryan Babbush"
  - "Simon C. Benjamin"
  - "Suguru Endo"
  - "William J. Huggins"
  - "Ying Li"
  - "Jarrod R. McClean"
  - "Thomas E. O'Brien"
year: 2023
citekey: cai2023_quantum
topics:
  - "quantum error mitigation"
  - "review"
  - "zero-noise extrapolation"
  - "probabilistic error cancellation"
  - "virtual distillation"
  - "NISQ"
status: "deep-read"
relevance: 3
doi: ""
url: "https://arxiv.org/abs/2210.00921"
venue: "Reviews of Modern Physics"
tags: [paper]
---

## Summary

Cai et al. provide a comprehensive review of quantum error mitigation (QEM) methods published in Reviews of Modern Physics (2023), covering all major techniques including zero-noise extrapolation, probabilistic error cancellation, symmetry verification, virtual distillation, and subspace expansion. The review systematically compares these methods in terms of assumptions, sampling overheads, applicability regimes, and experimental demonstrations.

## Key Findings

- QEM is distinct from QEC: QEM reduces the effect of noise in expectation values without correcting individual quantum states; it trades sampling overhead for qubit overhead.
- ZNE and PEC are the two most widely demonstrated techniques; ZNE requires minimal assumptions, PEC requires a noise model.
- Virtual distillation (exponential error suppression) suppresses errors exponentially in the number of circuit copies at the cost of $O(M^2)$ qubit overhead.
- Sampling overhead for PEC scales as $e^{2\gamma n}$ where $\gamma$ is the average error rate and $n$ is the circuit depth.
- Symmetry-based QEM is most efficient when the target quantity respects a symmetry (e.g., particle number, parity) and errors break it.
- QEM and QEC are complementary: QEM can reduce logical error rates in error-corrected circuits, not just physical circuits.

## Methodology

Comprehensive literature review and synthesis. The review organizes QEM methods by their underlying principle: noise extrapolation, noise inversion, error detection, state purification, and postprocessing. Provides unified analysis framework with sampling overhead as the common metric.

## Relevance

This is the standard reference for quantum error mitigation. It provides the context, language, and comparisons needed for understanding the QEM landscape. The review's treatment of QEM for error-corrected circuits (not just physical qubits) is particularly relevant to researchers working at the intersection of QEM and QEC. The sampling overhead analysis provides benchmarks for evaluating QEM methods.

## Key Equations / Results

ZNE expansion: $E(\lambda) = E_0 + \sum_k a_k \lambda^k$, with extrapolation to $\lambda \to 0$.

PEC sampling overhead: $\sim e^{2\gamma n}$ where $\gamma$ = error rate per layer, $n$ = depth.

Virtual distillation: $\langle O \rangle_\text{mitigated} = \text{Tr}[O \rho^M] / \text{Tr}[\rho^M]$ for $M$ copies.

## Key Quotes

- "Quantum error mitigation trades sampling overhead for qubit overhead."

## Questions / Critiques

- The review doesn't deeply address continuous-variable systems or bosonic QEM.
- The exponential sampling overhead limitations suggest fundamental limits that the review only partially addresses.

## Related Papers

- temme2017_error — original ZNE paper
- giurgicatiron2020_digital — digital ZNE implementation
- takagi2023_universal — fundamental sampling lower bounds
