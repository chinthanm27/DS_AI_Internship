import pandas as pd

# Create the Series with custom labels
products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])

# Print the full Series
print("Full Product Catalog:")
print(products)

# Access the price of 'Laptop' using label-based indexing
laptop_price = products['Laptop']
print("\nPrice of Laptop:", laptop_price)

# Slice the Series to show the first two products using positional indexing
first_two = products.iloc[:2]
print("\nFirst two products:")
print(first_two)
