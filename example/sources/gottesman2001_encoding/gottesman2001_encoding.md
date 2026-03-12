# Encoding a qubit in an oscillator

Daniel Gottesman,^{(1,2)} Alexei Kitaev,^{(1)} and John Preskill^{(3)} [ ^{(1)}Microsoft Corporation, One Microsoft Way, Redmond, WA 98052, USA
^{(2)}Computer Science Division, EECS, University of California, Berkeley, CA 94720, USA
^{(3)}Institute for Quantum Information, California Institute of Technology, Pasadena, CA 91125, USA ]

###### Abstract

Quantum error-correcting codes are constructed that embed a finite-dimensional code space in the infinite-dimensional Hilbert space of a system described by continuous quantum variables. These codes exploit the noncommutative geometry of phase space to protect against errors that shift the values of the canonical variables $q$ and $p$. In the setting of quantum optics, fault-tolerant universal quantum computation can be executed on the protected code subspace using linear optical operations, squeezing, homodyne detection, and photon counting; however, nonlinear mode coupling is required for the preparation of the encoded states. Finite-dimensional versions of these codes can be constructed that protect encoded quantum information against shifts in the amplitude or phase of a $d$-state system. Continuous-variable codes can be invoked to establish lower bounds on the quantum capacity of Gaussian quantum channels.

## I Introduction

Classical information can be carried by either a discrete (digital) signal or a continuous (analog) signal. Although in principle an analog signal can be processed, digital computing is far more robust – a digital signal can be readily re-standardized and protected from damage caused by the gradual accumulation of small errors.

Quantum information can also be carried by either a discrete (finite-dimensional) system like a two-level atom or an electron spin, or by a continuous (infinite-dimensional) system like a harmonic oscillator or a rotor. Even in the finite-dimensional case, quantum information is in a certain sense continuous – a state is a vector in a Hilbert space that can point in any direction. Nevertheless, we have known for nearly five years that cleverly encoded quantum states can be re-standardized and protected from the gradual accumulation of small errors, or from the destructive effects of decoherence due to uncontrolled interactions with the environment *[1, 2]*.

One is tempted to wonder whether we can go still further and protect the quantum state of a system described by continuous quantum variables. Probably this is too much to hope for, since even the problem of protecting analog classical information seems to pose insuperable difficulties.

In this paper we achieve a more modest goal: we describe quantum error-correcting codes that protect a state of a finite-dimensional quantum system (or “qudit”) that is encoded in an infinite-dimensional system. These codes may be useful for implementing quantum computation and quantum communication protocols that use harmonic oscillators or rotors that are experimentally accessible.

We also explain how encoded quantum states can be processed fault tolerantly. Once encoded states have been prepared, a universal set of fault-tolerant quantum gates can be implemented using, in the language of quantum optics, linear optical operations, squeezing, homodyne detection, and photon counting. However, for preparation of the encoded states, nonlinear couplings must be invoked.

Our continuous-variable quantum error-correcting codes are effective in protecting against sufficiently weak diffusive phenomena that cause the position and momentum of an oscillator to drift, or against losses that cause the amplitude of an oscillator to decay. By concatenating with conventional finite-dimensional quantum codes, we can also provide protection against errors that heavily damage a (sufficiently small) subset of all the oscillators in a code block.

A different scheme for realizing robust and efficient quantum computation based on linear optics has been recently proposed by Knill, Laflamme, and Milburn *[3, 4]*.

We begin in §II by describing codes that embed an $n$-state quantum system in a larger $d$-state system, and that protect the encoded quantum information against shifts in the amplitude or phase of the $d$-state system. A realization of this coding scheme based on a charged particle in a magnetic field is discussed in §III. Our continuous-variable codes are obtained in §IV by considering a $d\to\infty$ limit. Formally, the code states of the continuous-variable codes are nonnormalizable states, infinitely squeezed in both position and momentum; in §V we describe the consequences of using more realistic approximate code states that are finitely squeezed. In §VI we outline the theory of more general continuous-variable codes based on lattice sphere packings in higher-dimensional phase space.

We discuss in §VII how continuous-variable codes protect against quantum diffusion, amplitude damping, and unitary errors. In §VIII, we establish a lower bound on the quantum capacity of the Gaussian quantum channel.

*CALT-68-2273

\dagger D. Gottesman

\ddagger A. Kitaev

\S J. Preskill

---

We then proceed to develop schemes for fault-tolerant manipulation of encoded quantum information, starting in §IX with a discussion of the symplectic operations that can be implemented with linear optics and squeezing. In §X we discuss the measurement of the error syndrome and error recovery, which can be achieved with symplectic operations and homodyne detection. Completion of the fault-tolerant universal gate set by means of photon counting is described in §XI, and the preparation of encoded states is explained in §XII.

Finally, §XIII contains some further remarks about the physical realization of our coding schemes, and §XIV contains concluding comments.

## II SHIFT-RESISTANT QUANTUM CODES

The main novelty of our new codes is that they are designed to protect against a different type of error than has been considered in previous discussions of quantum coding. This distinction is more easily explained if we first consider not the case of a continuous quantum variable, but instead the (also interesting) case of a “qudit,” a $d$-dimensional quantum system. Quantum codes can be constructed that encode $k$ protected qudits in a block of $N$ qudits, so that the encoded qudits can be perfectly recovered if up to $t$ qudits are damaged, irrespective of the nature of the damage *[5, 6, 7, 8]*. Error recovery will be effective if errors that act on many qudits at once are rare. More precisely, a general error superoperator acting on $N$ qudits can be expanded in terms of a basis of operators, each of definite “weight” (the number of qudits on which the operator acts nontrivially). Encoded information is well protected if the error superoperator has nearly all its support on operators of weight $t$ or less.

But consider instead a different situation, in which the amplitude for an error to occur on each qudit is not small, but the errors are of a restricted type. The possible errors acting on a single qudit can be expanded in terms of a unitary operator basis with $d^{2}$ elements, the “Pauli operators”:

$X^{a}Z^{b},\quad a,b=0,1,2,\ldots,d-1\ .$ (1)

Here $X$ and $Z$ are generalizations of the Pauli matrices $\sigma_{x}$ and $\sigma_{z}$, which act in a particular basis $\{|j\rangle,j=0,1,2,\ldots,d-1\}$ according to

$X:|j\rangle$ $\rightarrow|j+1\ ({\rm mod}\ d)\rangle\ ,$
$Z:|j\rangle$ $\rightarrow\omega^{j}|j\rangle\ ,$ (2)

where $\omega=\exp(2\pi i/d)$. Note that it follows that

$ZX=\omega XZ.$ (3)

For $N$ qudits, there is a unitary operator basis with $d^{2N}$ elements consisting of all tensor products of single-qudit Pauli operators.

We will now imagine that errors with $|a|,|b|$ small compared to $d$ are common, but errors with large $|a|$ and $|b|$ are rare. This type of error model could be expected to apply in the case of a continuous quantum variable, which is formally the $d\rightarrow\infty$ limit of a qudit. For example, decoherence causes the position $q$ and momentum $p$ of a particle to diffuse with some nonzero diffusion constant. In any finite time interval $q$ and $p$ will drift by some amount that may be small, but is certainly not zero. How can we protect encoded quantum information under these conditions?

Fortunately, the general “stabilizer” framework *[9, 10]* for constructing quantum codes can be adapted to this setting. In this framework, one divides the elements of a unitary operator basis into two disjoint and exhaustive classes: the set ${\cal E}$ of “likely errors” that we want to protect against, and the rest, the “unlikely errors.” A code subspace is constructed as the simultaneous eigenspace of a set of commuting “stabilizer generators,” that generate an Abelian group, the “code stabilizer.” The code can reverse errors in the set ${\cal E}$ if, for each pair of errors $E_{a}$ and $E_{b}$, either $E_{a}^{\dagger}E_{b}$ lies in the stabilizer group, or $E_{a}^{\dagger}E_{b}$ fails to commute with some element of the stabilizer. (In the latter case, the two errors alter the eigenvalues of the generators in distinguishable ways; in the former case they do not, but we can successfully recover from an error of type $a$ by applying either $E_{a}^{\dagger}$ or $E_{b}^{\dagger}$.) In typical discussions of quantum coding, ${\cal E}$ is assumed to be the set of all tensor products of Pauli operators with weight up to $t$ (those that act trivially on all but at most $t$ qudits). But the same principles can be invoked to design codes that protect against errors in a set ${\cal E}$ with other properties.

Quantum codes for continuous variables have been described previously by Braunstein *[11]* and by Lloyd and Slotine *[12]*. For example, one code they constructed can be regarded as the continuous limit of a qudit code of the type originally introduced by Shor in the binary ($d=2$) case, an $[[N=9,k=1,2t+1=3]]$ code that protects a single qudit encoded in a block of 9 from arbitrary damage inflicted on any one of the 9. The 8 stabilizer generators of the code can be expressed as

$Z_{1}Z_{2}^{-1}\ ,Z_{2}Z_{3}^{-1}\ ,Z_{4}Z_{5}^{-1}\ ,Z_{5}Z_{6}^{-1}\ ,Z_{7}Z_{8}^{-1}\ ,Z_{8}Z_{9}^{-1}\ ,$
$(X_{1}X_{2}X_{3})\cdot(X_{4}X_{5}X_{6})^{-1}\ ,(X_{4}X_{5}X_{6})\cdot(X_{7}X_{8}X_{9})^{-1}\ ,$ (4)

and encoded operations that commute with the stabilizer and hence act on the encoded qudit can be chosen to be

$\bar{Z}$ $=$ $Z_{1}Z_{4}Z_{7}\ ,$
$\bar{X}$ $=$ $X_{1}X_{2}X_{3}\ .$ (5)

In the $d\rightarrow\infty$ limit, we obtain a code that is the simultaneous eigenspace of eight commuting operators acting on nine particles, which are

$q_{1}-q_{2}\ ,q_{2}-q_{3}\ ,q_{4}-q_{5}\ ,q_{5}-q_{6}\ ,q_{7}-q_{8},q_{8}-q_{9}\ ,$
$(p_{1}+p_{2}+p_{3})-(p_{4}+p_{5}+p_{6})\ ,$
$(p_{4}+p_{5}+p_{6})-(p_{7}+p_{8}+p_{9})\ .$ (6)

---

Logical operators that act in the code space are

$\bar{q}$ $=$ $q_{1}+q_{4}+q_{7}\ ,$
$\bar{p}$ $=$ $p_{1}+p_{2}+p_{3}\ .$ (7)

This code is designed to protect against errors in which one of the particles makes a large jump in $q$ or $p$ (or both) while the others hold still. But it provides little protection against small diffusive motions of all the particles, which allow $\bar{q}$ and $\bar{p}$ to drift.

Entanglement purification protocols for continuous variable systems have also been proposed — good entangled states can be distilled from noisy entangled states via a protocol that requires two-way classical communication *[13, 14]*. These purification protocols work well against certain sorts of errors, but their reliance on two-way classical communication makes them inadequate for accurately preserving unknown states in an imperfect quantum memory, or for robust quantum computation.

Returning to qudits, let us consider an example of a quantum code that can protect against small shifts in both amplitude and phase, but not against large shifts. It is already interesting to discuss the case of a system consisting of a single qudit, but where the dimension $n$ of the encoded system is (of course) less than $d$. For example, a qubit ($n=2$) can be encoded in a system with dimension $d=18$, and protected against shifts by one unit in the amplitude or phase of the qudit; that is, against errors of the form $X^{a}Z^{b}$ where $|a|,|b|\leq 1$. The stabilizer of this code is generated by the two operators

$X^{6},\quad Z^{6}\ ,$ (8)

and the commutation relations of the Pauli operators with these generators are

$(X^{a}Z^{b})\cdot X^{6}$ $=$ $\omega^{6b}\ X^{6}\cdot(X^{a}Z^{b})\ ,$
$(X^{a}Z^{b})\cdot Z^{6}$ $=$ $\bar{\omega}^{6a}\ Z^{6}\cdot(X^{a}Z^{b})\ .$ (9)

Therefore, a Pauli operator commutes with the stabilizer only if $a$ and $b$ are both multiples of $3=18/6$; this property ensures that the code can correct single shifts in both amplitude and phase. Logical operators acting on the encoded qudit are

$\bar{X}=X^{3}\ ,\quad\bar{Z}=Z^{3}\ ,$ (10)

which evidently commute with the stabilizer and are not contained in it.

Since the codewords are eigenstates of $Z^{6}$ with eigenvalue one, the only allowed values of $j$ are multiples of three. And since there are also eigenstates of $X^{6}$ with eigenvalue one, the codewords are invariant under a shift in $j$ by six units. A basis for the two-dimensional code space is

$|\bar{0}\rangle$ $=$ $\frac{1}{\sqrt{3}}\left(|0\rangle+|6\rangle+|12\rangle\right)\ ,$
$|\bar{1}\rangle$ $=$ $\frac{1}{\sqrt{3}}\left(|3\rangle+|9\rangle+|15\rangle\right)\ .$ (11)

If an amplitude error occurs that shifts $j$ by $\pm 1$, the error can be diagnosed by measuring the stabilizer generator $Z^{6}$, which reveals the value of $j$ modulo 3; the error is corrected by adjusting $j$ to the nearest multiple of 3. Phase errors are shifts in the Fourier transformed conjugate basis, and can be corrected similarly.

This code is actually perfect, meaning that each possible pair of eigenvalues of the generators $X^{6}$ and $Z^{6}$ is a valid syndrome for correcting a shift. There are nine possible errors $\{X^{a}Z^{b},\ |a|,|b|\leq 1\}$, and the Hilbert space of the qudit contains nine copies of the two-dimensional code space, one corresponding to each possible error. These “error spaces” just barely fit in the qudit space for $d=18=9\cdot 2$.

Similar perfect codes can be constructed that protect against larger shifts. For $d=r_{1}r_{2}n$, consider the stabilizer generators

$X^{r_{1}n},\quad Z^{r_{2}n}\ .$ (12)

There is an encoded qunit, acted on by logical operators

$\bar{X}$ $=$ $X^{r_{1}}\ ,$
$\bar{Z}$ $=$ $Z^{r_{2}}\ ,$ (13)

which evidently commute with the stabilizer and satisfy

$\bar{Z}\bar{X}=\omega^{r_{1}r_{2}}\bar{X}\bar{Z}=e^{2\pi i/n}\bar{X}\bar{Z}\ .$ (14)

The commutation relations of the Pauli operators with the generators are

$(X^{a}Z^{b})\cdot X^{r_{1}n}$ $=$ $\omega^{r_{1}nb}\ X^{r_{1}n}\cdot(X^{a}Z^{b})$
$=$ $e^{2\pi ib/r_{2}}\ X^{r_{1}n}\cdot(X^{a}Z^{b})\ ,$
$(X^{a}Z^{b})\cdot Z^{r_{2}n}$ $=$ $\bar{\omega}^{r_{2}na}\ Z^{r_{2}n}\cdot(X^{a}Z^{b})$
$=$ $e^{-2\pi ia/r_{1}}\ Z^{r_{2}n}\cdot(X^{a}Z^{b})\ .$ (15)

The phases are trivial only if $a$ is an integer multiple of $r_{1}$ and $b$ an integer multiple of $r_{2}$. Therefore, this code can correct all shifts with

