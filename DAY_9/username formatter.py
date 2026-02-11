import pandas as pd

# Create the Series with usernames
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove leading/trailing whitespace and convert to lowercase
cleaned = usernames.str.strip().str.lower()
print("Cleaned usernames:")
print(cleaned)

# Check which names contain the letter 'a'
contains_a = cleaned.str.contains('a')
print("\nContains 'a':")
print(contains_a)
