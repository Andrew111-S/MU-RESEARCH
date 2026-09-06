"""
Helper script for documenting the PandaX-4T digitized points used in the thesis.

This script does not perform automatic image digitization. The PandaX-4T
points were extracted manually from the published exclusion plot using a
plot-digitization tool and are recorded here so that the dataset can be
reproduced exactly.

Output:
    ../datasets/pandax4t_digitized.csv
"""

import pandas as pd

data = {
    "mV_GeV": [
        6.0, 7.0, 8.0, 10.0, 12.0, 15.0, 18.0, 20.0,
        25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0
    ],
    "sigmaSI_cm2": [
        3.49e-44, 1.11e-44, 4.95e-45, 2.31e-45,
        9.74e-46, 2.49e-46, 1.00e-46, 6.23e-47,
        4.93e-47, 4.23e-47, 3.97e-47, 3.84e-47,
        3.97e-47, 4.11e-47, 4.35e-47, 4.47e-47
    ],
}

df = pd.DataFrame(data)
df.to_csv("../datasets/pandax4t_digitized.csv", index=False)

# Reproducibility benchmark used in the thesis.
sigma40 = df.loc[df["mV_GeV"] == 40.0, "sigmaSI_cm2"].iloc[0]

print("Saved PandaX-4T digitized points to ../datasets/pandax4t_digitized.csv")
print(f"Number of digitized points: {len(df)}")
print(f"Validation point at 40 GeV: sigma_SI = {sigma40:.3e} cm^2")
print(df)