$|a|$ $<$ $\frac{r_{1}}{2}\ ,$
$|b|$ $<$ $\frac{r_{2}}{2}\ .$ (16)

The number of possible error syndromes is $r_{1}r_{2}=d/n$, so the code is perfect.

Expressed in terms of $Z$ eigenstates, the codewords contain only values of $j$ that are multiples of $r_{1}$ (since $Z^{r_{2}n}=1$), and are invariant under a shift of $j$ by $r_{1}n$ (since $X^{r_{1}n}=1$). Hence a basis for the $n$-dimensional code subspace is

$|\bar{0}\rangle$ $=$ $\frac{1}{\sqrt{r_{2}}}\left(|0\rangle+|nr_{1}\rangle+\ldots+|(r_{2}-1)nr_{1}\rangle\right)\ ,$
$|\bar{1}\rangle$ $=$ $\frac{1}{\sqrt{r_{2}}}\left(|r_{1}\rangle+\ldots+|((r_{2}-1)n+1)r_{1}\rangle\right)\ ,$
$\ .$
$\ .$
$|\bar{n}-\bar{1}\rangle$ $=$ $\frac{1}{\sqrt{r_{2}}}\left(|(n-1)r_{1}\rangle+\ldots+|(r_{2}n-1)r_{1}\rangle\right)\ .$ (17)

---

If the states undergo an amplitude shift, the value of $j$ modulo $r_{1}$ is determined by measuring the stabilizer generator $Z^{r_{2}n}$, and the shift can be corrected by adjusting $j$ to the nearest multiple of $r_{1}$. The codewords have a similar form in the Fourier transformed conjugate basis (the basis of $X$ eigenstates), but with $r_{1}$ and $r_{2}$ interchanged. Therefore, amplitude shifts by less than $r_{1}/2$ and phase shifts by less than $r_{2}/2$ can be corrected.

## III A QUDIT IN A LANDAU LEVEL

A single electron in a uniform magnetic field in two dimensions provides an enlightening realization of our codes. General translations in a magnetic field are noncommuting, since an electron transported around a closed path acquires an Aharonov-Bohm phase $e^{ie\Phi}$, where $\Phi$ is the magnetic flux enclosed by the path. Two translations $T$ and $S$ commute only if the operator $TST^{-1}S^{-1}$ translates an electron around a path that encloses a flux $\Phi=k\Phi_{0}$, where $\Phi_{0}=2\pi/e$ is the flux quantum and $k$ is an integer.

Translations commute with the Hamiltonian $H$, and two translations $T_{1}$ and $T_{2}$ form a maximally commuting set if they generate a lattice that has a unit cell enclosing one quantum of flux. Simultaneously diagonalizing $H$, $T_{1}$ and $T_{2}$, we obtain a Landau level of degenerate energy eigenstates, one state corresponding to each quantum of magnetic flux. Then $T_{1}$ and $T_{2}^{n}$ are the stabilizer generators of a code, where $\bar{Z}=T_{1}^{1/n}$ and $\bar{X}=T_{2}$ are the logical operators on a code space of dimension $n$.

Suppose the system is in a periodically identified box (a torus), so that $T_{1}^{r_{1}}=(T_{2}^{n})^{r_{2}}=1$ are translations around the cycles of the torus. The number of flux quanta through the torus, and hence the degeneracy of the Landau level, is $nr_{1}r_{2}$. The code, then, embeds an $n$ dimensional system in a system of dimension $d=r_{1}r_{2}n$.

In this situation, the logical operations $\bar{X}$ and $\bar{Z}$ can be visualized as translations of the torus in two different directions; the stabilizer generator $\bar{X}^{n}$ is a translation by a fraction $1/r_{2}$ of the length of the torus in one direction, and the stabilizer generator $\bar{Z}^{n}$ is a translation by $1/r_{1}$ of the length in the other direction. Therefore, for any state in the code space, the wave function of the electron in a cell containing $n$ flux quanta is periodically repeated altogether $r_{1}r_{2}$ times to fill the entire torus. Our code can be regarded as a novel kind of “quantum repetition code” – identical “copies” of the wave function are stored in each of $r_{1}r_{2}$ cells. But of course there is only one electron, so if we detect the electron in one cell its state is destroyed in all the cells.

This picture of the state encoded in a Landau level cautions us about the restrictions on the type of error model that the code can fend off successfully. If the environment strongly probes one of the cells and detects nothing, the wave function is suppressed in that cell. This causes a $\bar{X}$ error in the encoded state with a probability of about $1/2r_{2}$, and a $\bar{Z}$ error with a probability of about $1/2r_{1}$. The code is more effective if the typical errors gently deform the state in each cell, rather than strongly deforming it in one cell.

## IV CONTINUOUS VARIABLE CODES FOR A SINGLE OSCILLATOR

Formally, we can construct quantum codes for systems described by continuous quantum variables by considering the large-$d$ limit of the shift-resistant codes described in §II. We might have hoped to increase $d$ to infinity while holding $r_{1}/d$ and $r_{2}/d$ fixed, maintaining the ability to correct shifts in both amplitude and phase that are a fixed fraction of the ranges of the qudit. However, since the perfect codes satisfy

$\frac{r_{1}}{d}=\frac{1}{nr_{2}}\ ,\quad\frac{r_{2}}{d}=\frac{1}{nr_{1}}\ ,$ (18)

this is not possible. Nonetheless, interesting codes can be obtained as the amplitude and phase of the qudit approach the position $q$ and momentum $p$ of a particle – we can hold fixed the size of the shifts $\Delta q$ and $\Delta p$ that can be corrected, as the ranges of $q$ and $p$ become unbounded.

Another option is to take $d\rightarrow\infty$ with $r_{1}/d\equiv\frac{1}{m}$ fixed and $r_{2}=m/n$ fixed, obtaining a rotor $Z=e^{i\theta}$ (or a particle in a periodically identified finite box) that can be protected against finite shifts in both the orientation $\theta$ of the rotor and its (quantized) angular momentum $L$. The stabilizer of this code is generated by

$Z^{r_{2}n}$ $\rightarrow e^{i\theta m}\ ,$
$X^{r_{1}n}$ $=$ $X^{d/r_{2}}\rightarrow e^{-2\pi iL(n/m)}$ (19)

and the logical operations are

$\bar{Z}$ $=$ $e^{i\theta m/n}$
$\bar{X}$ $=$ $e^{-2\pi iL/m}$ (20)

Since $\bar{X}$ shifts the value of $\theta$ by $2\pi/m$, and $\bar{Z}$ shifts the value of $L$ by $m/n=r_{2}$, this code can correct shifts in $\theta$ with $\Delta\theta<\pi/m$ and shifts in $L$ with $|\Delta L|<m/2n$.

Alternatively, we can consider a limit in which $r_{1}$ and $r_{2}$ both become large. We may write $r_{1}=\alpha/\varepsilon$ and $r_{2}=1/n\alpha\varepsilon$, where $d=nr_{1}r_{2}=1/\varepsilon^{2}$, obtaining a code with stabilizer generators

$Z^{r_{2}n}$ $\rightarrow\left(e^{2\pi iq\varepsilon}\right)^{(1/\alpha\varepsilon)}=e^{2\pi iq/\alpha}\ ,$
$X^{r_{1}n}$ $\rightarrow\left(e^{-ip\varepsilon}\right)^{(n\alpha/\varepsilon)}=e^{-inp\alpha}\ ,$ (21)

and logical operations

$\bar{Z}=e^{2\pi iq/n\alpha}\ ,\quad\bar{X}=e^{-ip\alpha}\ ,$ (22)

where $\alpha$ is an arbitrary real number. Using the identity $e^{A}e^{B}=e^{[A,B]}e^{B}e^{A}$ (which holds if $A$ and $B$ commute

---

with their commutator) and the canonical commutation relation $[q,p]=i$, we verify that

$\bar{Z}\bar{X}=\omega\bar{X}\bar{Z}\ ,\quad\omega=e^{2\pi i/n}\ .$ (23)

Since $\bar{X}$ translates $q$ by $\alpha$ and $\bar{Z}$ translates $p$ by $2\pi/n\alpha$, the code protects against shifts with

$|\Delta q|&lt;\frac{\alpha}{2}\ ,$
$|\Delta p|&lt;\frac{\pi}{n\alpha}\ .$ (24)

Note that the shifts in momentum and position that the code can correct obey the condition

$\Delta p\Delta q&lt;\frac{\pi}{2n}\hbar\ .$ (25)

In typical situations, errors in $q$ and $p$ are of comparable magnitude, and it is best to choose $\alpha=\sqrt{2\pi/n}$ so that

$\bar{Z}=\exp\left(iq\sqrt{\frac{2\pi}{n}}\right)\ ,\quad\bar{X}=\exp\left(-ip\sqrt{\frac{2\pi}{n}}\right)\ .$ (26)

Formally, the codewords are coherent superpositions of infinitely squeezed states, e.g. (up to normalization)

$|\bar{Z}=\omega^{j}\rangle=\sum_{s=-\infty}^{\infty}|q=\alpha(j+ns)\rangle\ ,$
$|\bar{X}=\bar{\omega}^{j}\rangle=\sum_{s=-\infty}^{\infty}|p=\frac{2\pi}{n\alpha}(j+ns)\rangle\ .$ (27)

(See Fig. 1.) Of course, realistic codewords will be normalizable finitely squeezed states, rather than nonnormalizable infinitely squeezed states. But squeezing in at least one of $p$ and $q$ is required to comfortably fulfill the condition eq. (25).

![img-0.jpeg](images/img-0.jpeg)
Figure 1: Codewords of the $n=2$ code. The states $|\bar{0}\rangle$, $|\bar{1}\rangle$ are superpositions of $q$ eigenstates, periodically spaced with period $2\alpha$; the two basis states differ by a displacement in $q$ by $\alpha$. The states $(|0\rangle\pm|1\rangle)/\sqrt{2}$ are superpositions of $p$ eigenstates, periodically spaced with period $2\pi/\alpha$; the two basis states differ by a displacement in $p$ by $\pi/\alpha$.

The Wigner function associated with the codeword wave function $\psi^{(j)}(q)\equiv\langle q|\bar{Z}=\omega^{j}\rangle$ is a sum of delta functions positioned at the sites of a lattice in phase space, where three quarters of the delta functions are positive and one quarter are negative. Explicitly, we have

$W^{(j)}(q,p)$ $\equiv$ $\frac{1}{2\pi}\int_{-\infty}^{\infty}dx\ e^{ipx}\psi^{(j)}(q+x/2)^{*}\psi^{(j)}(q-x/2)$ (28)
$\propto$ $\sum_{s,t=-\infty}^{\infty}(-1)^{st}\delta\left(p-\frac{\pi}{n\alpha}\cdot s\right)$
$\times$ $\delta\left(q-\alpha j-\frac{n\alpha}{2}\cdot t\right)\ ;$

the delta functions are negative on the sublattice with $s,t$ odd. If we integrate over $p$, the oscillating sign causes the terms with odd $t$ to cancel in the sum over $s$, and the surviving positive delta functions have support at $q=(n\cdot\mbox{integer}+j)\alpha$. If we integrate over $q$, the terms with odd $s$ cancel in the sum over $t$, and the surviving positive delta functions have support at $p=(2\pi/n\alpha)\cdot\mbox{integer}$. Wigner functions for the $\bar{X}$ eigenstates are similar, but with the roles of $q$ and $p$ interchanged.

It is also of interest to express the encoded states in terms of the basis of coherent states. Consider for example the encoded state with $\bar{X}=1$, which is the unique simultaneous eigenstate with eigenvalue one of the operators $e^{2\pi iq/\alpha}$ and $e^{-ip\alpha}$. In fact starting with any state $|\psi\rangle$, we can construct the encoded state (up to normalization) as

$\left(\sum_{s=-\infty}^{\infty}e^{-isp\alpha}\right)\cdot\left(\sum_{t=-\infty}^{\infty}e^{2\pi itq/\alpha}\right)|\psi\rangle$ (29)
$=$ $\sum_{s,t}\exp\left[i\left(-sp\alpha+2\pi tq/\alpha+\pi st\right)\right]|\psi\rangle\ .$

In particular, if we choose $|\psi\rangle$ to be the ground state $|0\rangle$ of the oscillator, then the operator $\sum_{s,t}\exp\left[i\left(-sp\alpha+2\pi tq/\alpha+\pi st\right)\right]$ displaces it to a coherent state centered at the point $(q,p)=(s\alpha,2\pi t/\alpha)$ in the quadrature plane. Thus the encoded state is an equally weighted superposition of coherent states, with centers chosen from the sites of a lattice in the quadrature plane whose unit cell has area $2\pi$. Since the coherent states are overcomplete the expansion is not unique; indeed, if we choose $|\psi\rangle$ to be a coherent state rather than the vacuum, then the lattice is rigidly translated, but the encoded state remains invariant.

We can envision the stabilizer of the code as a lattice of translations in phase space that preserve the code words, the lattice generated by the translations $e^{2\pi iq/\alpha}$ and $e^{-inp\alpha}$. In fact, this lattice need not be rectangular – we can encode an $n$-dimensional system in the Hilbert space of a single oscillator by choosing any two variables $Q$ and $P$ that satisfy the canonical commutation relation $[Q,P]=i$, and constructing the code space as the simultaneous eigenstate of $e^{2\pi iQ}$ and $e^{-inP}$. The unit cell of the lattice has area $2\pi\hbar n$, in keeping with the principle that each quantum state “occupies” an area $2\pi\hbar$ in the phase space of a system with one continuous degree of freedom.

---

## V Finite squeezing

Strictly speaking, our codewords are nonnormalizable states, infinitely squeezed in both $q$ and $p$. In practice, we will have to work with approximate codewords that will be finitely squeezed normalizable states. We need to consider how using such approximate codewords will affect the probability of error.

We will replace a position eigenstate $\delta(0)$ by a normalized Gaussian of width $\Delta$ centered at the origin,

$|\psi_{0}\rangle$ $=$ $\int_{-\infty}^{\infty}\frac{dq}{(\pi\Delta^{2})^{1/4}}e^{-\frac{1}{2}q^{2}/\Delta^{2}}|q\rangle$ (30)
$=$ $\int_{-\infty}^{\infty}\frac{dp}{(\pi/\Delta^{2})^{1/4}}e^{-\frac{1}{2}\Delta^{2}p^{2}}|p\rangle\ .$

A codeword, formally a coherent superposition of an infinite number of $\delta$-functions, becomes a sum of Gaussians weighted by a Gaussian envelope function of width $\kappa^{-1}$; in the special case of a two-dimensional code space, the approximate codewords become

$|\tilde{0}\rangle$ $=$ $N_{0}\sum_{s=-\infty}^{\infty}e^{-\frac{1}{2}\kappa^{2}(2s\alpha)^{2}}T(2s\alpha)|\psi_{0}\rangle\ ,$
$|\tilde{1}\rangle$ $=$ $N_{1}\sum_{s=-\infty}^{\infty}e^{-\frac{1}{2}\kappa^{2}[(2s+1)\alpha)]^{2}}T[(2s+1)\alpha]|\psi_{0}\rangle\ ,$ (31)

