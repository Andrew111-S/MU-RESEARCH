import numpy as np
import pandas as pd

mh = 125.0

def A_of_mV(mV_arr, mh_val=mh):
    x = (mV_arr**2) / (mh_val**2)
    sqrt_term = np.sqrt(np.maximum(1.0 - 4.0 * x, 0.0))
    kin = (1.0 - 4.0 * x + 12.0 * x**2) * sqrt_term
    pref = (mh_val**3) / (128.0 * np.pi * (mV_arr**4))
    return pref * kin

def gmax_from_ginv(gamma_inv, A_arr):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.sqrt(np.maximum(gamma_inv / A_arr, 0.0))

df = pd.read_csv("../datasets/collider_width_limits.csv")

mV = np.linspace(1.0, 62.49, 1400)
A = A_of_mV(mV)

out = pd.DataFrame({"mV_GeV": mV})

for _, row in df.iterrows():
    key = row["Analysis"]
    out[f"{key}_g_obs"] = gmax_from_ginv(row["Gamma_inv_obs_GeV"], A)
    out[f"{key}_g_exp"] = gmax_from_ginv(row["Gamma_inv_exp_GeV"], A)

out.to_csv("../datasets/coupling_limits.csv", index=False)

print("Saved coupling limits to ../datasets/coupling_limits.csv")