import pandas as pd

# Example dataset
data = {
    'Transmission': ['Automatic', 'Manual', 'Manual', 'Automatic'],
    'Color': ['Red', 'Blue', 'Green', 'Red']
}

df = pd.DataFrame(data)

# Label Encoding for Transmission (binary/ordinal)
df['Transmission'] = df['Transmission'].map({'Automatic': 0, 'Manual': 1})

# One-Hot Encoding for Color (nominal, drop_first=True to avoid dummy variable trap)
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print(df)