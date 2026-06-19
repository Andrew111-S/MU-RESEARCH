import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mh = 125.0

df = pd.read_csv("../datasets/coupling_limits.csv")
bands = pd.read_csv("../datasets/atlas2022_vbf_coupling_bands.csv")

mV = df["mV_GeV"]

plt.figure(figsize=(10.5, 6.2))

plt.fill_between(
    bands["mV_GeV"],
    bands["ATLAS2022VBF_minus2sigma"],
    bands["ATLAS2022VBF_plus2sigma"],
    alpha=0.18,
    label=r"ATLAS 2022 VBF expected $\pm2\sigma$"
)

plt.fill_between(
    bands["mV_GeV"],
    bands["ATLAS2022VBF_minus1sigma"],
    bands["ATLAS2022VBF_plus1sigma"],
    alpha=0.30,
    label=r"ATLAS 2022 VBF expected $\pm1\sigma$"
)

for col in df.columns:
    if col.endswith("_g_obs"):
        label = col.replace("_g_obs", " obs")
        plt.plot(mV, df[col], label=label)

    if col.endswith("_g_exp"):
        label = col.replace("_g_exp", " exp")
        plt.plot(mV, df[col], linestyle="--", label=label)

plt.axvline(mh / 2.0, linestyle=":", linewidth=1.5)
plt.text(mh / 2.0 + 0.3, plt.ylim()[0] * 1.6, r"threshold $m_h/2$",
         rotation=90, va="bottom")

plt.yscale("log")
plt.xlim(0, 65)
plt.xlabel(r"$m_V$ [GeV]")
plt.ylabel(r"$g_{hVV}^{\max}$ [GeV]")
plt.title(r"Evolution of VBF $H\to$ inv constraints mapped to $g_{hVV}$ bounds")
plt.grid(True, which="both", linewidth=0.4, alpha=0.5)
plt.legend(fontsize=8, ncol=2, frameon=False, loc="lower right")
plt.tight_layout()

plt.savefig("../figures/figure5_1_evolution_overlay.png", dpi=300)
plt.savefig("../figures/figure5_1_evolution_overlay.pdf")
plt.show()