where $T(a)$ translates $q$ by $a$, $N_{0,1}$ are normalization factors, and we use e.g. $|\tilde{0}\rangle$ rather than $|\tilde{0}\rangle$ to denote the approximate codeword. We will assume that $\kappa\alpha$ and $\Delta/\alpha$ are small compared to one, so that $N_{0}\approx N_{1}\approx(4\kappa^{2}\alpha^{2}/\pi)^{1/4}$; then in momentum space, the approximate codeword becomes e.g.,

$(|\tilde{0}\rangle+|\tilde{1}\rangle)/\sqrt{2}$ $\approx$ $\left(\frac{\kappa^{2}\alpha^{2}}{\pi}\right)^{1/4}\int_{-\infty}^{\infty}\frac{dp}{(\pi/\Delta^{2})^{1/4}}e^{-\frac{1}{2}\Delta^{2}p^{2}}$ (32)
$\times$ $\sum_{s=-\infty}^{\infty}e^{-\frac{1}{2}\kappa^{2}(s\alpha)^{2}}e^{ip(\alpha s)}|p\rangle\ .$

By applying the Poisson summation formula,

$\sum_{m=-\infty}^{\infty}e^{-\pi a(m-b)^{2}}=(a)^{-1/2}\sum_{s=-\infty}^{\infty}e^{-\pi s^{2}/a}e^{2\pi isb}\ ,$ (33)

this approximate codeword can be rewritten as

$(|\tilde{0}\rangle+|\tilde{1}\rangle)/\sqrt{2}\approx\left(\frac{\kappa^{2}\alpha^{2}}{\pi}\right)^{1/4}\int_{-\infty}^{\infty}\frac{dp}{(\pi/\Delta^{2})^{1/4}}e^{-\frac{1}{2}\Delta^{2}p^{2}}$
$\times\frac{\sqrt{2\pi}}{\kappa\alpha}\sum_{m=-\infty}^{\infty}\exp\left[-\frac{1}{2}\left(p-\frac{2\pi}{\alpha}m\right)^{2}/\kappa^{2}\right]|p\rangle$
$=$ $\int_{-\infty}^{\infty}\frac{dp}{(\pi\kappa^{2})^{1/4}}\cdot\left(\frac{4\pi\Delta^{2}}{\alpha^{2}}\right)^{1/4}\sum_{m=-\infty}^{\infty}e^{-\frac{1}{2}\Delta^{2}p^{2}}$
$\times$ $\exp\left[-\frac{1}{2}\left(p-\frac{2\pi}{\alpha}m\right)^{2}/\kappa^{2}\right]|p\rangle\ ,$ (34)

again a superposition of Gaussians weighted by a Gaussian envelope. (See Fig. 2.)

Probability

Probability distribution in position space $P(q)=\frac{1}{2}|\langle q|(|\tilde{0}\rangle+|\tilde{1}\rangle)|^{2}$ for an approximate codeword with $\Delta=\kappa=.25$. The dashed line is the distribution’s Gaussian envelope.

The approximate codewords $|\tilde{0}\rangle,|\tilde{1}\rangle$ have a small overlap if $\Delta$ is small compared to $\alpha$ and $\kappa$ is small compared to $\pi/\alpha$. For estimating the error probability caused by the overlap, let’s consider the special case where $q$ and $p$ are treated symmetrically, $\alpha=\sqrt{\pi}$ and $\kappa=\Delta$; then

$|\langle q|\tilde{0}\rangle|^{2}\approx\frac{2}{\sqrt{\pi}}\sum_{s=-\infty}^{\infty}e^{-4\pi\Delta^{2}s^{2}}\exp[-(q-2s\sqrt{\pi})^{2}/\Delta^{2}]$ (35)

and

$\frac{1}{2}\left|\langle p|\tilde{0}\rangle+\langle p|\tilde{1}\rangle\right|^{2}$
$\approx$ $\frac{2}{\sqrt{\pi}}\sum_{m=-\infty}^{\infty}e^{-\Delta^{2}p^{2}}\exp[-(p-2m\sqrt{\pi})^{2}/\Delta^{2}]\ .$ (36)

To perform error recovery, we measure the value of $q$ and $p$ modulo $\sqrt{\pi}$ and then correct for the observed shift. In the state $|\tilde{0}\rangle$, the probability of failure is the probability that $q$ is closer to an odd multiple of $\sqrt{\pi}$ than an even multiple, and in the state $(|\tilde{0}\rangle+|\tilde{1}\rangle)/\sqrt{2}$, the error probability is the probability that $p$ is closer to an odd multiple of $\sqrt{\pi}$ than an even multiple. For both the amplitude and phase errors, the intrinsic error probability arising from the imperfections of the approximate codewords becomes exponentially small for small $\Delta$. Using the asymptotic expansion of the error function,

$\int_{x}^{\infty}dt\ e^{-t^{2}}=\left(\frac{1}{2x}\right)e^{-x^{2}}\left(1-O(1/x^{2})\right)\ ,$ (37)

we may estimate the error probability by summing the contributions from the tails of all the Gaussians, obtaining

---

$\mbox{Error Prob}<\frac{2}{\sqrt{\pi}}\left(\sum_{n=-\infty}^{\infty}e^{-4\pi\Delta^{2}n^{2}}\right)\cdot 2\int_{\sqrt{\pi}/2}^{\infty}dq\ e^{-q^{2}/\Delta^{2}}$
$\sim\frac{2}{\sqrt{\pi}}\cdot\frac{1}{2\Delta}\cdot 2\Delta\cdot\frac{\Delta}{\sqrt{\pi}}e^{-\pi/4\Delta^{2}}$
$=\frac{2\Delta}{\pi}e^{-\pi/4\Delta^{2}}\ .$ (38)

This error probability is about 1% for $\Delta\sim.5$, and is already less than $10^{-6}$ for a still modest value $\Delta\sim.25$. Using finitely squeezed approximate codewords does not badly compromise the error-correcting power of the code, since a gentle spreading in $p$ and $q$ is just the kind of error the code is intended to cope with.

The mean photon number of a finitely squeezed approximate codeword is

$\langle a^{\dagger}a\rangle+1/2=\frac{1}{2}\langle p^{2}+q^{2}\rangle\approx\Delta^{-2}$ (39)

for small $\Delta$. Therefore, an error probability of order $10^{-6}$ can be achieved with Gaussian approximate codewords that have mean photon number of about $(.25)^{-2}\sim 16$.

More generally, a finitely squeezed codeword $|\psi\rangle$ can be regarded as a perfect codeword $|\xi\rangle$ that has undergone an error; we may write

$|\psi\rangle\,=\,\int du\,dv\,\eta(u,v)\,e^{i(-up+vq)}|\xi\rangle,$ (40)

where $\eta(u,v)$ is an error “wave function.” In the special case of a Gaussian finitely squeezed codeword, we have

$\eta(u,v)\,=\,\frac{1}{\sqrt{\pi\kappa\Delta}}\exp\Bigl{(}-\frac{1}{2}(u^{2}/\Delta^{2}+v^{2}/\kappa^{2})\Bigr{)}\ ,$ (41)

where $\Delta$ and $\kappa$ are the squeezing parameters defined above.

If $\eta(u,v)$ vanishes for $|u|>\alpha/2$ or $|v|>\pi/(n\alpha)$, then the error is correctable. In this case, the interpretation of $\eta(u,v)$ as a wave function has a precise meaning, since there is an unambiguous decomposition of a state into codeword and error. Indeed, if $|\xi_{1}\rangle$, $|\xi_{2}\rangle$ are perfect codewords and $|\psi_{1}\rangle$, $|\psi_{2}\rangle$ are the corresponding finitely squeezed codewords with error wave functions $\eta_{1}$, $\eta_{2}$, then

$\langle\psi_{1}|\psi_{2}\rangle\,=\,\langle\xi_{1}|\xi_{2}\rangle\,\langle\eta_{1}|\eta_{2}\rangle\ ,$ (42)

where

$\langle\eta_{1}|\eta_{2}\rangle=\int du\,dv\ \eta_{1}(u,v)^{*}\,\eta_{2}(u,v)\ .$ (43)

## VI Continuous variable codes for many oscillators

The continuous variable codes described in §IV are based on simple lattices in the two-dimensional phase space of a single particle. We can construct more sophisticated codes from lattices in the $(2N)$-dimensional phase space of $N$ particles. Then codes of higher quality can be constructed that take advantage of efficient packings of spheres in higher dimensions.

For a system of $N$ oscillators, a tensor product of Pauli operators can be expressed in terms of the canonical variables $q_{i}$ and $p_{i}$ as

$U_{\alpha\beta}=\exp\left[i\sqrt{2\pi}\left(\sum_{i=1}^{N}\alpha_{i}p_{i}+\beta_{i}q_{i}\right)\right]\ ,$ (44)

where the $\alpha_{i}$’s and $\beta_{i}$’s are real numbers. (In this setting, the Pauli operators are sometimes called “Weyl operators.”) Two such operators commute up to a phase:

$U_{\alpha\beta}U_{\alpha^{\prime}\beta^{\prime}}=e^{2\pi i[\omega(\alpha\beta,\alpha^{\prime}\beta^{\prime})]}U_{\alpha^{\prime}\beta^{\prime}}U_{\alpha\beta}\ ,$ (45)

where

$\omega(\alpha\beta,\alpha^{\prime}\beta^{\prime})\equiv\alpha\cdot\beta^{\prime}-\alpha^{\prime}\cdot\beta$ (46)

is the symplectic form. Thus two Pauli operators commute if and only if their symplectic form is an integer.

Now a general continuous variable stabilizer code is the simultaneous eigenspace of commuting Pauli operators, the code’s stabilizer generators. If the continuous variable phase space is $2N$-dimensional and the code space is a finite-dimensional Hilbert space, then there must be $2N$ independent generators. The elements of the stabilizer group are in one-to-one correspondence with the points of a lattice ${\cal L}$ in phase space, via the relation

$U(k_{1},k_{2},\ldots k_{2N})=\exp\left[i\sqrt{2\pi}\left(\sum_{a=1}^{2N}k_{a}v_{a}\right)\right]\ .$ (47)

Here $\{v_{a},a=1,2,\ldots,2N\}$ are the basis vectors of the lattice (each a linear combination of $q$’s and $p$’s), the $k_{a}$’s are arbitrary integers, and $U(k_{1},k_{2},\ldots k_{2N})$ is the corresponding element of the stabilizer. For the stabilizer group to be Abelian, the symplectic inner product of any pair of basis vectors must be an integer; that is, the antisymmetric $2N\times 2N$ matrix

$A_{ab}=\omega(v_{a},v_{b})$ (48)

has integral entries. The lattice ${\cal L}$ has a $2N\times 2N$ generator matrix $M$ whose rows are the basis vectors,

\[ M=\left(\begin{array}[]{c}v_{1}\\
v_{2}\\
\cdot\\
\cdot\\
v_{2N}\end{array}\right)\ . \] (49)

In terms of $M$, the matrix $A$ can be expressed as

$A=M\omega M^{T}\ ,$ (50)

---

where $\omega$ denotes the $2N\times 2N$ matrix

\[ \omega=\left(\begin{array}[]{cc}0&I\\
-I&0\end{array}\right)\ , \] (51)

and $I$ is the $N\times N$ identity matrix.

The generator matrix of a lattice is not unique. The replacement

$M\rightarrow M^{\prime}=RM$ (52)

leaves the lattice unmodified, where $R$ is an invertible integral matrix with determinant $\pm 1$ (whose inverse is also integral). Under this replacement, the matrix $A$ changes according to

$A\rightarrow A^{\prime}=RAR^{T}\ .$ (53)

By Gaussian elimination, an $R$ can be constructed such that the antisymmetric matrix $A$ is transformed to

\[ A^{\prime}=\left(\begin{array}[]{cc}0&D\\
-D&0\end{array}\right)\ , \] (54)

where $D$ is a positive diagonal $N\times N$ matrix.

There are also Pauli operators that provide a basis for the operations acting on the code subspace – these are the Pauli operators that commute with the stabilizer but are not contained in the stabilizer. The operators that commute with the stabilizer themselves form a lattice ${\cal L}^{\perp}$ that is dual (in the symplectic form) to the stabilizer lattice. The basis vectors of this lattice can be chosen to be $\{u_{b},b=1,2,3,\ldots,2N\}$ such that

$\omega(u_{a},v_{b})=\delta_{ab}\ ;$ (55)

then the generator matrix

\[ M^{\perp}=\left(\begin{array}[]{c}u_{1}\\
u_{2}\\
\cdot\\
\cdot\\
u_{2N}\end{array}\right) \] (56)

of ${\cal L}^{\perp}$ has the property

$M^{\perp}\omega M^{T}=I\ .$ (57)

It follows from eq. (48) and eq. (55) that the ${\cal L}$ basis vectors can be expanded in terms of the ${\cal L}^{\perp}$ basis vectors as

$v_{a}=\sum_{b}\ A_{ab}u_{b}\ ,$ (58)

or

$M=AM^{\perp}\ ,$ (59)

and hence that

$\omega(u_{a},u_{b})=(A)^{-1}_{ba}\ ,$ (60)

or

$M^{\perp}\omega\left(M^{\perp}\right)^{T}=\left(A^{-1}\right)^{T}\ .$ (61)

If the lattice basis vectors are chosen so that $A$ has the standard form eq. (54), then

\[ \left(A^{-1}\right)^{T}=\left(\begin{array}[]{cc}0&D^{-1}\\
-D^{-1}&0\end{array}\right)\ . \] (62)

In the special case of a self-dual lattice, corresponding to a code with a one-dimensional code space, both $A$ and $A^{-1}$ must be integral; hence $D=D^{-1}$ and the standard form of $A$ is

\[ A=\left(\begin{array}[]{cc}0&I\\
-I&0\end{array}\right)=\omega\ . \] (63)

Since the code subspace is invariant under the translations in ${\cal L}$, we can think of the encoded information as residing on a torus, the unit cell of ${\cal L}$. The encoded Pauli operators $\{\bar{X}^{a}\bar{Z}^{b}\}$ are a lattice of translations on this torus, corresponding to the coset space ${\cal L}^{\perp}/{\cal L}$. The number of encoded Pauli operators is the ratio of the volume of the unit cell of ${\cal L}$ to the volume of the unit cell of ${\cal L}^{\perp}$, namely the determinant of $A$, which is therefore the square of the dimension of the Hilbert space of the code. Thus the dimension of the code space is

$n=|{\rm Pf}\ A|={\rm det}\ D\ ,$ (64)

where ${\rm Pf}\ A$ denotes the Pfaffian, the square root of the determinant of the antisymmetric matrix $A$.

The stabilizer lattice unit cell has volume $|{\rm Pf}\ A|$ in units with $h=2\pi\hbar=1$, and the unit cell of the lattice of encoded operations has volume $|{\rm Pf}\ A|^{-1}$ in these units. So the code fits an $n$-dimensional code space into $n$ units of phase space volume, as expected.

