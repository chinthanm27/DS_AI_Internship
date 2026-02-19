import pandas as pd
import numpy as np

# Example dataset: Human Heights (Normal distribution)
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=1000)
df = pd.DataFrame({'Height (cm)': heights})

# Calculate mean and standard deviation
mu = df['Height (cm)'].mean()
sigma = df['Height (cm)'].std()

# Calculate z-score
df['z_score'] = (df['Height (cm)'] - mu) / sigma

# Identify outliers (|z| > 3)
outliers = df[np.abs(df['z_score']) > 3]

print(f"Mean (μ): {mu:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
print("\nRows with |z| > 3 (Statistical Outliers):")
print(outliers)
