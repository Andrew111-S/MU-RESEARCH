import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mh = 125.0
mN = 0.939
v = 246.0
fN = 0.30
GEV2_TO_CM2 = 0.3894e-27

df = pd.read_csv("../datasets/coupling_limits.csv")

lz = pd.read_csv("../datasets/lz_limit.csv")
xenonnt = pd.read_csv("../datasets/xenonnt_limit.csv")
pandax = pd.read_csv("../datasets/pandax4t_digitized.csv")

mV = df["mV_GeV"]

def reduced_mass(mv):
    return (mv * mN) / (mv + mN)

def sigma_si(g, mv):
    mu = reduced_mass(mv)
    factor = (fN * mN * g) / (mh**2 * v)
    return (mu**2 / np.pi) * factor**2 * GEV2_TO_CM2

# Use ATLAS 2022 VBF observed as main collider-implied curve
g_col = df["ATLAS2022VBF_g_obs"]
sigma_col = sigma_si(g_col, mV)

plt.figure(figsize=(9.5, 6.2))

plt.plot(mV, sigma_col, linewidth=2.2, label="Collider-implied ATLAS 2022 VBF")

plt.plot(lz["mV_GeV"], lz["sigmaSI_cm2"], label="LZ")
plt.plot(xenonnt["mV_GeV"], xenonnt["sigmaSI_cm2"], label="XENONnT")
plt.plot(pandax["mV_GeV"], pandax["sigmaSI_cm2"], label="PandaX-4T")

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
plt.show()