# Performance and structure of single-mode bosonic codes

Victor V. Albert, Kyungjoo Noh, Kasper Duivenvoorden, Dylan J. Young, R. T. Brierley, Philip Reinhold, Christophe Vuillot, Linshu Li, Chao Shen, S. M. Girvin, Barbara M. Terhal, Liang Jiang

###### Abstract

The early Gottesman, Kitaev, and Preskill (GKP) proposal for encoding a qubit in an oscillator has recently been followed by cat- and binomial-code proposals. Numerically optimized codes have also been proposed, and we introduce new codes of this type here. These codes have yet to be compared using the same error model; we provide such a comparison by determining the entanglement fidelity of all codes with respect to the bosonic pure-loss channel (i.e., photon loss) after the optimal recovery operation. We then compare achievable communication rates of the combined encoding-error-recovery channel by calculating the channel’s hashing bound for each code. Cat and binomial codes perform similarly, with binomial codes outperforming cat codes at small loss rates. Despite not being designed to protect against the pure-loss channel, GKP codes significantly outperform all other codes for most values of the loss rate. We show that the performance of GKP and some binomial codes increases monotonically with increasing average photon number of the codes. In order to corroborate our numerical evidence of the cat/binomial/GKP order of performance occurring at small loss rates, we analytically evaluate the quantum error-correction conditions of those codes. For GKP codes, we find an essential singularity in the entanglement fidelity in the limit of vanishing loss rate. In addition to comparing the codes, we draw parallels between binomial codes and discrete-variable systems. First, we characterize one- and two-mode binomial as well as multi-qubit permutation-invariant codes in terms of spin-coherent states. Such a characterization allows us to introduce check operators and error-correction procedures for binomial codes. Second, we introduce a generalization of spin-coherent states, extending our characterization to qudit binomial codes and yielding a new multi-qudit code.

Keywords: continuous variable, microwave cavity, quantum communication

## I Introduction and problem setup

Continuous-variable (CV) systems [1; 2; 3; 4] continue to gain applications in quantum information processing and communication. The fundamental “moving part” of discrete-variable (DV) systems is one physical qubit, and one has to have a multitude of such qubits to construct a reliable logical qubit. By contrast, one may cleverly utilize the infinite-dimensional space of an oscillator or mode — the fundamental “moving part” of CV systems — in order to realize a comparably reliable logical qubit out of fewer moving parts. While many current linear-optical CV encodings use two modes per qubit in a “dual-rail” scheme [5; 6] and CV logical qubits may consist of several modes in the long-term, here we focus on a single mode since its theoretical limitations are not yet well-understood and since it is useful for communication.

There have been several error-correcting CV encoding schemes proposed to-date, formulated in terms of superpositions of either position/momentum eigenstates [7; 8; 9; 10; 11; 12], coherent states [13; 14; 15; 16; 17], or Fock states [18; 19; 20; 21; 22; 23; 24] (see also other hybrid CV-DV schemes [25; 26]). Besides the rich variety of quantum codes, there are two prevailing CV noise models: classical (i.e., Gaussian or displacement) noise and pure loss (more generally, thermal noise) [2]. Classical noise is modeled by a distribution of phase-space *displacements* while pure loss contracts phase space to the vacuum and is best understood in terms of *losses*. Due to the differing physical pictures and mathematical formalisms of these noise models, codes designed to protect against one may or may not protect against the other. However, it is often difficult to rigorously prove protection from noise against which a code wasn’t designed to protect. It is also difficult to study CV codes using the conventional stabilizer formalism because the noise model operators are not as well-behaved. This manuscript closes these gaps by applying tools from qubit-based quantum error-correction to CV codes which were not analyzed in this manner before.

### I.1 Codes and error model

The code classes we consider are

$\texttt{code}\in\{\texttt{cat},\texttt{bin},\texttt{num},\texttt{gkps},\texttt{gkp}\}\,.$ (1)

The logical states for the first code class — the cat-codes (5.1) — consist of superpositions of coherent states

---

![img-0.jpeg](images/img-0.jpeg)
![img-1.jpeg](images/img-1.jpeg)
![img-2.jpeg](images/img-2.jpeg)
![img-3.jpeg](images/img-3.jpeg)
![img-4.jpeg](images/img-4.jpeg)

Figure 1: Wigner function plots for maximally mixed logical states $\frac{1}{2}P_{\mathsf{code}}$ for code being cat (5.1), bin (6.1), num (Appx. B), gkps (7.7b), and gkp (7.8), evaluated for given values of the respective parameters of the codes. On the axes, $Q=\frac{1}{2}\langle\hat{a}+\hat{a}^{\dagger}\rangle$ and $I=\frac{i}{2}\langle\hat{a}^{\dagger}-\hat{a}\rangle$; color scales are not the same for all plots.

which are evenly distributed around a circle in phase space [13; 15; 27]. The second class of codes, the recently developed binomial codes (6.1), are designed to protect exactly against errors consisting of powers of raising/lowering operators up to some maximum order [23]. Here we show that bin codes are spin-coherent states embedded in an oscillator. We also include numerically optimized codes (some from Ref. [23] and the rest developed here) that were obtained by minimizing the photon number of the code states subject to the constraints of protecting exactly against the first few errors powers of the lowering operator. The last class consists of GKP codes [9] which are the $+1$ eigenspace of two commuting phase-space displacement operators; since the codespace is invariant under both displacements, the codespace makes a lattice in phase space. The gkps (7.8) class, with s standing for square, corresponds to a square lattice. The gkp (B4) class consists of GKP codes built out of both the square and other non-rectangular lattices as well as codes whose lattice is shifted by half a lattice spacing from the origin, thus subsuming the gkps class. The gkps codes are presented separately in order to quantify any advantages of other lattices.

A single-mode qubit CV code is a two-dimensional subspace of the bosonic Hilbert space picked to be able to protect quantum information against errors. It is unambiguously represented by the corresponding orthogonal projection onto the subspace,

$P_{\mathsf{code}}=|0_{\mathsf{code}}\rangle\langle 0_{\mathsf{code}}|+|1_{\mathsf{code}}\rangle\langle 1_{\mathsf{code}}|\,,$ (1.2)

where code is picked from Eq. (1.1) and $|\mu_{\mathsf{code}}\rangle$ (for $\mu\in\{0,1\}$) is any orthonormal basis for the code subspace. The maximally mixed state $\frac{1}{2}P_{\mathsf{code}}$ thus provides a concise basis-independent fingerprint for each code; we plot the Wigner function of this state in Fig. 1.

We deal exclusively with codes representing a single qubit and are guided by the question:

Which code best protects against the pure-loss channel?

We are interested in the pure-loss channel because it is a model for broadband-line and free-space communication [3] and it is the most common incoherent error process in optical and microwave cavities [23]. The second most common error is cavity dephasing, which is caused by fluctuations in the cavity frequency. Optical cavities have to be actively stabilized to fix the frequency, but the effects of such fluctuations are small relative to effects of energy loss, particularly in microwave cavities. There are also other coherent error processes, such as a Kerr nonlinearity [29], which we briefly consider in Sec. VIII.1.

The pure-loss bosonic channel (also known as bosonic amplitude damping or, more simply, as the lossy channel [2]) is Markovian: $\mathcal{N}=\exp(\chi\mathcal{D})$ with superoperator $\mathcal{D}(\cdot)=\hat{a}\cdot\hat{a}^{\dagger}-\frac{1}{2}\{\hat{n},\cdot\}$, where $\hat{a}/\hat{a}^{\dagger}$ is the lowering/raising operator for the bosonic mode and $\hat{n}\equiv\hat{a}^{\dagger}\hat{a}$. The dimensionless damping parameter equals $\chi=\kappa t$ for microwave or optical cavities (with excitation loss rate $\kappa$ and time interval $t$) or $\chi=l/l_{\mathrm{att}}$ for optical fibers (with fiber length $l$ and attenuation length $l_{\mathrm{att}}$). It is convenient to use the dimensionless loss rate

$\gamma\equiv 1-e^{-\chi}$ (1.3)

to quantify the severity of the error channel, denoted as $\mathcal{N}\equiv\mathcal{N}_{\gamma}$ from now on. This channel can be expressed via unraveling [18; 30; 31; 32] or Lie-algebraic [33] techniques in the Kraus representation, $\mathcal{N}_{\gamma}(\cdot)=\sum_{\ell=0}^{\infty}E_{\ell}\cdot E_{\ell}^{\dagger}$, with Kraus operators

$E_{\ell}\equiv\left(\frac{\gamma}{1-\gamma}\right)^{\ell/2}\frac{\hat{a}^{\ell}}{\sqrt{\ell!}}\left(1-\gamma\right)^{\hat{n}/2}\,.$ (1.4)

To leading order in $\gamma$, expansions of the first two Kraus operators suffice,

$E_{0}=I-\frac{1}{2}\gamma\hat{n}\quad\text{ and }\quad E_{1}=\sqrt{\gamma}\hat{a}\,.$ (1.5)

This channel can also be derived by introducing an environment mode $\hat{b}$, coupling our oscillator with the vacuum

---

state of this mode via a beam-splitter interaction

$\hat{a}\rightarrow\sqrt{1-\gamma}\,\hat{a}+\sqrt{\gamma}\,\hat{b}\,,$ (6)

and tracing out the $\hat{b}$-mode *[34, 3]*. The $K$-mode channel $\mathcal{N}_{\gamma}^{\otimes K}$ reduces to the multi-qubit amplitude damping channel when restricted to the first two Fock states of each mode and reduces to the erasure channel when restricted to the single-excitation subspace.

Notice that this channel does not contain the identity as a Kraus operator for $\gamma\neq 0$. This is due to the *backaction* or *damping* term $(1-\gamma)^{\bar{n}/2}$ in Eq. (4), which reduces the probabilities of being in Fock states $|n>0\rangle$ such that the only state remaining in the $\gamma\rightarrow 1$ limit is the vacuum Fock state $|n=0\rangle$. Thus, when no losses are recorded (i.e., if $E_{\ell>0}$ has not yet acted on the state), there is still a redistribution of probability caused by $E_{0}$. Colloquially for $\gamma>0$, if one hasn’t lost any photons, then one likely did not have many photons to begin with.

### II.2 Channel fidelity and recovery optimization

The combined quantum channel we consider consists of an encoding step $\mathcal{S}_{\texttt{code}}$, action of the pure-loss channel $\mathcal{N}_{\gamma}$, a recovery channel $\mathcal{R}$, and a perfect decoding step $\mathcal{S}_{\texttt{code}}^{-1}$. The encoding step maps the quantum information from the qubit *source space* $\mathsf{A}$ *[35]* into the code subspace of the bosonic Hilbert space; this step is represented by $\mathcal{S}_{\texttt{code}}$. More precisely, $\mathcal{S}_{\texttt{code}}(\rho)=S\rho S^{-1}$ where $S=|0_{\texttt{code}}\rangle\langle 0_{\mathsf{A}}|+|1_{\texttt{code}}\rangle\langle 1_{\mathsf{A}}|$, $\rho$ is a qubit density matrix in $\mathsf{A}$, and $|0_{\mathsf{A}}/1_{\mathsf{A}}\rangle$ is a basis for $\mathsf{A}$. Therefore, $SS^{-1}=P_{\texttt{code}}$ and, if $\{|0_{\texttt{code}}\rangle,|1_{\texttt{code}}\rangle\}$ are orthonormal, $S^{-1}S=I_{\mathsf{A}}$, the identity on $\mathsf{A}$. The combined channel

$\mathcal{E}\equiv\mathcal{S}_{\texttt{code}}^{-1}\circ\mathcal{R}\circ\mathcal{N}_{\gamma}\circ\mathcal{S}_{\texttt{code}}$ (7)

thus maps density matrices in $\mathsf{A}$ back to $\mathsf{A}$. In contrast, $\mathcal{R}\circ\mathcal{N}_{\gamma}$ is a map from the bosonic space to the code subspace. The form of $\mathcal{E}$ depends on the code, the loss rate $\gamma$, and the recovery $\mathcal{R}$. The channel can be written in the Kraus representation, $\mathcal{E}(\cdot)=\sum_{k}A_{k}\cdot A_{k}^{\dagger}$, or in the *matrix or Liouville representation* — as a $4\times 4$ matrix with elements

$\mathcal{E}_{kl}=\tfrac{1}{2}\text{Tr}\{\sigma_{k}\mathcal{E}(\sigma_{\ell})\}\,,$ (8)

using the three Pauli matrices $\sigma_{1,2,3}$ and identity $I_{\mathsf{A}}\equiv\sigma_{0}$ (e.g., *[36]*, Sec. 2.2). Composition “$\circ$” in Eq. (7) is equivalent to matrix multiplication in the matrix representation, so we omit the symbol.

None of the codes we consider protect against all errors in $\mathcal{N}_{\gamma}$, so we have to consider approximate quantum error correction *[37, 38]*. We compare the codes using the *channel fidelity* $F_{\mathcal{E}}$ *[39]* — a specific case of entanglement fidelity *[40]* that is motivated as follows. Let the source qubit $\mathsf{A}$ be in a maximally entangled state with ancillary qubit $\mathsf{B}$, i.e., $|\Psi\rangle=(|0_{\mathsf{A}}0_{\mathsf{B}}\rangle+|1_{\mathsf{A}}1_{\mathsf{B}}\rangle)/\sqrt{2}$. Qubit $\mathsf{B}$ is left alone (i.e., acted on by the identity superoperator $\mathcal{I}$) while the source qubit is acted on by the channel $\mathcal{E}$ in Eq. (7). The channel fidelity $F_{\mathcal{E}}$ is simply the overlap between the initial state $|\Psi\rangle$ and the final state

$\rho_{\mathcal{E}}\equiv\mathcal{E}\otimes\mathcal{I}(|\Psi\rangle\langle\Psi|)\,,$ (9)

(which we define to be the Choi matrix of $\mathcal{E}$):

$F_{\mathcal{E}}\equiv\langle\Psi|\rho_{\mathcal{E}}|\Psi\rangle\,.$ (10)

Remembering that $\text{Tr}_{\mathsf{B}}\{|\Psi\rangle\langle\Psi|\}$ is the maximally mixed state $\tfrac{1}{2}I_{\mathsf{A}}$ of qubit $\mathsf{A}$, a few simple manipulations yield

$F_{\mathcal{E}}=\frac{1}{4}\sum_{k=1}^{4}\left|\text{Tr}\{A_{k}\}\right|^{2}=\frac{1}{4}\text{Tr}\{\mathcal{E}\}\,,$ (11)

where $\text{Tr}$ is the trace in the matrix representation (8).

Besides clearly being an intrinsic property of $\mathcal{E}$ that is invariant under unitary rotations, several other properties of $F_{\mathcal{E}}$ make the quantity both meaningful and practically useful. We first mention the property that is crucial for our task, listing the remaining properties in Appx. A. It turns out that the recovery $\mathcal{R}$ which gives the optimal $F_{\mathcal{E}}$ is computable via a semi-definite program *[44]* (see also *[39, 45]*). This allows us to quickly obtain the highest possible $F_{\mathcal{E}}$ using a laptop (given reasonable $\bar{n}_{\texttt{code}}$) and without having to design a recovery for each code. This procedure was applied to the multi-qubit context by Fletcher, Shor, and Win *[43]* (see also *[35]* and references therein), and our benchmarking is in some sense a counterpart to that work in the oscillator context. From now on and unless otherwise noted, we let the recovery piece $\mathcal{R}$ of $\mathcal{E}$ (7) be one which gives the highest $F_{\mathcal{E}}$, given a member of the code family and a loss rate $\gamma$.

### II.3 Outline of this paper

In Sec. II, we state our main numerical code comparison results and summarize the supporting analytical calculations. In Sec. III, we numerically analyze communication rates of our codes by calculating the hashing bound of $\mathcal{E}$. In Sec. IV, we review the quantum error-correction conditions. In Secs. V, VI, and VII, we calculate these conditions for the cat, bin, and gkp codes, respectively. In Sec. VI.3, we characterize single-qubit bin codes in terms of spin-coherent states and relate them to two-mode binomial codes and multi-qubit permutation-invariant codes. In Sec. VIII, we analyze code performance after a Kerr interaction is added to the pure loss channel and briefly study the effect of tracking the photon number parity. We summarize our results and discuss future directions in Sec. IX.

---

# II. TAKE-HOME MESSAGES

Here we summarize the results related to code performance, but start off by mentioning two caveats to our primary numerical comparison. Results relating the structure of bin codes to spin-coherent states and other multi-qubit codes are summarized in Sec. IX B.

Caveat ① is that the encoding, recovery, and decoding are all assumed perfect, meaning that there are no other errors besides  $\mathcal{N}_{\gamma}$  incurred by the state. Therefore, the results of this section should be interpreted as theoretical bounds on code capabilities and not as practical suggestions on the best experimental design. Moreover, optimal recovery procedures are not created equal in the eyes of current technologies: cat code error correction has already been performed [29] while gkp states have yet to be realized. We briefly investigate one additional imperfection in Sec. VIII by including a nonlinearity. There, we also address the consequences of being able to perfectly track the photon number parity.

Caveat ② has to do with how we quantify the "size" of the codes. Namely, we organize the codes by mean occupation number

$$
\bar {n} _ {\text {c o d e}} \equiv \operatorname {T r} \left\{P _ {\text {c o d e}} \hat {n} \right\} / 2. \tag {2.1}
$$

While  $\bar{n}_{\mathrm{code}}$  is proportional to the average energy required to construct a code state, it does not describe the spread or variance in Fock space,  $\sigma_{\mathrm{code}}^2 \equiv \frac{1}{2} \mathrm{Tr}\{P_{\mathrm{code}} \hat{n}^2\} - \bar{n}_{\mathrm{code}}^2$ . While cat and bin codes follow approximately Poisson and binomial distributions in Fock space, respectively, we will show that gkp codes are geometrically (i.e., thermally) distributed and thus have much larger "tails" in Fock space at higher  $\bar{n}$ . Therefore, for the same  $\bar{n}_{\mathrm{code}}$ , gkp codes utilize much more of the Fock space than cat/bin and are therefore "larger" (in the same sense that multi-qubit codes constructed out of ten physical qubits are larger than those constructed out of five). A simple energy parameter does not quantify such a notion of size.

# A. Numerical comparison

The procedure we use to determine the channel fidelities shown in Fig. 2 is as follows. Recall that each code family (1.1) contains multiple instances of codes. For example, a member of the bin code family is parameterized by the number of dephasing and loss errors it can correct ( $N$  and  $S$ , respectively; more details are in Sec. IV). For each loss rate  $\gamma$  in Eq. (1.3), we calculate the optimal  $F_{\mathcal{E}}$  for all instances of each code family subject to the energy constraint that  $\bar{n}_{\mathrm{code}} \leq 2,5,10$  [shown in Figs. 2(a), (b), and (c), respectively]. Then, we pick the highest  $F_{\mathcal{E}}$  out of all members of the code family and plot it in the figure. We repeat for other values of  $\gamma \leq 0.5$  — the point at which the one-way channel capacity of  $\mathcal{N}_{\gamma}$  becomes zero (see Sec. III for details). As a result of this simultaneous optimization over each code family and over the recovery

![img-5.jpeg](images/img-5.jpeg)

![img-6.jpeg](images/img-6.jpeg)

![img-7.jpeg](images/img-7.jpeg)
Figure 2. Channel fidelity  $F_{\mathcal{E}}$  (1.11) given an optimal recovery operation and optimized over all instances of each code given an occupation number constraint  $\bar{n}_{\mathrm{code}} \leq 2$  (a), 5 (b), or 10 (c). The dotted diagonal line, drawn for reference, is the optimal  $F_{\mathcal{E}}$  for single-rail encoding [6] (whose logical states are the Fock states  $|0\rangle, |1\rangle$ ). While gkp codes perform worse than the other codes for sufficiently small  $\gamma$  (see insets), they outperform all other codes as  $\gamma$  is increased despite not being designed to protect against the pure-loss channel. We were not able to obtain significantly better num codes with  $\bar{n}_{\mathrm{num}} &gt; 5$  due to a large set of parameters to be optimized over, so red curves in (b) and (c) are identical. Parameters for all of the codes used are in Table IV.

for a given member of the family, the code which gives the highest  $F_{\mathcal{E}}$  may change with  $\gamma$  and curves in Fig. 2 may display discontinuous derivatives.

Let us first focus on the  $\bar{n}_{\mathrm{code}} \leq 2$  case in Fig. 2(a) and examine the infidelity  $(1 - F_{\mathcal{E}})$  shown in the log-plot inset. For  $\gamma \leq 0.025$ , specific members of num, bin, and cat perform the best (in that order), showing similar scaling

---

with  $\gamma$ . All three of these codes were designed to deal with errors  $\{I, \hat{a}\}$ , the dominant terms in  $E_{\ell=0,1}$  at small  $\gamma$  (1.5). The num and bin codes show quadratic scaling versus small  $\gamma$ : in a polynomial fit up to order two for  $\gamma \leq 0.025$ ,  $c_0 + c_1\gamma + c_2\gamma^2$ , num/bin codes have negligible coefficients  $c_0$ ,  $c_1 \approx 10^{-4}$ , and a  $c_2$  of  $1.3/1.8$ , respectively. The cat codes have negligible  $c_0$ ,  $c_1 \approx 10^{-3}$ , and  $c_2 \approx 2.2$ . Following these codes, gkps and gkp perform the worst for small  $\gamma$ , underperforming the other codes as  $\gamma \to 0$ . This should be expected since these codes were designed to protect against small displacements and not loss events. It is also reasonable that gkp should slightly outperform gkps due to the idea that non-square lattices allow for tighter packing than square lattices [9]. The main unexpected behavior for  $\bar{n}_{\mathrm{code}} \leq 2$  occurs for  $\gamma \geq 0.025$ . There, we see that gkps and gkp actually outperform the rest of the codes (this will be discussed later).

We remark here that, for each  $\gamma$ , the amplitude  $\alpha$  of the coherent states making up cat codes [see Fig. 1(a)] for the optimal cat code is at a fine-tuned "sweet spot"  $\alpha_{\star}(\gamma)$  which balances the backaction due to the difference in the mean occupation number of the logical states (significant for small  $\alpha$  but zero at  $\alpha \to \infty$ ) against the probability that a photon will be lost (zero at  $\alpha \to 0$ ). We discuss this effect more in Sec. V, noting that it has also been studied elsewhere [23, 46].

Continuing to  $\bar{n}_{\mathrm{code}} \leq 5$  in Fig. 2(b), we see substantial increases in performance for all codes. We list notable infidelities for selected  $\gamma$  and  $\bar{n}_{\mathrm{code}} \leq 5$  in Table I(b). For example, for the relatively lossy channel having  $\gamma = 0.0952$ , there exist codes in all five families which have a channel fidelity higher than  $99.4\%$ . Moreover, all such codes have only five photons in them on average, so they could be within reach even with noisy intermediate-scale quantum (NISQ) technologies [47]. At small  $\gamma$  [inset of Fig. 2(b)], we again see polynomial scaling for the cat/bin/num codes, which are able to deal with loss errors  $\{I, \hat{a}, \hat{a}^2\}$ . We also once again see gkp outperform the other codes for  $\gamma \geq 0.05$  and underperform as  $\gamma \rightarrow 0$ . The cat and bin code performances are almost identical, with the exception of small  $\gamma$ , where bin performs slightly better. Expounding on this behavior in Sec. VIA, we show that bin allows for better error suppression than cat in certain ranges of  $\bar{n}$ . One num code performs the best for all  $\gamma \leq 0.4$  — the code with  $\bar{n}_{\mathrm{num}} = 4.15$  (see Appx. B).

Let us now consider the case  $\bar{n}_{\mathrm{code}} \leq 10$  in Fig. 2(c). While these codes may be difficult to create and correct experimentally in the near future, it is nevertheless interesting to see whether doubling the occupation number constraint allows for any improvements of the code. The most noticeable difference between  $\bar{n}_{\mathrm{code}} \leq 10$  and  $\bar{n}_{\mathrm{code}} \leq 5$  is that gkp pulls away from the other codes for all values of  $\gamma$  sampled. While it is believable that the other codes will still scale more favorably for sufficiently small  $\gamma$ , this occurs only at  $\gamma &lt; 0.01$ . For larger  $\gamma$ , gkp codes demonstrate  $F_{\mathcal{E}} \geq 0.99$  even at  $\gamma = 0.2$  (see

(a)  $1 - F_{\varepsilon}(\bar{n}\leq 2)$

|  γ | cat | bin | num | gkps | gkp  |
| --- | --- | --- | --- | --- | --- |
|  0.01 | 4.2e10-4 | 2.9e10-4 | 2.0e10-4 | 6.0e10-4 | 2.5e10-4  |
|  0.05 | 5.3e10-3 | 4.3e10-3 | 3.1e10-3 | 3.4e10-3 | 1.9e10-3  |
|  0.10 | 1.8e10-2 | 1.6e10-2 | 1.2e10-2 | 1.0e10-2 | 7.1e10-3  |
|  0.20 | 6.2e10-2 | 6.6e10-2 | 5.3e10-2 | 4.5e10-2 | 3.9e10-2  |
|  0.31 | 1.3e10-1 | 1.5e10-1 | 1.2e10-1 | 1.2e10-1 | 1.1e10-1  |

(b)  $1 - F_{\varepsilon}(\bar{n}\leq 5)$

|  γ | cat | bin | num | gkps | gkp  |
| --- | --- | --- | --- | --- | --- |
|  0.01 | 4.4e10-5 | 2.8e10-5 | 3.7e10-7 | 1.4e10-6 | 3.2e10-7  |
|  0.05 | 1.1e10-3 | 1.1e10-3 | 8.8e10-5 | 6.3e10-5 | 2.2e10-5  |
|  0.10 | 4.9e10-3 | 5.4e10-3 | 1.2e10-3 | 7.6e10-4 | 3.9e10-4  |
|  0.20 | 3.4e10-2 | 3.6e10-2 | 2.1e10-2 | 1.5e10-2 | 1.2e10-2  |
|  0.31 | 1.1e10-1 | 1.1e10-1 | 9.2e10-2 | 8.2e10-2 | 7.7e10-2  |

(c)  $1 - F_{\varepsilon}(\bar{n}\leq 10)$

|  γ | cat | bin | gkps | gkp  |
| --- | --- | --- | --- | --- |
|  0.01 | 1.7e10-5 | 3.7e10-7 | 3.0e10-10 | 1.0e10-11  |
|  0.05 | 6.3e10-4 | 1.5e10-4 | 8.2e10-7 | 1.5e10-7  |
|  0.10 | 4.9e10-3 | 1.7e10-3 | 7.9e10-5 | 2.9e10-5  |
|  0.20 | 3.4e10-2 | 3.1e10-2 | 6.5e10-3 | 4.6e10-3  |
|  0.31 | 1.1e10-1 | 1.1e10-1 | 6.3e10-2 | 5.9e10-2  |

Table I. Channel infidelity  $1 - F_{\varepsilon}$  from Figs. 2(a-c) at selected loss rates  $\gamma$  (with  $\gamma$  rounded to the nearest hundredth).

Table I). Looking at Table IV, the best codes in those families for most  $\gamma$  are those which also have  $\bar{n}_{\mathrm{gkp}} \approx 10$ . In other words, gkp performs better with increasing  $\bar{n}$ . A similar monotonic increase in performance occurs for subsets  $\mathrm{bin}(N, S \approx \xi N)$  of binomial codes (with  $\xi$  dependent on  $\gamma$ ) when the  $\bar{n}_{\mathrm{bin}}$  constraints are relaxed (see Sec. VIB). We explain the bin increase in performance in Secs. VIA-VIB, revealing that they have a larger set of approximately correctable errors than previously thought. This behavior is not seen in cat codes, which do not perform much better than those in Fig. 2(b) and work best at some finite  $\bar{n}$ . This idea that increasing  $\bar{n}$  does not lead to better cat code performance has been observed before in different contexts [46, 48, 49]. By contrast, the ideal gkp codes have infinite  $\bar{n}$ , so it seems reasonable that increasing  $\bar{n}$  should improve performance. These results support the conjecture that the ordering of the codes with respect to  $F_{\varepsilon}$  is  $\mathrm{gkp} &gt; \mathrm{bin} &gt; \mathrm{cat}$  when there is no energy constraint.

The numerical results show that codes designed to work well at small  $\gamma$  do not perform well for large  $\gamma$ , and vice versa. More specifically, extensions of the ideas used to correct dominant errors at small  $\gamma$  do not necessarily lead to good codes at larger  $\gamma$ . For instance, the cat and bin codes protect exactly from the first few loss errors by making sure there is adequate Fock state spacing  $S$  between the states. As an example, an  $S = 2$  cat/bin code uses superpositions of Fock states  $|0\rangle, |6\rangle, \dots$  for  $|0_{\mathrm{code}}\rangle$  and  $|3\rangle, |9\rangle, \dots$  for  $|1_{\mathrm{code}}\rangle$ . This guarantees that loss events  $E_{\ell=1,2}$ , which lower each Fock state by either

