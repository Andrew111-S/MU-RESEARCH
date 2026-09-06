import numpy as np
import pandas as pd

mh = 125.0
GammaSM = 4.1e-3

def gamma_inv_max(br):
    return (br / (1.0 - br)) * GammaSM

def A_of_mV(mV_arr):
    x = (mV_arr**2) / (mh**2)
    sqrt_term = np.sqrt(np.maximum(1.0 - 4.0 * x, 0.0))
    kin = (1.0 - 4.0 * x + 12.0 * x**2) * sqrt_term
    pref = (mh**3) / (128.0 * np.pi * (mV_arr**4))
    return pref * kin

def gmax(gamma_inv, A):
    return np.sqrt(np.maximum(gamma_inv / A, 0.0))

bands = pd.read_csv("../datasets/atlas2022_vbf_uncertainty.csv")
br = dict(zip(bands["Quantity"], bands["BRinv"]))

# Same dense mass grid used for the final coupling analysis.
mV = np.linspace(1.0, 62.45, 1600)
A = A_of_mV(mV)

out = pd.DataFrame({
    "mV_GeV": mV,
    "ATLAS2022VBF_expected": gmax(gamma_inv_max(br["Expected"]), A),
    "ATLAS2022VBF_minus1sigma": gmax(gamma_inv_max(br["Minus1Sigma"]), A),
    "ATLAS2022VBF_plus1sigma": gmax(gamma_inv_max(br["Plus1Sigma"]), A),
    "ATLAS2022VBF_minus2sigma": gmax(gamma_inv_max(br["Minus2Sigma"]), A),
    "ATLAS2022VBF_plus2sigma": gmax(gamma_inv_max(br["Plus2Sigma"]), A),
})

out.to_csv("../datasets/atlas2022_vbf_coupling_bands.csv", index=False)

print("Saved ATLAS 2022 VBF expected-sensitivity quantile bands.")
print(f"Mass grid: {len(mV)} points from {mV[0]:.2f} to {mV[-1]:.2f} GeV")
