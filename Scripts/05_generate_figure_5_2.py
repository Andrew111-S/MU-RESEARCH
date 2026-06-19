import pandas as pd
import matplotlib.pyplot as plt

mh = 125.0

df = pd.read_csv("../datasets/coupling_limits.csv")
bands = pd.read_csv("../datasets/atlas2022_vbf_coupling_bands.csv")

zoom = (df["mV_GeV"] >= 55.0) & (df["mV_GeV"] <= 62.49)
zoom_band = (bands["mV_GeV"] >= 55.0) & (bands["mV_GeV"] <= 62.49)

mV = df.loc[zoom, "mV_GeV"]

plt.figure(figsize=(10.5, 6.2))

plt.fill_between(
    bands.loc[zoom_band, "mV_GeV"],
    bands.loc[zoom_band, "ATLAS2022VBF_minus2sigma"],
    bands.loc[zoom_band, "ATLAS2022VBF_plus2sigma"],
    alpha=0.18,
    label=r"ATLAS 2022 VBF expected $\pm2\sigma$"
)

plt.fill_between(
    bands.loc[zoom_band, "mV_GeV"],
    bands.loc[zoom_band, "ATLAS2022VBF_minus1sigma"],
    bands.loc[zoom_band, "ATLAS2022VBF_plus1sigma"],
    alpha=0.30,
    label=r"ATLAS 2022 VBF expected $\pm1\sigma$"
)

for col in df.columns:
    if col.endswith("_g_obs"):
        label = col.replace("_g_obs", " obs")
        plt.plot(mV, df.loc[zoom, col], label=label)

    if col.endswith("_g_exp"):
        label = col.replace("_g_exp", " exp")
        plt.plot(mV, df.loc[zoom, col], linestyle="--", label=label)

plt.axvline(mh / 2.0, linestyle=":", linewidth=1.5)
plt.text(mh / 2.0 + 0.05, plt.ylim()[0] * 1.4, r"$m_h/2$",
         rotation=90, va="bottom")

plt.yscale("log")
plt.xlim(55, 62.5)
plt.xlabel(r"$m_V$ [GeV]")
plt.ylabel(r"$g_{hVV}^{\max}$ [GeV]")
plt.title(r"Zoomed threshold region: $55$--$62.5$ GeV")
plt.grid(True, which="both", linewidth=0.4, alpha=0.5)
plt.legend(fontsize=8, ncol=2, frameon=False, loc="upper left")
plt.tight_layout()

plt.savefig("../figures/figure5_2_threshold_zoom.png", dpi=300)
plt.savefig("../figures/figure5_2_threshold_zoom.pdf")
plt.show()