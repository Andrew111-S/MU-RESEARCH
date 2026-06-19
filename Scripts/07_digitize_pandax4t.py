"""
Helper script for documenting PandaX-4T digitized points.

This script does not perform automatic image digitization. The PandaX-4T
points were extracted manually from the published exclusion plot using a
plot-digitization tool, then saved as pandax4t_digitized.csv.

Output:
    ../datasets/pandax4t_digitized.csv
"""

import pandas as pd

# Replace these example values with your actual digitized PandaX-4T points
data = {
    "mV_GeV": [
        5, 10, 20, 30, 40, 50, 60
    ],
    "sigmaSI_cm2": [
        2.1e-45, 8.5e-47, 2.4e-47, 1.6e-47, 1.3e-47, 1.1e-47, 1.0e-47
    ],
}

df = pd.DataFrame(data)

df.to_csv("../datasets/pandax4t_digitized.csv", index=False)

print("Saved PandaX-4T digitized points to ../datasets/pandax4t_digitized.csv")
print(df)
