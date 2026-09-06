"""
03_coupling_to_sigmaSI.py

Translate collider-derived Higgs-vector coupling limits into spin-independent
vector dark matter-nucleon scattering limits using the corrected vector
Higgs-portal relation.

Input:
    ../datasets/coupling_limits.csv

Output:
    ../datasets/sigmaSI_limits.csv
"""

import numpy as np
import pandas as pd

# Numerical inputs used in the thesis
MH = 125.0
MN = 0.939
V = 246.0
FN = 0.30
GEV2_TO_CM2 = 0.389379e-27


def reduced_mass(mv):
    """Vector-DM/nucleon reduced mass in GeV."""
    return (mv * MN) / (mv + MN)


def sigma_si(g_hvv, mv):
    """
    Spin-independent V-N scattering cross section in cm^2.

    Correct relation for the dimensionful trilinear coupling g_hVV:

        sigma_SI =
        [mu_VN^2 / (4*pi*mV^2)]
        * [f_N*m_N*g_hVV / (v*m_h^2)]^2
    """
    mu = reduced_mass(mv)
    factor = (FN * MN * g_hvv) / (V * MH**2)
    sigma_gev2 = (mu**2 / (4.0 * np.pi * mv**2)) * factor**2
    return sigma_gev2 * GEV2_TO_CM2


df = pd.read_csv("../datasets/coupling_limits.csv")
mV = df["mV_GeV"].to_numpy()

out = pd.DataFrame({"mV_GeV": mV})

for col in df.columns:
    if col.endswith("_g_obs") or col.endswith("_g_exp"):
        sigma_col = col.replace("_g_", "_sigmaSI_")
        out[sigma_col] = sigma_si(df[col].to_numpy(), mV)

out.to_csv("../datasets/sigmaSI_limits.csv", index=False)

# Numerical validation of the primary ATLAS 2022 VBF-only observed curve
if "ATLAS2022VBF_g_obs" in df.columns:
    g50 = np.interp(50.0, mV, df["ATLAS2022VBF_g_obs"].to_numpy())
    sigma50 = sigma_si(g50, 50.0)

    print("Validation benchmark:")
    print(f"  mV = 50 GeV")
    print(f"  ATLAS 2022 VBF-only g_hVV^max = {g50:.6g} GeV")
    print(f"  sigma_SI^max = {sigma50:.6e} cm^2")

print("Saved collider-implied scattering limits to ../datasets/sigmaSI_limits.csv")
