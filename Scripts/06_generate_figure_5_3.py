import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mh = 125.0
mN = 0.939
v = 246.0
fN = 0.30
GEV2_TO_CM2 = 0.389379e-27

df = pd.read_csv("../datasets/coupling_limits.csv")
lz = pd.read_csv("../datasets/lz_limit.csv")
xenonnt = pd.read_csv("../datasets/xenonnt_limit.csv")
pandax = pd.read_csv("../datasets/pandax4t_digitized.csv")

mV = df["mV_GeV"].to_numpy()

def reduced_mass(mv):
    return (mv * mN) / (mv + mN)

def sigma_si(g, mv):
    """Spin-independent V-N cross section in cm^2 for dimensionful g_hVV."""
    mu = reduced_mass(mv)
    factor = (fN * mN * g) / (v * mh**2)
    sigma_gev2 = (mu**2 / (4.0 * np.pi * mv**2)) * factor**2
    return sigma_gev2 * GEV2_TO_CM2

# Primary collider constraint: ATLAS 2022 VBF-only observed BR(H->inv) < 0.145.
g_vbf = df["ATLAS2022VBF_g_obs"].to_numpy()
sigma_vbf = sigma_si(g_vbf, mV)

# Overall reference: ATLAS 2023 combined observed BR(H->inv) < 0.107.
g_comb = df["ATLAS2023Combined_g_obs"].to_numpy()
sigma_comb = sigma_si(g_comb, mV)

plt.figure(figsize=(9.5, 6.2))

plt.plot(
    mV, sigma_vbf, linewidth=2.2,
    label="ATLAS 2022 VBF-only (primary)"
)
plt.plot(
    mV, sigma_comb, linewidth=1.8, linestyle="--",
    label="ATLAS 2023 combined (reference)"
)

plt.plot(lz["mV_GeV"], lz["sigmaSI_cm2"], label="LZ 2023")
plt.plot(xenonnt["mV_GeV"], xenonnt["sigmaSI_cm2"], label="XENONnT 2025")
plt.plot(pandax["mV_GeV"], pandax["sigmaSI_cm2"], label="PandaX-4T 2021")

plt.yscale("log")
plt.xlim(1, 65)
plt.xlabel(r"$m_V$ [GeV]")
plt.ylabel(r"$\sigma_{\mathrm{SI}}$ [cm$^2$]")
plt.title(r"Collider-implied $\sigma_{\mathrm{SI}}$ compared with direct detection")
plt.grid(True, which="both", linewidth=0.4, alpha=0.5)
plt.legend(fontsize=9, frameon=False)
plt.tight_layout()

plt.savefig("../figures/figure5_3_sigmaSI_overlay.png", dpi=300)
plt.savefig("../figures/figure5_3_sigmaSI_overlay.pdf")

# Numerical benchmark used to verify the corrected implementation.
g50 = np.interp(50.0, mV, g_vbf)
sigma50 = sigma_si(g50, 50.0)
print(f"ATLAS 2022 VBF-only at mV=50 GeV: g_hVV^max = {g50:.6g} GeV")
print(f"ATLAS 2022 VBF-only at mV=50 GeV: sigma_SI^max = {sigma50:.6e} cm^2")

plt.show()
