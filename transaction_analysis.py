import pandas as pd

df = pd.read_csv(
    "competitor_analysis_with_transactions.csv",
    encoding="latin1"
)

df.columns = df.columns.str.strip().str.replace(" ", "_")

df["Population"] = pd.to_numeric(df["Population"], errors="coerce")
df["Area_km_sq"] = pd.to_numeric(df["Area_km_sq"], errors="coerce")

TRANSACTION_RATE = 0.15  # ₹15,000 per person per year

df["Estimated_Transaction_Value_Lakh_Per_Year"] = (
    df["Population"] * TRANSACTION_RATE
)

df["Transaction_Intensity_Lakh_Per_Year_Per_km2"] = (
    df["Estimated_Transaction_Value_Lakh_Per_Year"] /
    df["Area_km_sq"].replace(0, pd.NA)
)

df.to_csv(
    "competitor_analysis_and_transactions_analysis.csv",
    index=False,
    encoding="utf-8"
)

print("Rows preserved:", len(df))