Codes of the CSS type (those analogous to the binary quantum codes first constructed by Calderbank and Shor *[15]* and by Steane *[16]*) are constructed by choosing one lattice ${\cal L}_{q}$ describing stabilizer generators that are linear combinations of the $q$’s, and another lattice ${\cal L}_{p}\subset{\cal L}^{\perp}_{q}$ describing stabilizer generators that are linear combinations of the $p$’s. (Here ${\cal L}^{\perp}_{q}$ denotes the Euclidean dual of the lattice ${\cal L}_{q}$.) The generator matrix of a CSS code has the form

\[ M=\left(\begin{array}[]{cc}M_{q}&0\\
0&M_{p}\end{array}\right)\ , \] (65)

where $M_{q}$ and $M_{p}$ are $N\times N$ matrices, and the integral matrix $A$ has the form

\[ A=\left(\begin{array}[]{cc}0&M_{q}M_{p}^{T}\\
-M_{p}M_{q}^{T}&0\end{array}\right)\ \] (66)

For single-oscillator codes described in §IV, $A$ is the $2\times 2$ matrix

\[ A=\left(\begin{array}[]{cc}0&n\\
-n&0\end{array}\right)\ , \] (67)

where $n$ is the code’s dimension. For a single-oscillator CSS code, the lattice is rectangular, as shown in Fig. 3.

---

![img-1.jpeg](images/img-1.jpeg)

Figure 3: The stabilizer lattice and its dual for an $n=2$ code of a single oscillator. Solid lines indicate the stabilizer lattice; solid and dotted lines together comprise the dual lattice. In units of $(2\pi\hbar)^{2}$, the unit cell of the stabilizer lattice (shaded) has area 2, and the unit cell of its dual has area $1/2$.

The closest packing of circles in two dimensions is achieved by the hexagonal lattice. The generator matrix for a hexagonally encoded qunit can be chosen to be

$M=\left(\frac{2}{\sqrt{3}}\cdot n\right)^{1/2}\left(\matrix{1&amp;0\cr 1/2&\sqrt{3}/2\cr}\right)\ ,$ (68)

and the dual lattice is generated by

$M^{\perp}=\frac{1}{n}\cdot M\ .$ (69)

The shortest vector of the dual lattice has length $\left(2/n\sqrt{3}\right)^{1/2}$, compared to length $1/\sqrt{n}$ for the square lattice. Therefore the size of the smallest uncorrectable shift is larger for the hexagonal code than for the square lattice code, by the factor $\left(2/\sqrt{3}\right)^{1/2}\approx 1.07457$.

An important special class of quantum codes for many oscillators are the concatenated codes. In particular, we can encode a qubit in each of $N$ oscillators using the code of §IV. Then we can use a binary stabilizer code that encodes $k$ qubits in a block of $N$ oscillators, and protects against arbitrary errors on any $t$ oscillators, where $2t+1$ is the binary code’s distance. The concatenated codes have the important advantage that they can protect against a broader class of errors than small diffusive shifts applied to each oscillator – if most of the oscillators undergo only small shifts in $p$ and $q$, but a few oscillators sustain more extensive damage, then concatenated codes still work effectively.

For example, there is a binary [[7, 1, 3]] quantum code, well suited to fault-tolerant processing, that encodes one logical qubit in a block of seven qubits and can protect against heavy damage on any one of the seven *[2]*. Given seven oscillators, we can encode a qubit in each one that is resistant to quantum diffusion, and then use the [[7, 1, 3]] block code to protect one logical qubit against severe damage to any one of the oscillators.

For $n\geq 5$, there is a [[5,1,3]] polynomial code *[17]*, also well suited to fault-tolerant processing, encoding one qunit in a block of 5. (Actually, [[5, 1, 3]] quantum codes exist for $n&lt;5$ as well *[6,7]*, but these codes are less conducive to fault-tolerant computing.) The larger value of $n$ increases the vulnerability of each qunit to shift errors. Hence, whether the [[7,1,3]] binary code or the [[5,1,3]] should be preferred depends on the relationship of the size of the typical shift errors to the rate of large errors.

## VII Error Models

What sort of errors can be corrected by these codes? The codes are designed to protect against errors that shift the values of the canonical variables $p$ and $q$. In fact the Pauli operators are a complete basis, so the action of a general superoperator ${\cal E}$ acting on the input density matrix $\rho$ of a single oscillator can be expanded in terms of such shifts, as in

${\cal E}(\rho)$ $=$ $\int d\alpha d\beta d\alpha^{\prime}d\beta^{\prime}\ C(\alpha,\beta;\alpha^{\prime}\beta^{\prime})$ (70)
$\times$ $e^{i(\alpha p+\beta q)}\ \rho\ e^{-i(\alpha^{\prime}p+\beta^{\prime}q)}\ .$

If the support of $C(\alpha,\beta;\alpha^{\prime},\beta^{\prime})$ is concentrated on sufficiently small values of its arguments, then the input $\rho$ can be recovered with high fidelity.

A useful model of decoherence is the special case of a “Pauli channel” in which $C(\alpha,\beta;\alpha^{\prime},\beta^{\prime})$ is diagonal and the superoperator can be expressed as

${\cal E}(\rho)=\int d\alpha d\beta\ P(\alpha,\beta)\ e^{i(\alpha p+\beta q)}\ \rho\ e^{-i(\alpha p+\beta q)}\ .$ (71)

Since ${\cal E}$ is positive and trace preserving, we infer that $P(\alpha,\beta)\geq 0$ and

$\int d\alpha d\beta\ P(\alpha,\beta)=1\ .$ (72)

Thus, we may interpret $P(\alpha,\beta)$ as a probability distribution: the phase space translation

$(q,p)\rightarrow(q-\alpha,p+\beta)$ (73)

is applied with probability $P(\alpha,\beta)$.

Weak interactions between an oscillator and its environment drive a diffusive process that can be well modeled by a Pauli channel. If the environment quickly “forgets” what it learns about the oscillator, the evolution of the oscillator can be described by a master equation. Over a short time interval $dt$, the shifts applied to the oscillator may be assumed to be small, so that the Pauli operator can be expanded in powers of $\alpha$ and $\beta$. Suppose that the shifts are symmetrically distributed in phase space such that

---

$\langle\alpha\rangle=\langle\beta\rangle=0\ ,$
$\langle\alpha^{2}\rangle=\langle\beta^{2}\rangle\ ,$
$\langle\alpha\beta\rangle=0\ ,$ (74)

where $\langle\cdot\rangle$ denotes the mean value determined by the probability distribution $P(\alpha,\beta)$. Suppose further that the shifts are diffusive, so that the mean square displacement increases linearly with $dt$; we may write

$\langle\alpha^{2}\rangle=\langle\beta^{2}\rangle=Ddt\ ,$ (75)

where $D$ is a diffusion constant. We then obtain

$\rho(t+dt)$ $=$ $\int d\alpha d\beta\ P(\alpha,\beta)\ e^{i(\alpha p+\beta q)}\rho\ e^{-i(\alpha p+\beta q)}$ (76)
$=$ $\rho(t)+Ddt\left(p\rho p-\frac{1}{2}p^{2}\rho-\frac{1}{2}\rho p^{2}\right)$
$+$ $Ddt\left(q\rho q-\frac{1}{2}q^{2}\rho-\frac{1}{2}\rho q^{2}\right)+O(dt^{3/2})\ ,$

or

$\dot{\rho}=-\frac{D}{2}[p,[p,\rho]]-\frac{D}{2}[q,[q,\rho]]\ .$ (77)

The interpretation of $D$ as a diffusion constant can be confirmed by computing

$\frac{d}{dt}\mbox{tr}\ \left(p^{2}\rho\right)=D=\frac{d}{dt}\mbox{tr}\ \left(q^{2}\rho\right)\ ;$ (78)

the mean square values of $p$ and $q$ increase with time as $Dt$.

More generally, the master equation contains a diffusive term determined by the covariance of the distribution $P(\alpha,\beta)$, and perhaps also a nondissipative drift term determined by the mean of $P(\alpha,\beta)$. Our quantum error-correcting codes can successfully suppress decoherence caused by quantum diffusion, if the recovery operation is applied often enough; roughly, the time interval $\Delta t$ between error correction steps should be small compared to the characteristic diffusion time $D^{-1}$.

Interactions with the environment might also damp the amplitude of the oscillator, as described by the master equation

$\dot{\rho}=\Gamma\left(a\rho a^{\dagger}-\frac{1}{2}a^{\dagger}a\rho-\frac{1}{2}\rho a^{\dagger}a\right)\ ;$ (79)

here $a=(q+ip)/\sqrt{2}$ is the annihilation operator and $\Gamma$ is a decay rate. This master equation cannot be obtained from a Pauli channel, but as for quantum diffusion, the effects of amplitude damping over short time intervals can be expressed in terms of small phase-space displacements.

The master equation for amplitude damping can be obtained as the $dt\to 0$ limit of the superoperator

$\rho(t+dt)$ $=$ $\mathcal{E}(\rho(t))=\left(\sqrt{\Gamma dt}\ a\right)\rho(t)\left(\sqrt{\Gamma dt}\ a^{\dagger}\right)$ (80)
$+\left(I-\frac{\Gamma dt}{2}a^{\dagger}a\right)\rho(t)\left(I-\frac{\Gamma dt}{2}a^{\dagger}a\right)\ .$

For $dt$ small, the annihilation operator can be expanded in terms of Pauli operators as

$\sqrt{\Gamma dt}\ a\approx$ $-\frac{i}{2}\left(e^{i\sqrt{\Gamma dt/2}\ q}-e^{-i\sqrt{\Gamma dt/2}\ q}\right)$ (81)
$+\frac{1}{2}\left(e^{i\sqrt{\Gamma dt/2}\ p}-e^{-i\sqrt{\Gamma dt/2}\ p}\right)$

Thus, if the time interval $\Delta t$ between error correction steps is small compared to the damping time $\Gamma^{-1}$, the displacements applied to codewords are small, and error correction will be effective.

Aside from decoherence, we also need to worry about “unitary errors.” For example, an inadvertent rotation of the phase of the oscillator induces the unitary transformation

$U(\theta)\equiv\exp\left(i\theta a^{\dagger}a\right)$ (82)

Like any unitary transformation, this phase rotation can be expanded in terms of Pauli operators. It is convenient to introduce the notation for the phase-space displacement operator

$D(\gamma)$ $\equiv$ $\exp\left(\gamma a-\gamma^{*}a^{\dagger}\right)$ (83)
$=$ $\exp\left(i\sqrt{2}\left[(\mbox{Im}\ \gamma)q-(\mbox{Re}\ \gamma)p\right]\right)\ ,$

where $\gamma$ is a complex number. The displacements satisfy the identity

$\mbox{tr}\left(D(\gamma)D(\eta)^{\dagger}\right)=\pi\delta^{2}(\gamma-\eta)\ ,$ (84)

so the operator $U(\theta)$ can be expanded in terms of displacements as

$U(\theta)=\frac{1}{\pi}\int d^{2}\gamma\ u_{\theta}(\gamma)D(\gamma)\ ,$ (85)

where

$u_{\theta}(\gamma)=\mbox{tr}\left(U(\theta)D(\gamma)^{\dagger}\right)\ .$ (86)

Evaluating the trace in the coherent state basis, we find that

$u_{\theta}(\gamma)=\frac{i\ e^{i\theta/2}}{2\sin(\theta/2)}\exp\left(-\frac{i}{2}|\gamma|^{2}\cot(\theta/2)\right)\ .$ (87)

For small $\theta$, the coefficient

$u_{\theta}(\gamma)\approx\frac{i}{\theta}\exp\left(-\ \frac{i}{\theta}|\gamma|^{2}\right)$ (88)

has a rapidly oscillating phase, and can be regarded as a distribution with support concentrated on values of $\gamma$ such that $|\gamma|^{2}\sim\theta$; indeed, formally

$\lim_{\theta\to 0}\ u_{\theta}(\gamma)=\pi\ \delta^{2}(\gamma)\ .$ (89)

Thus a rotation by a small angle $\theta$ can be accurately expanded in terms of small displacements – error correction is effective if an oscillator is slightly overrotated or underrotated.

---

VIII THE GAUSSIAN QUANTUM CHANNEL

At what rate can error-free digital information be conveyed by a noisy continuous signal? In classical information theory, an answer is provided by Shannon’s noisy channel coding theorem for the Gaussian channel *[18]*. This theorem establishes the capacity that can be attained by a signal with specified average power, for a channel with specified bandwidth and specified Gaussian noise power. The somewhat surprising conclusion is that a nonzero rate can be attained for any nonvanishing value of the average signal power.

A natural generalization of the Gaussian classical channel is the Gaussian quantum channel. The Gaussian quantum channel is a Pauli channel: $N$ oscillators are transmitted, and the $q$ and $p$ displacements acting on the oscillators are independent Gaussian random variables with mean 0 and variance $\sigma^{2}$. A code is an $M$-dimensional subspace of the Hilbert space of the $N$ oscillators, and the rate $R$ of the code (in qubits) is defined as

$R=\frac{1}{N}\log_{2}M\ .$ (90)

The quantum-information capacity $C_{Q}$ of the channel is the maximal rate at which quantum information can be transmitted with fidelity arbitrarily close to one.

The need for a constraint on the signal power to define the capacity of the Gaussian classical channel can be understood on dimensional grounds. The classical capacity (in bits) is a dimensionless function of the variance $\sigma^{2}$, but $\sigma^{2}$ has dimensions. Another quantity with the same dimensions as $\sigma^{2}$ is needed to construct a dimensionless variable, and the power fulfills this role. But no power constraint is needed to define the quantum capacity of the quantum channel. The capacity (in qubits) is a function of the dimensionless variable $\hbar/\sigma^{2}$, where $\hbar$ is Planck’s constant.

An upper bound on the quantum capacity of the Gaussian quantum channel was derived by Holevo and Werner *[19]*; they obtained (reverting now to units with $\hbar=1$)

$C_{Q}\leq\log_{2}(1/\sigma^{2})\ ,$ (91)

for $0<\sigma^{2}<1$, and $C_{Q}=0$ for $\sigma^{2}\geq 1$. They also computed the coherent information $I_{Q}$ of the Gaussian quantum channel, and maximized it over Gaussian signal states, finding *[19]*

$\left(I_{Q}\right)_{\rm max}=\log_{2}(1/e\sigma^{2})\ ,$ (92)

for $0<\sigma^{2}<1/e$ (where $e=2.71828\ldots$). The coherent information is conjectured to be an attainable rate *[20, 21, 22]*; if this conjecture is true, then eq. (92) provides a lower bound on $C_{Q}$.

Using our continuous variable codes, rigorous lower bounds on $C_{Q}$ can be established. For $\sigma^{2}$ sufficiently small, a nonzero attainable rate can be established asymptotically for large $N$ by either of two methods. In one method, the $n=2$ code described in §IV is invoked for each oscillator, and concatenated with a binary quantum code. In the other method, which more closely follows Shannon’s construction, a code for $N$ oscillators is constructed as in §VI, based on a close packing of spheres in $2N$-dimensional phase space. However (in contrast to the classical case), neither method works if $\sigma^{2}$ is too large. For large $\sigma^{2}$, encodings can be chosen that protect against $q$ shifts or against $p$ shifts, but not against both.

To establish an attainable rate using concatenated coding (the method that is easier to explain), we first recall a result concerning the quantum capacities of binary channels *[15, 23]*. If $X$ and $Z$ errors are independent and each occur with probability $p_{e}$, then binary CSS codes exist that achieve a rate

