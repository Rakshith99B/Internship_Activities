import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 50],
    "Salary": [20000, 25000, 40000, 60000, 80000, 35000, 45000, 90000, 100000]
})

scaler_std = StandardScaler()
df_standardized = pd.DataFrame(scaler_std.fit_transform(df), columns=df.columns)

scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(scaler_minmax.fit_transform(df), columns=df.columns)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.hist(df["Salary"], bins=5)
plt.title("Before Scaling")

plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized")
plt.xlim(-2, 2)

plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Normalized")
plt.xlim(0, 1)


plt.tight_layout()
plt.show()
