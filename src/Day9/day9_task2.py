import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

filled = grades.fillna(0)

filtered = filled[filled > 60]

print("Original:\n", grades)
print("\nFilled:\n", filled)
print("\nGreater than 60:\n", filtered)
