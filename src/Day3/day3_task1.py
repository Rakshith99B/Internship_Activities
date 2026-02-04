from typing import List


Str=["Apples", "Bananas", "Carrots", "Dates"]
print("Original List:", Str)

Str=list(Str)
Str.append("Eggs")
print(f"Updated list after appending: {Str}")

Str.remove("Bananas")
print(f"Updated list after removal: {Str}")
Str.sort()
print(f"Sorted list: {Str}")