---

1 or 2, do not cause the logical states to overlap with each other. Both cat and bin allow one to increase $S$ arbitrarily, while gkp codes have $S\in\{0,1\}$, depending on whether their lattice is shifted from the origin or not. Figure 5 shows that, for sufficiently large $\gamma$ and $\bar{n}_{\texttt{code}}$, correcting a few errors exactly with spacing (done by cat and bin) is not as helpful as suppressing all errors approximately (done by gkp).

### II.2 Analytical results

To summarize, the family of gkp codes outperforms all of the other codes for most $\gamma$, with the exception of small $\gamma$ (which gets even smaller as the energy constraint is loosened). We see similar behavior analyzing the optimal codes from an information-theoretic perspective in Sec. III. Since all of the other codes were specifically designed to protect against loss errors and gkp codes were designed to protect against displacement errors, gkp have apparently outperformed all of the other codes “at their own game” (albeit a game whose rules were set by caveats ① and ②). To understand this effect, we have undertaken extensive analytical calculations to determine the quantum error-correction conditions for the pure-loss channel for gkp codes [see Eq. (7.18)] as well as how $1-F_{\mathcal{E}}$ scales with $\gamma$. As noted in the previous subsection, while other codes protect against errors (to some order in $\gamma$) exactly, gkp protect against all errors *approximately*. In other words, other codes protect against the first few errors exactly, but have low fidelity when there is a large probability of an unprotected error occurring. By contrast, gkp codes do not protect against most errors exactly, but the contributions from *all errors* to the infidelity is small.

In order to bound the scaling of $F_{\mathcal{E}}(\texttt{gkp})$ and since there is no analytic expression for the optimal $\mathcal{R}$, we calculate a lower bound on the channel fidelity $F_{\mathcal{E}}^{\text{AGKP}}$ using a recovery $\mathcal{R}^{\text{AGKP}}$ (7.22) which consists of phase-insensitive amplification, followed by conventional gkp recovery consisting of displacement measurements and corrections. The recovery is based on the idea that, after fine-tuning some of the channel parameters,

$\textit{pure loss}+\textit{amplification}=\textit{Gaussian noise},$

where Gaussian noise corresponds to uniform diffusion in phase space and its channel has displacements for its Kraus operators ( [2], Sec. 2.3; see also [50]). In other words, amplification (with gain $\frac{1}{1-\gamma}$) exactly compensates the contractive effect of pure loss (with loss rate $\gamma$) while at the same time adding noise that, in this context, reduces to Gaussian noise (with variance $\frac{\gamma}{1-\gamma}$). This idea has been considered in the context of communication schemes [51; 52]; we apply it to bosonic error-correction by noting that Gaussian noise is *exactly* the type of noise that gkp was designed for. That way, we can use earlier tools [9; 53] developed to quantify gkp performance against such noise. We consider single-mode behavior here, noting that, in the multimode case, gkp codes can be used to communicate efficiently across more general Gaussian channels [54]. Note that the related idea of “*amplication*+*pure loss*=*Gaussian noise*” has been recently applied to determine bounds on quantum capacities of more general Gaussian channels [54; 55; 56].

The probability of failure of $\mathcal{R}^{\text{AGKP}}$ gives a lower bound on $F_{\mathcal{E}}^{\text{AGKP}}$, which in turn bounds $F_{\mathcal{E}}(\texttt{gkp})$ (see Sec. VII.2). The bound contains an essential singularity at $\gamma=0$,

$F_{\mathcal{E}}(\texttt{gkp})>1-\exp\left(-\frac{\pi}{4c}\frac{1-\gamma}{\gamma}\right)\,,$ (2.2)

where $c$ is a constant determined by the lattice used to construct the code. This exponential suppression of infidelity explains the non-trivial scaling of gkp codes at small $\gamma$ and accounts for their breakaway performance at higher $\gamma$. Due to the non-analyticity, having different lattices becomes important for $\gamma\ll 1$, where gkp outperforms gkps by an order of magnitude [see Table 1(c)].

## III The hashing bound of $\mathcal{E}$

Since channel fidelity provides a measure for entanglement preservation, it is also of interest to examine these results from an information-theoretic perspective. The question we aim to answer in this section is:

What is the achievable communication rate of $\mathcal{E}$?

As with the $F_{\mathcal{E}}$, this question also pre-supposes caveats ① and ② from Sec. II. In other words, we assume recovery operations $\mathcal{R}$ can be done perfectly and organize the codes by mean occupation number $\bar{n}_{\texttt{code}}$, ignoring their “size” in terms of the number of Fock states necessary to express the logical states.

The quantum communication rate of $\mathcal{E}=\mathcal{S}^{-1}_{\texttt{code}}\mathcal{R}\mathcal{N}_{\gamma}\mathcal{S}_{\texttt{code}}$ (1.7) is ultimately limited by its most destructive link — the pure-loss channel $\mathcal{N}_{\gamma}$ (1.4). Given an energy constraint of maximum $\bar{n}$, the quantum capacity of $\mathcal{N}_{\gamma}$ is given by { [57], Thm. 8; see also [58], Eq. (12), and [59]}

$Q_{\bar{n}}=\max\left\{0,g\left((1-\gamma)\bar{n}\right)-g\left(\gamma\bar{n}\right)\right\}\,,$ (3.1)

where $g\left(\bar{n}\right)=\left(\bar{n}+1\right)\log_{2}\left(\bar{n}+1\right)-\bar{n}\log_{2}\bar{n}$ is the von Neumann entropy of a thermal state with $\bar{n}$. Note that in the limit of $\bar{n}\to\infty$, this capacity approaches the unconstrained quantum capacity

$Q_{\infty}=\max\left\{0,\log_{2}\left(\frac{1-\gamma}{\gamma}\right)\right\}\,.$ (3.2)

---

![img-8.jpeg](images/img-8.jpeg)

![img-9.jpeg](images/img-9.jpeg)

![img-10.jpeg](images/img-10.jpeg)
Figure 3: Hashing bound $D_{\mathcal{E}}$ (11) of the codes which optimize $F_{\mathcal{E}}$ for a given $\gamma$ and given constraints $\bar{n}_{\texttt{code}}\leq 2$ (a), $5$ (b), or $10$ (c). The boundary of the gray region is $Q_{\bar{n}=2,5,10}$ (12), the capacity of $\mathcal{N}_{\gamma}$ given the energy constraint of $\bar{n}$. The gray line is the unconstrained capacity $Q_{\bar{n}\to\infty}$ (13). The thin dotted diagonal line is $D_{\mathcal{E}}$ for the single-rail encoding, which has the highest $D_{\mathcal{E}}$ at large $\gamma$. Recall that cat/bin codes include the single-rail encoding [i.e., this encoding is also $\texttt{cat}(\alpha=S=0)$ and $\texttt{bin}(N=S=0)$], so bin/cat eventually jump to match the dotted line. We also show $D_{\mathcal{E}}$ for the four-qubit 1eung code (14) vs. qubit amplitude damping (i.e., the pure-loss channel restricted to the first two Fock states of four modes). There are no num codes with $\bar{n}_{\texttt{num}}\geq 5$, so red curves in (b) and (c) are identical.

We see how close the codes giving the best $F_{\mathcal{E}}$ (see Fig. 2) come to $Q_{\bar{n}}$ for $\bar{n}\leq 2,5,10$ by calculating a lower bound on the capacity of $\mathcal{E}$ for each $\gamma$ and each code listed in Table 4. The lower bound we use is known as the *hashing bound* $D_{\mathcal{E}}$ of $\mathcal{E}$ [62] — the (reverse^{2} [63]) coherent quantum information of $\mathcal{E}$’s Choi matrix $\rho_{\mathcal{E}}$ (9), where $|\Psi\rangle=(|0_{\mathsf{A}}0_{\mathsf{B}}\rangle+|1_{\mathsf{A}}1_{\mathsf{B}}\rangle)/\sqrt{2}$ is a maximally entangled state of $\mathsf{A}$ and $\mathsf{B}$ in an arbitrary basis:

$D_{\mathcal{E}}\equiv H(\operatorname{Tr}_{\mathsf{B}}\{\rho_{\mathcal{E}}\})-H(\rho_{\mathcal{E}})\,,$ (14)

where $H(\rho)=-\operatorname{Tr}\{\rho\log_{2}\rho\}$. This one-shot (i.e., with one application of the channel) coherent information of $\rho_{\mathcal{E}}$ provides an achievable rate of quantum communication and entanglement distillation, assuming many copies of $\mathcal{E}$ are available ( [63; 64; 65]; see also Corr. 21.2.1 and Thm. 23.9.1 in [62]). Therefore, $D_{\mathcal{E}}$ *does not* supply an achievable rate of any one oscillator code, but instead gives an achievable rate of concatenation schemes of the oscillator code with other (outer) codes with the restriction that $\mathcal{R}$ is used as the recovery for the (inner) oscillator code.

The first term in $D_{\mathcal{E}}$ can be simplified to yield an expression only in terms of $\mathcal{E}$,

$D_{\mathcal{E}}=H\left(\left\{\tfrac{1}{2}\pm\tfrac{1}{2}\sqrt{\tfrac{1}{2}\|\mathcal{E}(I_{\mathsf{A}})\|^{2}-1}\right\}\right)-H(\rho_{\mathcal{E}})\,,$ (15)

where $H\left(\{x\}\right)=-\sum_{x}x\log_{2}x$ for a set of variables $\{x\}$, $\|O\|^{2}\equiv\operatorname{Tr}\{O^{\dagger}O\}$ is the Frobenius norm of an operator $O$, and $I_{\mathsf{A}}$ is the qubit identity. Derivation of the first term was done by determining the reduced qubit density matrix $\operatorname{Tr}_{\mathsf{B}}\{\rho_{\mathcal{E}}\}$ in terms $\mathcal{E}$’s matrix representation (8) and then diagonalizing to yield the two eigenvalues in the term’s argument. Note that this term is maximized when $\mathcal{E}$ is unital $[\mathcal{E}(I_{\mathsf{A}})=I_{\mathsf{A}}]$. The second term — the von Neumann entropy of the Choi matrix $\rho_{\mathcal{E}}$ — increases with the minimal number of Kraus operators needed to express $\mathcal{E}$ and is zero when $\mathcal{E}$ is a unitary channel.

Incidentally, the analytical formula for $D_{\mathcal{E}}$ provides an easily calculable lower bound on the quantum capacity $Q_{\mathcal{E}}$ of any qubit channel $\mathcal{E}$. It turns out that $D_{\mathcal{E}}$ is quite close to $Q_{\mathcal{E}}$ for a family of two-Kraus operator qubit channels { [66], Eq. (5)} which includes the dephasing and amplitude damping channel: we have checked numerically that the difference $Q_{\mathcal{E}}-D_{\mathcal{E}}&lt;0.005$.

### III.1 Hashing bound for codes giving optimal $F_{\mathcal{E}}$

In Fig. 3, we plot the hashing bound $D_{\mathcal{E}}$ for all of the codes which produce the optimal channel fidelity $F_{\mathcal{E}}$ in Fig. 2 for the three energy constraints $\bar{n}_{\texttt{code}}\leq 2,5,10$. In other words, this plot is not an optimization of $D_{\mathcal{E}}$ over all codes, but merely a plot of $D_{\mathcal{E}}$ for the codes which give optimal $F_{\mathcal{E}}$. Recall that $D_{\mathcal{E}}$ is a lower bound on the entanglement that is theoretically distillable from using unlimited instances of $\mathcal{E}$ and one-way classical communication from $\mathsf{B}$ to $\mathsf{A}$. By contrast, $F_{\mathcal{E}}$ is an overlap which gauges how well entanglement was transmitted over just one instance of $\mathcal{E}$. While $F_{\mathcal{E}}$ bounds one of the terms in $D_{\mathcal{E}}$ [see Eq. (10)] and the two yield a similar order of performance of the codes, there is no guarantee that codes giving the optimal value of $F_{\mathcal{E}}$ should also give *optimal* values for $D_{\mathcal{E}}$. In other words, even if $F_{\mathcal{E}}(\texttt{one})&gt;F_{\mathcal{E}}(\texttt{two})$ given two codes one and two, there could still exist an entanglement distillation scheme

---

which extracts more entanglement from the unlimited instances of $\mathcal{E}$ from code two. This is true for our codes at large $\gamma$. Let us for example consider $\bar{n}\leq 10$. At around $\gamma\approx 0.37$, all of the codes begin to have a lower $D_{\mathcal{E}}$ than the single-rail $\{|0\rangle,|1\rangle\}$ Fock state encoding [thin black line in Fig. 3(c)]. By contrast, the point at which the codes begin to have a lower $F_{\mathcal{E}}$ than the single-rail encoding is $\gamma\approx 0.42$ [see Fig. 2(c)]. The cat/bin codes include this encoding [i.e., single-rail is also $\texttt{cat}(\alpha=S=0)$ and $\texttt{bin}(N=S=0)$], so we can say for certain that the cat/bin codes which optimize $F_{\mathcal{E}}$ are not those which optimize $D_{\mathcal{E}}$ at $0.37\leq\gamma\leq 0.42$.

For $\gamma\lesssim 0.3$, we once again see similar behavior of the codes (relative to each other) as with $F_{\mathcal{E}}$. For $\bar{n}_{\texttt{code}}\leq 10$, gkp codes break from the pack and bridge the gap with $Q_{\bar{n}}$ most rapidly. For example, at the high loss rate $\gamma=0.3$, $D_{\mathcal{E}}[\texttt{gkp}(\bar{n}\leq 10)]\approx 0.63$ bits is about twice that of the naive Fock state code. Moreover, $D_{\mathcal{E}}[\texttt{gkp}(\bar{n})]$ approaches roughly $\frac{1}{2}Q_{\bar{n}}$ for large $\gamma$. In addition, bin codes exhibit better performance with increasing $\bar{n}$ in the $\gamma\lesssim 0.2$ range. This begs the question of how close $D_{\mathcal{E}}$ for gkp and bin comes to $Q_{\bar{n}}$ when one encodes more than a qubit’s worth of information and when one utilizes two- or higher-mode generalizations of the codes. Such a question is outside the scope of this work, but is being investigated for a subsequent publication.

Since the pure-loss bosonic channel reduces to qubit amplitude damping when restricted to the Fock states $|0\rangle$ and $|1\rangle$, one interesting question to ask is whether the $\bar{n}_{\texttt{code}}$ photons, which so far are concentrated in one mode, will produce a better rate when distributed the first two Fock states of multiple modes. While comparing single-mode codes to the various discrete-variable codes specialized to protect against qubit amplitude damping (e.g., *[37, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]*) is outside the scope of this work, we do provide a reference $D_{\mathcal{E}}$ for one specialized code — the four-qubit leung code *[37]* — that is the smallest known discrete-variable code to protect against one amplitude damping error. Each of the four physical qubits in the leung code,

$|\pm_{\texttt{leung}}\rangle=\frac{1}{2}\left(|00\rangle\pm|11\rangle\right)^{\otimes 2}\,,$ (3.5)

correspond to the first two Fock states of four oscillators. We can then apply $\mathcal{N}_{\gamma}^{\otimes 4}$ (which reduces to amplitude damping within the $|0\rangle,|1\rangle$ Fock state subspace), optimize $F_{\mathcal{E}}$ to yield $\mathcal{E}$, and calculate $D_{\mathcal{E}}$ via the same procedure as with the rest of the codes. A simple calculation yields a total occupation number of $\bar{n}_{\texttt{leung}}=2$ photons, which in this case are distributed over the first two Fock states of four modes. The leung code performs similar to the cat/bin/num($\bar{n}\leq 2$) codes from Fig. 3(a), but is outperformed by the gkp($\bar{n}\leq 2$) codes for $\gamma\leq 0.35$. This suggests that, at least for intermediate $\gamma$ and all else being equal, *it is better to encode two photons in a single-mode gkp state than to spread them out over four modes*. The leung code is outperformed at almost all $\gamma$ by all codes considered with $\bar{n}_{\texttt{code}}\leq 5$, but this is not a fair comparison since those codes use more photons.

## IV Primer: the QEC matrix

In order to analyze errors for the codes, we consider the quantum error-correction (QEC) conditions *[79, 80]* (see also *[81]*, Thm. 10.1). The errors we consider are the Kraus operators $E_{\ell}$ (1.4), where $\ell$ denotes the number of photons lost after application of the error. Calculating the effect of the error $E_{\ell}^{\dagger}E_{\ell^{\prime}}$ on the codespace yields a $2\times 2$ matrix $\epsilon_{\ell\ell^{\prime}}$,

$P_{\texttt{code}}E_{\ell}^{\dagger}E_{\ell^{\prime}}P_{\texttt{code}}=\epsilon_{\ell\ell^{\prime}}^{\texttt{code}}\in\text{Mat}_{2\times 2}\,.$ (4.1)

We write $\epsilon_{\ell\ell^{\prime}}^{\texttt{code}}$ as a superposition of $P_{\texttt{code}}$ and matrices

$Z_{\texttt{code}}$ $=|0_{\texttt{code}}\rangle\langle 0_{\texttt{code}}|-|1_{\texttt{code}}\rangle\langle 1_{\texttt{code}}|$ (4.2a)
$X_{\texttt{code}}$ $=|0_{\texttt{code}}\rangle\langle 1_{\texttt{code}}|+|1_{\texttt{code}}\rangle\langle 0_{\texttt{code}}|$ (4.2b)
$Y_{\texttt{code}}$ $=|1_{\texttt{code}}\rangle\langle 0_{\texttt{code}}|-|0_{\texttt{code}}\rangle\langle 1_{\texttt{code}}|\,.$ (4.2c)

We define our matrix basis as such because both $P_{\texttt{code}}$ and $E_{\ell}$ are real for our codes, so the *QEC matrix* $\epsilon^{\texttt{code}}$ is real, symmetric, and $2N$-dimensional (with $N\to\infty$ being the dimension of the oscillator). Expanding each $2\times 2$ subblock yields

$\epsilon_{\ell\ell^{\prime}}^{\texttt{code}}=c_{\ell\ell^{\prime}}^{\texttt{code}}P_{\texttt{code}}+x_{\ell\ell^{\prime}}^{\texttt{code}}X_{\texttt{code}}+y_{\ell\ell^{\prime}}^{\texttt{code}}Y_{\texttt{code}}+z_{\ell\ell^{\prime}}^{\texttt{code}}Z_{\texttt{code}}\,,$ (4.3)

with coefficients denoted by

$[c,x,y,z]_{\ell\ell^{\prime}}^{\texttt{code}}=\frac{1}{2}\text{Tr}\left\{[P,X,Y,Z]_{\texttt{code}}E_{\ell}^{\dagger}E_{\ell^{\prime}}\right\}\,.$ (4.4)

For $E_{\ell}$ to be perfectly correctable, one must satisfy the QEC condition

$\epsilon_{\ell\ell^{\prime}}^{\texttt{code}}=c_{\ell\ell^{\prime}}^{\texttt{code}}P_{\texttt{code}}$ (4.5)

(equivalently, $\langle\mu_{\texttt{code}}|E_{\ell}^{\dagger}E_{\ell^{\prime}}|\nu_{\texttt{code}}\rangle=c_{\ell\ell^{\prime}}^{\texttt{code}}\delta_{\mu\nu}$ for $\mu,\nu\in\{0,1\}$). In words, a correctable error must act as the identity within the code subspace (equivalently, the effect of the error must be the same on both code states). Therefore, the coefficient $c_{\ell\ell^{\prime}}^{\texttt{code}}$ represents the correctable part of $\epsilon_{\ell\ell^{\prime}}^{\texttt{code}}$ while $\{x_{\ell\ell^{\prime}}^{\texttt{code}},y_{\ell\ell^{\prime}}^{\texttt{code}},z_{\ell\ell^{\prime}}^{\texttt{code}}\}$ represent various uncorrectable parts corresponding to bit, phase, and joint bit-phase flips, respectively. Since not all errors $E_{\ell}$ can be corrected, we proceed to analyze the magnitude of the uncorrectable parts — the $2N$-dimensional matrix $\epsilon_{\ell\ell^{\prime}}^{\texttt{code}}-c^{\texttt{code}}$ — with $\epsilon_{\ell\ell^{\prime}}^{\texttt{code}},c_{\ell\ell^{\prime}}^{\texttt{code}}$ being $2\times 2$ submatrices of $\epsilon^{\texttt{code}},c^{\texttt{code}}$, respectively.

The QEC matrix block $\epsilon_{\ell\ell^{\prime}}^{\texttt{code}}$ can also be interpreted (*[81]*, Fig. 10.5) as a matrix of overlaps between the two error subspaces spanned by $\{E_{\ell}|\mu_{\texttt{code}}\rangle\}_{\mu=0}^{1}$ and

---

$\{E_{\ell^{\prime}}|\mu_{\texttt{code}}\rangle\}_{\mu=0}^{1}$, i.e., the range of $E_{\ell}P_{\texttt{code}}$ and $E_{\ell^{\prime}}P_{\texttt{code}}$. We call these subspaces $E_{\ell}P_{\texttt{code}}$ and $E_{\ell^{\prime}}P_{\texttt{code}}$ for short. When no loss events are occurring, the code state undergoes the backaction-induced evolution corresponding to the subspace $E_{0}P_{\texttt{code}}$. As $\ell$ loss events occur, one’s ability to detect them hinges on the orthogonality between $E_{0}P_{\texttt{code}}$ and $E_{\ell}P_{\texttt{code}}$, the latter being the space to which a state has gone after losing $\ell$ photons. The $\epsilon_{0\ell}^{\texttt{code}}$ and $\epsilon_{\ell 0}^{\texttt{code}}$ parts of the QEC matrix thus correspond to the ability to distinguish between $\ell$ losses and no losses, making their satisfaction similar to the satisfaction of the *error-detection conditions* $\delta_{\ell}^{\texttt{code}}=P_{\texttt{code}}E_{\ell}P_{\texttt{code}}\propto P_{\texttt{code}}$ *[82]*. While the backaction in $E_{0}$ makes $\epsilon_{0\ell}^{\texttt{code}}\neq\delta_{\ell}^{\texttt{code}}$, the two converge to each other as $\gamma\to 0$. Since bin and cat codes satisfy both $\epsilon_{0\ell}^{\texttt{code}},\delta_{\ell}^{\texttt{code}}\propto P_{\texttt{code}}$ exactly up to some $\ell\leq S$, uncorrectable parts in the QEC matrix blocks $\epsilon_{0\ell}^{\texttt{code}}$ quantify how well $\ell$-photon losses can be detected for those codes.

Uncorrectable parts $\{\varrho_{\ell\ell}^{\texttt{code}},\varrho_{\ell\ell}^{\texttt{code}},\varrho_{\ell\ell}^{\texttt{code}}\}$ for “diagonal” errors $E_{\ell}^{\dagger}E_{\ell}$ represent *distortion* of the quantum information within the subspace $E_{\ell}P_{\texttt{code}}$ and limit how well one is able to correct the error $E_{\ell}$ after detection. Since our codespace can become distorted even when there are no loss events, we have to also consider backaction-induced distortion captured by $\epsilon_{00}^{\texttt{code}}$. The loss event probability distribution is governed by $c_{\ell\ell}^{\texttt{code}}$ and depends on both $\gamma$ and $\bar{n}_{\texttt{code}}$. For a fixed $\gamma$ and sufficiently large $\bar{n}_{\texttt{code}}$, we will see that $c_{\ell\ell}^{\texttt{code}}$ for cat (gkps) is a Poisson (geometric) distribution having mean $\gamma\bar{n}_{\texttt{code}}$. In such cases, we can interpret $\gamma\bar{n}_{\texttt{code}}$ as the average number of photons lost, and only when $\gamma\bar{n}_{\texttt{code}}\ll 1$ can we say that $E_{0}$ is the most likely error for a code.

## V Cat codes

Cat code logical states are coherent states projected onto subspaces of occupation number modulo $2(S+1)$:

$|\mu_{\texttt{cat}}\rangle=\frac{\Pi_{(S+1)\mu}|\alpha\rangle}{\sqrt{N_{\alpha}^{(S+1)\mu}}}\,,$ (5.1)

with $\alpha$ real (for simplicity), $\mu\in\{0,1\}$, and normalization

$N_{\alpha}^{(S+1)\mu}=\langle\alpha|\Pi_{(S+1)\mu}|\alpha\rangle\,.$ (5.2)

The projections $\{\Pi_{0},\Pi_{S+1}\}$ used to define the code states belong to the family (for $r\in\{0,1,\cdots,2S+1\}$)

$\Pi_{r}=\sum_{n=0}^{\infty}|2n(S+1)+r\rangle\langle 2n(S+1)+r|\,.$ (5.3)

In the large $\alpha$ limit, i.e., when

$2\alpha\sin\left(\frac{\pi}{S+1}\right)\gg 1\,,$ (5.4)

cat-code states become equal superpositions of coherent states $\{|{\alpha}e^{i\frac{\pi}{S+1}k}\rangle\}_{k=0}^{2(S+1)-1}$ distributed equidistantly on a circle of radius $\alpha$ in phase space. In that limit, the seemingly bothersome normalization factors approach the same constant, while when $\alpha\lesssim S$, they become distinct in order to account for the various overlaps between the coherent states. Expressing the normalization factor in terms of such overlaps (*[83]*, Eq. (3.22)), we have

$N_{\alpha}^{(S+1)\mu}=\frac{1}{2(S+1)}\sum_{s=0}^{2S+1}\,(-1)^{\mu s}\,\langle\alpha|\alpha e^{i\frac{\pi}{S+1}s}\rangle\,.$ (5.5)

Since the cat codes which produce the optimal $F_{\mathcal{E}}$ have $\alpha\lesssim S$, we have to consider the factors $N_{\alpha}^{(S+1)\mu}$ at intermediate $\alpha$ in order to explain Fig. 2.

Due to properties of coherent states and for $\alpha\neq 0$, cat logical states satisfy

$(\hat{a}/\alpha)^{2(S+1)}\,|\mu_{\texttt{cat}}\rangle=|\mu_{\texttt{cat}}\rangle\,,$ (5.6)

and $\texttt{cat}(S)$ [and $\texttt{bin}(S)$, as we shall see] can detect exactly $S$ photon loss events using the check operator

$C_{\texttt{cat}}=C_{\texttt{bin}}=\exp\left(i\frac{2\pi\hat{n}}{S+1}\right)\,.$ (5.7)

Its square root, $\exp(i\frac{\pi\hat{n}}{S+1})$, makes for a logical $Z$-operator within cat and bin code subspaces. We call this a check operator (and not a stabilizer) since it has other eigenvalues which are not modulus one and is not part of a set of commuting such operators which is used to construct the code states.

The $S=0$ cat code was proposed in Ref. *[13]* for coherent-state quantum computation *[84, 85, 86, 87]*. This code cannot detect loss events since losing a photon causes a logical bit-flip, but it of course can be concatenated with, e.g., a bit-flip code *[85]*. The $\texttt{cat}(S=1,2)$ codes were studied first in Refs. *[15, 27]*, followed by investigations into $\texttt{cat}(S\geq 2)$ and qudit extensions *[88, 89, 46]*. There are several theoretical and experimental schemes for cat state preparation *[90]*. Schemes designed to protect against loss errors *[29]* (for $S=1$) and backaction errors *[91]* (for $S=0$), respectively, were realized using microwave cavities coupled to superconducting qubits.

### V.1 A simple example

As an example of the utility of cat codes, consider the simplest non-trivial code family $\texttt{cat}(S=1)$ whose logical states are

$|\mu_{\texttt{cat}}^{S=1}\rangle=\frac{|\alpha\rangle+|-\alpha\rangle+(-1)^{\mu}\,(|i\alpha\rangle+|-i\alpha\rangle)}{4\sqrt{2[\cosh\alpha^{2}+(-1)^{\mu}\cos\alpha^{2}]}}\,.$ (5.8)

---

In the Fock basis, the above $|0_{\mathsf{cat}}\rangle$ is a superposition of Fock states $|0\rangle, |4\rangle, |8\rangle, \cdots$ while $|1_{\mathsf{cat}}\rangle$ is supported by $|2\rangle, |6\rangle, |10\rangle, \cdots$. Therefore, there are exactly $S = 1$ Fock states separating the Fock states supporting $|0_{\mathsf{cat}}\rangle$ from those supporting $|1_{\mathsf{cat}}\rangle$, so we call $S$ the spacing between logical states. Due to this spacing, $\epsilon_{01}^{\mathsf{cat}} = 0$ — one loss event is always detectable. However, such an event is not always correctable since $\epsilon_{11}^{\mathsf{cat}}$ contains uncorrectable parts at generic values of $\alpha$.

