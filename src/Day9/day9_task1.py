import pandas as pd

products = pd.Series(
    [700, 150, 300],
    index=['Desktop', 'Mouse', 'Keyboard']
)

laptop_price = products['Desktop']
first_two_products = products.iloc[0:2]

print("Full Series:")
print(products)

print("\nPrice of Desktop:")
print(laptop_price)

print("\nFirst Two Products:")
print(first_two_products)