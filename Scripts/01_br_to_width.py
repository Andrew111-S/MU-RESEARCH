import pandas as pd

GAMMA_SM = 4.1e-3  # GeV

def gamma_inv_max(br_inv, gamma_sm=GAMMA_SM):
    return (br_inv / (1.0 - br_inv)) * gamma_sm

df = pd.read_csv("../datasets/collider_limits.csv")

df["Gamma_inv_obs_GeV"] = df["Observed_BRinv"].apply(gamma_inv_max)
df["Gamma_inv_exp_GeV"] = df["Expected_BRinv"].apply(gamma_inv_max)

df.to_csv("../datasets/collider_width_limits.csv", index=False)

print(df)