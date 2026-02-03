import pandas as pd
import re

# ==============================
# LOAD DATASET
# ==============================
df = pd.read_csv("competitor_and_transactions_analysis.csv")

# ==============================
# USER INPUT
# ==============================
user_postal_code = int(input("Enter Postal Code: "))
user_place_name = input("Enter Place Name: ").strip()
user_sector = input("Enter Sector: ").strip()

population_col = "Pop_per_sq_km2"
transaction_col = "Transaction_Intensity_Lakh_Per_Year_Per_km2"

# ==============================
# VALIDATIONS
# ==============================
if user_sector not in df.columns:
    raise ValueError(f"Sector '{user_sector}' does not exist in dataset")

# ==============================
# FILTER ROW
# ==============================
matched_rows = df[
    (df["PostalCode"] == user_postal_code) &
    (df["PlaceName"].str.lower() == user_place_name.lower())
]

if len(matched_rows) == 0:
    raise ValueError("No matching row found for given Postal Code and Place Name")

if len(matched_rows) > 1:
    raise ValueError("Multiple rows matched. Data is ambiguous.")

row = matched_rows.iloc[0]

# ==============================
# CLEAN & CONVERT FUNCTION
# ==============================
def convert_to_numeric(value):
    if pd.isna(value):
        return None
    value = str(value).replace(",", "").strip()
    nums = re.findall(r"\d+\.?\d*", value)
    if len(nums) == 2:
        return (float(nums[0]) + float(nums[1])) / 2
    elif len(nums) == 1:
        return float(nums[0])
    return None

population = convert_to_numeric(row[population_col])
transaction = convert_to_numeric(row[transaction_col])
sector_value = convert_to_numeric(row[user_sector])

if population is None or transaction is None or sector_value is None:
    raise ValueError("Numeric conversion failed for required fields")

# ==============================
# NORMALIZATION (single-row safe)
# ==============================
pop_norm = population / df[population_col].apply(convert_to_numeric).max()
txn_norm = transaction / df[transaction_col].apply(convert_to_numeric).max()
sector_norm = sector_value / df[user_sector].apply(convert_to_numeric).max()

# ==============================
# SCORE CALCULATION
# ==============================
score = (
    1 * txn_norm +
    0.4 * pop_norm +
    0.6 * sector_norm
) * 100

score = round(score, 2)

# ==============================
# OUTPUT
# ==============================
print("\n✅ MATCH FOUND")
print(f"Postal Code   : {user_postal_code}")
print(f"Place Name   : {user_place_name}")
print(f"Sector       : {user_sector}")          
print(f"Final Score  : {score} / 200")
