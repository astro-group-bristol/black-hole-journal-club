Please see below for the upcoming schedule and minutes from this year for our Journal Club.
If you would like to join this Journal Club (presenting is not compulsory) please email: darius.michienzi@bristol.ac.uk and use the subject: "BH Journal Club".

We meet every Tuesday at:

- **11:00 until 12:00 (UTC + 1)**

Check the group email for the room and the Teams invite.

## Agenda

- Brief discussion of papers from the week (~15 mins)
- Presentation of chosen paper (~30 mins)
- Discussion and questions for the main presenter (~10 mins)

## Rota

To generate additional entries for the rota, use `scripts/rota.py`.

| Date       | Presenter   | Room |
|------------|-------------|------|       
| 2026-09-15 |*Summer catch up*| 3.30 |
| 2026-09-22 | Darius      | 3.30 |
| 2026-09-29 | Shashanth   | 3.30 |
| 2026-10-06 | Andy        | 3.29 |
| 2026-10-13 | Biz         | 4.41 |
| 2026-10-20 | Thomas B    | 3.30 |
| 2026-10-27 | Belinda     | 3.30 |
| 2026-11-03 | Tom H       | 4.41 |
| 2026-11-10 | Teresa      | 3.30 |
| 2026-11-17 | Yimin       | 3.30 |



## Interesting Conferences

Please open an issue with any conferences you think might be of interest for the group and should be added to the list below. 

| Title | Dates | Location | Abstract Deadline |
|------------|--------|------|------------|
| [ERIS 2026 - XI European Radio Interferometry School](https://acme-eris-2026.sciencesconf.org) | 7-11 September | Noto, Scicily (Italy) | TBC |
| [AGN on the Beach II: A Multi-scale view of jetted AGN](https://www.jb.man.ac.uk/AGNbeachII/) | 21-25 September 2026 | Diani, Kenya | 17 April |
| [Many Faces of stellar-mass Black Holes](https://sites.google.com/view/bh-nepal-2026/home) | 12-16 October 2026 | Kathmandu, Nepal | 05 June |
| [The many tones of accretion - to the memory of Tommaso Belloni](https://indico.ict.inaf.it/event/3459) | 7-11 September 2026 | Cefalù, Sicily (Italy) | End of May |
| [NewAthena SWG2 Meeting](https://swg2meeting.com/#registration) | 25-29 January 2027 | Noordwijk The Netherlands | 23 October |

$^*$ Registration Only

## Minutes

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

