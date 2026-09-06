# MU-RESEARCH

## Vector Boson Fusion Invisible Higgs Decays as Constraints on Higgs-Portal Vector Dark Matter

This repository contains the numerical inputs, processed datasets, and computational material used to support the phenomenological reinterpretation presented in the thesis:

**Vector Boson Fusion Invisible Higgs Decays as Constraints on Higgs-Portal Vector Dark Matter**

The analysis begins from published ATLAS and CMS limits on invisible Higgs decays, converts those limits into bounds on the invisible Higgs width and the Higgs-portal vector coupling, studies the near-threshold region at m_V ≈ m_h/2, and translates the collider limits into spin-independent dark matter-nucleon scattering bounds for comparison with direct-detection experiments.

This repository is intended to make the analysis chain transparent, traceable, and reproducible. It is a phenomenological reinterpretation of published results and is not a detector-level reanalysis of ATLAS, CMS, LZ, XENONnT, or PandaX-4T data.

---

## Analysis workflow

The numerical workflow follows the sequence:

1. Published BR(H -> inv) limits
2. Maximum invisible Higgs width, Gamma_inv^max
3. Collider-derived Higgs-vector coupling bound, g_hVV^max(m_V)
4. Spin-independent scattering bound, sigma_SI^max(m_V)
5. Comparison with LZ, XENONnT, and PandaX-4T

The compact version of this sequence is also stored in `workflow_summary.csv`.

The invisible-width conversion used in the thesis is

Gamma_inv^max = [BR(H -> inv) / (1 - BR(H -> inv))] Gamma_SM.

For the vector Higgs-portal interpretation,

g_hVV = lambda_HV v,

and the corrected spin-independent scattering relation is

sigma_SI = [mu_VN^2 / (4 pi m_V^2)] [f_N m_N g_hVV / (v m_h^2)]^2,

where

mu_VN = m_V m_N / (m_V + m_N).

---

## Datasets included

### `collider_limits.csv`

Published invisible-Higgs limits used as collider inputs.

The dataset contains the CMS 2014 Run-1 result, CMS 2019 and CMS 2022 VBF-only results, the ATLAS 2022 VBF-only result, and the ATLAS 2023 combined result. The CMS 2014 result originates from the analysis that considered VBF together with the associated ZH production mode; this should not be interpreted as a later VBF-only Run-2 measurement.

The principal collider input used for the VBF-first interpretation and for the primary collider curve in Figure 5.3 is the **ATLAS 2022 VBF-only observed limit BR(H -> inv) < 0.145**. The **ATLAS 2023 combined observed limit BR(H -> inv) < 0.107** is retained as an overall reference.

### `atlas2022_vbf_uncertainty.csv`

Expected-limit sensitivity quantiles for the ATLAS 2022 VBF-only result.

The stored values are:

- observed: 0.145
- expected median: 0.103
- -1 sigma: 0.075
- +1 sigma: 0.144
- -2 sigma: 0.055
- +2 sigma: 0.196

These quantities are expected-limit sensitivity quantiles under the background-only hypothesis. They are not Gaussian measurement uncertainties on the observed branching-ratio limit.

### `higgs_constants.csv`

Numerical constants used in the analysis, including:

- m_h = 125 GeV
- Gamma_SM = 0.0041 GeV
- f_N = 0.30
- m_N = 0.939 GeV

### `sigmaSI_translation_parameters.csv`

Parameters used in the collider-to-direct-detection translation. This file records the constants and identifies the adopted theoretical interpretation as the vector Higgs-portal model.

### `workflow_summary.csv`

Compact record of the main analysis stages from the invisible-Higgs branching-ratio limit through to the comparison with direct-detection experiments.

### `lz_limit.csv`

LZ spin-independent dark matter-nucleon exclusion data used in the corrected Figure 5.3.

The final thesis figure uses the detailed machine-readable LZ numerical points associated with the published LZ result. The dataset is imported directly rather than reconstructed from a plotted curve.

Representative check:
- at m_V = 30 GeV: sigma_SI = 9.37582 x 10^-48 cm^2

### `xenonnt_limit.csv`

Reconstructed XENONnT 2025 spin-independent exclusion curve used in the corrected Figure 5.3.

The curve used in the final thesis workflow is treated as a reconstructed numerical comparison input rather than as a directly imported HEPData table. It was cross-checked against the published XENONnT result.

Representative check:
- reconstructed value at m_V = 30 GeV: 1.76 x 10^-47 cm^2
- published minimum observed limit at approximately 30 GeV: 1.7 x 10^-47 cm^2
- difference at this benchmark: approximately 3.5%

This benchmark agreement is a validation point and should not be interpreted as a uniform 3.5% uncertainty over the whole reconstructed curve.

### `pandax4t_digitized.csv`

Digitized PandaX-4T 2021 spin-independent exclusion curve used in the corrected Figure 5.3.

The curve was reconstructed from the published exclusion figure because the thesis workflow used figure-based points rather than a directly imported official numerical table.

Representative check:
- digitized value at m_V = 40 GeV: 3.84 x 10^-47 cm^2
- published minimum exclusion near 40 GeV: approximately 3.8 x 10^-47 cm^2
- benchmark difference: approximately 1.1%