$R$ $>1-2H_{2}(p_{e})$
$\equiv 1+2p_{e}\log_{2}p_{e}+2(1-p_{e})\log_{2}(1-p_{e})\ ;$ (93)

this rate is nonzero for $p_{e}<.1100$.

Now, for the Gaussian quantum channel, if we use the $n=2$ continuous variable code, errors afflicting the encoded qubit are described by a binary channel with independent $X$ and $Z$ errors. Since the code can correct shifts in $q$ or $p$ that satisfy $\Delta q,\Delta p<\sqrt{\pi}/2$, the error probability is

$p_{e}<2\cdot\frac{1}{\sqrt{2\pi\sigma^{2}}}\int_{\sqrt{\pi}/2}^{\infty}dx\ e^{-x^{2}/2\sigma^{2}}\ .$ (94)

Since the expression bounding $p_{e}$ in eq. (94) has the value $.110$ for $\sigma\approx.555$, we conclude that the Gaussian quantum channel has nonvanishing quantum capacity $C_{Q}$ provided that

$\sigma<.555\ .$ (95)

One might expect to do better by concatenating the hexagonal $n=2$ single-oscillator code with a binary stabilizer code, since the hexagonal code can correct larger shifts than the code derived from a square lattice. For the Gaussian quantum channel, the symmetry of the hexagonal lattice ensures that $X$, $Y$, and $Z$ errors afflicting the encoded qubit are equally likely. A shift is correctable if it lies within the “Voronoi cell” of the dual lattice, the cell containing all the points that are closer to the origin than to any other lattice site. By integrating the Gaussian distribution over the hexagonal Voronoi cell, we find that the probability $p_{e,{\rm total}}$ of an uncorrectable error satisfies

$p_{e,{\rm total}}<1-\frac{12}{2\pi\sigma^{2}}\int_{0}^{r}dx\int_{0}^{x/\sqrt{3}}dy\,e^{-(x^{2}+y^{2})/2\sigma^{2}}\ ,$ (96)

where $r=(\pi/2\sqrt{3})^{1/2}$ is the size of the smallest uncorrectable shift. For a binary quantum channel with

---

equally likely $X$, $Y$, and $Z$ errors, it is known *[24]* that there are stabilizer codes achieving a nonvanishing rate for $p_{e,{\rm total}}&lt;.1905$; our bound on $p_{e,{\rm total}}$ reaches this value for $\sigma\approx.547$.

Somewhat surprisingly, for very noisy Gaussian quantum channels, square lattice codes concatenated with CSS codes seem to do better than hexagonal codes concatenated with stabilizer codes. The reason this happens is that a CSS code can correct independent $X$ and $Z$ errors that occur with total probability $p_{e,{\rm total}}=p_{X}+p_{Z}-p_{X}\cdot p_{Z}$, which approaches $.2079&gt;.1905$ as $p_{X}=p_{Z}\rightarrow.1100.$ For a given value of $\sigma$, the qubit encoded in each oscillator will have a lower error probability if the hexagonal code is used. But if the square lattice is used, a higher qubit error rate is permissible, and this effect dominates when the channel is very noisy.

We remark that this analysis is readily extended to more general Gaussian quantum channels. We may consider Pauli channels acting on a single oscillator in which the probability distribution $P(\alpha,\beta)$ is a more general Gaussian function, not necessarily symmetric in $p$ and $q$. In that case, a symplectic transformation (one preserving the commutator of $p$ and $q$) can be chosen that transforms the covariance matrix of the Gaussian to a multiple of the identity; therefore, this case reduces to that already discussed above. We may also consider channels acting on $N$ oscillators that apply shifts in the $2N$-dimensional phase space, chosen from a Gaussian ensemble. Again there is a symplectic transformation that diagonalizes the covariance matrix; therefore, this case reduces to $N$ independent single oscillator channels, each with its own value of $\sigma^{2}$ *[25]*.

## IX Symplectic Operations

To use these codes for fault-tolerant quantum computation, we will need to be able to prepare encoded states, perform error recovery, and execute quantum gates that act on the encoded quantum information. The most difficult task is encoding; we will postpone the discussion of encoding until after we have discussed encoded operations and error recovery.

Suppose, for example, that we have $N$ oscillators, each encoding a qunit. We wish to apply $U(n^{N})$ transformations that preserve the code subspace of the $N$ qunits. As is typical of quantum codes, we will find that there is a discrete subgroup of $U(n^{N})$ that we can implement “easily;” but to complete a set of universal gates we must add further transformations that are “difficult.” In the case of our continuous variable codes, the easy gates will be accomplished using linear optical elements (phase shifters and beam splitters), along with elements that can “squeeze” an oscillator. For the “difficult” gates we will require the ability to count photons.

The easy gates are the gates in the Clifford group. In general, the Clifford group of a system of $N$ qunits is the group of unitary transformations that, acting by conjugation, take tensor products of Pauli operators to tensor products of Pauli operators (one says that they preserve the “Pauli group”). Since for $N$ oscillators the tensor products of Pauli operators have the form eq. (44), the Clifford group transformations, acting by conjugation, are linear transformations of the $p$’s and $q$’s that preserve the canonical commutation relations. Such transformations are called symplectic transformations. The symplectic group has a subgroup that preserves the photon number

${\rm total\ photon\ number}=\sum_{i=1}^{N}a_{i}^{\dagger}a_{i}\ .$ (97)

The transformations in this subgroup can be implemented with linear optics *[26]*. The full symplectic group also contains “squeeze operators” that take an $a$ to a linear combination of $a$’s and $a^{\dagger}$’s; equivalently, the squeeze operators rescale canonical operators by a real number $\lambda$ along one axis in the quadrature plane, and by $\lambda^{-1}$ along the conjugate axis, as in (for example)

$q_{1}\rightarrow\lambda q_{1}\ ,\ \ \ p_{1}\rightarrow\lambda^{-1}p_{1}\ .$ (98)

With squeezing and linear optics we can in principle implement any symplectic transformation.

Aside from the symplectic transformations, we will also assume that it is easy to do displacements that shift $q$ and $p$ by constants. A displacement of $q_{1}$ by $c$ is actually the limiting case of a symplectic transformation on two oscillators $q_{1}$ and $q_{2}$:

$q_{1}\rightarrow q_{1}+\varepsilon q_{2}\ ,\ \ \ p_{1}\rightarrow p_{1}+\varepsilon p_{2}$
$q_{2}\rightarrow q_{2}-\varepsilon q_{1}\ ,\ \ \ p_{2}\rightarrow p_{2}-\varepsilon p_{1}$ (99)

where $\varepsilon\rightarrow 0$ with $\varepsilon q_{2}=c$ held fixed.

Since for the code with stabilizer generators eq. (21) the Pauli operators acting on our encoded qunits are $\bar{X}=e^{ip\alpha}$ and $\bar{Z}=e^{2\pi iq/n\alpha}$, the Clifford group transformations acting on $N$ qunits constitute a subgroup of the symplectic transformations (including shifts) acting on $N$ oscillators, the subgroup that preserves a specified lattice in phase space. Thus we can do any encoded Clifford group gate we please by executing an appropriate symplectic transformation (possibly including a shift).

A similar comment applies to the case of a qunit encoded in a qudit. Since the logical Pauli operators are $\bar{X}=X^{r_{1}}$ and $\bar{Z}=Z^{r_{2}}$, each Clifford group transformation in the $n$-dimensional code space is also a Clifford group transformation on the underlying qudit.

But we must also be sure that our implementation of the Clifford group is fault tolerant. In previous discussions of quantum fault tolerance for $[[N,k,2t+1]]$ codes, the central theme has been that propagation of error from one qudit to another in the same code block must be very carefully controlled *[27, 28]*. For shift-resistant codes the main issue is rather different. Since each qudit typically

---

has a (small) error anyway, propagation of error from one qudit to another is not necessarily so serious. But what must be controlled is amplification of errors – gates that turn small errors into large errors should be avoided.

The Clifford group can be generated by gates that are fault-tolerant in this sense. The Clifford group for qunits can be generated by three elements. The SUM gate is a two-qunit gate that acts by conjugation on the Pauli operators according to

$\mbox{SUM}:~{}~{}~{}X_{1}^{a}X_{2}^{b}\rightarrow X_{1}^{a}X_{2}^{b-a}~{},~{}~{}~{}Z_{1}^{a}Z_{2}^{b}\rightarrow Z_{1}^{a+b}Z_{2}^{b}~{}.$ (100)

Here qunit 1 is said to be the control of the SUM gate, and qunit 2 is said to be its target; in the binary ($n=2$) case, SUM is known as controlled-NOT, or CNOT. The Fourier gate $F$ acts by conjugation as

$F:~{}~{}~{}X\rightarrow Z~{},~{}~{}~{}Z\rightarrow X^{-1}~{};$ (101)

for $n=2$ the Fourier Transform is called the Hadamard gate. The phase gate $P$ acts as

$P:~{}~{}~{}~{}X\rightarrow(\eta)XZ~{},~{}~{}~{}Z\rightarrow Z~{},$ (102)

where the $n$-dependent phase $\eta$ is $\omega^{1/2}$ if $n$ is even and 1 if $n$ is odd. Any element of the Clifford group can be expressed as a product of these three generators. (In Ref. *[8]* another gate $S$ was included among the generators of the Clifford group, but in fact the $S$ gate can be expressed as a product of SUM gates.)

For an $n$-dimensional system encoded in a continuous variable system, these Clifford group generators can all be realized as symplectic transformations. In the case where the stabilizer generators are symmetric in $q$ and $p$,

$\bar{X}=\exp\left(-ip\sqrt{\frac{2\pi}{n}}\right)~{},~{}~{}~{}\bar{Z}=\exp\left(iq\sqrt{\frac{2\pi}{n}}\right)~{},$ (103)

the required symplectic transformations are

$\mbox{SUM}:~{}~{}~{}q_{1}\rightarrow q_{1}~{},~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~~{}~{}~~{}~~{}~~{}~~{}~~{}~~~{}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 103$

where the $n$-dependent shift $c$ is 0 for $n$ even and $\sqrt{\pi/2n}$ for $n$ odd. Under these symplectic transformations, small deviations of $q$ and $p$ from the stabilizer lattice remain small; in this sense the transformations are fault tolerant.

## X Error recovery

If we are willing to destroy the encoded state, then measuring the encoded $\bar{X}$ or $\bar{Z}$ is easy – we simply conduct a homodyne measurement of the $q$ or $p$ quadrature of the oscillator. For example, suppose that we measure $q$ for a state in the code subspace. If there are no errors and the measurement has perfect resolution, the only allowed values of $q$ will be integer multiples of $\alpha$. If there are errors or the measurement is imperfect, classical error correction can be applied to the outcome, by adjusting it to the nearest $\alpha\cdot k$, where $k$ is an integer. Then the outcome of the measurement of $\bar{Z}$ is $\omega^{k}$.

To diagnose errors in a coded data state, we must measure the stabilizer generators. This measurement can be implemented by “feeding” the errors from the code block to a coded ancilla, and then measuring the ancilla destructively, following the general procedure proposed by Steane *[29]* (see Fig. 4). For example, to measure the generator $e^{2\pi iq/\alpha}$ (i.e., the value of $q$ modulo $\alpha$), we prepare the ancilla in the state $(|\bar{0}\rangle+|\bar{1}\rangle)/\sqrt{2}$, the equally weighted superposition of all $|q=s\cdot\alpha\rangle$, $s$ an integer. Then a SUM gate is executed with the data as control and the ancilla as target – acting according to

$q_{2}\rightarrow q_{1}+q_{2}~{},$ (105)

where $q_{1},q_{2}$ are the values of $q$ for the data and ancilla respectively, prior to the execution of the SUM gate. By measuring $q$ of the ancilla, the value of $q_{1}+q_{2}$ is obtained, and this value modulo $\alpha$ determines the shift that should be applied to the data to recover from the error.

Similarly, to measure the stabilizer generator $e^{inp\alpha}$, we prepare the ancilla in the state $|\bar{0}\rangle$, the equally weighted superposition of all $|p=s\cdot 2\pi/n\alpha\rangle$, $s$ an integer. Then a SUM gate is executed with the ancilla as control and the data as target. Finally, the $p$ quadrature of the ancilla is measured. The outcome reveals the value of $p_{2}-p_{1}$ prior to the SUM gate, where $p_{1}$ is the momentum of the data, and $p_{2}$ is the momentum of the ancilla. The measured value modulo $2\pi/n\alpha$ then determines the shift that should be applied to the data to recover from the error.

(a)

![img-2.jpeg](images/img-2.jpeg)

(b)

![img-3.jpeg](images/img-3.jpeg)

Figure 4: Measurement of the error syndrome. (a) To diagnose the $q$ shift, an ancilla is prepared in the encoded $\bar{X}=1$ state, a SUM gate is executed with the data as control and the ancilla as target, and the position of the ancilla is measured. (b) To diagnose the $p$ shift, the ancilla is prepared in the $\bar{Z}=1$ state, a SUM gate is executed with the ancilla as control and the data as target, and the momentum of the ancilla is measured.

---

Of course, the ancilla used in the syndrome measurement can also be faulty, resulting in errors in the syndrome and imperfect recovery. Similarly, the measurement itself will not have perfect resolution, and the shift applied to recover will not be precisely correct. Furthermore, as is discussed in §V, the ideal codewords are unphysical nonnormalizable states, so that the encoded information will always be carried by approximate codewords. For all these reasons, deviations from the code subspace are unavoidable. But if a fresh supply of ancilla oscillators is continuously available, we can prevent these small errors from accumulating and eventually damaging the encoded quantum information.

## XI Universal Quantum Computation

Symplectic transformations together with homodyne measurements are adequate for Clifford group computation and for error recovery (assuming we have a supply of encoded states). But to achieve universal computation in the code space, we need to introduce additional operations. Fortunately, the quantum optics laboratory offers us another tool that can be used to go beyond the symplectic computational model – the ability to count photons.

There are a variety of ways in which photon counting can be exploited to complete a universal set of fault-tolerant gates. We will describe two possible ways, just to illustrate how universal fault-tolerant quantum computation might be realized with plausible experimental tools. For this discussion, we will consider the binary case $n=2$.

### XI.1 Preparing a Hadamard eigenstate

We can complete the universal gate set if we have the ability to prepare eigenstates of the Hadamard operator $H$ *[30, 31]*. For this purpose it suffices to be able to destructively measure $H$ of an encoded qubit. Assuming we are able to prepare a supply of the encoded $\bar{Z}$ eigenstate $|\bar{0}\rangle$, we can make an encoded EPR pair using symplectic gates. Then by destructively measuring $H$ for one encoded qubit in the pair, we prepare the other qubit in an encoded eigenstate of $H$ with known eigenvalue.

But how can we destructively measure $H$? The Hadamard gate acts by conjugation on the encoded Pauli operators according to

$H:\quad\bar{X}\to\bar{Z}\ ,\quad\bar{Z}\to\bar{X}\ .$ (106)

If we use the code that treats $q$ and $p$ symmetrically so that $\bar{X}=\exp(-ip\sqrt{\pi})$ and $\bar{Z}=\exp(iq\sqrt{\pi})$, then the Hadamard gate can be implemented by the symplectic transformation.