In general, $\epsilon_{\ell \ell}^{\mathrm{cat}} \neq c_{\ell \ell} P_{\mathrm{cat}}$ because of the backaction term $(1 - \gamma)^{\bar{n}/2}$ in $E_{\ell}$. We will see that uncorrectable parts in $\epsilon_{\ell \ell}^{\mathrm{cat}}$ are well-suppressed as $\alpha \to \infty$, but in that limit the code consists of large-amplitude coherent states and there is a high chance of losing more than one photon (i.e., uncorrectable parts in $\epsilon_{02}^{\mathrm{cat}}$ become very large). Therefore, for more general codes with a given spacing $S$ and loss rate $\gamma$, there is an optimal or "sweet spot" value $\alpha = \alpha_{\star}(\gamma)$ that balances the backaction with the loss errors. This is exactly what we see in Figs. 4(a-c), where $F_{\mathcal{E}}$ is plotted vs $\bar{n}_{\mathrm{cat}}$ for various $\mathrm{cat}(S)$ and at a fixed $\gamma$. We can see that $F_{\mathcal{E}}[\mathrm{cat}(S)]$ is maximized at certain $\bar{n}_{\mathrm{cat}}$ [which in turn corresponds to a certain $\alpha_{\star}(\gamma)$] and decays with sufficiently large $\alpha$. Note that there can be multiple $\alpha_{\star}$ for a given $S$. By contrast, gkps code fidelities increase monotonically with $\bar{n}_{\mathrm{gkps}}$.

We now show how the sweet spot can be analytically determined for $\mathrm{cat}(S = 1)$ and in the limit $\gamma \to 0$, discussing general $\gamma$ in the next subsection. Recalling the form of the Kraus operators (1.5) for small $\gamma$, to suppress distortion due to backaction, one has to make sure that both code states have the same occupation number:

$$
\delta \bar {n} _ {\mathrm {c a t}} = \frac {1}{2} \operatorname {T r} \left\{Z _ {\mathrm {c a t}} \hat {n} \right\} = 0. \tag {5.9}
$$

While $\delta \hat{n}_{\mathrm{cat}} \to 0$ as $\alpha \to \infty$, there are certain fine-tuned $\alpha$ at which the occupation numbers of the two logical states also coincide due to the oscillatory nature of the normalization factors $N_{\alpha}$ (5.5). Solving the above equation using $|\mu_{\mathrm{cat}}^{S=1}\rangle$ (5.8) yields the transcendental equation

$$
\tan \alpha^ {2} = - \tanh  \alpha^ {2}, \tag {5.10}
$$

whose solution is $\alpha_{\star}(\gamma \to 0) \approx 1.538$ (corresponding to $\bar{n}_{\mathrm{code}} \approx 2.324$). Thus, in the small $\gamma$ limit and at this fine-tuned $\alpha_{\star}$, a single loss event is both detectable and correctable. This was about the value used in a recent cat-code error-correction experiment [29].

## B. QEC matrix for cat codes

