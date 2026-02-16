import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(2)

n = 200
price = np.random.gamma(shape=2.5, scale=80000, size=n)
city = np.random.choice(["Mumbai", "Delhi", "Bangalore"], n)

df = pd.DataFrame({
    "Price": price,
    "City": city
})

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
df["Price"].hist(bins=20, density=True)
df["Price"].plot(kind="kde")
plt.title("Histogram with KDE - Price")
plt.xlabel("Price")
plt.ylabel("Density")

plt.subplot(1,2,2)
df["City"].value_counts().plot(kind="bar")
plt.title("Count Plot - City")
plt.xlabel("City")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