$q\to p\ ,\quad p\to-q$ (107)

(recalling that $\bar{X}^{2}=\bar{Z}^{2}=I$ on the code subspace). This transformation is just the Fourier transform

$F:\quad\exp\left(i\frac{\pi}{2}a^{\dagger}a\right)$ (108)

(where $a^{\dagger}a$ is the photon number), which describes the natural evolution of the oscillator for one quarter cycle. Thus the phase of the Hadamard operator is simply the photon number modulo four; we can measure the eigenvalue of the encoded Hadamard transformation by counting photons.

In fact the photon number in the code space is even – all codewords are invariant under a $180^{\circ}$ rotation in the quadrature plane. Because of this feature, the preparation of the Hadamard eigenstate has some fault tolerance built in; if the photon count is off by one, the number will be odd and an error will be detected. In that case we reject the state we have prepared and make a new attempt. If the photon number is large, then obtaining a reliable determination of the photon number modulo four will require highly efficient photodetection. But on the other hand, the photon number need not be very large – the mean value of $a^{\dagger}a$ is about $\Delta^{-2}$ where $\Delta$ is the squeeze factor, and we have seen that the intrinsic error rate due to imperfect squeezing is quite small for $\Delta\sim 1/4$, or $\langle a^{\dagger}a\rangle\sim 16$.

An alternative to preparing an encoded EPR pair and destructively measuring one member of the pair is to prepare $|\bar{0}\rangle$ and then perform a quantum nondemolition measurement of the photon number modulo 4. This might be done by coupling the oscillator to a two-level atom as proposed in Ref. *[32]*. Indeed, since only one bit of information needs to be collected (the photon number is either 0 or 2 modulo 4), the measurement could be made in principle by reading out a single atom. Suppose that the coupling of oscillator to atom is described by the perturbation

$H^{\prime}=\lambda\ a^{\dagger}a\ \sigma_{z}\ ,$ (109)

where $\sigma_{z}=-1$ in the atomic ground state $|g\rangle$ and $\sigma_{z}=1$ in the atomic excited state $|e\rangle$. By turning on this coupling for a time $t=\pi/4\lambda$, we execute the unitary transformation

$U=\exp(-i(\pi/4)\ a^{\dagger}a\ \sigma_{z})\ .$ (110)

Then the atomic state $(|g\rangle+|e\rangle)/\sqrt{2}$ evolves as

$U:$ $\quad\frac{1}{\sqrt{2}}(|g\rangle+|e\rangle)$ (111)
$\quad\to\frac{1}{\sqrt{2}}e^{ia^{\dagger}a\pi/4}(|g\rangle+e^{-ia^{\dagger}a\pi/2}|e\rangle)\ .$

By measuring the atomic state in the basis $(|g\rangle\pm|e\rangle)/\sqrt{2}$, we read out the value of the photon number modulo 4 (assumed to be either 2 or 4). Since this is a nondemolition measurement, it can be repeated to improve reliability. By measuring the photon number mod 4 many times

---

(perhaps with rounds of error correction in between the measurements), we obtain a Hadamard eigenstate with excellent fidelity.

How does the ability to construct the Hadamard eigenstate enable us to achieve universal quantum computation? We can make contact with constructions that have been described previously in the literature by observing that the Hadamard eigenstate can be transformed by applying symplectic gates to the “$\pi/8$ phase state.” First note that the two Hadamard eigenstates can be converted to one another by applying the encoded gate $\bar{X}\bar{Z}$, which can be implemented by shifting both $p$ and $q$. Therefore it is sufficient to consider the eigenstate corresponding to the eigenvalue 1,

$|\psi_{H=1}\rangle\,=\,\cos(\pi/8)\,|0\rangle+\sin(\pi/8)\,|1\rangle\ .$ (112)

By applying the symplectic single-qubit gate

$H\cdot P^{-1}$ $\equiv$ \[ \frac{1}{\sqrt{2}}\left(\begin{array}[]{cc}1&1\\
1&-1\end{array}\right)\cdot\left(\begin{array}[]{cc}1&0\\
0&-i\end{array}\right) \] (113)
$=$ $\frac{1}{\sqrt{2}}\left(\begin{array}[]{cc}1&-i\\
1&i\end{array}\right)\ ,$

we obtain the $\pi/8$ state

$|\psi_{\pi/8}\rangle\,=\,\frac{1}{\sqrt{2}}\Big{(}e^{-i\pi/8}|0\rangle+e^{i\pi/8}\,|1\rangle\Big{)}\ .$ (114)

Now this $\pi/8$ state can be used to perform the non-symplectic phase gate

$S=\left(\begin{array}[]{cc}e^{-i\pi/8}&0\\
0&e^{i\pi/8}\end{array}\right)\ ,$ (115)

which completes the universal gate set *[33, 34]*. The gate is constructed by executing the circuit shown in Fig. 5. We perform a CNOT gate with the arbitrary single-qubit state $|\psi\rangle=a|0\rangle+b|1\rangle$ as the control, and the $\pi/8$ phase state as the target; then the target qubit is measured in the basis $\{|0\rangle,|1\rangle\}$. If the measurement outcome is $|0\rangle$ (which occurs with probability $1/2$), then the control qubit has become $ae^{i\pi/8}|0\rangle+be^{-i\pi/8}|1\rangle=S|\psi\rangle$ and we are done. If the measurement outcome is $|1\rangle$, then the control qubit has become $ae^{-i\pi/8}|0\rangle+be^{i\pi/8}|1\rangle$, and we obtain $S|\psi\rangle$ by applying the symplectic single-qubit gate

$e^{-i\pi/4}P=\left(\begin{array}[]{cc}e^{-i\pi/4}&0\\
0&e^{i\pi/4}\end{array}\right)\ .$ (116)

Implementation of the $S$ gate. An ancilla is prepared in the state $|\psi_{\pi/8}\rangle$, and a CNOT gate is executed with the data as control and the ancilla as target; then the ancilla is measured in the basis $\{|0\rangle,\,|1\rangle\}$. A $P$ gate is applied to the data conditioned on the measurement outcome.

Completing the universal gate set by measuring the Hadamard transformation has some drawbacks. For one thing, while photon number modulo four corresponds to the Hadamard eigenvalue in the ideal code space, this correspondence will not apply to approximate codewords unless they are of a special type.

Recall that the imperfections of the codewords arising from finite squeezing can be described by an “embedded error” $|\eta\rangle$ as in eq. (40); a Gaussian approximate codeword has a Gaussian embedded error

$\eta(u,v)\,=\,\frac{1}{\sqrt{\pi\Delta\kappa}}\exp\Big{(}-\frac{1}{2}(u^{2}/\Delta^{2}+v^{2}/\kappa^{2})\Big{)},$ (117)

where $\Delta$ is the width in $q$ and $\kappa$ is the width in $p$. Symplectic gates act separately on the encoded qubit and the “embedded error” $|\eta\rangle$; for example, the Fourier transform gate and the SUM gate act on the error according to

$F:$ $\qquad|u,v\rangle\qquad\rightarrow\,|v,-u\rangle\ ,$
$\mbox{SUM}:|u_{1},v_{1};u_{2},v_{2}\rangle$ $\rightarrow\,|u_{1},\,v_{1}+v_{2};\,u_{2}-u_{1},\,v_{2}\rangle\ .$ (118)

By measuring the photon number modulo 4, we actually measure the product of the eigenvalue of the Hadamard gate acting on the codeword and the eigenvalue of $F$ acting on the embedded error. The latter always equals 1 if we use symmetrically squeezed codewords, with $\Delta=\kappa$.

Symmetric squeezing is not in itself sufficient to ensure that the measurement of the photon number modulo 4 will prepare the desired encoded Hadamard eigenstate. We also need to consider how the embedded error is affected by the preparation of the EPR pair that precedes the measurement. To prepare the EPR pair, we use the SUM gate. Suppose that we start with two symmetrically squeezed states. Then the SUM gate yields the error wave function

$\eta^{\prime}(u_{1},v_{1};u_{2},v_{2})$ (119)
$=$ $\exp\left(-\left(u_{1}^{2}+(v_{1}-v_{2})^{2}+(u_{1}+u_{2})^{2}+v_{2}^{2}\right)/\Delta^{2}\right)\ .$

Not only is it not symmetric, but the error is entangled between the two oscillators. The Fourier transform measurement will not give the desired result when applied to either oscillator.

To ameliorate this problem, we could perform error correction after the preparation of the EPR pair and before the measurement, where the error correction protocol has been designed to produce symmetrically squeezed states. Or we could avoid preparing the EPR state by using the nondemolition measurement of photon number modulo 4, as described above.

### IV.2 Preparing a cubic phase state

Now we will describe another way to use photon counting to implement non-symplectic gates, which is less sensitive to the codeword quality. Again, we will complete

---

the universal gate set by constructing the $\pi/8$ phase gate $S$.

For our binary ($n=2$) code, the code subspace has the basis

$|\bar{0}\rangle$ $=$ $\sum_{s=-\infty}^{+\infty}\,|q=2s\alpha\rangle\ ,$
$|\bar{1}\rangle$ $=$ $\sum_{s=-\infty}^{+\infty}\,|q=(2s+1)\alpha\rangle\ .$ (120)

(For now we ignore the embedded error due to imperfect squeezing; it will be taken into account later.) An $S$ gate acting on the encoded qubit is implemented (up to an irrelevant overall phase) by the unitary operator

$W$ $=$ $\exp\left(\frac{i\pi}{4}\left[2(q/\alpha)^{3}+(q/\alpha)^{2}-2(q/\alpha)\right]\right)\ .$ (121)

Indeed, we can check that

