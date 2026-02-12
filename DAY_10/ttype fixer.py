import pandas as pd
from pathlib import Path

# Load dataset (CSV only)
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "customer_orders.csv"

if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    raise FileNotFoundError("Dataset not found. Expected 'customer_orders.csv'.")

print("Initial data types:")
print(df.dtypes)

# Remove currency symbols and convert Price to float
if "Price" in df.columns:
    df["Price"] = (
        df["Price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
else:
    print("Column 'Price' not found.")

# Convert Date to datetime
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
else:
    print("Column 'Date' not found.")

print("\nData types after conversion:")
print(df.dtypes)
