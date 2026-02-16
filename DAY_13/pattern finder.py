# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('../task 1/housing_prices.csv')

# 1. Generate correlation matrix and visualize with heatmap
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

# 2. Identify variables with correlation > 0.8 (excluding self-correlation)
high_corr = []
for i in corr_matrix.columns:
    for j in corr_matrix.columns:
        if i != j and abs(corr_matrix.loc[i, j]) > 0.8:
            high_corr.append((i, j, corr_matrix.loc[i, j]))
if high_corr:
    print('Highly correlated variable pairs (|corr| > 0.8):')
    for pair in high_corr:
        print(f'{pair[0]} & {pair[1]}: {pair[2]:.2f}')
else:
    print('No variable pairs with correlation > 0.8 found.')

# 3. Boxplot for outlier detection in Price
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Price'])
plt.title('Boxplot of Housing Prices')
plt.xlabel('Price')
plt.show()

# 4. Summary
print('\n--- Summary ---')
if high_corr:
    print('Warning: Multicollinearity detected. Consider removing or combining highly correlated features.')
else:
    print('No multicollinearity detected.')
print('Check the boxplot for outliers in the Price column. Outliers may need to be handled before modeling.')
