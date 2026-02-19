import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Generate datasets
np.random.seed(42)

# Normal distribution: Human Heights (mean=170cm, std=10cm)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-skewed: Household Incomes (log-normal, mean=10, sigma=0.8)
incomes = np.random.lognormal(mean=10, sigma=0.8, size=1000)

# Left-skewed: Test Scores (Beta distribution, a=5, b=1.5, scaled to 0-100)
scores = np.random.beta(a=5, b=1.5, size=1000) * 100

df = pd.DataFrame({
    'Heights (cm)': heights,
    'Incomes': incomes,
    'Test Scores': scores
})

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Heights (Normal)
sns.histplot(df['Heights (cm)'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Human Heights (Normal)')
axes[0].set_xlabel('Height (cm)')

# Incomes (Right-Skewed)
sns.histplot(df['Incomes'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Household Incomes (Right-Skewed)')
axes[1].set_xlabel('Income')

# Test Scores (Left-Skewed)
sns.histplot(df['Test Scores'], kde=True, ax=axes[2], color='lightgreen')
axes[2].set_title('Test Scores (Left-Skewed)')
axes[2].set_xlabel('Score')

plt.tight_layout()
plt.show()

print("\nMean and Median Comparison:")
for col in df.columns:
    mean = df[col].mean()
    median = df[col].median()
    print(f"{col}: Mean = {mean:.2f}, Median = {median:.2f}")

print("\nSkewness Observation:")
for col in df.columns:
    mean = df[col].mean()
    median = df[col].median()
    if mean > median:
        skew = 'Right-Skewed'
    elif mean < median:
        skew = 'Left-Skewed'
    else:
        skew = 'Normal/Symmetric'
    print(f"{col}: {skew} (Mean = {mean:.2f}, Median = {median:.2f})")

print("""
Why does this matter?
Many ML algorithms (like Linear Regression) assume a Normal distribution. If your data is skewed, your model's predictions might be biased. Consider transforming skewed data for better results.
""")
