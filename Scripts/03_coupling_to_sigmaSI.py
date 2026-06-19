"""
Convert Higgs-portal coupling limits into spin-independent
dark matter-nucleon scattering limits.

Input:
    ../datasets/coupling_limits.csv

Output:
    ../datasets/collider_sigmaSI_limits.csv
"""

import numpy as np
import pandas as pd

# Constants
m_h = 125.0          # Higgs mass [GeV]
m_N = 0.939          # nucleon mass [GeV]
v = 246.0            # Higgs vacuum expectation value [GeV]
f_N = 0.30           # Higgs-nucleon form factor
GEV2_TO_CM2 = 0.3894e-27


def reduced_mass(m_v, m_n=m_N):
    return (m_v * m_n) / (m_v + m_n)


def sigma_si(g_hvv, m_v):
    """
    Convert g_hVV into sigma_SI in cm^2.
    """
    mu = reduced_mass(m_v)
    factor = (f_N * m_N * g_hvv) / (m_h**2 * v)
    sigma_gev2 = (mu**2 / np.pi) * factor**2
    return sigma_gev2 * GEV2_TO_CM2


df = pd.read_csv("../datasets/coupling_limits.csv")
mV = df["mV_GeV"]

out = pd.DataFrame({"mV_GeV": mV})

for col in df.columns:
    if col.endswith("_g_obs") or col.endswith("_g_exp"):
        new_col = col.replace("_g_", "_sigmaSI_")
        out[new_col] = sigma_si(df[col], mV)

out.to_csv("../datasets/collider_sigmaSI_limits.csv", index=False)

print("Saved collider-implied sigma_SI limits to ../datasets/collider_sigmaSI_limits.csv")
print(out.head())
