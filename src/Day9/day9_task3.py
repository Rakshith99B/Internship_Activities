import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned = usernames.str.strip().str.lower()

contains_a = cleaned.str.contains('a')

print("Cleaned Usernames:\n", cleaned)
print("\nContains letter 'a':\n", contains_a)