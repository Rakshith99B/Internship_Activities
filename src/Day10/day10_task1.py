import pandas as pd
df = pd.read_csv("C:\\DS_AI_Internship\\src\\Day10\\customers_order.csv")
print("Original shape:", df.shape)

num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df = df.drop_duplicates()
print("\nCleaned shape:", df.shape)