Let us briefly elaborate on the discussion regarding sweet spots using the QEC matrix for cat codes for finite (but still small) $\gamma$. Due to the spacing of the codes, QEC matrix subblocks $\epsilon_{\ell \ell'}$ (4.1) contain uncorrectable parts only for certain values of $\ell, \ell'$. Let us first study the distortion due to errors $\epsilon_{\ell \ell'}^{\mathrm{cat}}$, which we can easily calculate [46, 92] by using the representation (5.1) of the cat states,

![img-11.jpeg](images/img-11.jpeg)

![img-12.jpeg](images/img-12.jpeg)

![img-13.jpeg](images/img-13.jpeg)
Figure 4. Channel fidelity $F_{\mathcal{E}}(\gamma = 0.095)$ (1.11) vs. mean occupation number $\bar{n}$ (2.1) for cat and bin at spacing (a) $S = 3$ and (b) $S = 4$. Note that cat(S) depends continuously on $\bar{n}$ and bin exists only at discrete values. For a given $S$, cat codes perform best at specific $\bar{n}$, corresponding to "sweet-spot" values of $\alpha = \alpha_{\star}$. However, due to the oscillatory nature of the errors in cat $(S \geq 3)$, the codes also develop troughs in $F_{\mathcal{E}}$. On the other hand, bin(S) performs similar to cat(S) at small and large $\bar{n}$ but does not suffer from troughs at intermediate $\bar{n}$. (c) Plots of cat and bin for $S \in \{1, 2, 3, 4, 5\}$ along with gkps, which turns out to outperform both cat and bin and increase monotonically with $\bar{n}$. Similar trends are observed for smaller $\gamma$.

observing that $\Pi_r\hat{a} = \hat{a}\Pi_{r + 1}$, and using Eq. (D1a):

$$
\epsilon_ {\ell \ell} ^ {\mathrm {c a t}} = \frac {(\gamma \alpha^ {2}) ^ {\ell} e ^ {- \gamma \alpha^ {2}}}{\ell !} \left( \begin{array}{c c} \frac {N _ {\alpha \sqrt {1 - \gamma}} ^ {- \ell}}{N _ {\alpha} ^ {0}} &amp; 0 \\ 0 &amp; \frac {N _ {\alpha \sqrt {1 - \gamma}} ^ {S + 1 - \ell}}{N _ {\alpha} ^ {S + 1}} \end{array} \right), \tag {5.11}
$$

where $N_{\alpha \sqrt{1 - \gamma}}$ are damped versions of the normalization factors in Eq. (5.5). Expansion yields the correctable part (4.4),

$$
c _ {\ell \ell} ^ {\mathrm {c a t}} \equiv \frac {1}{2} \frac {(\gamma \alpha^ {2}) ^ {\ell} e ^ {- \gamma \alpha^ {2}}}{\ell !} \left(\frac {N _ {\alpha \sqrt {1 - \gamma}} ^ {- \ell}}{N _ {\alpha} ^ {0}} + \frac {N _ {\alpha \sqrt {1 - \gamma}} ^ {S + 1 - \ell}}{N _ {\alpha} ^ {S + 1}}\right), \tag {5.12}
$$

and only one uncorrectable part (4.4),

$$
z _ {\ell \ell} ^ {\mathrm {c a t}} \equiv \frac {1}{2} \frac {(\gamma \alpha^ {2}) ^ {\ell} e ^ {- \gamma \alpha^ {2}}}{\ell !} \left(\frac {N _ {\alpha \sqrt {1 - \gamma}} ^ {- \ell}}{N _ {\alpha} ^ {0}} - \frac {N _ {\alpha \sqrt {1 - \gamma}} ^ {S + 1 - \ell}}{N _ {\alpha} ^ {S + 1}}\right). \tag {5.13}
$$

The correctable part represents the probability of losing $\ell$ photons. This distribution is Poisson in the large $\alpha$ limit, in which the ratios of normalization factors inside the parentheses both go to one exponentially with $-(1 - \gamma)\alpha^2$.

---

The uncorrectable part $z_{\ell\ell}^{\mathsf{cat}}$ represents the inability to correct against $\ell$ loss events. It is suppressed as $\alpha\to\infty$, but is also zero at certain “sweet-spots” $\alpha_{\star}$, which we discuss using another example.

Consider $\mathsf{cat}(S=2)$ for $\gamma\leq 0.0124$ and $\bar{n}_{\mathsf{cat}}\leq 5$. This is a case when $\gamma\bar{n}\ll 1$ and so we only have to consider distortion due to backaction $\epsilon^{\mathsf{cat}}_{00}$. We see from Table 4 that the $\mathsf{cat}$ code which achieves the highest $F_{\mathcal{E}}$ out of all $\mathsf{cat}$ codes with $\bar{n}\leq 5$ is $\mathsf{cat}(\alpha=1.739,S=2)$. This is exactly the sweet spot at which the distortion $z^{\mathsf{cat}}_{00}$ is approximately zero: $\alpha_{\star}(\gamma=0.005)\approx 1.739$. More generally, $\alpha_{\star}(\gamma)$ at which $z^{\mathsf{cat}}_{00}\approx 0$ decreases as $\gamma\to 0$ to the value $\alpha_{\star}(\gamma=0)\approx 1.737$. [The reason that $\mathsf{cat}(\alpha=1.739)$ and not $\mathsf{cat}(\alpha=1.737)$ is the optimal code at $\gamma<0.005$ is because the resolution in our sampling of $\alpha$ is not sufficient to resolve the difference.] As mentioned in our discussion of $\mathsf{cat}(S=1)$ in the previous subsection, in the limit $\gamma\to 0$, $z^{\mathsf{cat}}_{00}$ becomes proportional to

$\delta\bar{n}_{\mathsf{cat}}=\frac{1}{2}\mathrm{Tr}\{Z_{\mathsf{cat}}\hat{n}\}=\frac{\alpha^{2}}{2}\left(\frac{N_{\alpha}^{-1}}{N_{\alpha}^{0}}-\frac{N_{\alpha}^{S}}{N_{\alpha}^{S+1}}\right)\,.$ (5.14)

This $\delta\bar{n}_{\mathsf{cat}}$ tells us how well we are able to correct against distortion due to no loss events, the dominant error when $\gamma\bar{n}_{\mathsf{cat}}\ll 1$. It is zero at exactly the “sweet spot” $\alpha_{\star}(\gamma=0)$, and we can similarly relate $\alpha_{\star}$ to $\delta\bar{n}_{\mathsf{cat}}$ for $\mathsf{cat}$ at other values of $S$. Having only covered $\mathsf{cat}(S=2)$, we refer the reader to Ref. *[46]* for such calculations.

We have seen that at $\alpha<S$, backaction-induced errors are not suppressed due to $\alpha$ not being sufficiently large [see Eq. (5.4)]. So why are $\mathsf{cat}$ codes with high values of $\alpha$ not optimal? This is because for $\alpha\approx S$, the fraction $\gamma\bar{n}_{\mathsf{cat}}\approx\gamma\alpha^{2}$ of photons lost yields a large probability of losing $S+1$ photons, an uncorrectable error. More technically, recall that due to spacing $S$, the effect of $\ell\leq S$ loss events is zero, $\epsilon^{\mathsf{cat}}_{0\ell}=0$. However, the first uncorrectable loss at $\ell=S+1$ produces an error that scales unfavorably with $\alpha$, prohibiting $\alpha$ from getting too large. A calculation yields

$\epsilon^{\mathsf{cat}}_{0,S+1}=\frac{(\gamma\alpha^{2})^{\frac{S+1}{2}}e^{-\gamma\alpha^{2}}}{\sqrt{(S+1)!N_{\alpha}^{0}N_{\alpha}^{S+1}}}\begin{pmatrix}0&N_{\alpha}^{0}\sqrt{1-\gamma}\cr N_{\alpha\sqrt{1-\gamma}}^{S+1}&0\end{pmatrix}\,.$ (5.15)

Once again, the ratios of normalization factors go to one as $\alpha\to\infty$. In that limit, this error becomes proportional to a pure bit flip, $\epsilon^{\mathsf{cat}}_{0,S+1}\sim x^{\mathsf{cat}}_{0,S+1}X_{\mathsf{cat}}$ (where we use the mathematician’s definition of “$\sim$”), with

$x^{\mathsf{cat}}_{0,S+1}\sim\sqrt{c^{\mathsf{cat}}_{00}c^{\mathsf{cat}}_{S+1,S+1}}$ (5.16)

independently of $\gamma$. In other words, given even a very small $\gamma$, the above equation is still satisfied for a sufficiently large $\alpha$. We claim that this is the worst possible scaling, making such errors completely undetectable (and therefore uncorrectable). Recall that since the QEC matrix (4.1) is positive semidefinite ($\epsilon\geq 0$), in the absence of other errors for a given $\ell,\ell^{\prime}$, all bit-flip errors are bounded by $x_{\ell\ell^{\prime}}\leq\sqrt{c_{\ell\ell}c_{\ell^{\prime}\ell^{\prime}}}$. Ideally we would like to have no error ($x_{\ell\ell^{\prime}}=0$), and in the worst case the inequality is saturated ($x_{\ell\ell^{\prime}}=\sqrt{c_{\ell\ell}c_{\ell^{\prime}\ell^{\prime}}}$). In Eq. (5.16), we see that the inequality is saturated as $\alpha\to\infty$. Because the code states are eigenstates of $\hat{a}^{2(S+1)}$, the behavior upon $0$ to $2(S+1)-1$ losses repeats itself after $2(S+1)$ losses. More generally, a bit flip error of similar intensity occurs at any $\ell-\ell^{\prime}=S+1$ modulo $2(S+1)$. Thus, as $\alpha\to\infty$, the QEC matrix $\epsilon$ develops sparse but large bit-flip error entries at each such $\ell,\ell^{\prime}$, implying a large probability of undetectable errors. Therefore, $\mathsf{cat}$ codes should work best for values of $\alpha$ at which the probability of losing $\ell=S+1$ photons is small.

The reader should by now see that, for a given $\gamma$ and $S$, a $\mathsf{cat}$ code performs optimally at specific $\alpha_{\star}(\gamma)$. But how does one determine the optimal $S$? We do not claim to answer this question fully, only noting that (A) the optimal $S$ depends on $\gamma$ and (B) our energy constraints limit the selection of $\alpha_{\star}$ to choose from, which in turn limit the selection of $S$. For an example of (A), notice in Fig. 4(c) that $\bar{n}_{\mathsf{cat}}(\alpha_{\star},S=1)<2$ while $\bar{n}_{\mathsf{cat}}(\alpha_{\star},S>1)>2$, so the highest spacing achievable with a sweet-spot is $S=1$. Similarly for (B), for $\bar{n}_{\mathsf{cat}}\leq 5$, there are three available $\alpha_{\star}$, one for each $S=1,2,3$. At $\gamma=0.095$, the $F_{\mathcal{E}}$ is highest for $S=3$ [as shown in Fig. 4(c)] while at smaller $\gamma$, $S=2$ is optimal (see Table 4). In summary, $\mathsf{cat}$ codes cannot perform well at sufficiently large $\alpha$ and instead are optimal for specific values of $\alpha_{\star}\lesssim S$.

## VI Binomial codes

In terms of Fock states, the logical states (defined here in the $X_{\mathsf{bin}}$-basis *[23]*) are

$|\mu_{\mathsf{bin}}\rangle=\frac{1}{\sqrt{2^{N+1}}}\sum_{m=0}^{N+1}(-1)^{\mu m}\sqrt{\binom{N+1}{m}}|\,(S+1)\,m\rangle\,.$ (6.1)

Their mean occupation number (2.1) is

$\bar{n}_{\mathsf{bin}}=\frac{1}{2}\,(N+1)\,(S+1)\ .$ (6.2)

The non-negative integer $N$ governs the order in $\gamma$ to which dephasing errors $\{\hat{n}^{n}\}_{n=0}^{N}$ can be corrected exactly and is similar to $\alpha$ in $\mathsf{cat}$ codes. The spacing $S$ is the same as that of $\mathsf{cat}$ codes since $\mathsf{bin}(S)$ and $\mathsf{cat}(S)$ are spanned by the same Fock states. Therefore, the ability for $\mathsf{bin}(S)$ to perfectly detect $\ell\leq S$ loss events using the check operator (5.7) is identical to that of $\mathsf{cat}(S)$: $\epsilon^{\mathsf{bin}}_{0\ell}=P_{\mathsf{bin}}E_{0}^{\dagger}E_{\ell}P_{\mathsf{bin}}=0$ in the language of the QEC matrix (4.1). The difference lies in the other parameter $N$, the discrete analogue of $\alpha$ for $\mathsf{cat}$. Recall that for $\mathsf{cat}(S)$, the limit $\alpha\to\infty$ exponentially suppresses all uncorrectable parts in $\epsilon^{\mathsf{cat}}_{\ell\ell}$ for all $\ell$. Similarly, in $\mathsf{bin}(S)$, tuning $N$ allows one to suppress distortion due to loss events up to a given order $O(\gamma^{N})$. Therefore, it should be no surprise that for a fixed $S$,

$\mathsf{bin}(N\to\infty,S)\,\sim\,\mathsf{cat}(\alpha\to\infty,S)\,.$ (6.3)

---

![img-14.jpeg](images/img-14.jpeg)
(a) $\operatorname{cat}(\alpha = \sqrt{5.525}, S = 3)$

![img-15.jpeg](images/img-15.jpeg)
(b) $\mathrm{bin}(N = 2, S = 3)$

![img-16.jpeg](images/img-16.jpeg)
(c) $\mathrm{gkps}(\Delta = 0.283)$

![img-17.jpeg](images/img-17.jpeg)
(d) $\mathrm{gkp}(\Delta = 0.283, a = \sqrt{3})$

Figure 5. Uncorrectable parts of the QEC matrices, $\epsilon^{\mathrm{code}} - \epsilon^{\mathrm{code}}$ (see Sec. IV), for code being (a) cat (5.1), (b) bin (6.1), (c) gkps (7.8), and (d) gkp (B4) with parameters such that $\bar{n}_{\mathrm{code}} \approx 6$ for all codes and given $\gamma = 0.095$. Recall that $\epsilon^{\mathrm{code}}$ is a block matrix consisting of $2 \times 2$ matrices $\epsilon_{\ell \ell'}^{\mathrm{code}}$ that quantify the overlap between error subspaces $E_{\ell}P_{\mathrm{code}}$ and $E_{\ell'}P_{\mathrm{code}}$. These $2 \times 2$ matrices are delineated by dotted lines. The four entries in $\epsilon_{\ell \ell'}^{\mathrm{code}}$ are presented as colored squares; note that $\epsilon_{\ell \ell'}^{\mathrm{code}}$ has no imaginary part (all $E_{\ell}P_{\mathrm{code}}$ are real). From Fig. 4(c), we see that $F_{\mathcal{E}}(\mathrm{cat}) &lt; F_{\mathcal{E}}(\mathrm{bin}) &lt; F_{\mathcal{E}}(\mathrm{gkps})$ at $\bar{n}_{\mathrm{code}} \approx 6$, and the above QEC plots nicely corroborate that order of performance. Since cat and bin have spacing $S = 3$, there are no off-diagonal errors for $\ell \leq 3$ (inside the red square). However, both codes suffer from distortion on the diagonal portions of $\epsilon_{\ell \ell'}^{\mathrm{code}}$, with bin suffering noticeably less at this particular $\gamma$. On the other hand, gkps (square lattice) and gkp (shifted hexagonal lattice) barely suffer from any noticeable errors. Since gkps codes have spacing $S = 1$ due to a symmetry of their underlying lattice, $\epsilon_{\ell \ell'}$ does not contain off-diagonal errors for $\ell \leq 1$ (more generally, for $\ell - \ell'$ odd). Shifted gkp codes do not have that symmetry, but perform comparably.

While the two codes coincide in this limit, the advantage of bin codes is that, unlike cat, the suppression of distortion in $\epsilon_{\ell \ell}^{\mathrm{bin}}$ occurs without oscillations. While the oscillatory nature of the normalization factors in $\epsilon_{\ell \ell}^{\mathrm{cat}(S)}$ (5.11) allows for peaks as well as troughs in $F_{\mathcal{E}}$ vs. $\bar{n}$ [shown in Figs. 4(a-c)], there are no such oscillations in $\epsilon_{\ell \ell}^{\mathrm{bin}(S)}$. Note that this difference only shows up at $S \gtrsim 3$ since only then are there significant oscillations in $F_{\mathcal{E}}(\mathrm{cat})$. While cat and bin perform about the same at smaller $S$, there is an intermediate $\bar{n}$ regime for larger $S$ at which cat underperforms (due to being at a trough between two sweet spots $\alpha_{\star}$) while bin continues to improve. For example, observe the difference between cat and bin at $S = 3$ in Fig. 4(a): $F_{\mathcal{E}}(\mathrm{bin}) \approx F_{\mathcal{E}}(\mathrm{cat})$ for all $\bar{n} \leq 15$ except at $\bar{n} \approx 6$.

In Sec. VIA, we delve into the performance of bin codes from Figs. 2 and 4. In Sec. VIB, we comment on their performance with no energy constraints. Switching gears in Sec. VIC, we study their structure. We show that qubit bin codes are spin-coherent states embedded into the $\{|(S + 1)m\rangle\}_{m = 0}^{N + 1}$ subspace of the oscillator. In an alternative characterization in Appx. C, we link bin codes to discrete-variable bit-flip codes. These formulations extend to other sets of codes, summarized in Table 7(a), and allow one to construct bin check operators for dephasing errors. In Sec. VID, we introduce a scheme to detect and correct errors in bin using the check operators from before.

## A. QEC matrix for binomial codes

Let us fix $S$ and compare $\mathrm{bin}(S)$ to $\mathrm{cat}(S)$. A $\mathrm{bin}(N, S)$ code protects against loss errors $\hat{a}^{\ell \leq S}$ (due to spacing $S$) and dephasing errors $\hat{n}^{n \leq N}$ (due to the nature of the binomial distribution). Since loss operators $E_{\ell}$ (1.4) consist of superpositions of the two errors, we can readily read off the leading order in $\gamma$ for which there are uncorrectable parts in $\epsilon_{0\ell}^{\mathrm{bin}} - O(\gamma^{S + 1})$ — and distortion matrices $\epsilon_{\ell \ell}^{\mathrm{bin}} - O(\gamma^{N + 1})$. However, that is not the whole story.

We know that both bin and cat suppress all distortion errors $z_{\ell \ell}$ with increasing $\bar{n}$. The backaction distortion $z_{\ell \ell}^{\mathrm{bin}}$ does not oscillate with $\bar{n}$ (as opposed to $z_{\ell \ell}^{\mathrm{cat}}$ oscillation with $\alpha$) and yields a quicker suppression of errors than $z_{\ell \ell}^{\mathrm{cat}}$. We use the basis of positive/negative superpositions $|\pm_{\mathrm{bin}}\rangle$ of the bin states (6.1) to calculate it,

$$
P _ {\mathrm {b i n}} = \left| + _ {\mathrm {b i n}} \right\rangle \left\langle + _ {\mathrm {b i n}} \right| + \left| - _ {\mathrm {b i n}} \right\rangle \left\langle - _ {\mathrm {b i n}} \right|, \tag {6.4}
$$

in order to have the backaction-induced errors be along the $z$-axis and match $z_{\ell \ell}^{\mathrm{cat}}$. Note that this amounts to the $Z_{\mathrm{bin}}$-basis of the original paper [23]. The respective probabilities of no loss and backaction distortion can be concisely expressed,

$$
c _ {\ell \ell} ^ {\mathrm {b i n}} = \frac {\gamma^ {\ell}}{\ell !} \frac {d ^ {\ell}}{d x ^ {\ell}} \left(\frac {1 + x ^ {S + 1}}{2}\right) ^ {N + 1} \Bigg | _ {x = 1 - \gamma} \tag {6.5a}
$$

$$
z _ {\ell \ell} ^ {\mathrm {b i n}} = \frac {\gamma^ {\ell}}{\ell !} \frac {d ^ {\ell}}{d x ^ {\ell}} \left(\frac {1 - x ^ {S + 1}}{2}\right) ^ {N + 1} \Bigg | _ {x = 1 - \gamma}. \tag {6.5b}
$$

For $\ell = 0$, the above should be compared to $c_{00}^{\mathrm{cat}}$ (5.12) and $z_{00}^{\mathrm{cat}}$ (5.13). Clearly, $z_{00}^{\mathrm{bin}}$ does not oscillate vs. $N$.

---

While the above is still difficult to analyze analytically for $\ell&gt;0$, we see numerically that there are no oscillations in $\bar{n}$ of the fidelity of $\mathbf{bin}(S)$, leading to certain regimes of $\bar{n}$ at which bin outperforms cat for a given $\gamma$. Heuristically, as $\bar{n}\to\infty$, $z_{\ell\ell}^{\mathbf{bin}(S)}\to 0$ order-by-order in $\gamma$ while $z_{\ell\ell}^{\mathbf{cat}(S)}\to 0$ as a damped oscillating function with damping coefficient $(1-\gamma)\alpha^{2}$. The latter limit turns out to be less controlled, leading to detrimental oscillations in $F_{\mathcal{E}}^{\mathbf{cat}(S)}$. For example, we plot the uncorrectable parts of $\epsilon_{\ell\ell^{\prime}}^{\mathbf{cat}}$ and $\epsilon_{\ell\ell^{\prime}}^{\mathbf{bin}}$ for $\gamma=0.095$, $\bar{n}_{\mathrm{code}}\approx 6$, and $S=3$ in Fig. 5(a) and (b), respectively. While the uncorrectable parts $x_{0\ell}^{\mathbf{bin}}$, $x_{0\ell}^{\mathbf{cat}}$ are comparable in magnitude, one can see that $z_{\ell\ell}^{\mathbf{bin}}$ is visibly less than $z_{\ell\ell}^{\mathbf{cat}}$. However, this effect is most prominent only when $E_{0}$ is the only dominant error ($\gamma\bar{n}_{\mathrm{code}}\ll 1$) and when cat oscillations begin to have a detrimental effect ($S\gtrsim 3$ and $\bar{n}_{\mathrm{code}}\geq 5$). Inside those regimes, we can see that bin breaks away from cat [see Figs. 4(a-c) and insets in Figs. 2(b,c)] while outside of those regions, the two codes perform quite similarly.

Another advantage of bin codes manifests itself at large $\bar{n}_{\mathrm{bin}}$. Studying $x_{0,\ell}^{\mathrm{bin}}$ and $y_{0,\ell}^{\mathrm{bin}}$ is quite difficult, so we explain the advantage by studying subspaces that are mapped to under errors. For cat codes, the undetectable error $\hat{a}^{S+1}$ maps the code exactly to the code subspace, $\hat{a}^{S+1}P_{\mathrm{cat}}\propto P_{\mathrm{cat}}$. For bin codes, the mapping is to a subspace that has a component orthogonal to the code space. Quantum information in this component (which may only be one-dimensional) can then be mapped back to the code space, yielding an extra layer of approximate error correction. The same is true for $\ell&gt;S+1$ as long as $N$ is sufficiently high. We consider two examples of this effect, one known and one new.

Let us consider the action of the undetectable error $\hat{a}^{2}$ on $\mathbf{bin}(N=1,S=1)$ and $\mathbf{cat}(\alpha\gg 1,S=1)$ ($\alpha$ is large only for simplicity; its value is irrelevant to the key point). The logical states $|+\mathbf{bin}\rangle\propto|0\rangle+|4\rangle$ and $|-\mathbf{bin}\rangle=|2\rangle$ are mapped to states $|2\rangle$ and $|0\rangle$, respectively. We see that the latter error state, $\hat{a}^{2}|-\mathbf{bin}\rangle\propto|0\rangle$, overlaps with $|0\rangle-|4\rangle$, a state orthogonal to the code space. One can thus add an extra Kraus operator to the recovery that maps any quantum information in this extra error subspace back to the code space. This cannot be done for cat, where the logical states $|+\mathbf{cat}\rangle\propto|\alpha\rangle+|-\alpha\rangle$ and $|-\mathbf{cat}\rangle\propto|i\alpha\rangle+|-i\alpha\rangle$ are mapped to $\pm|\pm_{\mathrm{cat}}\rangle$ under $\hat{a}^{2}$ (recall that $\hat{a}|\alpha\rangle=\alpha|\alpha\rangle$), yielding a completely uncorrectable phase flip. For $\mathbf{bin}(N=1,S=1)$, this extra one-dimensional subspace is used to correct from the leading-order backaction error [23]. However, there are enough such extra subspaces for sufficiently high $N$ to correct for both backaction (up to $\gamma^{N}$) and some loss errors $\hat{a}^{\ell\geq S+1}$.

Now consider $\mathbf{bin}(N=4,S=1)$. Recall that a $\mathbf{bin}(N=4)$ protects from backaction up to $\gamma^{4}$, so our calculations are only to that order. While the code exactly detects only one loss $E_{1}$, it turns out there is an extra subspace allowing for approximate correction of $E_{2}$ and even $E_{3}$. The two-dimensional code subspace $\mathrm{Span}\{|\pm_{\mathrm{bin}}\rangle\}$ is supported on the six-dimensional Fock subspace

![img-18.jpeg](images/img-18.jpeg)
Figure 6: Log_{10} plot of $1-F_{\mathcal{E}}(\gamma=0.095)$ (1.11) vs. (a) cat code parameters $S$ and $\alpha$ and (b) bin code parameters $S$ and $N$ (cf. Fig. 1 in Ref. [23]). For a given $S$, cat achieves the best performance (purple) at multiple $S$-dependent sweet-spots $\alpha_{\star}$. While $F_{\mathcal{E}}(\alpha_{\star})$ for $\mathbf{cat}(S)$ does not increase with increasing $S$ for the values we’ve sampled, performance of $\mathbf{bin}(N,S\approx 2N)$ clearly does (cyan). There is thus reason to believe that bin outperforms cat when no energy constraints are imposed.

$\mathcal{F}_{0}=\mathrm{Span}\{|0\rangle,|2\rangle,|4\rangle,|6\rangle,|8\rangle,|10\rangle\}.$ (6.6)

Another two-dimensional subspace is reserved for correcting backaction $E_{0}$. This leaves an extra two dimensions $\mathrm{Span}\{Q_{0}E_{2}|\pm_{\mathrm{bin}}\rangle\}\subset\mathcal{H}_{\mathrm{no-loss}}$ for approximately correcting the loss error $E_{2}$, where the projection $Q_{0}$ removes any overlap with the code space and the subspace used for correcting backaction. Indeed, one can add an extra isometry mapping such error states

$Q_{0}E_{2}|+\mathbf{bin}\rangle$ $\propto\sqrt{2}\eta^{2}|2\rangle-(1+\eta^{2})|6\rangle+\sqrt{10}|10\rangle$ (6.7a)
$Q_{0}E_{2}|-\mathbf{bin}\rangle$ $\propto\sqrt{10}\eta^{2}|0\rangle-(1+\eta^{2})|4\rangle+\sqrt{2}|8\rangle$ (6.7b)

back into the code space ($\eta\equiv 1-\gamma$).

Similarly, this code can also approximately correct the next error $E_{3}$. The relevant Fock subspace is now

$\mathcal{F}_{1}=\mathrm{Span}\{|1\rangle,|3\rangle,|5\rangle,|7\rangle,|9\rangle\}.$ (6.8)

The two-dimensional subspace $\mathrm{Span}\{E_{1}|\pm_{\mathrm{bin}}\rangle\}$ is devoted to correcting $E_{1}$, leaving three extra dimensions. Two of those dimensions are then used to correct against $E_{3}$. Letting $Q_{1}$ be the projection on the remaining three-dimensional subspace $\mathcal{F}_{1}/\mathrm{Span}\{E_{1}|\pm_{\mathrm{bin}}\rangle\}$, one can construct a mapping from the extra error subspace $\mathrm{Span}\{Q_{1}E_{3}|\pm_{\mathrm{bin}}\rangle\}$ back to the code space.

### III.2 Removing energy constraints

We have numerically investigated $\bar{n}_{\mathrm{bin}}\geq 10$ in order to see whether a certain direction in the $N,S$ parameter space produces increasing $F_{\mathcal{E}}$ with increasing $\bar{n}_{\mathrm{bin}}$ (6.2). While it is unlikely that $F_{\mathcal{E}}\to 1$ as $\bar{n}\to\infty$ for any

---

single-mode code, we have numerical evidence showing that $F_{\mathcal{E}}^{\mathsf{bin}(N)}$ for certain $S=\xi N$ monotonically increases to some value $F_{\mathcal{E}}^{\mathsf{bin}(\infty)}<1$, with $\xi\geq 1$ dependent on $\gamma$. For example, as shown in Fig. 6, the limit $S\approx 2N\to\infty$ does seem to be giving us monotonically increasing $F_{\mathcal{E}}$; we have verified this monotonic increase for $N\leq 14$ and $S\leq 36$ at $\gamma=0.1$ but it could very well be that the curves eventually decrease for sufficiently high $N,S$.

The performance improvement of bin codes at large $\bar{n}_{\mathtt{bin}}$ can be attributed to the advantage of having extra error subspaces, discussed in the latter portion of Sec. VI.1. To quantify this advantage, one can cook up a recovery procedure consisting of two sets of isometries. The *first-level set* of recovery isometries maps the *correctable* ($\ell\in\{0,1\cdots,S\}$) error-subspace code states $E_{\ell}|\pm_{\mathtt{bin}}\rangle$ back to the codespace. This part is similar to the cat code recovery scheme from Ref. *[46]* and to the bin scheme in Sec. VI.4. The *second-level set* consists of isometries mapping extra error subspaces $Q_{\ell}E_{\ell+S+1}|\pm_{\mathtt{bin}}\rangle$ back into the code space, where $Q_{\ell}$ project out the first-level error subspaces $\mathrm{Span}\{E_{\ell}|\pm_{\mathtt{bin}}\rangle\}$ (and, in the case of $\ell=0$, the codespace as well). Of course, such a multi-level recovery can be extended to three and more levels. When implemented, the two-level recovery yields a similar scaling with $N,S$ as the optimal recovery in Fig. 6(b) for the $N,S$ we were able to sample. Nevertheless, it does not explain why $S$ increases faster than $N$ for the best codes in that figure. While we have shown that increasing both $S$ and $N$ allows bin to correct (at least) approximately for more loss events, the intricate choice of which parameter to increase faster to give the optimal fidelity remains an interesting open question.

### VI.3 Relation to spin-coherent states

We characterize all single-mode binomial codes, two-mode binomial codes (closely related to noon codes *[22]*), and multi-qubit permutation invariant codes *[73]* using irreducible representations (irreps) of the Lie algebra $\mathfrak{su}(2)$. Interestingly, $\mathtt{bin}(S=0)$ were of interest to the quantum optical community due to their sub-Poissonian distribution *[93]* (see also *[94]*, Ch. 5), and the connection to $\mathfrak{su}(2)$ was noticed first back then *[95, 96]*.

Consider a spin-$J$ consisting of $2J+1$ levels and define the standard spin operators

$J_{z}\equiv\sum_{m=0}^{2J}(m-J)|J,m-J\rangle\langle J,m-J|\,,$ (100)

and similarly $J_{x}$ and $J_{y}$ (*[97]*, Ch. 7). We can then define its rotated version $J_{r}\left(\theta,\phi\right)=R_{\theta,\phi}J_{z}R_{\theta,\phi}^{\dagger}$, where $R_{\theta,\phi}$ is a rotation by azimuthal angle $\theta\in[0,\pi]$ and polar angle $\phi\in[0,2\pi)$ in the spherical coordinate system parameterizing the spin’s Bloch sphere. For each $\{\theta,\phi\}$, $J_{r}(\theta,\phi)$ has eigenstates $|\theta,\phi\rangle_{J}$ with eigenvalue $J$. These are called the $\mathfrak{su}(2)$ or spin-coherent states *[98]* (see also *[99]*):

$|\theta,\phi\rangle_{J}=\sum_{m=0}^{2J}\frac{(e^{i\phi}\tan\frac{\theta}{2})^{m}}{(1+\tan^{2}\frac{\theta}{2})^{J}}\sqrt{\binom{2J}{m}}|J,m-J\rangle\,.$ (101)

For each $J\in\{0,\frac{1}{2},1,\cdots\}$, $\{J_{x},J_{y},J_{z}\}$ form an irrep of the $\mathfrak{su}(2)$ algebra, satisfying the well-known angular momentum commutation relations. The labeling by $J$ *exhaustively characterizes* the irreps of $\mathfrak{su}\left(2\right)$, so every spin-coherent state corresponds to some irrep $J$. We go through several codes and show how they all correspond to the spin-coherent states

$\big{|}\tfrac{\pi}{2},\pi\mu\big{\rangle}_{J}=\frac{1}{2^{J}}\sum_{m=0}^{2J}(-1)^{\mu m}\sqrt{\binom{2J}{m}}|J,m-J\rangle,$ (102)

whose basis elements $|J,m-J\rangle$ are mapped either to Fock states of an oscillator(s) or a multi-qubit system, summarized in Fig. 7(a). Moreover,

$\frac{J_{x}}{J}\big{|}\tfrac{\pi}{2},\pi\mu\big{\rangle}_{J}=(-1)^{\mu}\big{|}\tfrac{\pi}{2},\pi\mu\big{\rangle}_{J}\,,$ (103)

providing us with a logical $Z$-operator $J_{x}/J$ and a check operator $(J_{x}/J)^{2}$ for all of the codes. In addition, since spin-coherent states resolve the identity operator of the spin, they offer a way to visualize the location of various states before and after certain errors on a generalized Bloch sphere of the spin. Shown in Fig. 7(b), $|\tfrac{\pi}{2},\pi\mu\rangle_{J}$ correspond to spin-coherent states at the antipodal points $(\tfrac{\pi}{2},0)$ and $(\tfrac{\pi}{2},\pi)$.

#### VI.3.1 Binomial codes

Setting $2J=N+1$, the coefficients of $|\tfrac{\pi}{2},\pi\mu\rangle_{J}$ (102) match those of the bin states (100). If we additionally map the spin states $|J,m-J\rangle$ into Fock states $|m\rangle$, then

$|\tfrac{\pi}{2},\pi\mu\big{\rangle}_{J=\frac{N+1}{2}}\to\left|\mu_{\mathtt{bin}(N,S=0)}\right\rangle.$ (104)

The operator $J_{z}$ (100) is then mapped to $\hat{n}-J$, revealing the well-known Holstein-Primakoff mapping of a spin into a boson. For larger spacing $S>0$, we map $|J,m-J\rangle$ into Fock states $|(S+1)m\rangle$. Therefore, we have shown that bin codes correspond to single-mode irreps of $\mathfrak{su}(2)$ produced by the Holstein-Primakoff mapping.

For bin codes, the check operator $(J_{x}/J)^{2}$ is related to the protection from dephasing errors (characterized by $N$), and its non-destructive measurement can be used to detect such errors (see Sec. VI.4). Moreover, the Bloch sphere picture offers a nice interpretation of why a $\mathtt{bin}(N,S)$ code protects against $k\leq N$ dephasing errors. Since $J_{z}=\hat{n}-J$ in this irrep, the action of a dephasing error $\hat{n}^{k}$ is directly related to application of $J_{z}$ and the code states are eigenstates of $J_{x}$ at antipodal parts of the Bloch sphere. Thus, one action of $J_{z}$ raises (lowers) the expectation value of $J_{x}$ for the logical zero (one) state,

---

moving them closer together from their antipodal positions at the equator [Fig. 7(b)]. The states only begin to overlap when a high enough power $(J_{z})^{k&gt;N}$ has been applied, which corresponds to an unprotected dephasing error $\hat{n}^{k&gt;N}$ in the bosonic representation.

#### III.2.2 Permutation-invariant codes

These codes (denoted here as perm) were introduced by Ouyang [73] (see also [100]) to tackle single-qubit amplitude damping. Given $M$ qubits and parameters $\{J,S\}$, the logical states are

$|\mu_{\text{\tt perm}}\rangle=\frac{1}{2^{J}}\sum_{m=0}^{2^{J}}(-1)^{\mu m}\sqrt{\binom{2J}{m}}|D_{(S+1)m}^{M}\rangle\,,$ (104)

where the Dicke state $|D_{(S+1)m}^{N}\rangle$ is the fully symmetrized $M$-qubit state with $(S+1)\,m$ qubits in state $|1\rangle$ and the remaining qubits in $|0\rangle$. Therefore, we need to have $M\geq 2J(S+1)$ in order to accommodate all of the required Dicke states. If $2J=3S+1$ and $M=3S^{2}+5S$, these codes can protect against qubit amplitude damping errors of weight $S$ [73]. In this context, the spacing $S$ (between excitations of the Dicke states) quantifies a distance of the codes. We can already see the resemblance to spin-coherent states, but here the irrep is more complicated. For simplicity, let us set $S=0$ and $M=2J$; the $S&gt;0$ case is a straightforward extension whose basis elements are shown in Fig. 7(a). For such cases, $|\mu_{\text{\tt perm}}\rangle$ are spin-coherent states of the largest irrep of $\mathfrak{su}\,(2)$ arising from tensoring $M$ spin-$\nicefrac{{1}}{{2}}$ particles, with $J=\nicefrac{{M}}{{2}}$ playing the role of a collective spin.

#### III.2.3 Two-mode binomial codes

There is another well-known $\mathfrak{su}(2)$-related construct — the Jordan-Schwinger mapping of a spin into two bosons. Letting $\hat{a}_{1},\hat{a}_{2}$ be the lowering operators of the two bosons and $X,Y,Z$ be the Pauli matrices, we have

$J_{[x,y,z]}=\frac{1}{2}\sum_{j,k=0}^{1}\hat{a}_{j}^{\dagger}[X,Y,Z]_{jk}\hat{a}_{k}\,.$ (105)

For example, $J_{z}=\frac{1}{2}(\hat{a}_{1}^{\dagger}\hat{a}_{1}-\hat{a}_{2}^{\dagger}\hat{a}_{2})$. The state space associated with each irrep of this type corresponds to the subspace of fixed total occupation number, i.e., all two-mode Fock states $|n_{1},n_{2}\rangle$ such that $n_{1}+n_{2}=2J$ for an irrep of spin $J$. One can thus see that the total spin is proportional to the “identity” component on the subspace, $J=\frac{1}{2}(\hat{a}_{1}^{\dagger}\hat{a}_{1}+\hat{a}_{2}^{\dagger}\hat{a}_{2})$. Any code within a subspace of fixed $J$ thus consists of eigenstates of the joint backaction $(1-\gamma)^{(\hat{a}_{1}^{\dagger}\hat{a}_{1}+\hat{a}_{2}^{\dagger}\hat{a}_{2})/2}$ in the two-mode pure-loss error operators (4) (assuming identical $\gamma$’s for both modes). Codes having this structure were first considered in Ref. [18].

(a) $\boxed{\text{code}}$ basis bin Fock states $|(S+1)m\rangle$ perm $M$-qubit Dicke states $|D_{(S+1)m}^{M\geq 2J(S+1)}\rangle$ bin2 Fock states $|(S+1)(2J-m),(S+1)m\rangle$

(b) $N=7$ ![img-19.jpeg](images/img-19.jpeg)
![img-20.jpeg](images/img-20.jpeg)
![img-21.jpeg](images/img-21.jpeg)
![img-22.jpeg](images/img-22.jpeg)
![img-23.jpeg](images/img-23.jpeg)
![img-24.jpeg](images/img-24.jpeg)

Figure 7: (a) Table listing the basis elements used to express binomial (104), permutation-invariant (103), and two-mode binomial codes bin2 (104) (with $m\in\{0,1,\cdots,2J\}$). The coefficients next to these basis states are those of spin-coherent states $|\frac{\pi}{2},\pi\mu\rangle_{J}$ (105) of a spin $J$. (b) Plots of overlaps $|_{J}(\theta,\phi|\psi\rangle|^{2}$ vs. $\theta,\phi$ given a spin state $|\psi\rangle$. The first (second, third) column shows normalized states $\{(J_{z})^{p}|\frac{\pi}{2},\pi\mu\rangle_{J=4}\}_{\mu=0}^{1}$ for $p\in\{0,2,4\}$. These plots show that powers of the “error” $J_{z}$ cause $|\frac{\pi}{2},0\rangle_{J}$ and $|\frac{\pi}{2},1\rangle_{J}$ to approach each other in the Bloch sphere and eventually overlap at the two poles. The dashed arcs connecting $\theta=\pm\frac{\pi}{2J}p$ serve as a guide to the eye. Since $J_{z}$ is mapped to $\hat{n}-J$ under the Holstein-Primakoff transformation, this provides an interpretation of dephasing errors for bin codes, which are correctable as long as $p&lt;J=\frac{1}{2}(N+1)$. Here, $N=7$ and one can see from the third column that $(J_{z})^{4}|\frac{\pi}{2},0\rangle_{J}$ and $(J_{z})^{4}|\frac{\pi}{2},1\rangle_{J}$ overlap.

Spin-coherent states of these irreps correspond to a class of two-mode binomial codes (bin2). Mapping the basis $|J,m-J\rangle$ from Eq. (103) to Fock states $|(S+1)(2J-m),(S+1)m\rangle$ yields the bin2 code states

$|\mu_{\text{\tt bin2}}\rangle=\frac{1}{2^{J}}\sum_{m=0}^{2^{J}}(-1)^{\mu m}\sqrt{\binom{2J}{m}}|2J-(S+1)m,(S+1)m\rangle.$ (106)

As with bin, we can parameterize bin2 in terms of spacing $S$ and a dephasing error parameter $N$. Then, $J=\frac{1}{2}(N+1)(S+1)$ in order to fit all of the required two-mode Fock states. Note that bin2$(S=0)$ can be obtained by acting on the Fock state $|S+1,0\rangle$ with a 50:50 beamsplitter [22] and were considered before in the context of three-mode squeezing [101].

#### III.2.4 Further generalizations

We have covered four bases in which to embed a spin — the spin’s own basis $\{|J,m-J\rangle\}_{m=0}^{2J}$, Fock states

---

$\{|m\rangle\}_{m=0}^{2J}$, Dicke states $\{|D_{m}^{M}\rangle\}_{m=0}^{2J}$, and two-mode Fock states $\{|2J-m,m\rangle\}_{m=0}^{2J}$. There are other relations between these bases and further code extensions. First, we can go in reverse of what was discussed above and embed any bosonic code into a multi-qubit Hilbert space by mapping Fock states to Dicke states. While this produces perm codes when the bosonic code is bin, it produces previously unexplored codes when the bosonic code is, e.g., cat or gkp (although such states require $J\to\infty$ due their infinite-dimensional support). Second, Dicke states $\{|D_{m}^{M}\rangle\}_{m=0}^{2J}$ converge to Fock states in the limit of fixed $J$ but large $M\gg 2J$ *[98]*. This famous limit is equivalent to the south pole of the Bloch sphere flattening out into ordinary bosonic phase space in the limit that the Bloch sphere is infinitely large. In this limit,

$\texttt{perm}(M\to\infty,J,S)\to\texttt{bin}(N=2J-1,S)\,.$ (6.17)

Third, the bin2 states can be tensored $2J$ times to construct logical states for the $4J$-mode noon code *[22]*, $|\mu_{\texttt{noon}}\rangle=|\mu_{\texttt{bin2}}\rangle^{\otimes 2J}$. The same procedure can of course be applied to bin codes. Offering an interesting alternative to spacing, noon codes instead concatenate bin2 with a $2J$-block bit-flip code to correct for up to $2J-1$ loss errors. Fourth, qubit (qudit) bin codes can *themselves* be thought of as bit-flip codes when expressed in a basis of multi-qubit (multi-qudit) states (see Appx. C).

### VI.4 Error-correction procedure for binomial codes

The existence of approximate error recovery maps for the various codes does not explicitly suggest by what means these recovery maps can be implemented nor whether fault-tolerant error recovery is possible for these codes. For qubit stabilizer codes, the theory of fault-tolerant error correction has been developed. For gkp, methods of fault-tolerant quantum error correction *[9]* are possible which simply generalize the techniques of qudit ($d$-dimensional) stabilizer codes to $d\to\infty$.

In this section, we investigate for the binomial qubit codes what measurements of commuting check operators could give sufficient error information to undo a set of errors. The recovery procedure we give is not necessarily the optimal one obtained by optimization in Sec. II. The binomial code family $\texttt{bin}(N,S)$ can correct against errors in the error set $\mathscr{E}=\{I,\hat{a},\ldots,\hat{a}^{L},\hat{a}^{\dagger},\ldots,(\hat{a}^{\dagger})^{G},\hat{n},\ldots\hat{n}^{D}\}$ with $S=L+G$ and $N=\max(L,G,2D)$. We know from Eq. (6.11) that the codewords correspond to antipodal spin-coherent states of spin $J=\frac{1}{2}(N+1)$. We will refer to the $N+1$-dimensional subspace as the spin-space.

Imagine that one error from the set $\mathscr{E}$ has taken place on an encoded state. The following procedure describes how to undo this error. First, one non-destructively measures the eigenvalues of the check operator $J_{x}^{2}$ which has eigenvalue $+J^{2}$ on all states in the codespace. Here we assume that the operator $J_{x}$ only has support on the Fock states $|m(S+1)\rangle$ and thus has zero eigenvalues elsewhere. Of course the check operator $J_{x}$ is not unique and any form of non-destructively learning the value $|m_{x}|$ is permitted. For odd $N$ (integer spin $J$), such a measurement has outcomes $|m_{x}|^{2}$ with $|m_{x}|=0,1,\cdots,J$. The outcome $m_{x}=0$ cannot have come about from one of the dephasing errors of the form $\hat{n}^{k}$ since this error operator maps an initial state with $|m_{x}|=J$ to a superposition of states with $|m_{x}|\geq J-k$ so that for $k\leq D$, one can not reach $|m_{x}|=0$. For even $N$ (half-integer spin $J$), $m_{x}$ will never be zero by the application of a dephasing error. Hence if one finds the eigenvalue $m_{x}=0$, one concludes that photon loss or photon gain errors of the form $\hat{a}^{k}$, $k\leq L$ and $(\hat{a}^{\dagger})^{l}$, $l\leq G$ must have occurred. In order to learn more about these photon loss and gain errors, one then measures the photon parity check operator (5.7). If one finds any another value of $|m_{x}|=k$ for the first measurement, one rotates the two-dimensional $m_{x}=\pm k$ subspace back to the two-dimensional $m_{x}=\pm J$ subspace by some unitary transformation. For stabilizer (resp. gkp), this correction can be a Pauli operator (resp. small displacement). Note that, unlike for stabilizer, cat or gkp codes, it is necessary to physically apply the correction. In other words, unlike the use of Pauli frames *[102]*, we cannot just record the value of $|m_{x}|$ and keep the quantum information in this error space with a lower value for $|m_{x}|$: subsequent dephasing errors would lead to more laddering up and down in the spin-space so the QEC conditions would no longer be met [see Fig. 7(b)]. In case $m_{x}=0$, one non-destructively measures the eigenvalues of $C_{\texttt{bin}}$ (5.7) (via phase estimation, say), allowing one to learn the photon parity $k$ modulo $S+1$. When $k\leq G$ (at most $G$ photons are gained), one applies

$U_{k}^{+}=\sum_{\mu=0}^{1}\frac{|\mu_{\texttt{bin}}\rangle\langle\mu_{\texttt{bin}}|\hat{a}^{k}}{\sqrt{\langle\mu_{\texttt{bin}}|\hat{a}^{k}(\hat{a}^{\dagger})^{k}|\mu_{\texttt{bin}}\rangle}}+V_{\mathrm{else}}^{+}\,,$ (6.18)

where $V_{\mathrm{else}}^{+}$ is chosen to make $U_{k}^{+}$ unitary. When $k>G$ (at most $L$ photons lost), one applies

$U_{l}^{-}=\sum_{\mu=0}^{1}\frac{|\mu_{\texttt{bin}}\rangle\langle\mu_{\texttt{bin}}|(\hat{a}^{\dagger})^{l}}{\sqrt{\langle\mu_{\texttt{bin}}|(\hat{a}^{\dagger})^{l}\hat{a}^{l}|\mu_{\texttt{bin}}\rangle}}+V_{\mathrm{else}}^{-}$ (6.19)

with $l=S+1-k$. These rotations are not a simple adding or subtracting of photons since some Fock states in $|\mu_{\texttt{bin}}\rangle$ have been annihilated.

This form of error correction unfortunately does not correct products of dephasing and photon loss/gain errors, which are in principle errors against which the code can correct *[23]*. Note also that Ref. *[23]* has shown that specifically for the photon loss channel with errors as in Eq. (1.4), only the measurement of the rotation operator $C_{\texttt{bin}}$ (5.7) is required (since there is one particular dephasing error associated with a particular number of photon losses). The procedure above thus falls short of giving a general prescription for error correction for the binomial codes. However, for the binomial qubit code $\texttt{bin}(N=2,S=1)$, one can give a scheme which corrects all the errors which meet the quantum

---

error conditions. The code $\mathbf{bin}(N = 2, S = 1)$ can correct against the errors in $\mathcal{E} = \{I, \hat{a}, \hat{n}\}$. For these parameters, the code space is inside the Fock space with a maximum of 6 photons, $\mathcal{F}_6 = \mathrm{Span}\{|0\rangle, \dots, |6\rangle\}$. We split this space into the direct sum of the even subspace and the odd subspace, that is $\mathcal{F}_6 = \mathcal{F}_6^{\mathrm{even}} \oplus \mathcal{F}_6^{\mathrm{odd}} = \mathrm{Span}\{|0\rangle, |2\rangle, |4\rangle, |6\rangle\} \oplus \mathrm{Span}\{|1\rangle, |3\rangle, |5\rangle\}$.

The code space is inside $\mathcal{F}_6^{\mathrm{even}}$. We identify $\mathcal{F}_6^{\mathrm{even}}$ with a spin $J = 3/2$ via the mapping

$$
| 6 \rangle \equiv | m _ {z} = \frac {3}{2} \rangle , \quad | 4 \rangle \equiv | m _ {z} = \frac {1}{2} \rangle ,
$$

$$
| 2 \rangle \equiv | m _ {z} = - \frac {1}{2} \rangle , \quad | 0 \rangle \equiv | m _ {z} = - \frac {3}{2} \rangle ,
$$

so that $|0_{\mathrm{bin}}\rangle$ and $|1_{\mathrm{bin}}\rangle$ code states are the highest and lowest eigenstates of $J_{x}(J = 3 / 2)$,

$$
| 0 _ {\mathrm {b i n}} \rangle = | m _ {x} = \frac {3}{2} \rangle , \qquad | 1 _ {\mathrm {b i n}} \rangle = | m _ {x} = - \frac {3}{2} \rangle .
$$

One dephasing error leaves the code states inside $\mathcal{F}_6^{\mathrm{even}}$. More precisely, it is a linear combination of the identity and $J_{z}(J = 3 / 2)$ such that

$$
\hat {n} \left| 0 _ {\text {b i n}} \right\rangle = 2 \left| m _ {x} = \frac {1}{2} \right\rangle + 3 \left| 0 _ {\text {b i n}} \right\rangle , \tag {6.20a}
$$

$$
\hat {n} \left| 1 _ {\text {b i n}} \right\rangle = 2 \left| m _ {x} = - \frac {1}{2} \right\rangle + 3 \left| 1 _ {\text {b i n}} \right\rangle . \tag {6.20b}
$$

For convenience, we relabel the error states $\left|m_x = \pm \frac{1}{2}\right\rangle \equiv |n\pm \rangle$.

Remarkably, one photon loss maps $\mathcal{F}_6^{\mathrm{even}}$ onto $\mathcal{F}_6^{\mathrm{odd}}$ in such a way that the code states are mapped onto shifted code states for $N = 1$. This is in fact true for general $N$ and $S$: one photon loss maps the code space $(N,S)$ to the code space $(N - 1,S)$ but shifted by $+S$ in the Fock basis [23]. With this in mind, we can identify $\mathcal{F}_6^{\mathrm{odd}}$ with a spin $J = 1$ with the mapping

$$
| 5 \rangle \equiv | m _ {z} = 1 \rangle , \quad | 3 \rangle \equiv | m _ {z} = 0 \rangle , \quad | 1 \rangle \equiv | m _ {z} = - 1 \rangle ,
$$

and then the error states are the highest and lowest eigenstates of $J_{x}(J = 1)$,

$$
\hat {a} | 0 _ {\mathrm {b i n}} \rangle \propto | m _ {x} = 1 \rangle , \quad \hat {a} | 1 _ {\mathrm {b i n}} \rangle \propto | m _ {x} = - 1 \rangle ,
$$

which we rename for convenience: $|m_x = \pm 1\rangle \equiv |a\pm \rangle$. The third state of this spin-1 subspace is called the unknown state as ending up in this state means the loss of logical information, $|m_{x} = 0\rangle \equiv |\ref{eq:1}\rangle$. To complete the description, one can note that the action of $\hat{n}$ on $\mathcal{F}_6^{\mathrm{odd}}$ is also a linear combination of $J_{z}(J = 1)$ and the identity $I$, i.e. mapping $|a\pm \rangle$ to a linear combination of itself and $|\ref{eq:1}\rangle$, and using the fact that $\hat{a}\hat{n} = \hat{n}\hat{a} -\hat{a}$, one can note that $|n\pm \rangle$ is mapped by $\hat{a}$ onto a linear combination of $|a\pm \rangle$ and $|\ref{eq:1}\rangle$. These relations are summarized in Table II.

One possible way to extract error information is then to measure (via phase estimation) the eigenvalues of the following unitary

$$
U = \exp \left\{\frac {2 \pi i}{b} \left[ a \left(J _ {x} (3 / 2)\right) ^ {2} \oplus \left(J _ {x} (1)\right) ^ {2} \right] \right\}, \tag {6.21}
$$

where the two parameters $a$ and $b$ can be chosen to obtain good spacing between different eigenvalues. For example one can choose $a = 8$ and $b = 5$, leading to Table III.

|  J_{x}(J = 3/2) | F_{6}^{even} | F_{6}^{odd} | J_{x}(J = 1)  |
| --- | --- | --- | --- |
|  3/2 | |μ_{bin}=0⟩ | |a+⟩ | 1  |
|   | ˆμ↓ | ↓ˆn |   |
|  1/2 | |n+⟩ | |?⟩ | 0  |
|  -1/2 | |n-⟩ |  |   |
|   | ˆn↑ | ↑ˆn |   |
|  -3/2 | |μ_{bin}=1⟩ | |a-⟩ | -1  |

Table II. Relations between code states and error states for $\mathbf{bin}(N = 2,S = 1)$.

To obtain the 4 eigenvalues of $U$ (via phase estimation), one needs at least 2 qubit ancillas. A more direct method would be to first measure photon parity. If odd, then correct for photon loss. If even, then one measures the eigenvalues of $J_{x}^{2}$ by measuring $U = \exp (i32\pi J_{x}(3 / 2)^{2} / 9)$, which has eigenvalue $+1$ for the no-error case and eigenvalue $\exp (i32\pi /36)\approx -1$ in the dephasing error case.

|  Eigenstates | |μ=0 or 1⟩ | |n+⟩, |n-⟩ | |a+⟩, |a-⟩ | ?⟩  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Eigenvalues | e^{i6π/5} | e^{i4π/5} | e^{i2π/5} | 1  |
|  Decoding | no error | dephasing | photon loss | failure  |

Table III. Eigenstructure of the proposed unitary to be measured for error correction of $\mathbf{bin}(N = 2,S = 1)$.

# VII. GKP CODES

While their error-correcting properties were first revealed in Ref. [9], gkp states have connections to quantum foundations [103], solid-state physics [104], and signal processing (where their analogues are frequency combs). The ideal (i.e., infinite $\bar{n}$) square lattice gkps codespace, denoted by its projection $P_{\mathbf{gkps}}^{\mathrm{ideal}}$, is the simultaneous $+1$ eigenspace of the two commuting stabilizers

$$
S _ {\mathbf {x}} = D _ {\sqrt {2 \pi}} \quad \text {and} \quad S _ {\mathbf {p}} = D _ {i \sqrt {2 \pi}}, \tag {7.1}
$$

where $D_{\alpha} \equiv e^{\alpha \hat{a}^{\dagger} - \alpha^{*}\hat{a}}$ is the displacement operator (note that $D_{\sqrt{2\pi}} = e^{-i2\sqrt{\pi}\hat{p}}$). The projection onto the code can be constructed out of all of their powers,

$$
P _ {\mathbf {g k p s}} ^ {\text {i d e a l}} \equiv \left(\frac {1}{\sqrt {\pi}} \sum_ {n \in \mathbb {Z}} S _ {\mathbf {x}} ^ {n}\right) \left(\frac {1}{\sqrt {\pi}} \sum_ {n \in \mathbb {Z}} S _ {\mathbf {p}} ^ {n}\right) \equiv P _ {\mathbf {x}} P _ {\mathbf {p}}. \tag {7.2}
$$

Applying the Poisson summation formula allows us to express $P_{\mathbf{x}}(P_{\mathbf{p}})$ as a sum of projections onto eigenstates

---

$|n\sqrt{\pi}\rangle_{\hat{x}}\;(|n\sqrt{\pi}\rangle_{\hat{p}})$ of $\hat{x}\;(\hat{p})$. We demonstrate this for $P_{\mathbf{p}}$:

$P_{\mathbf{p}}$ $=\frac{1}{\sqrt{\pi}}\sum_{n\in\mathbb{Z}}e^{i2\sqrt{\pi}n\hat{x}}$ (12a)
$=\sum_{n\in\mathbb{Z}}\delta\left(\hat{x}-\sqrt{\pi}n\right)$ (12b)
$=\sum_{n\in\mathbb{Z}}|\sqrt{\pi}n\rangle_{\hat{x}}\langle\sqrt{\pi}n|\,.$ (12c)

These sets of positions and momenta makes up the *code lattice*, the lattice dual to the stabilizer lattice (in the language of Ref. *[9]*) and generated by the logical operators

$X_{\tt gkps}$ $=D_{\sqrt{\pi/2}}=S_{\mathbf{x}}^{1/2}$ (13a)
$Z_{\tt gkps}$ $=D_{i\sqrt{\pi/2}}=S_{\mathbf{p}}^{1/2}\,.$ (13b)

The maximally mixed state $\frac{1}{2}P_{\tt gkps}$ reproduces this lattice, shown in the fourth panel in Fig. 1.

Conventionally, gkps logical states are expressed in terms of squeezed states,

$|\mu^{\rm ideal}_{\tt gkps}\rangle\propto\sum_{n\in\mathbb{Z}}|\sqrt{\pi}(2n+\mu)\rangle_{\hat{x}}\,.$ (14)

One can obtain an equivalent (see Appx. D.2) representation in terms of coherent states by projecting the vacuum state $|0\rangle$ onto the code and the $\pm 1$ eigenstates of $Z_{\tt gkps}$:

$|\mu^{\rm ideal}_{\tt gkps}\rangle$ $\propto[I+(-1)^{\mu}Z_{\tt gkps}]P^{\rm ideal}_{\tt gkps}|0\rangle$ (15)
$=\sum_{\vec{n}\in\mathbb{Z}^{2}}D_{\sqrt{\frac{\pi}{2}}(2n_{1}+\mu)}D_{i\sqrt{\frac{\pi}{2}}n_{2}}|0\rangle\,,$

where $\vec{n}\equiv(n_{1},n_{2})$. The above displacements generate the two *state lattices* for $Z_{\tt gkps}$-logical states, whose horizontal spacing is twice that of the code lattice due to the $I\pm Z_{\tt gkps}$ term. In general, the state lattice depends on the logical basis used (see Fig. 8) while the code lattice is basis-independent.

The usual way to make the states (14) have finite $\bar{n}$ (and therefore be normalizable) is to assume finite squeezing for each position eigenstate and add a $\Delta^{2}$-dependent Gaussian envelope, producing the gkps states in Eq. (13a) below. Alternatively, one can add a Gaussian envelope to Eq. (15), yielding a representation in terms of coherent states, Eq. (13b). A third finite-$\bar{n}$ representation can be written in terms of $|\mu^{\rm ideal}_{\tt gkps}\rangle$ smeared by a Gaussian distribution of displacements *[9]*, making contact with the errors that the codes are designed to correct. This is the third equation below:

$|\mu^{\Delta}_{\tt gkps}\rangle$ $\propto\sum_{n\in\mathbb{Z}}e^{-\frac{\pi}{2}\Delta^{2}(2n+\mu)^{2}}D_{\sqrt{\frac{\pi}{2}}(2n+\mu)}S_{-\ln\Delta}|0\rangle$ (16a)
$\sim\sum_{\vec{n}\in\mathbb{Z}^{2}}e^{-\frac{\pi}{2}\Delta^{2}[(2n_{1}+\mu)^{2}+n_{2}^{2}]}D_{\sqrt{\frac{\pi}{2}}(2n_{1}+\mu)}D_{i\sqrt{\frac{\pi}{2}}n_{2}}|0\rangle$ (16b)
$\sim\int d^{2}\alpha\frac{e^{-|\alpha|^{2}/\Delta^{2}}}{\sqrt{\pi\Delta^{2}/2}}D_{\alpha}|\mu^{\rm ideal}_{\tt gkps}\rangle\,,$

where $\mu\in\{0,1\}$ and $S_{r}=e^{+\frac{1}{2}r(\hat{a}^{2}-\hat{a}^{\dagger 2})}$ is the squeezing operator. We use $\Delta\in[0,1]$ for both the envelope and squeezing parameters for simplicity. These representations numerically converge to each other very quickly in the $\Delta\to 0$ limit, but there are visual differences between them for small envelopes. A fourth representation in terms of Fock states is possible using Eq. (86) from Ref. *[94]*. Note that $|0^{\Delta}_{\tt gkps}\rangle$ and $|1^{\Delta}_{\tt gkps}\rangle$ are non-orthogonal for nonzero $\Delta$, and this source of error manifests itself in the QEC matrix.

Recall that gkps($\Delta\to 0$) states can protect against displacement errors $D_{\alpha_{1}+i\alpha_{2}}$ in phase space, where $|\alpha_{1}|,|\alpha_{2}|<\sqrt{\pi/{\rm s}}$. The representations can easily generalize to more tightly-packed lattices, yielding a slightly larger volume of correctable displacements. To construct the coherent-state representation of the $Z_{\tt gkp}$-logical states, one first constructs commuting stabilizers (following Ref. *[9]*) and repeats Eq. (15). Adding an envelope, this representation (13b) is particularly simple to express:

$|\mu^{\Delta}_{\tt gkp}\rangle\propto\sum_{\alpha\in L(\mu)}e^{-\Delta^{2}|\alpha|^{2}}e^{-i\alpha_{1}\alpha_{2}}|\alpha\rangle\,,$ (17)

where $|\alpha=\alpha_{1}+i\alpha_{2}\rangle$ is a coherent state and $L(\mu)$ is the state lattice for each code state $\mu$. We considered both these lattices and their shifted versions (11) for the gkp numerics (see Appx. B). For all analytics below, we use the finite-$\bar{n}_{\tt gkps}$ unshifted square-lattice states $|\mu^{\Delta}_{\tt gkps}\rangle$ (16c), noting any generalizations to other lattices.

We have calculated moments of the occupation number, yielding a geometric (i.e., thermal) distribution:

$\overline{n^{\ell}_{\tt gkps}}\equiv\frac{1}{2}\text{Tr}\{P_{\tt gkps}\tilde{n}^{\ell}\}\sim\ell!\bar{n}^{\ell}_{\tt gkps}\,,$ (18)

where the average occupation number is

$\bar{n}_{\tt gkps}\sim\frac{1}{2\Delta^{2}}-\frac{1}{2}\,.$ (19)

As expected, the moments diverge as the states become unnormalizable in the small $\Delta$ limit.

### V.1 QEC matrix for GKP codes

Recall that any trace class bosonic operator $A$ (i.e., satisfying $\text{Tr}\{A^{\dagger}A\}<\infty$) can be expanded in terms of displacement operators using the orthogonality condition of $D_{\alpha}$ at the superoperator level *[105]*,

$\text{Tr}\{D^{\dagger}_{\alpha}D_{\beta}\}=\pi\delta^{2}\left(\alpha-\beta\right)\,.$ (20)

The expansion is then $A=\int\frac{d^{2}\alpha}{\pi}\text{Tr}\{D^{\dagger}_{\alpha}A\}D_{\alpha}$, where the integral is over all of phase space and $\text{Tr}\{D^{\dagger}_{\alpha}A\}$ is the *characteristic function* of $A$. Protection of gkp against pure loss was previously discussed using an approximation of $\hat{a}$ in terms of a *sum* of displacements instead of

---

![img-25.jpeg](images/img-25.jpeg)
Figure 8: Wigner function sketches of the two $Z_{\tt gkps^{-}}$, $X_{\tt gkps^{+}}$, $Y_{\tt gkps^{-}}$-logical states. Comparing to the fourth panel in Fig. 1, which shows that the code lattice is square, here we see that the lattices formed by the logical states may be square or rectangular, depending on which logical operator is considered. The unit cell of the state lattices (103) is marked by “$\times$” in the two leftmost panels; the remaining dots appear as a result of the coherences between different coherent states.

An integral, at first very briefly [9] and subsequently taking into account the maximum number of photons in the oscillator [106]. Here we calculate the QEC matrix $c_{\ell\ell^{\prime}}^{\tt gkps}$ (100) by expressing Kraus operators in terms of the full integral expansion.

Unlike $\hat{a}$, the error operator $E_{\ell}$ and its variants are trace class due to the damping term, yielding

$E_{\ell}^{\dagger}E_{\ell^{\prime}}=\int\frac{d^{2}\alpha}{\pi}e^{-\frac{1}{2}(1-\gamma)|\alpha|^{2}}\langle\ell|D_{\alpha^{*}}|\ell^{\prime}\rangle D_{\alpha\sqrt{\gamma}}\,,$ (104)

where $\langle\ell|D_{\alpha^{*}}|\ell^{\prime}\rangle$ are matrix elements of the displacement operator $D_{\alpha}$ in the Fock state basis (103). To obtain this, one can express the trace in $\mathrm{Tr}\{D_{\alpha}^{\dagger}E_{\ell}^{\dagger}E_{\ell^{\prime}}\}$ as a sum over Fock states, plug in Eq. (103), and use the generating function of Laguerre polynomials (105). Complementing the expansion of Gaussian noise $\{D_{\alpha}\}$ in terms of photon creation and annihilation operators (e.g., Ref. [107]), the above equation completes the “Rosetta stone” expressing each of the two primary noise models in the language of the other.

To gain a flavor of the calculations below, let us first examine how we can calculate $c_{\ell\ell}^{\tt gkps}=\frac{1}{2}\mathrm{Tr}\{P_{\tt gkps}E_{\ell}^{\dagger}E_{\ell}\}$. Using Eq. (104), this calculation boils down to determining $\mathrm{Tr}\{P_{\tt gkps}D_{\alpha}\}$. Consider first the infinite $\bar{n}_{\tt gkps}$ limit, recalling from Fig. 1 that $P_{\tt gkps}$ is a sum of (unphysical) points of fixed position and momentum arranged in a square code lattice. Then, $\mathrm{Tr}\{P_{\tt gkps}D_{\alpha}\}$ will be nonzero only for those $\alpha$ which displace the lattice back on top of itself, i.e., $\alpha$ displaces by a multiple of the lattice’s unit cell. For those cases, the overlap of each point with itself will be infinite, and so the total result is $\sum_{\Lambda}\delta^{2}(\alpha-\Lambda)$, where the sum is over all displace-ments $\Lambda\in\sqrt{\pi/2}(n_{1},n_{2})$ (with integers $n_{1,2}$) preserving the code lattice. Coming back to finite $\bar{n}_{\tt gkps}$, a natural guess would be to substitute the Gaussian representation $\frac{1}{\Delta}e^{-\frac{1}{2\Delta^{2}}|\alpha-\Lambda|^{2}}$ for the Dirac $\delta$-function in the sum. This almost obtains the right result, but there are two more steps. The first is normalization, which cancels the $\frac{1}{\Delta}$ in front of the Gaussian representation of the $\delta$-function. The second is addition of the Gaussian envelope, yielding

$\frac{1}{2}\mathrm{Tr}\{P_{\tt gkps}D_{\alpha}\}\sim\sum_{\Lambda}e^{-\frac{1}{2\Delta^{2}}|\alpha-\Lambda|^{2}}e^{-\frac{\Delta^{2}}{2}|\Lambda|^{2}}\,.$ (105)

Notice that what used to be a Dirac $\delta$ is now a Kronecker $\delta_{\alpha,\Lambda}\sim e^{-\frac{1}{2\Delta^{2}}|\alpha-\Lambda|^{2}}$ in the small $\Delta$ limit. As a sanity check, setting $\alpha=0$ yields unity in that limit.

Calculating these overlaps is more involved (see Appx. D.3), but we can nevertheless use the above intuition to understand the more general element (with $\nu\in\{0,1\}$)

$\langle\mu_{\tt gkps}^{\Delta}|D_{\alpha}|\nu_{\tt gkps}^{\Delta}\rangle\sim$ (106)
$\sum_{\vec{n}\in\mathbb{Z}^{2}}e^{i\pi(n_{1}+\frac{\mu+\nu}{2})n_{2}}e^{-\frac{1}{2\Delta^{2}}|\alpha-\Lambda_{\delta\mu}^{\vec{n}}|^{2}}e^{-\frac{\Delta^{2}}{2}|\Lambda_{\delta\mu}^{\vec{n}}|^{2}}\,,$

where $\delta\mu\equiv\mu-\nu$ and $\Lambda_{\delta\mu}^{\vec{n}}\equiv\sqrt{\frac{\pi}{2}}[(2n_{1}+\delta\mu)+in_{2}]$. Since there are two different state lattices, there are extra phases in the sum and the sum is over displacements $\alpha\in\Lambda_{\delta\mu}^{\vec{n}}$ which overlap the two lattices. We can now plug this into $E_{\ell}^{\dagger}E_{\ell^{\prime}}$ (104) and proceed to calculate the integral (see Appx. D.4), yielding

$\langle\mu_{\tt gkps}^{\Delta}|E_{\ell}^{\dagger}E_{\ell^{\prime}}|\nu_{\tt gkps}^{\Delta}\rangle\sim\sqrt{c_{\ell\ell}^{\tt gkps}c_{\ell^{\prime}\ell^{\prime}}^{\tt gkps}}\sum_{\vec{n}\in\mathbb{Z}^{2}}e^{-\frac{(1-\gamma)}{2\gamma}|\Lambda_{\delta\mu}^{\vec{n}}|^{2}}$
$\times e^{i\pi(n_{1}+\frac{\mu+\nu}{2})n_{2}}e^{-\frac{\Delta^{2}}{2}|\Lambda_{\delta\mu}^{\vec{n}}|^{2}}\langle\ell|D_{(\Lambda_{\delta\mu}^{\vec{n}})^{*}/\sqrt{\gamma}}|\ell^{\prime}\rangle,$

for $\gamma\bar{n}_{\tt gkps}\to\infty$, where $c_{\ell\ell}^{\tt gkps}$ will turn out to be the probability of losing $\ell$ photons,

$c_{\ell\ell}^{\tt gkps}=\frac{1}{2}\mathrm{Tr}\{P_{\tt gkps}E_{\ell}^{\dagger}E_{\ell}\}\sim\frac{(\gamma\bar{n}_{\tt gkps})^{\ell}}{(\gamma\bar{n}_{\tt gkps}+1)^{\ell+1}}.$ (107)

Thus, the photon loss distribution for gkps is a asymptotically thermal with mean $\gamma\bar{n}$. Ignoring the $\Delta^{2}$ envelope term from now on, all $\Delta$-dependence of Eq. (107) is contained in $c_{\ell\ell}^{\tt gkps}$.

Notice that $|\langle\ell|D_{(\Lambda_{\delta\mu}^{\vec{n}})^{*}/\sqrt{\gamma}}|\ell^{\prime}\rangle|\leq 1$ because they are overlaps between two states. Thus, the only quantity regulating the sum (107) is $e^{-\frac{(1-\gamma)}{2\gamma}|\Lambda_{\delta\mu}^{\vec{n}}|^{2}}$. Assuming $\gamma\ll 1$, the “on-site” term ($\vec{n}=\vec{0}$) in Eq. (107) is $\mu$-independent and thus contributes to

$c_{\ell\ell^{\prime}}^{\tt gkps}\sim c_{\ell\ell}^{\tt gkps}\delta_{\ell\ell^{\prime}}\,,$ (108)

while the “nearest-neighbor” terms ($|\vec{n}|=1$) contribute to the leading-order uncorrectable parts

$|z_{\ell\ell^{\prime}}^{\tt gkps}|\sim\sqrt{c_{\ell\ell}^{\tt gkps}c_{\ell^{\prime}\ell^{\prime}}^{\tt gkps}}e^{-\frac{\pi}{4}\frac{1-\gamma}{\gamma}}\langle\ell|(D_{\sqrt{\frac{\gamma}{2\gamma}}}+D_{\sqrt{\frac{\gamma}{2\gamma}}}^{\dagger})|\ell^{\prime}\rangle$ (109)

---

and $|x_{\ell\ell^{\prime}}^{\sf gkps}|=|z_{\ell\ell^{\prime}}^{\sf gkps}|$. (There is no $|y_{\ell\ell^{\prime}}^{\sf gkps}|$ to this order.) The uncorrectable parts are the same (up to sign) due to the identical effect of position and momentum displacements on the code. So, while the nearest neighbors $\vec{n}=(0,\pm 1)$ contributed to $z_{\ell\ell^{\prime}}^{\sf gkps}$ and $\vec{n}=(\pm 1,0)$ contributed to $x_{\ell\ell^{\prime}}^{\sf gkps}$, the two quantities have to be equal in magnitude due to this effect. (Considering more general lattices can of course break this balance.) We can also see another symmetry manifest itself — the invariance of the lattice under parity $(-1)^{\bar{n}}$. Since the sum of displacements is even under parity, it does not connect even Fock states to odd ones and guarantees that $z_{\ell\ell^{\prime}}^{\sf gkps}=0$ unless $\ell-\ell^{\prime}$ is even. This means that technically gkps codes have spacing $S=1$. However, this spacing disappears when the lattice is slightly shifted and the symmetry lost, but the performance of the codes remains. This should not be surprising since shifted gkps codespaces are akin to Pauli frames in the stabilizer formalism *[106]*. The most striking result is that the reason for this high performance is not due to the spacing, but to the suppression by the $\gamma$-dependent exponential factor in Eq. (7.18). Namely, while $\epsilon_{\ell\ell^{\prime}}^{\sf gkps}$ contains uncorrectable parts for all $\ell,\ell^{\prime}$ (modulo symmetry constraints), all of these parts are suppressed exponentially by $e^{-\frac{\pi}{4}\frac{1-\gamma}{\gamma}}$ when $\gamma\ll 1$. As an example, we show the comparable strength of the exponential suppression of uncorrectable parts for gkps($\bar{n}\approx 6$) in Fig. 5. Assuming that the infidelity $1-F_{\mathcal{E}}$ to leading order in $\gamma$ is polynomial in all uncorrectable parts, one expects $1-F_{\mathcal{E}}$ to also be exponentially suppressed by $\frac{1-\gamma}{\gamma}$. We proceed to show this by bounding $1-F_{\mathcal{E}}$ using an explicit recovery.

### VII.2 Removing energy constraints

In Fig. 2, we have observed that $F_{\mathcal{E}}^{\sf gkps}$ is significantly higher than that for all other codes for most $\gamma$. While the non-trivial exponential suppression of uncorrectable parts (7.18) of the QEC matrix hints at an analytical explanation, this still does not tell us how $F_{\mathcal{E}}$ scales with $\gamma$. For this, we need to consider a specific analytically tractable recovery. Having investigated several recoveries, the simplest one we found is based on the fact that the combination of amplification and pure loss produces Gaussian (i.e., displacement) noise *[2]* — a channel which most naturally fits the error-correction capabilities of gkps.

Coming back to the formulation of $\mathcal{N}$ in terms of a beam-splitter (1.6), consider amplifying the signal

$\hat{a}\rightarrow\sqrt{G}\hat{a}+\sqrt{G-1}\hat{b}^{\dagger}$ (7.19)

after application of $\mathcal{N}$. Here, $G$ is the gain of the amplifier, which we set to $G=e^{\chi}=\frac{1}{1-\gamma}$ to compensate the effect of damping. Tracing out the $\hat{b}$ mode, amplification is simply the properly normalized transpose of pure loss,

$\mathcal{A}(\cdot)=(1-\gamma)\,\mathcal{N}^{\dagger}(\cdot)\,,$ (7.20)

where “$\updownarrow$” is the adjoint in the matrix representation. The Kraus operators of $\mathcal{A}$ are $\sqrt{1-\gamma}E_{\ell}^{\dagger}$ for $\ell\in\{0,1,\cdots\}$ {e.g., Ref. *[34]*, Eq. (5.5)} and it is simple to verify that $\mathcal{A}$ is indeed a channel: $(1-\gamma)\sum_{\ell=0}^{\infty}E_{\ell}E_{\ell}^{\dagger}=I$.

Upon amplification, the pure-loss channel $\mathcal{N}$ is transformed into a Gaussian noise channel with variance $\frac{\gamma}{1-\gamma}$. The noise comes from two parts: the intrinsic noise due to amplification and the amplified noise due to pure loss. More explicitly, we can apply Eq. (7.12) to express $\mathcal{A}\mathcal{N}$ in terms of displacements and use displacement orthogonality (7.11):

$\mathcal{A}\mathcal{N}(\rho)$ $=(1-\gamma)\int\frac{d^{2}\alpha}{\pi}\frac{d^{2}\beta}{\pi}e^{-\frac{1-\gamma}{2}(|\alpha|^{2}+|\beta|^{2})}D_{\frac{\alpha}{\sqrt{\gamma}}}\,\rho\,D_{\frac{\beta}{\sqrt{\gamma}}}\sum_{\ell,\ell^{\prime}=0}^{\infty}\langle\ell|D_{\alpha^{*}}|\ell^{\prime}\rangle\langle\ell^{\prime}|D_{\beta^{*}}|\ell\rangle$ (7.21)
$=(1-\gamma)\int\frac{d^{2}\alpha}{\pi}d^{2}\beta e^{-\frac{1-\gamma}{2}(|\alpha|^{2}+|\beta|^{2})}D_{\frac{\alpha}{\sqrt{\gamma}}}\,\rho\,D_{\frac{\beta}{\sqrt{\gamma}}}\delta^{2}(\alpha+\beta)=\frac{1-\gamma}{\gamma}\int\frac{d^{2}\alpha}{\pi}e^{-\frac{1-\gamma}{\gamma}|\alpha|^{2}}D_{\alpha}\,\rho\,D_{\alpha}^{\dagger}\,.$

Appending amplification with the conventional gkp recovery $\mathcal{R}^{\rm GKP}$ which measures and corrects displacements within the correctable unit cell *[9]*, the total recovery we consider is

$\mathcal{R}^{\rm AGKP}=\mathcal{R}^{\rm GKP}\mathcal{A}\,.$ (7.22)

Note that the above derivation of Gaussian noise is exact for all values of $\gamma$. We bound $F_{\mathcal{E}}$ by calculating the success probability that $\mathcal{R}^{\rm AGKP}$ will succeed in correcting the above Gaussian noise $\mathcal{A}\mathcal{N}$ starting with ideal (i.e., infinite $\bar{n}_{\sf gkps}$) code states:

$P_{\rm succ}(\gamma)=\frac{1-\gamma}{\gamma}\int_{\blacksquare}\frac{d\alpha_{1}d\alpha_{2}}{\pi}e^{-\frac{1-\gamma}{\gamma}(\alpha_{1}^{2}+\alpha_{2}^{2})}\,,$ (7.23)

where the integration is over correctable displacements $|\alpha_{1}|,|\alpha_{2}|\leq\sqrt{\nicefrac{{\pi}}{{s}}}$ denoted by $\blacksquare$. The channel infidelity $1-F_{\mathcal{E}}^{\rm AGKP}$ can then be estimated using the failure probability, which is the complementary integral outside of the

---

![img-26.jpeg](images/img-26.jpeg)
Figure 9: Contour plot of $F_{\mathcal{E}}$ vs. dimensionless Kerr parameter $Kt$ and damping parameter $\chi\equiv\kappa t$ for cat, bin, num, and gkps picked such that they all have $\bar{n}\approx 2$. Here, $K$ is the strength of the Kerr Hamiltonian (107), $\kappa$ is the cavity decay rate, and $t$ is time. Starting with a fixed $\chi$ and tracking increasing $Kt$, we see that $F_{\mathcal{E}}$ quickly decreases to a constant for all codes considered, implying a potentially universal failure of error-correction when $Kt$ is large. However, $F_{\mathcal{E}}$ is minimal at high-symmetry points of the codes (dashed red lines) and maximal in-between. For example, $\frac{1}{2}P_{\mathsf{num}}$ for the num code is three-fold symmetric (see Fig. 1), and $F_{\mathcal{E}}(\mathsf{num})$ is minimal at $Kt$ being the first few multiples of $\nicefrac{{2\pi}}{{3}}$.

unit cell. Upper bounding that integral by integrating the complement of the circle with radius $\sqrt{\nicefrac{{\pi}}{{8}}}$ (instead of the complement of the square with length $\sqrt{\nicefrac{{\pi}}{{8}}}$) yields

$P_{\mathrm{fail}}(\gamma)<\frac{1-\gamma}{\gamma}\int_{|\alpha|\geq\sqrt{\frac{\pi}{8}}}\frac{d^{2}\alpha}{\pi}e^{-\frac{1-\gamma}{\gamma}|\alpha|^{2}}=e^{-\frac{\pi}{8}\frac{1-\gamma}{\gamma}}\,.$ (108)

We remark that this bound can be improved to $e^{-\frac{\pi}{4\sqrt{3}}\frac{1-\gamma}{\gamma}}$ using ideal hexagonal gkp.

## VIII Additional features

### VIII.1 Nonlinearity

We have tried to address the effect of pure loss on our codes, but real-world microwave cavities have undesired unitary evolution (i.e., coherent errors). In general, the joint effect of pure loss and a unitary process on the state depends not only on how many losses have occurred, but also their specific times. The purpose of this subsection is to answer the following:

Does adding coherent errors reduce code performance?

The answer to this, at least in our case, is a firm “yes”.

The coherent (i.e., unitary) error we add is generated by a Kerr nonlinearity with Hamiltonian

$H_{K}\equiv\frac{1}{2}K\hat{n}\left(\hat{n}-1\right)=\frac{1}{2}K\hat{a}^{\dagger 2}\hat{a}^{2}\,,$ (109)

with Kerr parameter $K$. Here, we show what happens when our codes get exposed to the joint evolution of pure loss and Kerr, namely, the channel

$\mathcal{N}_{\chi,Kt}(\cdot)=e^{-iKt\left[\frac{1}{2}\hat{n}(\bar{n}-1),\cdot\right]+\chi\mathcal{D}(\cdot)}\,,$ (110)

where $\mathcal{D}(\cdot)$ is the Lindbladian for the pure loss channel from Sec. I.1. Since the Kerr nonlinearity is prominent in cavities coupled with transmons (as opposed to optical fibers), we use the excitation loss rate $\kappa$ to quantify the strength of pure loss (recall that $\gamma=1-e^{-\kappa t}$). Thus, the two unitless scales of the problem are $\chi\equiv\kappa t$ and $Kt$. An analytic Kraus representation for $\mathcal{N}_{\chi,Kt}$ has yet to be obtained, but various approaches have come close [108; 109].

Figure 9 plots $F_{\mathcal{E}}(Kt,\chi)$ for four code families at $\bar{n}_{\mathsf{code}}\approx 2$. For $Kt=0$ (horizontal axis in each plot), we see the same behavior in $F_{\mathcal{E}}$ vs. pure loss strength as we saw before. For the other extreme of $\chi=0$ (vertical axis), we see unit $F_{\mathcal{E}}$ since Kerr nonlinearity alone is a perfectly correctable unitary process. Starting with a fixed nonzero $\chi$ and looking up at the vertical line of increasing $Kt$, we see that $F_{\mathcal{E}}$ quickly decreases to a (roughly) constant value for all codes. Since the optimal recovery is not able to ascertain exactly when photon loss events occurred, Kerr evolution induces rotations of unknown angle between those events, $e^{-iH_{K}t}\hat{a}\propto\hat{a}e^{i\hat{n}Kt}e^{-iH_{K}t}$, and thus destroys the quantum information. Metrology protocols are also susceptible to this effect [110]. The value to which $F_{\mathcal{E}}$ decreases at large $Kt$ seems to be (roughly) universal across all codes, so there might be a fundamental limit to correcting large $\bar{n}$-dependent coherent errors in the presence of incoherent errors. However, it is still possible to use error-correction to our advantage in, e.g., the $Kt\approx 1$ regime (given $\bar{n}\approx 2$). Incidentally, in that regime, cat shows an increase in $F_{\mathcal{E}}$, implying that a slight amount of Kerr is actually helping cat-code performance. We are investigating this effect in a subsequent publication.

Lastly, we want to mention that $F_{\mathcal{E}}$ for a given code is minimal when $Kt$ is at an angle by which rotating $\frac{1}{2}P_{\mathsf{code}}$ leaves the projection invariant. Recall that evolution under $e^{-iH_{K}t}$ causes a coherent state to transform into cat states at certain rational $t$ [111; 112; 113], but such recurrences are quickly degraded under pure loss [114]. Nevertheless, we see some periodicity in code performance, e.g., in the case of num in the third panel in Fig. 9. From

---

Fig. 1, we know that $\frac{1}{2}P_{\mathrm{num}}$ for this num code is three-fold rotationally symmetric in phase space. Coincidentally, $F_{\mathcal{E}}(\mathrm{num})$ is minimal at $Kt$ being the first few multiples of $2\pi/3$ (dashed red lines) and maximal in-between. We do not know the reason for this effect, but one can see that it occurs for all codes to various extent.

### III.2 Parity measurements

Here, we briefly consider the question

What if we know how many photons were lost?

While microwave cavities still do not have the capability to directly count photons, one can perform non-demolition photon parity measurements of microwave cavity modes [29; 115] and vibrational modes of trapped ions [116]. If we assume that (1) we have a fixed-parity initial state and (2) we can measure parity $(-1)^{\hat{n}}$ during the loss portion of the channel $\mathcal{E}$ perfectly and faster than any timescale of the system, then we can in principle track every loss event $\hat{a}$ without destroying the state. This results in an unraveled [117] system, where part of the knowledge reserved for the environment — the number and times of the loss events — is now learned by the experimenter. For example, a trajectory lasting time $t$ during which jumps occurred at times $\tau_{2}\geq\tau_{1}$ would incur the conditional evolution

$\widetilde{E}_{2}|\psi\rangle\equiv e^{-\frac{1}{2}\kappa(t-\tau_{2})\hat{n}}\hat{a}e^{-\frac{1}{2}\kappa(\tau_{2}-\tau_{1})\hat{n}}\hat{a}e^{-\frac{1}{2}\kappa\tau_{1}\hat{n}}|\psi\rangle\,,$ (10)

where $|\psi\rangle$ is the initial state of the oscillator and we have not yet renormalized the state. Defining $\widetilde{E}_{\ell}$ in similar fashion and permuting all $\hat{a}$’s to the left leaves us with $\widetilde{E}_{\ell}=f_{\ell}E_{\ell}$, where $E_{\ell}$ (4) is the Kraus operator for the pure-loss channel and $f_{\ell}$ is a function of the jump times. Since $f_{\ell}$ is a scalar, knowledge of jump times is irrelevant to error-correction against pure loss, and we can ignore it from now on. We model this process using an extended version of pure loss $\mathcal{N}$ — the quantum instrument [62]

$\widetilde{\mathcal{N}}(\rho)=\sum_{\ell=0}^{\infty}E_{\ell}\rho E_{\ell}^{\dagger}\otimes|\ell\rangle\langle\ell|\,,$ (11)

where $\rho$ is a single-mode density matrix. The second tensor factor represents our knowledge of $\ell$, making sure that each $E_{\ell}\rho E_{\ell}^{\dagger}$ is mapped into an orthogonal subspace of the extended Hilbert space. The corresponding recovery $\mathcal{R}$ has Kraus operators $U_{\ell}^{\mathrm{code}}\otimes\langle\ell|$, with $U_{\ell}^{\mathrm{code}}$ being a unitary mapping $E_{\ell}P_{\mathrm{code}}$ into $P_{\mathrm{code}}$.

We compare $F_{\mathcal{E}}$ (11) with $F_{\widetilde{\mathcal{E}}}$, the fidelity given the extended loss channel $\widetilde{\mathcal{N}}$ (10), in Figs. 10(a) and (b), respectively. Code performance improves for all codes, even the naive $0/1$ Fock state encoding (dashed gray line). Note that, given this extra knowledge, only the diagonal blocks $\epsilon_{\ell\ell^{\prime}}^{\mathrm{code}}$ of the QEC matrix (4) are relevant. The gkps codes have the largest uncorrectable parts in these blocks at this $\bar{n}_{\mathrm{gkps}}$ [see Fig. 10(c)], so their performance increases the least out of all the codes. The num code winds up being the optimal encoding in the eyeball norm, but the parity-tracking procedure described above is not applicable to this code since its states (B2a) are not of fixed parity.

---

## IX Conclusion

The results of this manuscript can be categorized into two parts: one regarding code performance and one regarding code structure. Here, we summarize these results and comment on future directions and open questions.

### IX.1 Code performance

We gave a numerical and analytical performance comparison of the four primary single-mode continuous-variable quantum codes — cat *[13, 15, 27]*, binomial *[23]*, numerically optimized (*[23]* and here), and gkp *[9]* codes — against the pure loss channel with loss rate $\gamma$. For the numerical part, we compared the codes’ ability to preserve entanglement using channel-adapted error correction *[35]* subject to two caveats: the encoding, recovery, and decoding are all assumed perfect and the codes are grouped by their mean occupation number $\bar{n}_{\texttt{code}}\leq 2,5,10$. For the analytical part, we calculated the quantum error-correction (QEC) conditions for cat, bin, and gkp. We briefly discuss our results below, but encourage the reader to peruse Sec. II for more details.

Even though cat and bin follow the traditional convention of correcting exactly against a subset of errors, their performance is significantly worse than that of gkp for many $\gamma$. While gkp do not exactly correct against any errors, we find that the violation of the QEC conditions for each error is insignificant compared to the violation of the leading-order uncorrectable errors for cat and bin for most $\bar{n}_{\texttt{code}}$.

In the limit of vanishing $\gamma$, we observe the following order of performance: gkp $<$ cat $<$ bin $<$ num. On the one hand, since cat and bin codes correct exactly against the first few errors, their performance scales polynomially with $\gamma$. We further reveal the regions in the $\{\gamma,\bar{n}_{\texttt{code}}\}$ parameter space in which bin codes outperform cat codes. On the other hand, we analytically show that gkp code entanglement infidelity is $O(e^{-\frac{c}{\gamma}})$ (with $c$ a constant dependent on the type of gkp code).

As $\gamma$ increases, gkp quickly overpowers the rest of the codes and their performance persists even for high $\gamma$. For example, optimal recovery of a gkp state with 10 photons on average yields a fidelity of 99.5% given $\gamma\approx 20\%$, compared to a fidelity of 96.9% for bin and 96.6% for cat. At $\gamma\approx 30\%$, where about one in every three photons are lost, the fidelity of gkp is still 95%, which is 5% higher than that of cat and bin. At such high $\gamma$, we observed the following order of performance: bin $\lesssim$ cat $<$ num $<$ gkp.

We extended our analysis of entanglement preservation to determine achievable rates of quantum communication using these codes, where we saw similar orders of performance. We also show that sending a gkp state with an average occupation number of two photons produces a higher communication rate than distributing two photons among four modes using the smallest encoding protecting against one loss error.

Relaxing the $\bar{n}_{\texttt{code}}$ constraint, we have numerical evidence showing that performance of gkp codes and a subset of bin codes increases with increasing $\bar{n}_{\texttt{code}}$. Since the ideal gkp states indeed have infinite $\bar{n}_{\texttt{gkp}}$, it is reasonable that their performance increases monotonically as they become more ideal. To back this claim analytically, we cook up a simple recovery procedure involving phase-insensitive amplification that converts the pure-loss channel into Gaussian noise; this procedure can also be used in multimode extensions of gkp codes *[54]*. The bin increase in performance can be justified by showing they have a larger set of approximately correctable errors than previously thought; we do so in Secs. VI.1-VI.2.

We added a unitary error in the form of a Kerr nonlinearity $K$ in order to see how code performance is changed. We observed that cat code performance increases slightly at small $K$ and that all code performance oscillates with periods depending on their symmetries; these are subjects of future investigation. We also observed that, at sufficiently large $K$, the performance of all codes fails at about the same rate, signaling the need to keep such coherent errors low in a real device. We also briefly addressed changes in code performance if one is able to learn how many photons were lost.

There are obvious generalizations of this analysis to other multi-mode codes mentioned in the introduction, storing multiple qubits worth of information; we are currently pursuing some of them. Another direction has to do with having gkp and bin codes catch up to cat codes in terms of experimental realizability. While gkp codes may have been considered by some to be unphysical in the past, recent technological advances in, e.g., microwave cavity *[118]*, atomic ensemble *[119, 120]*, or trapped ion *[121]* control, suggest that making these states may be within reach. In fact, there are recent theoretical proposals related to making and maintaining gkp states in two of the aforementioned technologies *[106, 122]* (see Refs. *[123, 124, 125, 126, 127, 128]* for other proposals) and a related trapped-ion experiment *[129]*. While the comparison offered here is completely free from consideration of experimental imperfections, we hope that our conclusions will motivate the community to pursue quantum information processing and communication schemes with bin and gkp states.

### IX.2 Code structure

We discussed a connection between bin codes and spin-coherent states and used it to characterize related two-mode binomial codes as well as multi-qubit permutation-invariant codes *[73]*. This connection yields a check operator for bin dephasing errors, and we discussed an error-correction scheme that utilizes this operator. This connection was also extended to qudit versions of the aforementioned codes, yielding a generalization of spin-

---

coherent states and a check operator for qudit codes.

By mapping the coefficients of the qudit bin code into a particular subspace of multiple qudits, we introduced a multi-qudit (i.e., discrete variable) code that extends the multi-qubit permutation-invariant codes. The extension, which we call perm^{′} in order to differentiate it from another extension *[75]*, turns out to be nothing but a multi-qudit bit-flip code when expressed in the basis of products of the individual qudit states. However, when expressed in terms of a qudit extension of Dicke states, the coefficients next to those states match those of the qudit binomial codes. This relates the protection of the continuous-variable binomial codes to that of a discrete-variable bit-flip code. A similar bit-flip-like trick was used for another code — the noon code *[22]* — where two-mode noon states and their multi-mode generalizations were tensored together to form codes protecting against pure loss. Such intriguing connections between discrete- and continuous-variable codes should be investigated further. In addition, the generalization of spin-coherent states introduced here may be useful in experimental settings such as atomic ensembles (e.g., *[120, 130]*) and magnetometry (e.g., *[131, 132, 133]*).

###### Acknowledgements.

The authors acknowledge Steven T. Flammia, David Poulin, Saikat Guha, Richard Kueng, Mazyar Mirrahimi, John Preskill, R. J. Schoelkopf, Matti Silveri, Murphy Yuezhen Niu, and Bei Zeng for enlightening discussions. V.V.A. thanks Misha Guy and the Yale Center for Research Computing for resources and support and acknowledges support from the Walter Burke Institute for Theoretical Physics at Caltech. V.V.A., K.N., C.S., L.L., and L.J. acknowledge support through the ARL-CDQI, ARO (Grants No. W911NF-14-1-0011 and No. W911NF-14-1-0563), ARO MURI (W911NF-16-1-0349), NSF (EFMA-1640959), AFOSR MURI (FA9550-14-1-0052 and FA9550-15-1-0015), the Alfred P. Sloan Foundation (BR2013-049), the Packard Foundation (2013-39273). K.D., C.V., and B.M.T. acknowledge support through the ERC Consolidator Grant (682726). S.M.G. acknowledges support through the NSF (DMR-1609326) and ARO (W911NF1410011).

## Appendix A The many faces of channel fidelity

A well-known property of $F_{\mathcal{E}}$ is the relation to the average input-output fidelity of $\mathcal{E}$ *[134]* (see also *[135]*),

$\int d\psi\langle\psi|\mathcal{E}(|\psi\rangle\langle\psi|)|\psi\rangle=\frac{dF_{\mathcal{E}}+1}{d+1}\,,$ (10)

where $d$ is the dimension of the system. Above, $\langle\psi|\mathcal{E}(|\psi\rangle\langle\psi|)|\psi\rangle$ is the input-output fidelity for some initial state $|\psi\rangle$ of the source qubit and $d\psi$ is a uniform distribution over all pure states. Due to the above equality, one should not be surprised that the capacity of entanglement transmission determined by $F_{\mathcal{E}}$ is equivalent to the capacity of pure state preservation determined by the input-output fidelity *[136]*. In addition, since $F_{\mathcal{E}}$ is a fidelity between two states, it gives rise to a metric, is stable under addition of ancillary systems, and satisfies the chaining property (meaning that it can be used to provide a bound on the error of a larger quantum computation). These properties can be proven using Ref. *[137]*, where $F_{\mathcal{E}}=F_{\mathrm{pro}}(\mathcal{E},\mathcal{I})$.

The channel fidelity can be related to the worst-case input-output fidelity $\min_{|\psi\rangle}\langle\psi|\mathcal{E}(|\psi\rangle\langle\psi|)|\psi\rangle$ *[138]*,

$1-d\sqrt{1-F_{\mathcal{E}}^{2}}\leq\min_{|\psi\rangle}\langle\psi|\mathcal{E}(|\psi\rangle\langle\psi|)|\psi\rangle\,.$ (11)

The dependence of the bound on the dimension as well as the square of $F_{\mathcal{E}}$ suggests that $F_{\mathcal{E}}$ is not a good measure of the worst case scenario. There is indeed a discrepancy between average and worst-case behavior for channels that contain a combination of coherent and incoherent noise *[139, 140]*. Such an example here is pure loss with an additional Kerr nonlinearity, considered in Sec. VIII. However, the pure loss channel alone contains only incoherent noise and so $F_{\mathcal{E}}$ is a reasonable marker of even worst-case behavior; moreover, one can prove that the dimension dependence goes away entirely *[141]*. Note that Eq. (11) was derived starting from the worst-case infidelity $1-\min_{|\psi\rangle}\langle\psi|\mathcal{E}(|\psi\rangle\langle\psi|)|\psi\rangle$, applying the Fuchs–van de Graaf inequalities *[142]* to convert the infidelity to the maximum trace distance $\max_{|\psi\rangle}\|(\mathcal{E}-\mathcal{I})(|\psi\rangle\langle\psi|)\|_{\mathrm{tr}}$ (with $\|A\|_{\mathrm{tr}}\equiv\mathrm{Tr}\{\sqrt{A^{\dagger}A}\}$), upper-bounding said trace distance by its stabilized version $\max_{|\psi\rangle}\|(\mathcal{E}\otimes\mathcal{I}-\mathcal{I}^{\otimes 2})(|\psi\rangle\langle\psi|)\|_{\mathrm{tr}}$ (i.e., the diamond norm), upper-bounding the diamond norm by the trace norm $d\|\rho_{\mathcal{E}}-\rho_{\mathcal{I}}\|_{\mathrm{tr}}$ between the Choi matrices of $\mathcal{E}$ and $\mathcal{I}$ using Lemma 7 from Refs. *[143, 144]* (this is where the $d$-dependence comes in), and once again applying Fuchs–van de Graaf to turn the trace norm into $d\sqrt{1-F_{\mathcal{E}}^{2}}$.

An information-theoretic property of $F_{\mathcal{E}}$ is its presence in the quantum Fano inequality *[145]* (see also *[81]*, Thm. 12.9). This is an upper bound on the von Neumann entropy of $\rho_{\mathcal{E}}$,

$H(\rho_{\mathcal{E}})\leq H(\{F_{\mathcal{E}},1-F_{\mathcal{E}}\})+(1-F_{\mathcal{E}})\log_{2}(d^{2}-1)\,,$ (12)

where $H(\rho_{\mathcal{E}})=-\mathrm{Tr}\{\rho_{\mathcal{E}}\log_{2}\rho_{\mathcal{E}}\}$. The entropy $H(\rho_{\mathcal{E}})$ is also called the entropy exchange since it quantifies the entropy gained by the environment responsible for the non-unitary nature of $\mathcal{E}$. There is also the anti-Fano inequality *[36]*, a lower bound on $F_{\mathcal{E}}$ in terms of the entropy,

$F_{\mathcal{E}}\geq e^{-2H(\rho_{\mathcal{E}})}\,.$ (13)

A similar relation to information-theoretic quantities can be made regarding a specific error map — the erasure channel. Let us divide $\mathsf{B}$ into two regions, $\mathsf{B}_{1}$ and $\mathsf{B}_{2}$, and

---

trace over $\mathsf{B}_{2}$. Then, the $F_{\mathcal{E}}$ given the optimal recovery which reconstructs $\mathsf{B}_{2}$ using only $\mathsf{B}_{1}$ satisfies

$F_{\mathcal{E}}\geq e^{-\frac{1}{2}I(\mathsf{A};\mathsf{B}_{2}|\mathsf{B}_{1})}\,,$ (10)

where $I(\mathsf{A}:\mathsf{B}_{2}|\mathsf{B}_{1})$ is the conditional mutual information quantifying correlations between $\mathsf{A}$ and $\mathsf{B}_{2}$ given information from $\mathsf{B}_{1}$ *[146]*. In this context, $F_{\mathcal{E}}$ is also called the fidelity of recovery *[147]*.

From yet another information theory perspective (*[41]*, Thm. 2), the optimal $F_{\mathcal{E}}$ yields the equality

$dF_{\mathcal{E}}=2^{-H_{\min}(\mathsf{B}|\mathsf{A})_{\mathcal{NS}}}\,,$ (11)

where $H_{\min}\left(\mathsf{B}|\mathsf{A}\right)_{\mathcal{NS}}$ is the conditional min entropy of the Choi matrix $\rho_{\mathcal{NS}}$ (9) of the encoding and loss portions of $\mathcal{E}$. This inequality can be adapted from the equation below Eq. (4.5) in Ref. *[42]* by noting that $\mathcal{R}^{\dagger}\mathcal{S}$ is a unital map. In this context, $\mathsf{A}$ and $\mathsf{B}$ (of dimensions $\infty$ and two, respectively) share a state $\rho_{\mathcal{NS}}=\mathcal{NS}\otimes\mathcal{I}(|\Psi\rangle\langle\Psi|)$, and $H_{\min}\left(\mathsf{B}|\mathsf{A}\right)_{\mathcal{NS}}$ is the most conservative way to quantify the uncertainty about the state of $\mathsf{B}$ after the state of $\mathsf{A}$ is sampled.

## Appendix B Numerical benchmarking details

The parameters for the specific members of the cat/bin/gkps/gkp code families that optimize $F_{\mathcal{E}}(\gamma)$ in Fig. 2 are given in Table 4.

There are a total of five num codes, organized by their approximate mean occupation number

$\bar{n}_{\mathsf{num}}\in\left\{1.562,2.696,2.770,4.149,4.336\right\}.$ (12)

Interestingly, the first code — the $\sqrt{17}$ code *[23]* — can be expressed as

$|0^{\bar{n}\approx 1.562}_{\mathsf{num}}\rangle$ $=\tfrac{1}{\sqrt{6}}\left(\sqrt{7-\sqrt{17}}|0\rangle+\sqrt{\sqrt{17}-1}|3\rangle\right),$ (13a)
$|1^{\bar{n}\approx 1.562}_{\mathsf{num}}\rangle$ $=\tfrac{1}{\sqrt{6}}\left(\sqrt{9-\sqrt{17}}|1\rangle-\sqrt{\sqrt{17}-3}|4\rangle\right).$ (13b)

All five code states are listed in the ancillary Mathematica notebook accompanying this manuscript on the arXiv. The $\bar{n}_{\mathsf{num}}\in\{1.562,2.696,4.149\}$ codes are from Ref. *[23]* while the $\bar{n}_{\mathsf{num}}\in\{2.770,4.336\}$ codes were obtained here using a different optimization routine, described as follows. In order to find logical states $|\mu_{\mathsf{num}}\rangle$ for $\mu\in\{0,1\}$ which allow for the correction of error operators $e_{\ell}\in\{I,\hat{a},\hat{a}^{2}\}$, we create a cost function from the QEC matrix $f_{\mu\nu\ell\ell^{\prime}}=\langle\mu_{\mathsf{num}}|e^{\dagger}_{\ell}e_{\ell^{\prime}}|\nu_{\mathsf{num}}\rangle$, $c_{1}=\sum_{\ell,\ell^{\prime}}|f_{00\ell\ell^{\prime}}-f_{11\ell\ell^{\prime}}|^{2}+|f_{01\ell\ell^{\prime}}|^{2}.$ In order to prefer lower occupation, the penalty $c_{2}=\lambda_{\bar{n}}\bar{n}_{\mathsf{num}}$ is introduced with $\lambda_{\bar{n}}=10^{-3}$. Code words are produced by numerically optimizing the total cost over complex unit vectors:

$\underset{|\psi_{0}\rangle,|\psi_{1}\rangle\in\mathbb{C}^{N_{\max}}}{\text{minimize}}\hskip 5.69046ptc_{1}+c_{2}\,,$ (14)

where $N_{\max}$ is the Fock space cutoff. The $\sqrt{17}$ code is the only code below $\bar{n}_{\mathsf{num}}=2$. For $\bar{n}_{\mathsf{num}}\leq 5,10$, the best-performing code for $\gamma\leq 0.3935$ is $\mathsf{num}(4.149)$, for $\gamma=0.4084$ is $\mathsf{num}(2.770)$, and for $\gamma\geq 0.4231$ is the $\sqrt{17}$ code. We were unable to find good codes with $\bar{n}_{\mathsf{num}}>5$ due to the prominence of shallow local minima.

For the numerical comparison, we swept all values of the code parameters for $\mathsf{cat}(\alpha,S)$, $\mathsf{bin}(N,S)$, $\mathsf{num}(\bar{n})$, and $\mathsf{gkps}(\Delta)$ subject to the energy constraints. For $\mathsf{gkp}(\Delta,a)$, we only considered values of $\Delta$ which gave $\bar{n}_{\mathsf{gkp}}\approx 2$, $5$, or $10$ (since we knew from the $\mathsf{gkps}$ calculations that increasing $\bar{n}$ generally increased $F_{\mathcal{E}}$ for all but the largest values of $\gamma$). We also did not consider all possible non-rectangular lattices, but instead implemented a subset of them by sweeping the lattice parameter $a\in[1,2]$ in the following coherent-state representation for the shifted non-square $\mathsf{gkp}$ code states:

$|\mu^{\text{shift}}_{\mathsf{gkp}}\rangle$ $\propto\sum_{\vec{n}\in\mathbb{Z}}(-1)^{\mu n_{1}}\,e^{-i\frac{\pi}{2}n_{2}(2n_{1}+\mu)}e^{-\frac{\pi a}{4}\Delta^{2}\left[(2n_{1}+\mu)^{2}+(\frac{2}{a}n_{2})^{2}\right]}\left|\frac{\sqrt{\pi a}}{2}\left(2n_{1}+\mu+i\frac{2}{a}n_{2}\right)\right\rangle\,.$ (15)

The $\Delta\to 0$ states are stabilized by

$S_{\mathbf{x}}=-D_{\sqrt{\frac{\pi a}{2}}\left(1+i\frac{2}{a}\right)}\hskip 14.22636pt\text{and}\hskip 14.22636ptS_{\mathbf{p}}=D_{4i\sqrt{\frac{\pi}{2a}}}.$

The resulting code lattice formed by $\frac{1}{2}P^{\text{shift}}_{\mathsf{gkp}}$ is shifted, retaining its error-correcting properties but not having a lattice point at the origin. Both shifted and unshifted lattices are used in the numerics, but only unshifted lattices are used for analytical calculations in Appx. D. Note that $|0^{\text{shift}}_{\mathsf{gkp}}\rangle$ is odd while $|1^{\text{shift}}_{\mathsf{gkp}}\rangle$ is even under parity $(-1)^{\bar{n}}$, so there is no spacing $S$.

Since $\mathsf{cat}$ and $\mathsf{gkp}$ code states are formally superpositions of an infinite number of Fock states, we have to truncate them and use a finite Fock state superposi

---

|  γ | ncode ≤ 2  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|   | cat | bin | gkps | gkp |  |   |
|   | α | S | N | S | Δ | a  |
|  0.0124 | 1.440 | 1 | 1 | 1 | 0.481 | 0.477  |
|  0.0247 | 1.440 | 1 | 1 | 1 | 0.481 | 0.477  |
|  0.0488 | 1.396 | 1 | 1 | 1 | 0.481 | 0.477  |
|  0.0723 | 1.369 | 1 | 1 | 1 | 0.481 | 0.477  |
|  0.0952 | 1.351 | 1 | 1 | 1 | 0.481 | 0.477  |
|  0.1175 | 1.332 | 1 | 1 | 1 | 0.481 | 0.477  |
|  0.1393 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.1605 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.1813 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.2015 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.2212 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.2404 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.2592 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.2775 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.2953 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.3127 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.3297 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.3462 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.3624 | 1.508 | 2 | 1 | 1 | 0.481 | 0.477  |
|  0.3781 | 1.194 | 1 | 0 | 0 | 0.481 | 0.477  |
|  0.3935 | 1.183 | 1 | 0 | 0 | 0.481 | 0.477  |
|  0.4084 | 1.173 | 1 | 0 | 0 | 0.481 | 0.477  |
|  0.4231 | 1.173 | 1 | 0 | 0 | 0.481 | 0.510  |
|  0.4373 | 1.162 | 1 | 0 | 0 | 0.500 | 0.659  |
|  0.4512 | 0 | 0 | 0 | 0 | 0.535 | 0.659  |
|  0.4647 | 0 | 0 | 0 | 0 | 0.577 | 0.913  |
|  0.4780 | 0 | 0 | 0 | 0 | 0.632 | 0.933  |
|  0.4908 | 0 | 0 | 0 | 0 | 0.632 | 0.953  |
|  0.5034 | 0 | 0 | 0 | 0 | 0.632 | 0.976  |
|  ncode ≤ 5  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
|  cat | bin |   | gkps |   | gkp  |
|  α | S | N | S | Δ | Δ  |
|  1.739 | 2 | 2 | 2 | 0.309 | 0.309  |
|  1.746 | 2 | 2 | 2 | 0.309 | 0.309  |
|  1.962 | 3 | 1 | 2 | 0.309 | 0.309  |
|  1.969 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.975 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.981 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.987 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.994 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.994 | 3 | 1 | 3 | 0.309 | 0.309  |
|  2.000 | 3 | 1 | 3 | 0.309 | 0.309  |
|  2.000 | 3 | 1 | 3 | 0.309 | 0.309  |
|  2.000 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.994 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.994 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.987 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.981 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.975 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.969 | 3 | 1 | 3 | 0.309 | 0.309  |
|  1.643 | 2 | 1 | 3 | 0.309 | 0.309  |
|  1.636 | 2 | 1 | 2 | 0.316 | 0.312  |
|  1.628 | 2 | 1 | 2 | 0.392 | 0.394  |
|  1.612 | 2 | 1 | 2 | 0.471 | 0.510  |
|  1.162 | 1 | 0 | 0 | 0.500 | 0.659  |
|  0 | 0 | 0 | 0 | 0.535 | 0.659  |
|  0 | 0 | 0 | 0 | 0.577 | 0.913  |
|  0 | 0 | 0 | 0 | 0.632 | 0.933  |
|  0 | 0 | 0 | 0 | 0.632 | 0.953  |
|  0 | 0 | 0 | 0 | 0.632 | 0.976  |
|  ncode ≤ 10  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
|  cat | bin |   | gkps |   | gkp  |
|  α | S | N | S | Δ | Δ  |
|  2.890 | 3 | 3 | 4 | 0.221 | 0.221  |
|  2.890 | 3 | 3 | 4 | 0.221 | 0.221  |
|  3.162 | 4 | 2 | 4 | 0.221 | 0.221  |
|  3.162 | 4 | 2 | 5 | 0.221 | 0.221  |
|  1.975 | 3 | 2 | 5 | 0.221 | 0.221  |
|  1.981 | 3 | 2 | 5 | 0.221 | 0.221  |
|  1.987 | 3 | 2 | 5 | 0.221 | 0.221  |
|  1.994 | 3 | 2 | 5 | 0.221 | 0.221  |
|  2.000 | 3 | 2 | 5 | 0.221 | 0.221  |
|  2.000 | 3 | 2 | 5 | 0.221 | 0.221  |
|  2.000 | 3 | 1 | 3 | 0.221 | 0.221  |
|  2.000 | 3 | 1 | 3 | 0.221 | 0.221  |
|  1.994 | 3 | 1 | 3 | 0.221 | 0.221  |
|  1.994 | 3 | 1 | 3 | 0.221 | 0.221  |
|  1.987 | 3 | 1 | 3 | 0.221 | 0.221  |
|  1.981 | 3 | 1 | 3 | 0.221 | 0.221  |
|  1.975 | 3 | 1 | 3 | 0.221 | 0.221  |
|  1.969 | 3 | 1 | 3 | 0.221 | 0.221  |
|  1.643 | 2 | 1 | 3 | 0.246 | 0.243  |
|  1.636 | 2 | 1 | 2 | 0.316 | 0.312  |
|  1.628 | 2 | 1 | 2 | 0.392 | 0.394  |
|  1.612 | 2 | 1 | 2 | 0.471 | 0.510  |
|  1.162 | 1 | 0 | 0 | 0.500 | 0.659  |
|  0 | 0 | 0 | 0 | 0.535 | 0.659  |
|  0 | 0 | 0 | 0 | 0.577 | 0.913  |
|  0 | 0 | 0 | 0 | 0.632 | 0.933  |
|  0 | 0 | 0 | 0 | 0.632 | 0.953  |
|  0 | 0 | 0 | 0 | 0.632 | 0.976  |

Table IV. Code parameters for the code giving the highest  $F_{\mathcal{E}}$  (1.11) out of all codes of a given code family with the constraint  $\bar{n}_{\mathrm{code}} \leq 2, 5, 10$  and a given loss rate  $\gamma$  (1.3). The first column lists the  $\gamma$ 's sampled while the next three sets of seven columns give the code parameters for  $\operatorname{cat}(\alpha, S)$  (5.1),  $\operatorname{bin}(N, S)$  (6.1),  $\operatorname{gkps}(\Delta)$  (7.8), and  $\operatorname{gkp}(\Delta, a)$  (B4). Each of the three sets corresponds to one of the three energy constraints. Optimal code values below  $\gamma \leq 0.0124$  do not change significantly and so are not shown. For  $\gamma \geq 0.4512$ , a small  $\bar{n}$  is preferable for all codes and optimal cat and bin switch to encoding into the first two Fock states. For  $\bar{n}_{\mathrm{gkp}} \leq 10$  and  $\gamma \leq 0.05$ , denoted with the  $^n$  symbol in the last column, we bound  $F_{\mathcal{E}}$  with the channel fidelity  $F_{\mathcal{E}}^{\mathrm{QR}}$  that uses the quadratic recovery  $\mathcal{R}^{\mathrm{QR}}$  [148] (see also [149, 150]) for unshifted hexagonal  $\mathrm{gkp}$  (7.8) because  $F_{\mathcal{E}}$  decreases significantly around that regime due to numerical precision limitations of the optimization. We also use  $F_{\mathcal{E}}^{\mathrm{QR}}$  to bound  $F_{\mathcal{E}}$  in Sec. VI B.

tion  $\sum_{n = 0}^{N_{\mathrm{max}}}c_n|n\rangle$  for each logical state. We picked  $N_{\mathrm{max}}$  such that  $\sum_{n = 0}^{N_{\mathrm{max}}}|c_n|^2\geq 0.99999$  for both logical states. For gkps/gkp code states, we used the coherent state representation and picked only the lattice points values  $s,t\leq \lfloor 4 / \Delta \rfloor$  . The codes were generated with MATHEMATICA while the semidefinite program was executed using the CVX package [151] in MATLAB, with the MATLAB add-on [152] for MATHEMATICA acting as the bridge. Helpful routines were borrowed from Toby S. Cubitt [153].

# Appendix C: Qudit bin and bin2 codes

Here we extend the analogy from Sec. VIC between bin codes and spin-coherent states to qudit bin codes, introducing a new multi-qudit code  $\text{perm}'$  in the process and eventually yielding a logical  $X_{\text{code}}$ -operator and a check operator for the qudit bin [23] and bin2 codes. We consider the following generalization of spin-coherent

---

![img-27.jpeg](images/img-27.jpeg)
Figure 11. Overlap  $|J\langle \theta ,\phi |\frac{\pi}{2},\frac{2\pi}{d}\mu \rangle_{J,d}|^2$  vs.  $\theta ,\phi$  (in radians) for qudit states  $|\frac{\pi}{2},\frac{2\pi}{d}\mu \rangle_{J,d}$  (C1) with  $\mu = 0$  and  $d,N$  picked such that the spin  $J = \frac{1}{2} (d - 1)(N + 1) = 12$ . These states resemble spin-squeezed states and characterize the qudit bin and bin2 codes (see Appx. C). For fixed  $J$ , the degree of squeezing increases with  $d$ .

states (6.10),

$$
\left| \theta , \phi \right\rangle_ {J, d} = \sum_ {m = 0} ^ {2 J} \frac {\sqrt {\binom {N + 1} {m}} _ {d} e ^ {i \phi m} \tan^ {2 m} \frac {d - 1}{d} \theta}{\sqrt {\left(\sum_ {\mu = 0} ^ {d - 1} \tan^ {2 \mu} \frac {d - 1}{d} \theta\right) ^ {N + 1}}} | J, m - J \rangle , \tag {C1}
$$

where  $|J, m - J\rangle$  is the spin basis of a spin  $J = \frac{1}{2} (d - 1)(N + 1)$ , and  $\binom{N+1}{m}_d$  are extended binomial coefficients [154] (also called polynomial coefficients [155]), defined by

$$
\left(1 + x + \dots + x ^ {d - 1}\right) ^ {N + 1} = \sum_ {m = 0} ^ {(d - 1) (N + 1)} \binom {N + 1} {m} _ {d} x ^ {m}. \tag {C2}
$$

(Note a similar generalization in the proof of Ref. [75], Thm. 1.2). For  $d = 2$ ,  $\{|\frac{\pi}{2}, \pi \mu \rangle_{J,d=2}\}_{\mu=0}^{1}$  reduce to the two antipodal spin-coherent states discussed in the main text. In general, the  $d$  states  $\{|\frac{\pi}{2}, \frac{2\pi}{d} \mu \rangle_{J,d}\}_{\mu=0}^{d-1}$  are similar to squeezed spin-coherent states equidistantly distributed along the equator of the Bloch sphere. For a fixed  $J$ , the amount of squeezing increases with increasing  $d$ , as shown in an example in Fig. 11. This is sensible since increasing  $d$  for fixed  $J$  means fitting more quantum information in the same amount of space.

Mapping the basis  $|J, m - J\rangle$  to Fock states  $|(S + 1)m\rangle$  or two-mode Fock states

$$
\left| (S + 1) \left[ (d - 1) (N + 1) - m \right], (S + 1) m \right\rangle
$$

yields qudit versions of bin and bin2, respectively, for general parameters  $N,S$ . It was shown in Ref. [23] that qudit bin codes can protect to order  $O(\gamma^{N})$  against dephasing and  $O(\gamma^{S})$  against loss. We do not prove this for bin2 here, but anticipate this to also be the case for

those codes. Observing the protection offered by noon codes [22], it is also reasonable to believe that tensor products  $\left| \frac{\pi}{2}, \frac{2\pi}{d} \mu \right\rangle_{J,d}^{\otimes M}$  (with  $|J, m - J\rangle$  mapped to one-or two-mode Fock states) will yield yet another class of multi-mode codes. Regarding the multi-qubit mapping, we introduce  $\text{perm}'$  — a new extension of qubit perm codes to quubits. These codes can be obtained by mapping  $|J, m - J\rangle$  to a qudit generalization of Dicke states  $|D_{m}^{N+1}\rangle$  that we denote as the extended binomial states  $|E_{m}^{d-1,N+1}\rangle$ , i.e.,

$$
\left| \mu_ {\text {p e r m} ^ {\prime}} \right\rangle = \sum_ {m = 0} ^ {(d - 1) (N + 1)} \frac {e ^ {i \frac {2 \pi}{d} \mu m}}{\sqrt {d ^ {N + 1}}} \sqrt {\binom {N + 1} {m}} _ {d} \left| E _ {m} ^ {d - 1, N + 1} \right\rangle . \tag {C3}
$$

The states  $|E_m^{d-1,N+1}\rangle$  are defined as normalized equal superpositions of all multi-qudit states having a total of  $m$  excitations distributed over  $N+1$  qubits,

$$
\left| E _ {m} ^ {d - 1, N + 1} \right\rangle = \frac {1}{\sqrt {\binom {N + 1} {m}} _ {d}} \sum_ {\substack {v _ {1}, \dots , v _ {N + 1} = 0 \\ \sum_ {i} v _ {i} = m}} ^ {d - 1} \left| v _ {1}, \dots , v _ {N + 1} \right\rangle . \tag{C4}
$$

The normalization of these states happens to be exactly the extended binomial coefficient because  $\binom{N+1}{m}_d$  is, by definition, the number of ways of obtaining  $m$  as the sum of  $N+1$  independent random variables which take values from 0 to  $d-1$  [155].

The code perm' is different from the qudit perm codes [75] because those utilize a different generalization of qubit Dicke states. For example, extended binomial states for  $d = 3$  and  $N = 1$  are

$$
\left| E _ {0} ^ {2, 2} \right\rangle = | 0 0 \rangle , \quad \left| E _ {1} ^ {2, 2} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 1 \right\rangle + \left| 1 0 \right\rangle\right), \quad (\mathrm {C} 5 \mathrm {a})
$$

$$
\left| E _ {2} ^ {2, 2} \right\rangle = \frac {1}{\sqrt {3}} \left(\left| 0 2 \right\rangle + \left| 1 1 \right\rangle + \left| 2 0 \right\rangle\right), \tag {C5b}
$$

$$
\left| E _ {3} ^ {2, 2} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 2 1 \right\rangle + \left| 1 2 \right\rangle\right), \quad \left| E _ {4} ^ {2, 2} \right\rangle = \left| 2 2 \right\rangle . \tag {C5c}
$$

In contrast, qudit Dicke states [75] are superpositions of a multi-qudit state which has a fixed number of excitations for each qudit and all of that state's permutations. For the above case, the qudit Dicke states are  $|E_0^{2,2}\rangle$ ,  $|E_1^{2,2}\rangle$ ,  $|E_3^{2,2}\rangle$ ,  $|E_4^{2,2}\rangle$  along with  $\frac{1}{\sqrt{2}}(|02\rangle + |20\rangle)$  and  $|11\rangle$ . In the general case of  $N + 1$  qubits, there are  $\binom{N+d}{d-1}$  qudit Dicke states while only  $(d-1)(N+1)+1$  extended binomial states. While the qudit Dicke states span the entire fully symmetric  $N + 1$ -qudit subspace, extended binomial states span only a subspace of that subspace. After introduction of a spacing  $S \neq 0$  in similar fashion to perm codes (see Sec. VIC 2), it may be that  $|\mu_{\mathrm{perm}'}\rangle$  protects against multi-qubit amplitude damping, but such properties have yet to be proven.

We conclude this section by relating  $\text{perm}'$  to eigenstates of an  $N$ -qudit generalization of an  $N$ -qubit collective spin operator. This reveals that such codes are

---

closely related to bit-flip codes and provides a check operator for qudit bin and bin2 codes.

### C.1 Relating perm^{′} codes to bit-flip codes

We start with the spin-coherent states from Sec. VI (i.e., $d=2$) written in the irrep for which $J_{x}$ is a collective operator for a $2J=M$-qubit system with $S=0$. In other words, $J_{x}=\frac{1}{2}\sum_{k=1}^{M}X_{k}$, where $X_{k}$ is the Pauli matrix of the $k$th qubit. For those parameters, the qubit states $\ket{\mu_{\texttt{perm}}}$ in this irrep are simply tensor products of eigenstates $\ket{(-1)^{\mu}}_{k}$ of $X_{k}$,

$\ket{\mu_{\texttt{perm}}}=\bigotimes_{k=1}^{M}\ket{(-1)^{\mu}}_{k}=\frac{1}{\sqrt{2^{M}}}\bigotimes_{k=1}^{M}\left[\ket{0}_{k}+(-1)^{\mu}\ket{1}_{k}\right]$ (10)

with $X_{k}\ket{(-1)^{\mu}}_{k}=(-1)^{\mu}\ket{(-1)^{\mu}}_{k}$. Proving this is simple if one writes out $\bigotimes_{k=1}^{M}\ket{(-1)^{\mu}}_{k}$ in terms of the Dicke states $\{\ket{D_{m}^{M}}_{m}\}_{m=1}^{M}$. Observe that, after performing all tensor products, $\ket{\mu_{\texttt{perm}}}$ will consist of an equal linear superposition of multi-qubit states (denoted by binary strings) with coefficients $\pm 1/\sqrt{2^{M}}$. To change basis to Dicke states, we group multi-qubit states by their total number of excitations (i.e., the number of $1$’s in each binary string). For $m$ excitations out of $M$ qubits, the number of such states is $\binom{M}{m}$. Moreover, since each additional excitation brings about an additional factor of $-1$, all states with the same number of excitations have matching coefficients. Thus, we can group each superposition of states with fixed excitations into unnormalized Dicke states. Multiplying and dividing each unnormalized Dicke state by $\binom{M}{m}^{-1/2}$ yields the original form of $\ket{\mu_{\texttt{perm}}}$ in Eq. (11).

We can now generalize the above setup to qudits. Consider $M$ qudits of dimension $d$ and let

$X=\sum_{\nu=0}^{d-1}\ket{\nu}\bra{\nu+1\text{ mod }d}$ (11)

now be the shift operator for a qudit (i.e., defined such that $X\ket{d-1}=\ket{0}$). This $X$ has $d$ eigenstates

$\ket{e^{i\frac{2\pi}{d}\mu}}=\frac{1}{\sqrt{d}}\sum_{\nu=0}^{d-1}e^{i\frac{2\pi}{d}\mu\nu}\ket{\nu}$ (12)

(with $\mu\in\{0,1,\cdots,d-1\}$) whose eigenvalues are $e^{i\frac{2\pi}{d}\mu}$. Using the same procedure as above, one can consider tensor products of $\ket{e^{i\frac{2\pi}{d}\mu}}$,

$\ket{\mu_{\texttt{perm}^{\prime}}}=\left(\ket{e^{i\frac{2\pi}{d}\mu}}\right)^{\otimes M},$ (13)

and express them in the extended binomial basis. Now, $\ket{\mu_{\texttt{perm}^{\prime}}}$ consists of equal superpositions of multi-qudit states with coefficients $\{e^{i\frac{2\pi}{d}\mu\nu}/\sqrt{d^{M}}\}_{\nu=0}^{d-1}$, but the coefficients in front of multi-qudit states of fixed total excitation match. The normalization of $\ket{E_{m}^{d-1,M}}$ is the square root of the number of multi-qudit states in $\ket{E_{m}^{d-1,M}}$, which we have already defined to be $\binom{M}{m}_{d^{\prime}}$. This yields the perm^{′} code states from Eq. (10) with $M=N+1$.

An important consequence of the above description is that now all qudit codes $\in\{\texttt{bin},\texttt{bin2}\}$ admit a logical operator

$X_{\texttt{code}}=\frac{1}{M}\sum_{k=1}^{M}X_{k}\,,$ (14)

where $X_{k}$ is $X$ for the $k$th qudit, and a corresponding check operator $(X_{\texttt{code}})^{M}$. It is implied that both of these are projected only onto the subspace spanned by the extended binomial states $\{\ket{E_{m}^{d-1,M}}\}_{m=0}^{(d-1)M}$ (vs. the full permutation-symmetric subspace spanned by the qudit Dicke states discussed above). Thus, the logical operator will be a matrix of dimension $(d-1)\,M$ satisfying

$X_{\texttt{code}}\ket{\mu_{\texttt{perm}^{\prime}}}=e^{i\frac{2\pi}{d}\mu}\ket{\mu_{\texttt{perm}^{\prime}}}.$ (15)

Mapping the extended binomial state basis to the corresponding Fock states thus creates analogous check operators for bin and bin2. One can also consider products of $X_{k}$’s and form other check operators. Such check operators should prove useful in experimental realizations of the error correcting procedures of these codes.

## Appendix D Calculations for gkp codes

### D.1 Useful identities

Throughout the text, we have used the following standard identities for coherent states $D_{\alpha}\ket{0}=\ket{\alpha}$ and $\ket{\beta}$:

$e^{x\hat{n}}\ket{\alpha}$ $=e^{-\frac{1}{2}\ket{\alpha}^{2}(1-\ket{e^{x}}^{2})}\ket{\alpha}e^{x}$ (16a)
$D_{\alpha}D_{\beta}$ $=e^{\frac{1}{2}(\alpha\beta^{*}-\alpha^{*}\beta)}D_{\alpha+\beta}$ (16b)
$\bra{\alpha}\ket{\beta}$ $=e^{-\frac{1}{2}\left(\ket{\alpha}^{2}+\ket{\beta}^{2}\right)+\alpha^{*}\beta}.$ (16c)

We also use the Fock space matrix elements of $D_{\alpha}$ *[156]*,

$\bra{\ell}D_{\alpha}\ket{\ell^{\prime}}=e^{-\frac{\ket{\alpha}^{2}}{2}}\sqrt{\frac{\ell^{\prime}!}{\ell!}}L_{\ell^{\prime}}^{(\ell-\ell^{\prime})}(\ket{\alpha}^{2})\alpha^{\ell-\ell^{\prime}}$ (17)

for $\ell\geq\ell^{\prime}$ and $\bra{\ell}D_{\alpha}\ket{\ell^{\prime}}=(\bra{\ell^{\prime}}D_{-\alpha}\ket{\ell})^{\star}$ for $\ell<\ell^{\prime}$, where $L_{n}^{(\kappa)}(x)$ is the generalized Laguerre polynomial. The generating function of these polynomials is

$\sum_{p=0}^{\infty}\frac{(m+p)!}{p!}t^{p}L_{m+p}^{(\alpha)}(x)=\frac{m!e^{-\frac{tx}{1-t}}}{(1-t)^{m+\alpha+1}}L_{m}^{(\alpha)}\left(\frac{x}{1-t}\right)\,.$ (18)

Finally, we use the Poisson summation formula; for a function $f\left(x\right)$,

$\sum_{n\in\mathbb{Z}}f\left(n\right)=\sum_{n\in\mathbb{Z}}\int_{-\infty}^{\infty}dxe^{2\pi inx}f\left(x\right)\,.$ (19)

---

2. Equivalence between squeezed and coherent state representations for gkp

We sketch a derivation of Eq. (7.5) from Eq. (7.6). Writing the displacements in Eq. (7.7b) in terms of position and momentum operators $\hat{x}$ and $\hat{p}$, inserting a resolution of the identity in terms of position eigenstates between the displacements, and using $e^{-ix_{2}\hat{p}}|x_{1}\rangle_{\hat{x}}=|x_{1}+x_{2}\rangle_{\hat{x}}$ yields

$|\mu^{\text{ideal}}_{\text{gkps}}\rangle$ $\propto\sum_{\vec{n}\in\mathbb{Z}^{2}}\int dx|x+\sqrt{\pi}(2n_{1}+\mu)\rangle_{\hat{x}}\>_{\hat{x}}\langle x|e^{i\sqrt{\pi}n_{2}\hat{x}}|\text{vac}\rangle\,,$ (D5)

where $\vec{n}=(n_{1},n_{2})$, $|\text{vac}\rangle$ is the Fock state $|0\rangle$, and we use “$\propto$” to ignore normalization and any constant prefactors that we obtain throughout the calculation. Now, we recall that $\hat{x}\langle x|\text{vac}\rangle\propto\exp(-\frac{1}{2}x^{2})$ and apply the Poisson summation (D4) to the sum over $n_{2}$, yielding a sum over Dirac $\delta$-functions. We can then easily evaluate the integral over $x$, yielding

$|\mu^{\text{ideal}}_{\text{gkps}}\rangle$ $\propto\sum_{\vec{n}\in\mathbb{Z}_{2}}e^{-2\pi n_{2}^{2}}|\sqrt{\pi}(2n_{1}+2n_{2}+\mu)\rangle_{\hat{x}}\,.$ (D6)

Finally, we can redefine indices and evaluate one of the new sums to yield

$|\mu^{\text{ideal}}_{\text{gkps}}\rangle$ $\propto\sum_{n\in\mathbb{Z}}|\sqrt{\pi}(2n+\mu)\rangle_{\hat{x}}\,.$ (D7)

### D.3 Projecting displacements onto the gkp code space

We have utilized all three representations (7.7a-c) to verify the calculations below, initially calculating overlaps $\langle\mu^{\Delta}_{\text{gkps}}|\hat{a}^{\dagger p}\hat{a}^{q}|\mu^{\Delta}_{\text{gkps}}\rangle$ and summing them up to yield the QEC matrix $\imath^{\text{gkps}}_{\ell\ell^{\prime}}$. We will not report on these calculations, noting that they are cumbersome, but do yield the right answers.

We evaluate matrix elements $\langle\mu^{\text{ideal}}_{\text{gkps}}|D_{\alpha}|\nu^{\text{ideal}}_{\text{gkps}}\rangle$ of the displacement operator for ideal gkps states (written in terms of position eigenstates $|\sqrt{\pi}(2n+\mu)\rangle_{\hat{x}}$) from Eq. (7.5). We can split $D_{\alpha}=D_{\alpha_{1}+i\alpha_{2}}$ into a shift by $\sqrt{2}\alpha_{1}$ in position and by $\sqrt{2}\alpha_{2}$ in momentum. The latter translates $|\sqrt{\pi}(2n+\mu)\rangle_{\hat{x}}$ while the former turns into a phase since $|\sqrt{\pi}(2n+\mu)\rangle_{\hat{x}}$ are eigenstates of $\hat{x}$. We can then use the orthogonality of position eigenstates, $\hat{x}\langle x_{1}|x_{2}\rangle_{\hat{x}}=\delta(x_{1}-x_{2})$, and change indices to obtain

$\langle\mu^{\text{ideal}}_{\text{gkps}}|D_{\alpha}|\nu^{\text{ideal}}_{\text{gkps}}\rangle$ $=\sqrt{\frac{2}{\pi}}\sum_{n_{1},n_{2}\in\mathbb{Z}}e^{-i\alpha_{1}\alpha_{2}}e^{-i\sqrt{2\pi}(2n_{2}+\mu)\alpha_{2}}\delta\left(\alpha_{1}-\sqrt{\frac{\pi}{2}}(2n_{1}+\delta\mu)\right)\,,$ (D8)

where we multiplied each $|\mu^{\text{ideal}}_{\text{gkps}}\rangle$ by $(\frac{2}{\sqrt{\pi}})^{1/2}$ to remove constants in front of the sum (D9) below. We now apply the Poisson summation formula (D4) to turn the sum of $n_{2}$-dependent phases into another sum of Dirac $\delta$-functions for $\alpha_{2}$, yielding

$\langle\mu^{\text{ideal}}_{\text{gkps}}|D_{\alpha}|\nu^{\text{ideal}}_{\text{gkps}}\rangle$ $=\sum_{\vec{n}\in\mathbb{Z}}e^{i\pi(n_{1}+\frac{\mu+\nu}{2})n_{2}}\delta^{2}\left(\alpha-\Lambda^{\vec{n}}_{\delta\mu}\right)\,,$ (D9)

where $\Lambda^{\vec{n}}_{\delta\mu}=\sqrt{\frac{\pi}{2}}[(2n_{1}+\delta\mu)+in_{2}]$.

Now let us consider finite gkps states in the smeared representation (7.7c) and calculate

$\langle\mu^{\Delta}_{\text{gkps}}|D_{\alpha}|\nu^{\Delta}_{\text{gkps}}\rangle$ $=\int\frac{d^{2}\beta d^{2}\gamma}{\pi\Delta^{2}/2}e^{-\frac{1}{\Delta^{2}}(|\beta|^{2}+|\gamma|^{2})}\langle\mu^{\text{ideal}}_{\text{gkps}}|D_{-\beta}D_{\alpha}D_{\gamma}|\nu^{\text{ideal}}_{\text{gkps}}\rangle\,.$ (D10)

We add the displacements and use Eq. (D9), whose $\delta$-functions allow us to immediately evaluate one of the integrals. The remaining Gaussian integral is also simply evaluated to yield

$\langle\mu^{\Delta}_{\text{gkps}}|D_{\alpha}|\nu^{\Delta}_{\text{gkps}}\rangle$ $=\sum_{\vec{n}\in\mathbb{Z}^{2}}e^{i\pi(n_{1}+\frac{\mu+\nu}{2})n_{2}}e^{-\frac{1}{2\Delta^{2}}|\alpha-\Lambda^{\vec{n}}_{\delta\mu}|^{2}}e^{-\frac{\Delta^{2}}{2}|\alpha+\Lambda^{\vec{n}}_{\delta\mu}|^{2}}\,.$ (D11)

We can then substitute $\alpha\sim\Lambda^{\vec{n}}_{\delta\mu}$ into the envelope function in the $\Delta\to 0$ limit, yielding Eq. (7.14).

### D.

---

To compute the QEC matrix for gkps, let us sandwich both sides of Eq. (7.12) by $\langle \mu_{\mathbf{gkps}}^{\Delta}|$ and $|\nu_{\mathbf{gkps}}^{\Delta}\rangle$:

$$
\langle \mu_ {\mathbf {g k p s}} ^ {\Delta} | E _ {\ell} ^ {\dagger} E _ {\ell^ {\prime}} | \nu_ {\mathbf {g k p s}} ^ {\Delta} \rangle = \int \frac {d ^ {2} \alpha}{\pi} e ^ {- \frac {(1 - \gamma)}{2} | \alpha | ^ {2}} \langle \ell | D _ {\alpha^ {\star}} | \ell^ {\prime} \rangle \langle \mu_ {\mathbf {g k p s}} ^ {\Delta} | D _ {\sqrt {\gamma} \alpha} | \nu_ {\mathbf {g k p s}} ^ {\Delta} \rangle . \tag {D12}
$$

Plugging in Eq. (D11) with  $\alpha \sim \Lambda_{\delta \mu}^{\vec{n}}$  in the  $\Delta^2$ -dependent envelope and switching the sum and integral, one obtains

$$
\langle \mu_ {\mathbf {g k p s}} ^ {\Delta} | E _ {\ell} ^ {\dagger} E _ {\ell^ {\prime}} | \nu_ {\mathbf {g k p s}} ^ {\Delta} \rangle \sim \sum_ {\vec {n} \in \mathbb {Z} ^ {2}} e ^ {i \pi (n _ {1} + \frac {\mu + \nu}{2}) n _ {2}} e ^ {- \frac {\Delta^ {2}}{2} | \Lambda_ {\delta \mu} ^ {\vec {n}} | ^ {2}} \int \frac {d ^ {2} \alpha}{\pi} e ^ {- \frac {(1 - \gamma)}{2} | \alpha | ^ {2}} \langle \ell | D _ {\alpha^ {\star}} | \ell^ {\prime} \rangle e ^ {- \frac {\gamma}{2 \Delta^ {2}} | \alpha - \Lambda_ {\delta \mu} ^ {\vec {n}} / \sqrt {\gamma} | ^ {2}}. \tag {D13}
$$

Next, we evaluate the integral by changing to polar coordinates  $\alpha = |\alpha|e^{i\theta}$  and evaluating the angular integral first. This integral turns out to be integral representation of the modified Bessel function of the first kind,  $I_{n}(z) = \int_{0}^{\pi}\frac{d\theta}{\pi} e^{z\cos \theta}\cos (n\theta)$ . Recalling that  $\langle \ell |D_{\alpha^{\star}}|\ell^{\prime}\rangle$  (D2) contains Laguerre polynomials, the remaining integral over  $|\alpha|$  contains both  $L_{i_{\mathrm{min}}}^{(|\ell -\ell '|)}$  and  $I_{|\ell -\ell '|}$ . Luckily, it can be evaluated using Ref. [157], Sec. 2.19.12, Eq. (6):

$$
\int_ {0} ^ {\infty} d x x ^ {\frac {\lambda}{2}} e ^ {- p x} I _ {\lambda} (2 b \sqrt {x}) L _ {n} ^ {(\lambda)} (x) = b ^ {\lambda} \frac {(p - 1) ^ {n}}{p ^ {\lambda + n + 1}} e ^ {\frac {b ^ {2}}{p}} L _ {n} ^ {(\lambda)} \left(\frac {b ^ {2}}{p (p - 1)}\right). \tag {D14}
$$

The pre-factor  $\frac{(p - 1)^n}{p^{n + 1}}$  eventually gives the thermal weights in the QEC coefficients  $c_{\ell \ell}^{\mathbf{gkps}}$  (7.16). The resulting Laguerre polynomials can then be re-expressed in terms of displacement matrix elements (D2). During this simplification, we take the limit

$$
\gamma \left(\frac {1}{2 \Delta^ {2}} - \frac {1}{2}\right) \sim \gamma \bar {n} _ {\mathbf {g k p s}} \gg 1, \tag {D15}
$$

relating  $\gamma$  to  $\bar{n}_{\mathbf{gkps}}$ . This yields the QEC matrix elements

$$
\langle \mu_ {\mathbf {g k p s}} ^ {\Delta} | E _ {\ell} ^ {\dagger} E _ {\ell^ {\prime}} | \nu_ {\mathbf {g k p s}} ^ {\Delta} \rangle \sim \frac {\left(\gamma \bar {n} _ {\mathbf {g k p s}}\right) ^ {\frac {\ell + \ell^ {\prime}}{2}}}{\left(\gamma \bar {n} _ {\mathbf {g k p s}} + 1\right) ^ {\frac {\ell + \ell^ {\prime}}{2} + 1}} \sum_ {\vec {n} \in \mathbb {Z} ^ {2}} e ^ {- \frac {(1 - \gamma)}{2 \gamma} | \Lambda_ {\delta \mu} ^ {\vec {n}} | ^ {2}} e ^ {i \pi (n _ {1} + \frac {\mu + \nu}{2}) n _ {2}} e ^ {- \frac {\Delta^ {2}}{2} | \Lambda_ {\delta \mu} ^ {\vec {n}} | ^ {2}} \langle \ell | D _ {(\Lambda_ {\delta \mu} ^ {\vec {n}}) ^ {\star} / \sqrt {\gamma}} | \ell^ {\prime} \rangle , \tag {D16}
$$

where we can once again let  $\Delta \to 0$  to produce Eq. (7.15).

[1] S. L. Braunstein and P. van Loock, Quantum information with continuous variables, Rev. Mod. Phys. 77 (2005).
[2] N. J. Cerf, G. Leuchs, and E. S. Polzik, Quantum Information with Continuous Variables of Atoms and Light (World Scientific, London, 2007).
[3] C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro, and S. Lloyd, Gaussian quantum information, Rev. Mod. Phys. 84, 621 (2012).
[4] A. Serafini, Quantum Continuous Variables: A Primer of Theoretical Methods (CRC Press, Boca Raton FL, 2017).
[5] I. L. Chuang and Y. Yamamoto, Simple quantum computer, Phys. Rev. A 52, 3489 (1995).
[6] P. Kok, W. J. Munro, K. Nemoto, T. C. Ralph, J. P. Dowling, and G. J. Milburn, Linear optical quantum computing with photonic qubits, Rev. Mod. Phys. 79, 135 (2007).
[7] S. Lloyd and J.-J. E. Slotine, Analog Quantum Error Correction, Phys. Rev. Lett. 80, 4088 (1998).
[8] S. L. Braunstein, Error Correction for Continuous Quantum Variables, Phys. Rev. Lett. 80, 4084 (1998).
[9] D. Gottesman, A. Yu. Kitaev, and J. Preskill, Encoding a qubit in an oscillator, Phys. Rev. A 64, 012310 (2001).
[10] N. C. Menicucci, Fault-Tolerant Measurement-Based Quantum Computing with Continuous-Variable Cluster States, Phys. Rev. Lett. 112, 120504 (2014).
[11] P. Hayden, S. Nezami, G. Salton, and B. C. Sanders, Spacetime replication of continuous variable quantum information, New J. Phys. 18, 083043 (2016).
[12] A. Ketterer, A. Keller, S. P. Walborn, T. Coudreau, and P. Milman, Quantum information processing in phase space: A modular variables approach, Phys. Rev. A 94, 022325 (2016).
[13] P. T. Cochrane, G. J. Milburn, and W. J. Munro, Macroscopically distinct quantum-superposition states as a bosonic code for amplitude damping, Phys. Rev. A 59, 2631 (1999).
[14] J. Niset, U. L. Andersen, and N. J. Cerf, Experimentally Feasible Quantum Erasure-Correcting Code for Continuous Variables, Phys. Rev. Lett. 101, 130503 (2008).
[15] Z. Leghtas, G. Kirchmair, B. Vlastakis, R. J. Schoelkopf, M. H. Devoret, and M. Mirrahimi,

---

Hardware-Efficient Autonomous Quantum Memory Protection, Phys. Rev. Lett. 111, 120501 (2013).
- (16) F. Lacerda, J. M. Renes, and V. B. Scholz, Coherent state constellations for Bosonic Gaussian channels, 2016 IEEE Int. Symp. Inf. Theory , 2499 (2016).
- (17) V. V. Albert, S. O. Mundhada, A. Grimm, S. Touzard, M. H. Devoret, and L. Jiang, Multimode cat codes, arXiv:1801.05897.
- (18) I. L. Chuang, D. W. Leung, and Y. Yamamoto, Bosonic quantum codes for amplitude damping, Phys. Rev. A 56, 1114 (1997).
- (19) E. Knill, R. Laflamme, and G. J. Milburn, A scheme for efficient quantum computation with linear optics, Nature 409, 46 (2001).
- (20) T. C. Ralph, A. J. F. Hayes, and A. Gilchrist, Loss-Tolerant Optical Qubits, Phys. Rev. Lett. 95, 100501 (2005).
- (21) W. Wasilewski and K. Banaszek, Protecting an optical qubit against photon loss, Phys. Rev. A 75, 042316 (2007).
- (22) M. Bergmann and P. van Loock, Quantum error correction against photon loss using NOON states, Phys. Rev. A 94, 012311 (2016).
- (23) M. H. Michael, M. Silveri, R. T. Brierley, V. V. Albert, J. Salmilehto, L. Jiang, and S. M. Girvin, New Class of Quantum Error-Correcting Codes for a Bosonic Mode, Phys. Rev. X 6, 031006 (2016).
- (24) M. Y. Niu, I. L. Chuang, and J. H. Shapiro, Hardware-Efficient Bosonic Quantum Error-Correcting Codes Based on Symmetry Operators, arXiv:1709.05302.
- (25) S.-W. Lee and H. Jeong, Near-deterministic quantum teleportation and resource-efficient quantum computation using linear optics and hybrid qubits, Phys. Rev. A 87, 022326 (2013).
- (26) E. Kapit, Hardware-Efficient and Fully Autonomous Quantum Error Correction in Superconducting Circuits, Phys. Rev. Lett. 116, 150501 (2016).
- (27) M. Mirrahimi, Z. Leghtas, V. V. Albert, S. Touzard, R. J. Schoelkopf, L. Jiang, and M. H. Devoret, Dynamically protected cat-qubits: a new paradigm for universal quantum computation, New J. Phys. 16, 045014 (2014).
- (28) D. Kribs and D. Poulin, in Quantum Error Correct., edited by D. A. Lidar, T. A. Brun, and T. Brun (Cambridge University Press, Cambridge) pp. 163–180.
- (29) N. Ofek, A. Petrenko, R. Heeres, P. Reinhold, Z. Leghtas, B. Vlastakis, Y. Liu, L. Frunzio, S. M. Girvin, L. Jiang, M. Mirrahimi, M. H. Devoret, and R. J. Schoelkopf, Extending the lifetime of a quantum bit with error correction in superconducting circuits, Nature 536, 441 (2016).
- (30) M. Ueda, Probability-density-functional description of quantum photodetection processes, Quantum Opt. 1, 131 (1989).
- (31) C. T. Lee, Superoperators and their implications in the hybrid model for photodetection, Phys. Rev. A 49, 4888 (1994).
- (32) D. Vitali, P. Tombesi, and G. J. Milburn, Quantum-state protection in cavities, Phys. Rev. A 57, 4930 (1998).
- (33) A. B. Klimov and S. M. Chumakov, A Group-Theoretical Approach to Quantum Optics (Wiley, Weinheim, 2009).
- (34) J. S. Ivan, K. K. Sabapathy, and R. Simon, Operator-sum representation for bosonic Gaussian channels, Phys. Rev. A 84, 042311 (2011).
- (35) A. S. Fletcher, Channel-Adapted Quantum Error Correction, Ph.D. thesis, MIT (2007).
- (36) C. M. Caves, Quantum Error Correction and Reversible Operations, J. Supercond. 12, 707 (1999).
- (37) D. W. Leung, M. A. Nielsen, I. L. Chuang, and Y. Yamamoto, Approximate quantum error correction can lead to better codes, Phys. Rev. A 56, 2567 (1997).
- (38) C. Crépeau, D. Gottesman, and A. Smith, in Adv. Cryptol. - EUROCRYPT 2005. Lect. Notes Comput. Sci. vol. 3494, edited by R. Cramer (Springer, Berlin, Heidelberg, 2005) pp. 285–301.
- (39) M. Reimpell and R. F. Werner, Iterative Optimization of Quantum Error Correcting Codes, Phys. Rev. Lett. 94, 080501 (2005).
- (40) B. W. Schumacher and M. D. Westmoreland, Quantum Processes, Systems, and Information (Cambridge University Press, New York, 2010).
- (41) R. Konig, R. Renner, and C. Schaffner, The Operational Meaning of Min- and Max-Entropy, IEEE Trans. Inf. Theory 55, 4337 (2009).
- (42) M. Tomamichel, A Framework for Non-Asymptotic Quantum Information Theory, Ph.D. thesis, ETH Zurich (2012).
- (43) A. S. Fletcher, P. W. Shor, and M. Z. Win, Optimum quantum error recovery using semidefinite programming, Phys. Rev. A 75, 012338 (2007).
- (44) K. M. R. Audenaert and B. De Moor, Optimizing completely positive maps using semidefinite programming, Phys. Rev. A 65, 030302 (2002).
- (45) R. L. Kosut and D. A. Lidar, Quantum error correction via convex optimization, Quantum Inf. Process. 8, 443 (2009).
- (46) L. Li, C.-l. Zou, V. V. Albert, S. Muralidharan, S. M. Girvin, and L. Jiang, Cat Codes with Optimal Decoherence Suppression for a Lossy Bosonic Channel, Phys. Rev. Lett. 119, 030502 (2017).
- (47) J. Preskill, Quantum Computing in the NISQ era and beyond, arXiv:1801.00862.
- (48) M. Mirrahimi, Cat-qubits for quantum computation, Comptes Rendus Phys. 17, 778 (2016).
- (49) Z. Leghtas and M. Mirrahimi, private communication, (2012).
- (50) F. Caruso, V. Giovannetti, and A. S. Holevo, One-mode bosonic Gaussian channels: a full weak-degradability classification, New J. Phys. 8, 310 (2006).
- (51) D. Gottesman and J. Preskill, Secure quantum key distribution using squeezed states, Phys. Rev. A 63, 022309 (2001).
- (52) R. Garcia-Patron, C. Navarrete-Benlloch, S. Lloyd, J. H. Shapiro, and N. J. Cerf, Majorization Theory Approach to the Gaussian Channel Minimum Entropy Conjecture, Phys. Rev. Lett. 108, 110505 (2012).
- (53) J. Harrington and J. Preskill, Achievable rates for the Gaussian quantum channel, Phys. Rev. A 64, 062301 (2001).
- (54) K. Noh, V. V. Albert, and L. Jiang, Improved quantum capacity bounds of Gaussian loss channels and achievable rates with Gottesman-Kitaev-Preskill codes, arXiv:1801.07271.
- (55) M. Rosati, A. Mari, and V. Giovannetti, Narrow Bounds for the Quantum Capacity of Thermal Attenuators, arXiv:1801.04731.
- (56) K. Sharma, M. M. Wilde, S. Adhikari, and M. Takeoka,

---

Bounding the energy-constrained quantum and private capacities of phase-insensitive Gaussian channels, arXiv:1708.07257.
- (57) M. M. Wilde, P. Hayden, and S. Guha, Quantum trade-off coding for bosonic communication, Phys. Rev. A 86, 062306 (2012).
- (58) M. M. Wilde and H. Qi, Energy-constrained private and quantum capacities of quantum channels, arXiv:1609.01997v1.
- (59) M. M. Wilde, P. Hayden, and S. Guha, Information Trade-Offs for Optical Quantum Communication, Phys. Rev. Lett. 108, 140501 (2012).
- (60) M. M. Wolf, D. Pérez-García, and G. Giedke, Quantum Capacities of Bosonic Channels, Phys. Rev. Lett. 98, 130501 (2007).
- (61) A. S. Holevo and R. F. Werner, Evaluating capacities of Bosonic Gaussian channels, arXiv:9912067 [quant-ph].
- (62) M. M. Wilde, Quantum Information Theory, 2nd ed. (Cambridge University Press, Cambridge, 2013).
- (63) R. García-Patrón, S. Pirandola, S. Lloyd, and J. H. Shapiro, Reverse Coherent Information, Phys. Rev. Lett. 102, 210501 (2009).
- (64) S. Pirandola, R. García-Patrón, S. L. Braunstein, and S. Lloyd, Direct and Reverse Secret-Key Capacities of a Quantum Channel, Phys. Rev. Lett. 102, 050503 (2009).
- (65) S. Pirandola, R. Laurenza, C. Ottaviani, and L. Banchi, Fundamental limits of repeaterless quantum communications, Nat. Commun. 8, 15043 (2017).
- (66) M. M. Wolf and D. Perez-Garcia, Quantum capacities of channels with small environment, Phys. Rev. A 75, 012303 (2007).
- (67) D. Gottesman, Stabilizer codes and quantum error correction, Ph.D. thesis, California Institute of Technology (1997).
- (68) R. Lang and P. W. Shor, Nonadditive quantum error correcting codes adapted to the ampltitude damping channel, arXiv:0712.2586.
- (69) A. S. Fletcher, P. W. Shor, and M. Z. Win, Channel-Adapted Quantum Error Correction for the Amplitude Damping Channel, IEEE Trans. Inf. Theory 54, 5705 (2008).
- (70) R. Duan, M. Grassl, Z. Ji, and B. Zeng, Multi-error-correcting amplitude damping codes, 2010 IEEE Int. Symp. Inf. Theory , 2672 (2010).
- (71) P. W. Shor, G. Smith, J. A. Smolin, and B. Zeng, High Performance Single-Error-Correcting Quantum Codes for Amplitude Damping, IEEE Trans. Inf. Theory 57, 7180 (2011).
- (72) C. Han, Quantum error correction of photon loss with quantum encoding, J. Korean Phys. Soc. 62, 721 (2013).
- (73) Y. Ouyang, Permutation-invariant quantum codes, Phys. Rev. A 90, 062317 (2014).
- (74) T. Jackson, M. Grassl, and B. Zeng, Concatenated codes for amplitude damping, 2016 IEEE Int. Symp. Inf. Theory , 2269 (2016).
- (75) Y. Ouyang, Permutation-invariant qudit codes from polynomials, Linear Algebr. Appl. 532, 43 (2017).
- (76) Y. Ouyang and J. Fitzsimons, Permutation-invariant codes encoding more than one qubit, Phys. Rev. A 93, 042340 (2016).
- (77) M. Grassl, T. Beth, and T. Pellizzari, Codes for the quantum erasure channel, Phys. Rev. A 56, 33 (1997).
- (78) L. Vaidman, L. Goldenberg, and S. Wiesner, Error prevention scheme with four particles, Phys. Rev. A 54, R1745 (1996).
- (79) C. H. Bennett, D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters, Mixed-state entanglement and quantum error correction, Phys. Rev. A 54, 3824 (1996).
- (80) E. Knill and R. Laflamme, Theory of quantum error-correcting codes, Phys. Rev. A 55, 900 (1997).
- (81) M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2011).
- (82) J. Preskill, Lecture notes on Quantum Computation, (2004).
- (83) V. V. Albert and L. Jiang, Symmetries and conserved quantities in Lindblad master equations, Phys. Rev. A 89, 022118 (2014).
- (84) H. Jeong and M. S. Kim, Efficient quantum computation using coherent states, Phys. Rev. A 65, 042305 (2002).
- (85) T. C. Ralph, A. Gilchrist, G. J. Milburn, W. J. Munro, and S. Glancy, Quantum computation with optical coherent states, Phys. Rev. A 68, 042319 (2003).
- (86) S. Glancy, H. M. Vasconcelos, and T. C. Ralph, Transmission of optical coherent-state qubits, Phys. Rev. A 70, 022317 (2004).
- (87) A. P. Lund, T. C. Ralph, and H. L. Haselgrove, Fault-Tolerant Linear Optical Quantum Computing with Small-Amplitude Coherent States, Phys. Rev. Lett. 100, 030503 (2008).
- (88) V. V. Albert, C. Shu, S. Krastanov, C. Shen, R.-B. Liu, Z.-B. Yang, R. J. Schoelkopf, M. Mirrahimi, M. H. Devoret, and L. Jiang, Holonomic Quantum Control with Continuous Variable Systems, Phys. Rev. Lett. 116, 140502 (2016).
- (89) M. Bergmann and P. van Loock, Quantum error correction against photon loss using multicomponent cat states, Phys. Rev. A 94, 042332 (2016).
- (90) U. L. Andersen, J. S. Neergaard-Nielsen, P. van Loock, and A. Furusawa, Hybrid discrete- and continuous-variable quantum information, Nat. Phys. 11, 713 (2015).
- (91) Z. Leghtas, S. Touzard, I. M. Pop, A. Kou, B. Vlastakis, A. Petrenko, K. M. Sliwa, A. Narla, S. Shankar, M. J. Hatridge, M. Reagor, L. Frunzio, R. J. Schoelkopf, M. Mirrahimi, and M. H. Devoret, Confining the state of light to a quantum manifold by engineered two-photon loss, Science (80- . ). 347, 853 (2015).
- (92) V. V. Albert, Lindbladians with multiple steady states: theory and applications, Ph.D. thesis, Yale University (2017).
- (93) D. Stoler, B. Saleh, and M. Teich, Binomial States of the Quantized Radiation Field, Opt. Acta (Lond). 32, 345 (1985).
- (94) V. Dodonov and V. Man’ko, Theory of Nonclassical States of Light (CRC Press, New York, 2003).
- (95) G. Dattoli, J. Gallardo, and A. Torre, Binomial states of the quantized radiation field: comment, J. Opt. Soc. Am. B 4, 185 (1987).
- (96) F. Hong-yi and J. Si-cong, Connection of a type of q-deformed binomial state with q-spin coherent states, Phys. Rev. A 50, 1909 (1994).
- (97) L. I. Schiff, Quantum Mechanics (McGraw-Hill Book Company, New York, 1968).
- (98) F. T. Arecchi, E. Courtens, R. Gilmore, and H. Thomas, Atomic Coherent States in Quantum Optics, Phys. Rev. A 6, 2211 (1972).

---

- (99) R. R. Puri, Mathematical methods of quantum optics (Springer, Berlin/Heidelberg, 2001).
- (100) Y. Ouyang, Transmitting Quantum Information Reliably across Various Quantum Channels, Ph.D. thesis, University of Waterloo (2013).
- (101) Z. Shaterzadeh-Yazdi, P. S. Turner, and B. C. Sanders, SU(1,1) symmetry of multimode squeezed states, J. Phys. A Math. Theor. 41, 055309 (2008).
- (102) E. Knill, Quantum computing with realistically noisy devices, Nature 434, 39 (2005).
- (103) Y. Aharonov, H. Pendleton, and A. Petersen, Modular variables in quantum theory, Int. J. Theor. Phys. 2, 213 (1969).
- (104) J. Zak, Finite Translations in Solid-State Physics, Phys. Rev. Lett. 19, 1385 (1967).
- (105) K. E. Cahill and R. J. Glauber, Ordered Expansions in Boson Amplitude Operators, Phys. Rev. 177, 1857 (1969).
- (106) B. M. Terhal and D. Weigand, Encoding a qubit into a cavity mode in circuit QED using phase estimation, Phys. Rev. A 93, 012315 (2016).
- (107) P. P. Hofer, J.-R. Souquet, and A. A. Clerk, Quantum heat engine based on photon-assisted Cooper pair tunneling, Phys. Rev. B 93, 041418 (2016).
- (108) A. B. Klimov and J. L. Romero, An algebraic solution of Lindblad-type master equations, J. Opt. B - Quantum S. O. 5, S316 (2003).
- (109) L. Kunz, M. G. A. Paris, and K. Banaszek, Noisy propagation of coherent states in a lossy Kerr medium, arXiv:1707.09196.
- (110) K. Duivenvoorden, B. M. Terhal, and D. Weigand, Single-mode displacement sensor, Phys. Rev. A 95, 012305 (2017).
- (111) B. Yurke and D. Stoler, Generating quantum mechanical superpositions of macroscopically distinguishable states via amplitude dispersion, Phys. Rev. Lett. 57, 13 (1986).
- (112) A. Miranowicz, R. Tanas, and S. Kielich, Generation of discrete superpositions of coherent states in the anharmonic oscillator model, Quantum Opt. 2, 253 (1990).
- (113) K. Tara, G. S. Agarwal, and S. Chaturvedi, Production of Schrodinger macroscopic quantum-superposition states in a Kerr medium, Phys. Rev. A 47, 5024 (1993).
- (114) G. J. Milburn and C. A. Holmes, Dissipative Quantum and Classical Liouville Mechanics of the Anharmonic Oscillator, Phys. Rev. Lett. 56, 2237 (1986).
- (115) L. Sun, A. Petrenko, Z. Leghtas, B. Vlastakis, G. Kirchmair, K. M. Sliwa, A. Narla, M. Hatridge, S. Shankar, J. Blumoff, L. Frunzio, M. Mirrahimi, M. H. Devoret, and R. J. Schoelkopf, Tracking photon jumps with repeated quantum non-demolition parity measurements. Nature 511, 444 (2014).
- (116) L. G. Lutterbach and L. Davidovich, Method for Direct Measurement of the Wigner Function in Cavity QED and Ion Traps, Phys. Rev. Lett. 78, 2547 (1997).
- (117) A. Barchielli and M. Gregoratti, Quantum Trajectories and Measurements in Continuous Time: the Diffusive Case (Springer, Berlin/Heidelberg, 2009).
- (118) R. W. Heeres, P. Reinhold, N. Ofek, L. Frunzio, L. Jiang, M. H. Devoret, and R. J. Schoelkopf, Implementing a universal gate set on a logical qubit encoded in an oscillator, Nat. Commun. 8, 94 (2017).
- (119) W. Chen, J. Hu, Y. Duan, B. Braverman, H. Zhang, and V. Vuletić, Carving Complex Many-Atom Entangled States by Single-Photon Detection, Phys. Rev. Lett. 115, 250502 (2015).
- (120) R. McConnell, H. Zhang, J. Hu, S. Cuk, and V. Vuletic, Entanglement with negative Wigner function of almost 3,000 atoms heralded by one photon, Nature 519, 439 (2016).
- (121) D. Kienzler, H.-Y. Lo, V. Negnevitsky, C. Fluhmann, M. Marinelli, and J. P. Home, Quantum Harmonic Oscillator State Control in a Squeezed Fock Basis, Phys. Rev. Lett. 119, 033602 (2017).
- (122) K. R. Motes, B. Q. Baragiola, A. Gilchrist, and N. C. Menicucci, Encoding qubits into oscillators with atomic ensembles and squeezed light, Phys. Rev. A 95, 053819 (2017).
- (123) B. C. Travaglione and G. J. Milburn, Preparing encoded states in an oscillator, Phys. Rev. A 66, 052322 (2002).
- (124) S. Pirandola, S. Mancini, D. Vitali, and P. Tombesi, Constructing finite-dimensional codes with optical continuous variables, EPL 68, 323 (2004).
- (125) S. Pirandola, S. Mancini, D. Vitali, and P. Tombesi, Continuous variable encoding by ponderomotive interaction, Eur. Phys. J. D 37, 283 (2006).
- (126) S. Pirandola, S. Mancini, D. Vitali, and P. Tombesi, Generating continuous variable quantum codewords in the near-field atomic lithography, J. Phys. B At. Mol. Opt. Phys. 39, 997 (2006).
- (127) H. M. Vasconcelos, L. Sanz, and S. Glancy, All-optical generation of states for "Encoding a qubit in an oscillator", Opt. Lett. 35, 3261 (2010).
- (128) D. J. Weigand and B. M. Terhal, Generating Grid States From Schrodinger Cat States without Post-Selection, (2017), arXiv:1709.08580.
- (129) C. Fluhmann, V. Negnevitsky, M. Marinelli, and J. P. Home, Sequential modular position and momentum measurements of a trapped ion mechanical oscillator, Phys. Rev. X , (in press) (2017), arXiv:1709.10469.
- (130) J. Hu, W. Chen, Z. Vendeiro, H. Zhang, and V. Vuletic, Entangled collective-spin states of atomic ensembles under nonuniform atom-light interaction, Phys. Rev. A 92, 063816 (2015).
- (131) D. Budker and M. Romalis, Optical magnetometry, Nat. Phys. 3, 227 (2007).
- (132) J. M. Taylor, P. Cappellaro, L. Childress, L. Jiang, D. Budker, P. R. Hemmer, A. Yacoby, R. Walsworth, and M. D. Lukin, High-sensitivity diamond magnetometer with nanoscale resolution, Nat. Phys. 4, 810 (2008).
- (133) V. M. Acosta, E. Bauch, M. P. Ledbetter, C. Santori, K.-M. C. Fu, P. E. Barclay, R. G. Beausoleil, H. Linget, J. F. Roch, F. Treussart, S. Chemerisov, W. Gawlik, and D. Budker, Diamonds with a high density of nitrogen-vacancy centers for magnetometry applications, Phys. Rev. B 80, 115202 (2009).
- (134) M. Horodecki, P. Horodecki, and R. Horodecki, General teleportation channel, singlet fraction, and quasidistillation, Phys. Rev. A 60, 1888 (1999).
- (135) M. A. Nielsen, A simple formula for the average gate fidelity of a quantum dynamical operation, Phys. Lett. A 303, 249 (2002).
- (136) H. Barnum, E. Knill, and M. A. Nielsen, On quantum fidelities and channel capacities, IEEE Trans. Inf. Theory 46, 1317 (2000).
- (137) A. Gilchrist, N. K. Langford, and M. A. Nielsen, Distance measures to compare real and ideal quantum processes, Phys. Rev. A 71, 062310 (2005).
- (138) H. K. Ng and P. Mandayam, Simple approach to approx-

---

imate quantum error correction based on the transpose channel, Phys. Rev. A 81, 062342 (2010).
- (139) R. Kueng, D. M. Long, A. C. Doherty, and S. T. Flammia, Comparing Experiments to the Fault-Tolerance Threshold, Phys. Rev. Lett. 117, 170502 (2016).
- (140) J. J. Wallman, Bounding experimental quantum error rates relative to fault-tolerant thresholds, arXiv:1511.00727.
- (141) S. T. Flammia, Quantifying photon loss errors in quantum gates, unpublished.
- (142) C. Fuchs and J. van de Graaf, Cryptographic distinguishability measures for quantum-mechanical states, IEEE Trans. Inf. Theory 45, 1216 (1999).
- (143) J. J. Wallman and S. T. Flammia, Randomized benchmarking with confidence, New J. Phys. 16, 103032 (2014).
- (144) J. J. Wallman and S. T. Flammia, Corrigendum: Randomized benchmarking with confidence (2014 New J. Phys. 16 103032), New J. Phys. 18, 079501 (2016).
- (145) B. Schumacher, Sending entanglement through noisy quantum channels, Phys. Rev. A 54, 2614 (1996).
- (146) O. Fawzi and R. Renner, Quantum Conditional Mutual Information and Approximate Markov Chains, Commun. Math. Phys. 340, 575 (2015).
- (147) K. P. Seshadreesan and M. M. Wilde, Fidelity of recovery, squashed entanglement, and measurement recoverability, Phys. Rev. A 92, 042321 (2015).
- (148) J. Tyson, Two-sided bounds on minimum-error quantum measurement, on the reversibility of quantum dynamics, and on maximum overlap using directional iterates, J. Math. Phys. 51, 092204 (2010).
- (149) C. Bény and O. Oreshkov, General Conditions for Approximate Quantum Error Correction and Near-Optimal Recovery Channels, Phys. Rev. Lett. 104, 120501 (2010).
- (150) C. Bény and O. Oreshkov, Approximate simulation of quantum channels, Phys. Rev. A 84, 022333 (2011).
- (151) M. Grant and S. Boyd, CVX: Matlab software for disciplined convex programming, (2013).
- (152) R. S. Menon and S. Horvát, MATLAB, (2013).
- (153) T. S. Cubitt, Matlab code, (2016).
- (154) T. Neuschel, A Note on Extended Binomial Coefficients, J. Integer Seq. 17, 14.10.4 (2014).
- (155) C. Caiado and P. Rathie, in Eighth Annu. Conf. Soc. Spec. Funct. their Appl., edited by A. M. Mathai, M. A. Pathan, K. Jose, and J. Jacob (Society for Special Functions & their Applications, 2007).
- (156) W. Vogel and D.-G. Welsch, Quantum Optics, 3rd ed. (Wiley, Weinheim, 2006).
- (157) A. P. Prudnikov, Y. A. Brychkov, and O. I. Marichev, Integrals and Series Vol. 2: Special Functions, 1st ed. (Gordon and Breach Science Publishers, 1998).