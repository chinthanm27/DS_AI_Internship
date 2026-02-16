# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('housing_prices.csv')

# Plot histogram with KDE for Price
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, bins=30, color='skyblue')
plt.title('Distribution of Housing Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Calculate skewness and kurtosis for Price
skewness = df['Price'].skew()
kurtosis = df['Price'].kurtosis()
print(f"Skewness of Price: {skewness:.2f}")
print(f"Kurtosis of Price: {kurtosis:.2f}")

# Count plot for City column
plt.figure(figsize=(8, 5))
sns.countplot(x='City', data=df, palette='Set2')
plt.title('Count of Houses by City')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()

# --- Summary and Recommendations ---
print("\n--- Summary ---")
if abs(skewness) > 1:
    print("The Price data is highly skewed. Consider applying a log transformation before ML modeling.")
else:
    print("The Price data is approximately symmetric. No transformation needed for normality.")
if kurtosis > 3:
    print("The Price data has heavy tails (more outliers than normal distribution).")
else:
    print("The Price data has light or normal tails.")
most_frequent_city = df['City'].value_counts().idxmax()
print(f"Most frequent city: {most_frequent_city}")
