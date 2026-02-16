import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)

n = 100
sqft = np.random.randint(600, 3000, n)
price = sqft * 150 + np.random.normal(0, 20000, n)
bedrooms = sqft // 500
tax = price * 0.01

df = pd.DataFrame({
    "SquareFootage": sqft,
    "Price": price,
    "Bedrooms": bedrooms,
    "Tax": tax
})

corr = df.corr()

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Matrix")
plt.colorbar()

plt.subplot(1,2,2)
plt.boxplot(df["Price"])
plt.title("Boxplot of Price")

plt.tight_layout()
plt.show()

high_corr = [(corr.columns[i], corr.columns[j], corr.iloc[i,j])
             for i in range(len(corr.columns))
             for j in range(i+1, len(corr.columns))
             if abs(corr.iloc[i,j]) > 0.8]

print("Highly Correlated Pairs (>0.8):")
print(high_corr)
