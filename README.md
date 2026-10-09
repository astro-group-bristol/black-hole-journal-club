Please see below for the upcoming schedule and minutes from this year for our Journal Club.
If you would like to join this Journal Club (presenting is not compulsory) please email: darius.michienzi@bristol.ac.uk and use the subject: "BH Journal Club".

We meet every Tuesday at:

- **11:00 until 12:00 (UTC + 1)**

Check the group email for the room and the Zoom link.

## Agenda

- Brief discussion of papers from the week (~15 mins)
- Presentation of chosen paper (~30 mins)
- Discussion and questions for the main presenter (~10 mins)

## Rota

To generate additional entries for the rota, use `scripts/rota.py`.

| Date       | Presenter   | Room |
|------------|-------------|------|       
| 2026-10-13 | Biz         | 4.41 |
| 2026-10-20 | Thomas B    | 3.30 |
| 2026-10-27 | Jiachen     | 3.30 |
| 2026-11-03 | Tom H       | *online* |
| 2026-11-10 | Teresa      | 3.30 |
| 2026-11-17 | Yimin       | 3.30 |

## Interesting Conferences

Please open an issue with any conferences you think might be of interest for the group and should be added to the list below. 

| Title | Dates | Location | Abstract Deadline |
|-------|-------|----------|-------------------|
| [Many Faces of stellar-mass Black Holes](https://sites.google.com/view/bh-nepal-2026/home) | 12-16 October 2026 | Kathmandu, Nepal | 05 June |
| [The many tones of accretion - to the memory of Tommaso Belloni](https://indico.ict.inaf.it/event/3459) | 7-11 September 2026 | Cefalù, Sicily (Italy) | End of May |
| [NewAthena SWG2 Meeting](https://swg2meeting.com/#registration) | 25-29 January 2027 | Noordwijk The Netherlands | 23 October |

$^*$ Registration Only

## Minutes

### 2026-10-06 Andy

Discussed papers: 

[Beyond Disk Truncation: X-ray Reverberation Signatures of an Outflowing Corona](https://arxiv.org/abs/2609.21732) (Quin et al,. 09-2026)
- The paper looks at the spectral and timing signatures of a mildly relativistic outflowing corona in BH XRBs, an alternative to disk truncation for explaining the hard spectra, weak reflection and higher than expected polarisation degree of the hard state.
- They use Monte Carlo radiative-transfer simulations of a truncated thin disk and an ellipsoidal corona with a prescribed bulk outflow velocity, calculating the Comptonised continuum, the disk reflection and the lag-frequency spectra for different outflow velocities and truncation radii.
- Increasing the outflow velocity reduces the reflection fraction through relativistic beaming, as fewer Comptonised photons irradiate the disk.
- For $\beta \lesssim 0.5$, the high-frequency soft lag is only weakly affected by the outflow velocity. Increasing the truncation radius instead shifts the zero-crossing frequency $\nu_0$ to much lower frequencies, so the timing properties can help distinguish the two scenarios.
- Applied to MAXI J1820+070, the unusual $R$–$\Gamma$ anti-correlation during the plateau phase is qualitatively consistent with a contracting corona with increasing bulk velocity. Disk recession alone would predict the opposite evolution of $\nu_0$. Future polarisation calculations will provide an additional test.

[XClass: An Automated Multiwavelength Machine-Learning Pipeline for Classification of Extragalactic X-ray Sources. I. Pipeline Description](https://arxiv.org/abs/2610.00459) (Rangelov et al,. 09-2026)
- The paper looks at XClass, a machine-learning pipeline for classifying the many extragalactic X-ray point sources detected by Chandra in nearby galaxies that currently lack a classification. Sources are sorted into seven classes: AGN, LMXBs, HMXBs, CVs, low- and high-mass foreground stars, and SNRs.
- The main challenge is photometric heterogeneity. The training sources are mostly Galactic with PanSTARRS and 2MASS photometry, while the extragalactic targets need HST imaging in a different filter system.
- This is solved with an SED translation. Class-appropriate spectral models are fitted to each training source and convolved through the HST filter curves, giving synthetic magnitudes in a common feature space.
- The classifier is an asymmetric two-stage Random Forest. Stage 1 separates AGN, X-ray binaries, SNRs and stars, then Stage 2 splits the X-ray binaries into LMXBs and HMXBs, using the Stage 1 probabilities as extra features. The features are X-ray hardness ratios, SED-translated HST colours and X-ray-to-optical flux ratios.
- On the optical baseline sample (sources with at least one optical magnitude), it reaches 99.6% accuracy and a balanced accuracy of 0.90, and is well calibrated. The pipeline is modular and generalisable to any HST filter configuration, and will be applied to M31 and M33 in a companion paper.

Presented Paper: [Disk truncation triggers relativistic jet launching of a highly accreting supermassive black hole](https://arxiv.org/abs/2609.27057) (Noda et al., 09-2026)
- The paper looks at how powerful jets are launched in highly accreting AGN, where the cold, geometrically-thin disk should not be able to sustain the large-scale magnetic fields needed for the Blandford–Znajek mechanism. They use contemporaneous XRISM and VLBI (GMVA, VLBA and EAVN) observations of the broad-line radio galaxy 3C120, which has $L/L_{\rm Edd}$ of 0.1–0.2, to probe the inner accretion flow and the jet base together.
- The XRISM spectrum requires a relativistically broadened Fe K$\alpha$ line on top of the thermal Comptonisation continuum and the narrow lines from the BLR and the torus. This is the first high-resolution view of the line profile in 3C120, as earlier CCD spectra could not separate it from the narrow lines and disk-wind features.
- The line profile puts the inner edge of the cold disk at 20 $R_g$, with the region inside replaced by a hot, geometrically-thick flow, consistent with the hard continuum ($\Gamma = 1.8$). This is robust to the choice of reflection model and electron temperature. The spin is not constrained, as the inner radius lies well outside the ISCO.
- Combining the GMVA 86 GHz image with the VLBA and EAVN images resolves the jet collimation profile, which is parabolic ($R_{\rm jet} \propto z^{0.61}$) in the inner region. Extrapolating this to the horizon gives a jet radius of $\lesssim 7\,R_g$, comparable to or narrower than the hot flow. A small viewing angle (< 19°, from the superluminal motion) and the radio core-shift effect would both further support this.
- This points to the jet being launched from the hot, geometrically-thick flow rather than the cold thin disk, possibly via the Blandford–Znajek process. The jet magnetic flux is consistent with the maximum sustainable on the horizon, and the hot flow can advect such a flux. If this geometric transition is common in highly accreting systems, an inner hot flow would be necessary but not sufficient for powerful jets.

### 2026-09-29 Shashanth

Presented Paper: [Broad-band spectral-timing: simultaneous NICER and HXMT observations reveal an anticorrelation between the softest and hardest X-ray fluxes in MAXI J1820+070](https://arxiv.org/abs/2609.27608) (Bollemeijer, Uttley, & You, 09-2026)

- The paper looks at simultaneous NICER and Insight-HXMT spectral-timing of the BH XRB MAXI J1820+070 across the 0.3-250 keV band, to study how lags and coherence between energy bands depend on Fourier frequency and on the reference band chosen.
- At low frequencies (timescales > 50 s), the softest (< 1 keV) and hardest (> 80 keV) X-ray fluxes are anti-correlated, with phase lags of $|\pi|$ rad, accompanied by a drop in coherence that partially recovers at the highest energies.
- The anti-correlation only shows up using a soft reference band below ~1 keV. With harder reference bands, lags stay near zero up to 250 keV (though coherence still drops gradually above ~30-50 keV), and the energy at which the lag switches from 0 to $|\pi|$ rad scales roughly linearly with the reference-band energy.
- Two single-component explanations are found wanting: a coronal cut-off modulated by seed-photon flux should also anti-correlate the soft coronal power-law with the hard band, which isn't seen, and a pivoting power-law should produce anti-correlation over a broad range around the pivot point, not just between the extremes, making it unlikely.
- The explanation they find most plausible, though still speculative, is a hybrid plasma, where a non-thermal electron tail producing the >80 keV emission exchanges energy with the disc through an unknown mechanism while staying partly decoupled from the thermal corona. This would also explain the coherence drop and the reference-band dependence via a varying disc/soft-power-law mix below 1 keV.

### 2026-09-22 Darius

Presented Paper: [Spinning Between Models: Continuum and Reflection Constraints in the Intermediate States of GRS 1716-249 and GRS 1739-278](https://arxiv.org/abs/2609.13372) (Tausch et al. 09-2026)

- The paper looks at joint continuum and reflection spin fits for two black hole X-ray binaries, GRS 1716-249 and GRS 1739-278, using paired Swift/XRT and NuSTAR observations from their intermediate states, chosen because this state balances soft-band flux (continuum) against hard-band flux (reflection).
- Both sources are jointly fit with kerrbb and relxillCp, linking or separately varying the spin parameter between the two components, with the parameter space explored via MCMC.
- GRS 1716 strongly favours a high spin, while the GRS 1739 data allow high- and low-spin solutions with nearly identical fit statistics.
- Parameter-stepping shows this comes from multidimensional parameter covariance rather than a simple degeneracy. Coordinated changes across mass, distance, accretion rate, hardening factor, inclination, and the reflection parameters let very different configurations fit almost equally well, and in the low-spin branch the emissivity breaking radius approaches the inner disk radius and drives the inner emissivity index to an extreme value, which the authors read as a parameterisation artefact rather than real evidence for low spin.
- Energy-band tests show the Fe band gives the strongest direct handle on spin, the Compton hump mainly constrains the other reflection parameters, and the soft band anchors the continuum. Removing the Fe band costs the most spin sensitivity and can flip which solution the fit prefers.

### 2026-09-15 *Summer catch up*

Discussed papers:

[Unified modelling of broad and narrow optical-UV emission lines from massive black holes: interpreting high-redshift JWST observations](https://arxiv.org/abs/2609.12062) (Plat et al., 09-2026)
- JWST is uncovering a large population of AGN at high redshift, motivating the extension of photoionisation models beyond those calibrated on local sources. The paper presents a suite of broad and narrow line photoionisation models based on ionising spectra that vary with BH mass and Eddington ratio, spanning sub- to super-Eddington accretion.
- For the BLR, broad Hα may be detectable down to $M_{BH} \approx 10^{5.7}\,M_\odot$ at $z=6$ for a BH accreting at the Eddington limit. They also derive new bolometric corrections for type I and type II AGN, and provide diagnostics for distinguishing BH accretion from star formation.

[Emulation of non-linear 1D spectral models: relativistic X-ray reflection](https://arxiv.org/abs/2607.04785) (Ricketts et al., 07-2026)
- The paper looks at using machine learning to emulate the reltrans X-ray spectral model, which computes relativistically smeared reflection from the accretion disk. Rather than emulating the full model, they adopt a modular approach targeting only the convolved reflection spectrum (~1-10% of total flux).
- Using an operator-learning architecture with Fourier feature embeddings, they reproduce the reflection spectrum to O(0.1)% precision across 0.1-100 keV with a 4-10x speed-up.

[What Is the Black Hole Spin in Cyg X-1?](https://arxiv.org/abs/2402.12325) (Zdziarski et al., 04-2024)
- The paper looks at the BH spin of Cyg X-1 using simultaneous NICER and NuSTAR soft-state observations supplemented by INTEGRAL. Unlike most previous studies, the spin parameters of the disk continuum and relativistic broadening models are tied together, combining the continuum and reflection methods.
- Accounting for magnetic support of the disk (increasing the colour correction $f_{\rm col}$), they find $a_* \approx 0.87$, lower than earlier near-maximal estimates, highlighting the sensitivity of spin measurements to disk atmosphere assumptions.

[Model dependence of XRISM black-hole spin constraints in Cyg X-1](https://arxiv.org/abs/2605.24664) (Zdziarski et al., 06-2026)
- The paper looks at Cyg X-1 observed by XRISM Resolve with simultaneous NICER and NuSTAR in the hard state. Fitting with the simplest reflection model, relxill, recovers near-maximal spin ($a_* = 0.99$), but fitting with the Comptonisation-based relxillCp instead yields $a_* = 0.0^{+0.17}$.
- The spin of Cyg X-1 is therefore strongly model-dependent, with low spin values consistent with gravitational wave constraints from BH merger events.

[Black Hole Spin in X-ray Binaries: Giving Uncertainties an ](https://arxiv.org/abs/2010.11948) (Salvesen & Miller, 11-2020)
- The paper looks at why the two established spin measurement techniques — disk continuum fitting and iron line modelling — often yield conflicting results. The key issue is that continuum fitting effectively treats the colour correction factor $f_{\rm col}$ as a known quantity, despite it being poorly constrained; an uncertainty of $\pm 0.2$-$0.3$ in $f_{\rm col}$ dominates the spin error budget in most cases.
- Plausible departures from the standard $f_{\rm col}$ values can bring the discrepant spin measurements from the two methods into agreement, suggesting the tension is a systematic modelling issue rather than a fundamental conflict.