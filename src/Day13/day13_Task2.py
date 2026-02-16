import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(5)

n = 120
square_footage = np.random.randint(500, 3000, n)
price = square_footage * 155 + np.random.normal(0, 25000, n)
location = np.random.choice(["Urban", "Suburban", "Rural"], n)

df = pd.DataFrame({
    "SquareFootage": square_footage,
    "Price": price,
    "Location": location
})

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.scatter(df["SquareFootage"], df["Price"])
plt.xlabel("SquareFootage")
plt.ylabel("Price")
plt.title("Scatter Plot")


plt.subplot(1,2,2)
data_to_plot = [
    df[df["Location"] == "Urban"]["Price"],
    df[df["Location"] == "Suburban"]["Price"],
    df[df["Location"] == "Rural"]["Price"]
]

plt.boxplot(data_to_plot, labels=["Urban", "Suburban", "Rural"])
plt.xlabel("Location")
plt.ylabel("Price")
plt.title("Boxplot")

plt.tight_layout()
plt.show()
