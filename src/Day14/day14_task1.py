import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})


le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df)
