import pandas as pd

data = {
    "Price": ["₹100", "₹250", "₹75"],
    "Date": ["2026-01-01", "2026-01-05", "2026-01-10"]
}

df = pd.DataFrame(data)

print("Before Conversion:\n")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("₹", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

print("\nAfter Conversion:\n")
print(df.dtypes)
print("\nUpdated DataFrame:\n")
print(df)
