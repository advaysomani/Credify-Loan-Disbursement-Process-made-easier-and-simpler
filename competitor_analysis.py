import pandas as pd
import numpy as np

# Load dataset (change filename if needed)
df = pd.read_csv("competitor_analysis.csv")
# If Excel:
# df = pd.read_excel("dataset.xlsx")

# Dictionary of sectors and their value ranges
sector_ranges = {
    "Agriculture and Allied Activities": (4, 10),
    "Transport Operators": (20, 55),
    "Computer Software": (30, 70),
    "Tourism, Hotels and Restaurants": (80, 110),
    "Shipping": (2, 10),
    "Aviation": (1, 5),
    "Professional Services": (90, 140),
    "Commercial Real Estate": (40, 70),
    "Education": (10, 45),
    "Housing": (100, 150),
    "Export Credit": (15, 25),
    "Housing Finance Companies (HFCs)": (10, 20),
    "Public Financial Institutions (PFIs)": (1, 5),
    "Wholesale Trade": (25, 40),
    "Retail Trade": (50, 100),
    "Consumer Durables": (1, 5),
    "Renewable Energy": (10, 15),
    "Healthcare": (15, 30)
}

# Add sector columns with random values per row
for sector, (low, high) in sector_ranges.items():
    df[sector] = np.random.randint(low, high + 1, size=len(df))

# Save updated dataset
df.to_csv("dataset_with_sectors.csv", index=False)
# Or Excel:
# df.to_excel("dataset_with_sectors.xlsx", index=False)

print("Sector columns added successfully!")
