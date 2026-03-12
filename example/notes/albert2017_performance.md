---
title: "Performance and structure of single-mode bosonic codes"
authors:
  - "Victor V. Albert"
  - "Kyungjoo Noh"
  - "K. Duivenvoorden"
  - "Dylan J. Young"
  - "R. T. Brierley"
  - "P. Reinhold"
  - "Christophe Vuillot"
  - "Linshu Li"
  - "Chao Shen"
  - "S. Girvin"
  - "B. Terhal"
  - "Liang Jiang"
year: 2017
citekey: albert2017_performance
topics:
  - "gkp"
  - "bosonic-codes"
  - "qec"
  - "cat-codes"
  - "binomial-codes"
  - "pure-loss-channel"
  - "entanglement-fidelity"
status: "deep-read"
relevance: 5
doi: "10.1103/PhysRevA.97.032346"
url: "https://www.semanticscholar.org/paper/01c43ab213317e08dd54617d6ce395a602f6b65b"
venue: "Physical Review A"
tags: [paper]
---

## Summary

A systematic numerical comparison of all major single-mode bosonic codes (GKP, cat, binomial, and numerically optimized codes) under the bosonic pure-loss channel (photon loss), using entanglement fidelity after the optimal recovery operation as the performance metric. The paper establishes that GKP codes significantly outperform cat and binomial codes across most loss rates, despite not being designed specifically for the pure-loss channel. It also introduces numerically optimized codes and characterizes an essential singularity in GKP entanglement fidelity at vanishing loss rate.

## Key Findings

- GKP codes significantly outperform cat and binomial codes for most values of the photon-loss rate $\kappa$.
- At small loss rates, the performance ordering is: GKP > binomial > cat.
- GKP performance increases monotonically with increasing average photon number $\bar{n}$ of the code.
- An essential singularity exists in the entanglement fidelity of GKP codes in the limit of vanishing loss rate: $F_e \sim 1 - C \cdot e^{-\alpha/\kappa}$ as $\kappa \to 0$.
- The achievable communication rate (hashing bound) is also computed for each code family.
- Binomial codes are characterized in terms of spin-coherent states, enabling check operators and error-correction procedures analogous to discrete-variable codes.

## Methodology

The entanglement fidelity $F_e$ is computed numerically for each code after the optimal (Petz) recovery channel. The pure-loss channel is modeled as a beamsplitter interaction with a vacuum environment. Optimal recovery is the Petz map. Codes are truncated in photon-number space for numerical tractability. Channel capacity (hashing bound) computed from the coherent information.

## Relevance

This is the key benchmarking reference for bosonic quantum error correction. The Petz map recovery used here is the standard optimal recovery map. The entanglement fidelity metric and the essential singularity result are central to understanding why GKP codes are exceptional among bosonic codes. The numerical methods here (Fock-space truncation, Petz recovery, fidelity computation) form the basis for many subsequent analyses.

## Key Equations / Results

Entanglement fidelity after optimal recovery:
$$F_e(\mathcal{E}, \mathcal{R}) = \langle \Phi^+ | (\mathcal{R} \circ \mathcal{E} \otimes \mathbb{I})(|\Phi^+\rangle\langle\Phi^+|) | \Phi^+\rangle$$

Essential singularity of GKP fidelity at small loss:
$$1 - F_e^{\text{GKP}} \sim e^{-\pi/(2\kappa)} \quad \text{as } \kappa \to 0$$

## Key Quotes

"GKP codes significantly outperform all other codes for most values of the loss rate."

## Questions / Critiques

- The numerically optimized codes introduced here are not widely used in later literature — need to verify whether they have been followed up.
- The Petz map computation is numerically intensive; verify Fock space truncation used.
- The paper predates experimental demonstrations — confirm that the theoretical predictions match experimental results.

## Related Papers

- gottesman2001_encoding — original GKP code definition
- brady2023_advances — comprehensive review including performance comparisons