$2x^{3}+x^{2}-2x\ ({\rm mod}\ 8)$ $=$ \[ \left\{\begin{array}[]{ll}0,&\mbox{if }x=2s\ ,\\
1,&\mbox{if }x=2s+1\ .\end{array}\right. \] (122)

The operator $W$ is the product of a symplectic gate and the cubic phase gate

$V_{\gamma}$ $=$ $\exp(i\gamma q^{3})\ ,$ (123)

where $\gamma=\pi/(2\alpha^{3})$. But how do we implement the cubic gate? In fact, if we are able to prepare a “cubic phase state”

$|\gamma\rangle=\int dx\,e^{i\gamma x^{3}}|x\rangle\ ,$ (124)

then we can perform the gate $V_{\gamma}$ by executing the circuit shown in Fig. 6.

Implementation of the cubic phase gate. An ancilla is prepared in the state $|\gamma\rangle$, and a SUM^{-1} gate is executed with the data as control and the ancilla as target; then the position of the ancilla is measured. A symplectic gate $U(a)$ is then applied to the data, conditioned on the outcome $a$ of the measurement.

To understand how the circuit works, consider the more general problem of implementing a phase gate that acts on the position eigenstates according to

$V_{\phi}:|q\rangle\rightarrow e^{i\phi(q)}|q\rangle$ (125)

(where $\phi(q)$ is a real-valued function), using the prepared phase state

$|\phi\rangle=\int dx\,e^{i\phi(x)}|x\rangle\ .$ (126)

If we perform the gate SUM^{-1} with position eigenstate $|q\rangle$ as control and $|\phi\rangle$ as target, and then measure the position of the target obtaining the outcome $|a\rangle$, the state of the control oscillator has become $e^{i\phi(q+a)}|q\rangle$. We can therefore complete the construction of $V_{\phi}$ by applying the transformation

$U(a)=e^{i[\phi(q)-\phi(q+a)]}\ .$ (127)

If the function $\phi(q)$ is cubic, then the argument of the exponential is quadratic and hence $U(a)$ is a symplectic transformation.

Now the problem of implementing universal quantum computation in the code subspace has been reduced to the problem of preparing the cubic phase state $|\gamma\rangle$. We can accomplish this task by preparing an EPR pair, and then performing a suitable photon counting measurement (a nonideal homodyne measurement) on one member of the pair.

Of course, the EPR pair will not be perfect. To be definite, let us suppose (although this assumption is not really necessary) that it is a Gaussian state

$|\psi_{\sigma_{p},\sigma_{q}}\rangle$ $=$ $\left(\frac{\sigma_{p}}{\pi\sigma_{q}}\right)^{1/2}\int dq_{1}dq_{2}\ \exp\left[-\frac{1}{2}\sigma_{p}^{2}\left(\frac{q_{1}+q_{2}}{2}\right)^{2}\right]$ (128)
$\times\exp\left[-\frac{1}{2}\left(q_{1}-q_{2}\right)^{2}/\sigma_{q}^{2}\right]|q_{1},q_{2}\rangle$

with $\sigma_{p},\sigma_{q}\ll 1$.

Now suppose that the second oscillator is mixed with a coherent light beam, resulting in a large shift in momentum,

$|\psi\rangle\rightarrow e^{iwq}|\psi\rangle\ ,\quad w\gg\sigma_{q}^{-1},\sigma_{p}^{-1}\ ;$ (129)

then the photon number is measured and $n$ photons are detected. Thus the state of the first oscillator becomes (up to normalization)

$|\psi_{1}^{(n)}\rangle$ $\approx$ $\left(\frac{\sigma_{p}}{\pi\sigma_{q}}\right)^{1/2}\int dq_{1}\,|q_{1}\rangle\,e^{-\frac{1}{2}\sigma_{p}^{2}q_{1}^{2}}$ (130)
$\times\int dq_{2}\,\varphi_{n}^{*}(q_{2})e^{iwq_{2}}e^{-\frac{1}{2}(q_{1}-q_{2})^{2}/\sigma_{q}^{2}}\ ,$

where $|\varphi_{n}\rangle$ denotes the photon number eigenstate, the eigenstate with eigenvalue $n+\frac{1}{2}$ of the Hamiltonian $H=\frac{1}{2}(p^{2}+q^{2})$.

We can evaluate the $q_{2}$ integral in eq. (130) by appealing to the semiclassical approximation. For $q_{2}$ in the classically allowed region and far from the classical turning points, we may write

$\varphi_{n}^{*}(q_{2})$ $\sim$ $\frac{1}{\sqrt{2\pi p(q_{2})}}\exp\left(-i\int^{q_{2}}dx\,p(x)\right)$ (131)
$+\frac{1}{\sqrt{2\pi p(q_{2})}}\exp\left(+i\int^{q_{2}}dx\,p(x)\right)\ ,$

where

---

where

$p(x)=\sqrt{2n+1-x^{2}}\ .$ (132)

For $w\gg\sigma_{q}^{-1}$, the rapid phase oscillations strongly suppress the contribution to the integral arising from the left-moving part of $\varphi^{(n)}(q_{2})$. A contribution from the right-moving part survives provided that

$|p(q_{1})-w|<\sigma_{q}^{-1}\ .$ (133)

When this condition is satisfied, it is a reasonable approximation to replace the Gaussian factor $e^{-\frac{1}{2}(q_{1}-q_{2})^{2}/\sigma_{q}^{2}}$ in the $q_{2}$ integral by $\sqrt{2\pi\sigma_{q}^{2}}\ \delta(q_{1}-q_{2})$, so that we obtain

$|\psi_{1}^{(n)}\rangle$ $\approx(2\sigma_{p}\sigma_{q})^{1/2}\int dq_{1}\,|q_{1}\rangle\,e^{-\frac{1}{2}\sigma_{p}^{2}q_{1}^{2}}$
$\times$ $\frac{1}{\sqrt{2\pi p(q_{1})}}\exp\left(-i\int^{q_{1}}dx\ (p(x)-w)\right)\ .$ (134)

The probability that $n$ photons are detected is given by the norm of this $|\psi_{1}^{(n)}\rangle$. The values of $n$ that occur with appreciable probability satisfy eq. (133) for some $q_{1}$ with $|q_{1}|<\sigma_{p}^{-1}$; thus typical measurement outcomes are in the range

$n+\frac{1}{2}\sim\frac{1}{2}\left(w\pm\sigma_{q}^{-1}\right)^{2}+\frac{1}{2}\sigma_{p}^{-2}\ ,$ (135)

with a flat probability distribution

${\rm Prob}(n)=\langle\psi_{1}^{(n)}|\psi_{1}^{(n)}\rangle\sim\frac{\sigma_{q}}{w}\ .$ (136)

Heuristically, after the momentum shift is applied, the oscillator that is measured has momentum of order $w\pm\sigma_{q}^{-1}$, and position of order $\sigma_{p}^{-1}$, so that the value of the energy is $n+\frac{1}{2}=\frac{1}{2}(p^{2}+q^{2})\sim\frac{1}{2}\left(w\pm\sigma_{q}^{-1}\right)^{2}+\frac{1}{2}\sigma_{p}^{-2}$.

For a particular typical outcome of the photon-counting measurement, since $|\psi_{1}^{(n)}\rangle$ has its support on $|q_{1}|<\sigma_{p}^{-1}\ll w$, we can Taylor expand $p(x)$ about $x=q_{1}$ to express $|\psi_{1}^{(n)}\rangle$ as

$\psi_{1}^{(n)}(q_{1})\propto\exp\left(-i\int^{q_{1}}\bigl{(}\sqrt{(2n+1)-x^{2}}-w\bigr{)}\,dx\right)$
$\propto\exp\Biggl{(}\frac{i}{6\sqrt{2n+1}}q_{1}^{3}-i\bigl{(}\sqrt{2n+1}-w\bigr{)}q_{1}$
$+O(q_{1}^{5}/w^{3})\Biggr{)}\ .$ (137)

This is a cubic phase state to good precision if $w$ is large enough.

The coefficient $\gamma^{\prime}$ of $q_{1}^{3}$ in the phase of $\psi_{1}$ is of order $n^{-1/2}$, while the phase $\gamma$ of the operator $V_{\gamma}$ that we wish to execute is of order one. However, we can construct $V_{\gamma}$ from $V_{\gamma^{\prime}}$ as

$V_{\gamma}=\left(S_{\gamma/\gamma^{\prime}}\right)^{-1}V_{\gamma^{\prime}}\left(S_{\gamma/\gamma^{\prime}}\right)\ ,$ (138)

where $S_{r}$ is a squeeze operation that acts according to

$S_{r}:q\rightarrow(r)^{1/3}q\ ,$
$p\rightarrow(r)^{-1/3}p\ .$ (139)

Alternatively, we could squeeze the phase state $|\gamma^{\prime}\rangle$ before we use it to implement the cubic phase gate.

Is this procedure fault tolerant? Before considering the errors introduced during the implementation of the cubic phase gate, we should check that the gate does not catastrophically amplify any preexisting errors. In general, a phase gate can transform a small position shift error into a potentially dangerous momentum shift error. Commuting $V(\phi)=e^{i\phi(q)}$ through the shift operator $e^{-iup}$, we find

$e^{i\phi(q)}e^{-iup}=e^{-iup}e^{if_{u}(q)}e^{i\phi(q)}\ ,$ (140)

where $f_{u}(q)=\phi(q+u)-\phi(q)$; the operator $e^{if_{u}(q)}$ can be expanded in terms of momentum shift operators of the form $e^{ivq}$ by evaluating the Fourier transform

$\tilde{f}_{u}(v)=\int\frac{dq}{2\pi}e^{i(f_{u}(q)-vq)}\ .$ (141)

Assuming we use a code where the parameter $\alpha$ is of order one, uncorrectable errors will be likely if $\tilde{f}_{u}(v)$ has significant support on values of $v$ that are order one.

Suppose that $V(\phi)$ acts on an approximate codeword whose wave function is concentrated on values of $q$ in the domain $|q|<L$. Phase cancellations will strongly suppress $\tilde{f}_{u}(v)$, unless the stationary phase condition $f_{u}^{\prime}(q)=v$ is satisfied for some value of $q$ in the domain of the approximate codeword. Therefore, $V(\phi)$ can propagate a preexisting position shift $u$ to a momentum shift error of magnitude

$|v|\sim\max_{|q|\leq L}|f_{u}^{\prime}(q)|\ .$ (142)

The cubic phase gate needed to implement the encoded $S$ gate is $W=e^{i\phi(q)}$ where $\phi(q)=\pi q^{3}/2\alpha^{3}$, so that $f_{u}(q)=3\pi uq^{2}/2\alpha^{3}+\cdots$ (ignoring small terms linear and constant in $q$), and $f_{u}^{\prime}(q)=3\pi uq/\alpha^{3}$; the gate transforms the position shift $u$ to a momentum shift

$v\sim 3\pi Lu/\alpha^{3}\ .$ (143)

For $\alpha$ of order one, then, to ensure that $v$ is small we should use approximate codewords with the property that the typical embedded position shift $u$ satisfies

$|u|\ll L^{-1}\ .$ (144)

In particular, if the approximate codeword’s embedded errors are Gaussian, where $\kappa$ is the typical size of a momentum shift and $\Delta$ is the typical size of a position shift, we require

---

$\Delta\ll\kappa\ .$ (145)

We assume that shift errors due to other causes are no larger than the embedded error.

In the circuit Fig. 6 that implements the cubic phase gate, position shift errors in either the encoded state $|\psi\rangle$ or the ancilla state $|\gamma\rangle$ might cause trouble. A shift by $u$ in $|\psi\rangle$ is transformed to a phase error $e^{if_{u}(q)}$, and a shift by $u$ in $|\gamma\rangle$ infects $|\psi\rangle$ with a phase error $e^{if_{u}(q+a)}$. Therefore, we should require that position shift errors in both $|\psi\rangle$ and $|\gamma\rangle$ satisfy the criterion eq. (144), where $L$ is the larger of the two wave packet widths.

When a cubic phase state is prepared by measuring half of an EPR pair, the packet width is of order $\sigma_{p}^{-1}$ and typical position shift errors have $u\sim\sigma_{q}$. However, we must also take into account that either the encoded state or the ancilla must be squeezed as in eq. (139). Suppose that the ancilla is squeezed, by a factor of order $n^{1/6}\sim w^{1/3}$; the wave packet is rescaled so that, after squeezing, the width $L^{\prime}$ and the typical shifts $u^{\prime}$ are given by

$L^{\prime}\sim\sigma_{p}^{-1}w^{-1/3}\ ,\qquad u^{\prime}\sim\sigma_{q}w^{-1/3}\ .$ (146)

Then the condition $|u^{\prime}|\ll L^{\prime-1}$ is satisfied provided that $\sigma_{q}\ll\sigma_{p}w^{2/3}$. We also require that the rescaled packet has width large compared to 1, or $\sigma_{p}\ll w^{-1/3}$.

For the derivation of eq. (137), we used the approximations $w\sigma_{q}\gg 1$ and $w\sigma_{p}\gg 1$. We also need to check that the remainder terms in the Taylor expansion give rise to a phase error that is acceptably small. This error has the form $e^{if(q_{1})}$, where $f(q_{1})=O(q_{1}^{5}/w^{3})$, corresponding to a momentum shift

$v\sim f^{\prime}(q_{1})\sim\sigma_{p}^{-4}w^{-3}\ .$ (147)

Squeezing amplifies this momentum shift error to $v^{\prime}\sim vw^{1/3}\sim\sigma_{p}^{-4}w^{-8/3}$, which will be small compared to 1 provided that $\sigma_{p}\gg w^{-2/3}$. To summarize, our implementation of the cubic phase gate works well if the approximate codewords have embedded errors satisfying $\Delta\ll\kappa$, and if widths $\sigma_{q}$ and $\sigma_{p}$ of the approximate EPR state satisfy $w\gg\sigma_{q}^{-1}$ and

$w^{-1/3}\gg\sigma_{p}\gg w^{-2/3}\ .$ (148)

Finally, how accurately must we count the photons? An error $\Delta n$ in the photon number results in a phase error $e^{ivq_{1}}$ with $|v|\sim n^{-1/2}\Delta n$ in $\psi_{1}^{(n)}(q_{1})$, which will be amplified by squeezing to $|v^{\prime}|\sim|v|w^{1/3}\sim n^{-1/3}\Delta n$. Therefore, the precision of the photon number measurement should satisfy

$\Delta n\ll n^{1/3}$ (149)

to ensure that this error is acceptably small.

### IV.3 Purification

Either of the above two methods could be used to implement a nonsymplectic phase transformation that completes the universal gate set. Of course, experimental limitations might make it challenging to execute the gate with very high fidelity. One wonders whether it is possible to refine the method to implement fault-tolerant universal gates of improved fidelity.

In fact, such refinements are possible. We have seen that we can reach beyond the symplectic transformations and achieve universal quantum computation if we have a supply of appropriate “nonsymplectic states” that can’t be created with the symplectic gates. If the nonsymplectic states have the right properties, then we can carry out a purification protocol to distill from our initial supply of noisy nonsymplectic states a smaller number of nonsymplectic states with much better fidelity *[35, 36]*.

An example of a nonsymplectic state that admits such a purification protocol is a variant of the state originally introduced by Shor *[27]*, the three-qubit state

$2^{-3/2}\sum_{a,b,c\in\{0,1\}}(-1)^{abc}|a\rangle_{1}|b\rangle_{2}|c\rangle_{3}\ ;$ (150)

it can be characterized as the simultaneous eigenstate of three commuting symplectic operators: $\Lambda(Z)_{1,2}X_{3}$ and its two cyclic permutations, where $\Lambda(Z)$ is the two-qubit conditional phase gate

$\Lambda(Z):|a,b\rangle\rightarrow(-1)^{ab}|a,b\rangle$ (151)

As Shor explained, this nonsymplectic state can be employed to implement the Toffoli gate

$T:|a,b,c\rangle\rightarrow|a,b,c\oplus ab\rangle\ ,$ (152)

and so provides an alternative way to complete the universal gate set.

To purify our supply of nonsymplectic states, symplectic gates are applied to a pair of nonsymplectic states and then one of the states is measured. Based on the outcome of the measurement, the other state is either kept or discarded. If the initial ensemble of states approximates the nonsymplectic states with adequate fidelity, then as purification proceeds, the fidelity of the remaining ensemble converges rapidly toward one.

The details of the purification protocol will be described elsewhere; here we will only remark that these Shor states can be readily created using symplectic gates and $\pi/8$ phase gates. The Shor state is obtained if we apply the transformation

$\Lambda^{2}(Z):|a,b,c\rangle\rightarrow(-1)^{abc}|a,b,c\rangle$ (153)

to the state

$H_{1}H_{2}H_{3}|0,0,0\rangle=2^{-3/2}\sum_{a,b,c\in\{0,1\}}|a,b,c\rangle\ .$ (154)

---

As shown in Fig. 7, $\Lambda^{2}(Z)$ can be applied by executing a circuit containing 5 $S$ gates, 4 $S^{-1}$ gates, and 8 CNOT gates.

![img-4.jpeg](images/img-4.jpeg)
Figure 7: Construction of the three-qubit gate $\Lambda^{2}(Z)$. ($a$) A $\Lambda(P)$ gate can be constructed (up to an overall phase) from two $S$ gates, an $S^{-1}$ gate, and two CNOT’s. The circuit is executed from left to right. ($b$) A $\Lambda^{2}(Z)$ gates can be constructed from two $\Lambda(P)$ gates, a $\Lambda(P^{-1})$ gate, and two CNOT’s.

Therefore, if we can apply symplectic gates accurately, and are also able to create a supply of $\pi/8$ states of reasonable fidelity (or can otherwise implement $S$ gates of reasonable fidelity), then we can use the purification protocol to implement Toffoli gates with very good fidelity.

## XII Encoding

Now we have discussed how to execute universal quantum computation fault tolerantly, and how to perform error recovery. But the discussion has all been premised on the assumption that we can prepare encoded states. It is finally time to consider how this can be done. In fact, preparing simultaneous eigenstates of the stabilizer generators $\exp(2\pi iq/\alpha)$ and $\exp(-inp\alpha)$ is a challenging task.

For the $[[N,k]]$ stabilizer codes that have been discussed previously, encoding is not intrinsically difficult in that it can be accomplished with Clifford group gates. Acting by conjugation, Clifford group transformations take tensor products of Pauli matrices to tensor products of Pauli operators. In particular, there is a Clifford group transformation that takes the state $|0\rangle^{\otimes N}$ (the simultaneous eigenstate with eigenvalue one of all $N$ single-qubit $Z$’s) to the encoded $|\bar{0}\rangle^{\otimes k}$ (the simultaneous eigenstate with eigenvalue one of $(N-k)$ stabilizer generators and $k$ encoded $\bar{Z}$’s).

Where our codes are different, in both their finite-dimensional and infinite-dimensional incarnations, is that a single qudit or oscillator is required to obey two independent stabilizer conditions – i.e., to be the simultaneous eigenstate of two independent Pauli operators. Hence there is no Clifford group encoder. In the continuous variable case, the problem can be stated in more familiar language: the symplectic transformations take Gaussian (coherent or squeezed) states to Gaussian states. Hence no symplectic transformation can take (say) the oscillator’s ground state to a state in the code subspace.

So encoding requires nonsymplectic operations, and as far as we know it cannot be accomplished by counting photons either – we must resort to a nonlinear coupling between oscillators, such as a $\chi^{(3)}$ coupling. We will describe one possible encoding scheme: First, we prepare a squeezed state, an eigenstate of the momentum with $p=0$. This state is already an eigenstate with eigenvalue one of the stabilizer generator $e^{inp\alpha}$, but not an eigenstate of $e^{2\pi iq/\alpha}$; rather its value of $q$ is completely indefinite. To obtain an encoded state, we must project out the component with a definite value of $q$ modulo $\alpha$.

This can be achieved by coupling the oscillator to another oscillator that serves as a meter, via the perturbation of the Hamiltonian

$H^{\prime}=\lambda\ q\ \left(b^{\dagger}b\right)\ ,$ (155)

where $b$ is the annihilation operator of the meter. This perturbation modifies the frequency of the meter,

$\Delta\omega_{\rm meter}=\lambda\ q\ ;$ (156)

then if this coupling is turned on for a time $t=2\pi/\lambda n\alpha$, the phase of the meter advances by

$\Delta\theta_{\rm meter}=2\pi q/n\alpha\ .$ (157)

By reading out the phase, we can determine the value of $q$ modulo $n\alpha$, and apply a shift if necessary to obtain the state with $q\equiv 0\ ({\rm mod}\ n\alpha)$, the known state $|\bar{0}\rangle$ in the code subspace. (See Fig. 8.)

![img-5.jpeg](images/img-5.jpeg)
Figure 8: Preparation of an encoded state. ($a$) An eigenstate of $p$ is prepared, which has an indefinite value of $q$. ($b$) The value of $q$ modulo $n\alpha$ is measured, projecting out a state that differs from the encoded $\bar{Z}$ eigenstate by a shift in $q$.

##

---

Of course, in practice the state squeezed in $p$ prepared in the first step will be only finitely squeezed, and the measurement of $q$ modulo $n\alpha$ will have imperfect resolution. If the squeezed state is Gaussian and the measurement has a Gaussian acceptance, then this procedure will produce an approximate codeword of the sort described in §V.

If we are able to prepare “good enough” encoded states, we can distill better ones. The distillation protocol is similar to the error recovery procedure, but where the ancilla used for syndrome measurement may be fairly noisy. We might improve the convergence of the distillation procedure by discarding the data oscillator if the measurement of the ancilla oscillator yields a value of $q$ or $p$ that is too distant from the values allowed by the code stabilizer.

So far, we have described how to prepare encoded states for the “single-oscillator” codes described in §IV. To prepare an encoded state for one of the $N$-oscillator codes described in §VI, we proceed in two steps. First we prepare each of $N$ oscillators in a single-oscillator encoded state. Then we apply a symplectic transformation to obtain the encoded state of the $N$-oscillator code.

A particular known encoded state of a lattice stabilizer code can itself be regarded as a code with an ($n=1$)-dimensional code space. Hence it can be characterized by a self-dual symplectic lattice. For example, the $\bar{X}=1$ state of a qunit encoded in a single oscillator is the simultaneous eigenstate with eigenvalue one of the operators $e^{-ip\alpha}$ and $e^{2\pi iq/\alpha}$ – the state associated with the self-dual lattice whose basis vectors are $p\alpha/\sqrt{2\pi}$ and $q\sqrt{2\pi}/\alpha$.

One encoded state can be transformed to another by symplectic gates if there is a symplectic linear transformation that takes the self-dual lattice associated with the first state to the self-dual lattice associated with the second. In fact, such a symplectic transformation exists for any pair of self-dual lattices.

A linear transformation acting on the $p$’s and $q$’s modifies the generator matrix $M$ of a lattice according to

$M\rightarrow MS\ ;$ (158)

this transformation is symplectic if

$S\omega S^{T}=\omega\ ,$ (159)

where

\[ \omega=\left(\begin{array}[]{cc}0&I\\
-I&0\end{array}\right)\ . \] (160)

We saw in §VI that we can always choose the generator matrix $M$ of a self-dual lattice so that the matrix $A$ has the form

$A\equiv M\omega M^{T}=\omega\ ;$ (161)

that is, so that $M$ is a symplectic matrix. Therefore, the generator matrices $M_{1}$ and $M_{2}$ of two self-dual lattices can each be chosen to be symplectic; then the linear transformation

$S=M_{1}^{-1}M_{2}$ (162)

that takes one lattice to the other is also symplectic.

Thus, while the task of preparing the encoded states of the single-oscillator codes can be accomplished only by introducing a nonlinear coupling between oscillators, proceeding from single-oscillator encoded states to many-oscillator encoded states can be achieved with linear optical operations and squeezing.

## XIII Physical fault tolerance?

In a physical setting, making use of the continuous variable quantum error-correcting codes proposed here (or “digital” quantum codes that have been proposed previously) is a daunting challenge. We must continually measure the stabilizer operators (the “error syndrome”) to diagnose the errors; to recover we must apply frequent shifts of the canonical variables that are conditioned on the measurement outcomes. Cold ancilla oscillators must be provided that are steadily consumed by the syndrome measurements. The ancillas must be discarded (or refreshed) to rid the system of excess entropy that has been introduced by the accumulated errors.

An alternative to this complex scheme was suggested in Ref. *[38]*. Perhaps we can engineer a quantum system whose (degenerate) ground state is the code subspace. Then the natural coupling of the system to its environment will allow the system to relax to the code space, removing errors introduced by quantum and thermal noise, or through the imperfect execution of quantum gates. Such a system, if it could be built, would be a highly stable quantum memory.

Continuous variable coding suggests new approaches to implementing this type of physical fault tolerance. For example, the Hamiltonian

$H=2-[\cos p+\cos(2\pi nq)]$ (163)

has an $n$-fold degenerate (but nonnormalizable) ground state that is just the code space of a continuous variable code. (The operators $\cos p$ and $\cos 2\pi nq$ commute and can be simultaneously diagonalized.) The low-lying states of a real system whose Hamiltonian is a reasonable approximation to $H$ would resemble the approximate codewords described in §V.

One possible way to realize physical fault tolerance is suggested by the codes for an electron in a Landau level, described in §III. The wave functions in the code space are doubly periodic with a unit cell that encloses $n$ flux quanta, where $n$ is the code’s dimension. If we turn on a tunable periodic potential whose unit cell matches that of the code, then the Landau level is split into $n$ energy bands, and the codewords are the states with vanishing Bloch momentum. Therefore, an encoded state could be prepared by turning on the potential, waiting for dissipative effects to cause the electrons to relax to the bottom

---

of the lowest band, and then adiabatically turning off the potential. If dissipative effects cause electrons to relax to the bottom of a band on a time scale that is short compared to spontaneous decay from one band to another, then more general encoded states could be prepared by a similar method. Furthermore, turning on the potential from time to time would remove the accumulated Bloch momentum introduced by errors, allowing the electron to relax back to the code space.

## XIV Concluding comments

We have described codes that protect quantum states encoded in a finite-dimensional subspace of the Hilbert space of a system described by continuous quantum variables. With these codes, continuous variable systems can be used for robust storage and fault-tolerant processing of quantum information.

For example, the coded information could reside in the Hilbert space of a single-particle system described by canonical quantum variables $q$ and $p$. In practice, these variables might describe the states of a mode of the electromagnetic field in a high-finesse microcavity, or the state of the center of mass motion of an ion in a trap. Or the continuous Hilbert space could be the state space of a rotor described by an angular variable $\theta$ and its conjugate angular momentum $L$; in practice, these variables might be the phase and charge of a superconducting quantum dot. Our coding scheme can also be applied to a charged particle in a magnetic field.

Our codes are designed to protect against small errors that occur continually – diffusive drifts in the values of the canonical variables. The codes are less effective in protecting against large errors that occur rarely. In some settings, we may desire protection against both kinds of errors. One way to achieve that would be to concatenate our continuous-variable codes with conventional finite-dimensional quantum codes.

When we consider how to manipulate continuous-variable quantum information fault tolerantly, the issues that arise are rather different than in previous discussions of quantum fault tolerance. With continuous variable codes, propagation of error from one oscillator to another is not necessarily a serious problem. More damaging are processes that amplify a small shift of the canonical variables to a large shift. We have described how to implement a universal set of fault-tolerant quantum gates; with these, harmful error amplification can be avoided as the encoded state is processed.

Apart from encouraging the intriguing possibility that continuous quantum variables might prove useful for the construction of robust quantum memories and computers, these new quantum codes also have important theoretical applications. In this paper we have discussed an application to the theory of the quantum capacity of the Gaussian quantum channel. Furthermore, quantum codes can be invoked to investigate the efficacy of quantum cryptographic protocols, even in cases where the protocol makes no direct use of the encoded states *[39]*. With continuous variable codes, we can demonstrate the security of key distribution protocols based on the transmission of continuous variable quantum information. This application is discussed in a separate paper *[40]*.

We gratefully acknowledge helpful discussions with Isaac Chuang, Sumit Daftuar, David DiVincenzo, Andrew Doherty, Steven van Enk, Jim Harrington, Jeff Kimble, Andrew Landahl, Hideo Mabuchi, Harsh Mathur, Gerard Milburn, Michael Nielsen, and Peter Shor. This work has been supported in part by the Department of Energy under Grant No. DE-FG03-92-ER40701, and by the Caltech MURI Center for Quantum Networks under ARO Grant No. DAAD19-00-1-0374. Some of this work was done at the Aspen Center for Physics.

## References

- [1] P. W. Shor, “Scheme for reducing decoherence in quantum computer memory,” Phys. Rev. A 52, R2493 (1995).
- [2] A. Steane, “Error-correcting codes in quantum theory,” Phys. Rev. Lett. 77, 793 (1996).
- [3] E. Knill, R. Laflamme, and G. Milburn, “A scheme for efficient quantum computation with linear optics,” Nature 409, 46-52 (2001); “Efficient linear optics quantum computation,” quant-ph/0006088.
- [4] E. Knill, R. Laflamme, and G. Milburn, “Thresholds for linear optics quantum computation,” quant-ph/0006120.
- [5] E. Knill, “Non-binary unitary error bases and quantum codes,” quant-ph/9608048; E. Knill, “Group representations, error bases and quantum codes,” quant-ph/9608049.
- [6] H. F. Chau, “Correcting quantum errors in higher spin systems,” Phys. Rev. A 55, R839 (1997), quant-ph/9610023; H. F. Chau, “Five quantum register error correction for higher spin systems,” Phys. Rev. A 56, R1 (1997), quant-ph/9702033.
- [7] E. M. Rains, “Nonbinary quantum codes,” quant-ph/9703048.
- [8] D. Gottesman, “Fault-tolerant quantum computation with higher-dimensional systems,” Lect. Notes. Comp. Sci. 1509, 302 (1999), quant-ph/9802007.
- [9] A. R. Calderbank, E. M. Rains, P. W. Shor, and N. J. A. Sloane, “Quantum error correction and orthogonal geometry,” Phys. Rev. Lett. 78, 405 (1997), quant-ph/9605005.
- [10] D. Gottesman, “A class of quantum error-correcting

---

codes saturating the quantum Hamming bound,” Phys. Rev. A 54, 1862 (1996), quant-ph/9604038.
- [11] S. Braunstein, “Error correction for continuous quantum variables,” Phys. Rev. Lett. 80, 4084 (1998), quant-ph/9711049.
- [12] S. Lloyd and J. E. Slotine, “Analog quantum error correction,” Phys. Rev. Lett. 80, 4088 (1998), quant-ph/9711021.
- [13] S. Parker, S. Bose, and M. B. Plenio, “Entanglement quantification and purification in continuous variable systems,” Phys. Rev. A 61, 32305 (2000), quant-ph/9906098.
- [14] L. M. Duan, G. Giedke, J. I. Cirac, and P. Zoller, “Entanglement purification of Gaussian continuous variable quantum states,” Phys Rev. Lett. 84, 4002-4005 (2000), quant-ph/9912017; L. M. Duan, G. Giedke, J. I. Cirac, and P. Zoller, “Physical implementation for entanglement purification of Gaussian continuous variable quantum systems,” Phys. Rev. A 62, 032304 (2000), quant-ph/0003116.
- [15] A. R. Calderbank and P. W. Shor, “Good quantum error-correcting codes exist,” Phys. Rev. A 54, 1098 (1996), quant-ph/9512032.
- [16] A. Steane, “Multiple particle interference and quantum error correction,” Proc. Roy. Soc. London, Ser. A 452, 2551 (1996), quant-ph/9601029.
- [17] D. Aharonov and M. Ben-Or, “Fault-tolerant quantum computation with constant error,” Proc. 29th Ann. ACM Symp. on Theory of Computing, p. 176 (ACM, New York, 1998), quant-ph/9611025; D. Aharonov and M. Ben-Or, “Fault-tolerant quantum computation with constant error rate,” quant-ph/9906129.
- [18] T. M. Cover and J. A. Thomas, Elements of Information Theory, Wiley, New York (1991).
- [19] A. S. Holevo and R. F. Werner, “Evaluating capacities of bosonic Gaussian channels,” quant-ph/9912067.
- [20] S. Lloyd, “The capacity of the noisy quantum channel,” Phys. Rev. A 56, 1613 (1997), quant-ph/9604015.
- [21] B. W. Schumacher and M. A. Nielsen, “Quantum data processing and error correction,” Phys. Rev. A 54, 2629 (1996), quant-ph/9604022.
- [22] H. Barnum, M. A. Nielsen, and B. Schumacher, “Information transmission through a noisy quantum channel,” Phys. Rev. A 57, 4153 (1998), quant-ph/9702049.
- [23] C. H. Bennett, D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters, “Mixed state entanglement and quantum error correction,” Phys. Rev. A 54, 3824 (1996), quant-ph/9604024.
- [24] P. W. Shor and J. A. Smolin, “Quantum error-correcting codes need not completely reveal the error syndrome,” quant-ph/9604006; D. P. DiVincenzo, P. W. Shor and J. A. Smolin, “Quantum channel capacity of very noisy channels,” Phys. Rev A 57, 830 (1998), quant-ph/9706061.
- [25] We thank the anonymous referee for this comment.
- [26] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, “Experimental realization of any discrete unitary operator,” Phys. Rev. Lett. 73, 58 (1994).
- [27] P. W. Shor, “Fault-tolerant quantum computation,” Proc. 37th Annual Symp. on Found. of Comp. Sci., p. 56 (IEEE, Los Alamitos, CA, 1996), quant-ph/9605011.
- [28] D. Gottesman, “A theory of fault-tolerant quantum computation,” Phys. Rev. A 57, 127 (1998), quant-ph/9702029.
- [29] A. Steane, “Active stabilization, quantum computation, and quantum state synthesis,” Phys. Rev. Lett. 78, 2252 (1997), quant-ph/9611027.
- [30] E Knill, R. Laflamme, W. H. Zurek, “Resilient quantum computation: error models and thresholds,” Proc. Roy. Soc. London, Ser. A 454, 365 (1998), quant-ph/9702058.
- [31] D. Gottesman and I. Chuang, “Quantum teleportation is a universal computational primitive,” Nature 402, 390 (1999), quant-ph/9908010.
- [32] S. Schneider, H. M. Wiseman, W. J. Munro, and G. J. Milburn, “Measurement and state preparation via ion trap quantum computing,” Fort. der Physik 46, 391 (1998), quant-ph/9709042.
- [33] P. O. Boykin, T. Mor, M. Pulver, V. Roychowdhury, and F. Vatan, “A new universal and fault-tolerant quantum basis,” Inform. Process Lett. 75, 101-107 (2000), quant-ph/9906054.
- [34] X. Zhou, D. W. Leung, and I. L. Chuang, “Methodology for quantum logic gate construction,” Phys. Rev. A 62, 052316 (2000), quant-ph/0002039.
- [35] A. Yu. Kitaev, unpublished.
- [36] E. Dennis, Fault-tolerant computation without concatenation, quant-ph/9905027.
- [37] V. Giovannetti, S. Mancini, and P. Tombesi, “Radiation pressure induced Einstein-Podolsky-Rosen paradox,” quant-ph/0005066, and references therein.
- [38] A. Yu. Kitaev, “Fault-tolerant quantum computation by anyons,” quant-ph/9707021.
- [39] P. W. Shor and J. Preskill, “Simple proof of security of the BB84 quantum key distribution protocol,” Phys. Rev. Lett. 85, 441-444 (2000), quant-ph/0003004.
- [40] D. Gottesman and J. Preskill, “Secure quantum key distribution using squeezed states,” Phys. Rev. A 63, 022309 (2001), quant-ph/0008046.