The 1.1% agreement applies only to this validation point and is not treated as a uniform uncertainty over the entire digitized curve.

---

## Figure 5.3 provenance

The corrected Figure 5.3 compares:

- the ATLAS 2022 VBF-only collider-implied sigma_SI bound as the primary collider constraint;
- the ATLAS 2023 combined collider-implied bound as an overall collider reference;
- LZ 2023;
- XENONnT 2025;
- PandaX-4T 2021.

The collider-derived curves use the corrected vector-mass-dependent scattering formula shown above.

At m_V = 50 GeV, the ATLAS 2022 VBF-only observed limit gives approximately

g_hVV^max = 1.50 GeV

and

sigma_SI^max = 1.26 x 10^-46 cm^2.

The approximate crossover masses found in the corrected comparison are:

- LZ: 22.5 GeV
- XENONnT: 26.6 GeV
- PandaX-4T: 35.3 GeV

The PandaX-4T crossover is treated as approximate because it depends on the digitized curve.

---

## Threshold-region treatment

The on-shell invisible decay h -> VV is kinematically allowed for

m_V < m_h/2.

The final numerical analysis evaluates the coupling bound on a dense grid of 1600 mass points between 1.0 GeV and 62.45 GeV, corresponding to a spacing of approximately 0.038 GeV.

Near m_V ≈ m_h/2, phase-space suppression causes the coupling bound and the collider-implied scattering bound to weaken rapidly. The dedicated threshold-region figure is therefore used to resolve this behaviour rather than treating the endpoint as a single coarse mass bin.

---

## Direct-detection assumptions

The collider-to-direct-detection mapping adopts

f_N = 0.30

for the central Higgs-nucleon form factor.

Because sigma_SI is proportional to f_N^2, varying f_N from 0.27 to 0.33 rescales the collider-implied cross section by factors of approximately 0.81 and 1.21, respectively.

The published underground limits are compared under their standard full-local-density interpretation. No relic-density calculation is performed in this thesis. Therefore, no underabundance rescaling factor is applied to the LZ, XENONnT, or PandaX-4T limits in the baseline Figure 5.3 comparison.

---

## Software environment

The computational workflow was implemented in Python using standard scientific libraries:

- NumPy
- pandas
- Matplotlib
- SciPy

For strict reproducibility, the exact versions from the environment used to generate the final thesis figures should be archived in a `requirements.txt` file.

From the final working Python environment, run:

```bash
python -m pip freeze > requirements.txt
```

The resulting `requirements.txt` should be committed to this repository together with the final scripts and datasets.

The Python version used for the final archived run should also be recorded, for example:

```bash
python --version
```

---

## Reproducing the analysis

Run the analysis from the repository root using the archived Python scripts.

The logical execution order is:

1. load `collider_limits.csv`, `higgs_constants.csv`, and `atlas2022_vbf_uncertainty.csv`;
2. convert BR(H -> inv) limits into Gamma_inv^max;
3. evaluate g_hVV^max(m_V) across the mass grid;
4. propagate the ATLAS 2022 expected-limit sensitivity quantiles;
5. generate the full coupling-bound plot and threshold-region plot;
6. translate the coupling bounds into sigma_SI^max(m_V) using `sigmaSI_translation_parameters.csv`;
7. load `lz_limit.csv`, `xenonnt_limit.csv`, and `pandax4t_digitized.csv`;
8. generate the corrected collider-versus-direct-detection comparison.

The final repository should preserve the exact scripts used for these stages so that the figures can be regenerated without manually modifying intermediate numerical values.

---

## Validation checks

The final archived workflow should reproduce the following benchmark values:

- ATLAS 2022 VBF-only at m_V = 50 GeV:
  - g_hVV^max ≈ 1.50 GeV
  - sigma_SI^max ≈ 1.26 x 10^-46 cm^2

- XENONnT reconstructed curve at 30 GeV:
  - sigma_SI ≈ 1.76 x 10^-47 cm^2

- PandaX-4T digitized curve at 40 GeV:
  - sigma_SI ≈ 3.84 x 10^-47 cm^2

These provide simple numerical checks that the correct datasets and corrected scattering relation are being used.

---

## Recommended archive-integrity record

For a fixed thesis-submission archive, file hashes may be recorded so that the exact inputs can be independently verified.

Linux/macOS example:

```bash
sha256sum *.csv *.py requirements.txt > checksums.sha256
```

Windows PowerShell example:

```powershell
Get-ChildItem *.csv,*.py,requirements.txt | Get-FileHash -Algorithm SHA256
```

If a checksum file is committed, it identifies the exact input and script versions associated with the final thesis results.

---

## Scope

This repository supports a phenomenological reinterpretation of published experimental limits. It does not contain raw LHC event data, detector simulation, reconstructed likelihoods, or a new experimental statistical analysis.

The collider-derived dark matter constraints therefore depend on the adopted vector Higgs-portal model, coupling convention, Higgs-width input, Higgs-nucleon form factor, threshold treatment, and assumptions used when comparing with direct-detection experiments.

---

## Thesis reference

The repository accompanies the thesis:

**Vector Boson Fusion Invisible Higgs Decays as Constraints on Higgs-Portal Vector Dark Matter**

The numerical inputs and code archived here are intended to provide a traceable record of the analysis used for the corrected thesis results.
