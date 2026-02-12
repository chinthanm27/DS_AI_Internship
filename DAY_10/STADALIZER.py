import pandas as pd
from pathlib import Path

# Load dataset (update filename if needed)
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "customer_orders.csv"
df = pd.read_csv(csv_path)

# Check if 'Location' column exists
if 'Location' in df.columns:
	# Normalize: strip whitespace and standardize casing
	df['Location'] = df['Location'].astype(str).str.strip().str.title()
	# Show unique values for verification
	print("Unique values in 'Location' after normalization:")
	print(df['Location'].unique())
else:
	print("Column 'Location' not found in the dataset.")
