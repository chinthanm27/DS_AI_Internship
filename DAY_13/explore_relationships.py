import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'housing_prices.csv'
df = pd.read_csv(file_path)

 # Scatter plot: Area vs Price
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Area', y='Price')
plt.title('Scatter Plot: Area vs Price')
plt.xlabel('Area (Square Footage)')
plt.ylabel('Price')
plt.tight_layout()#space out the plot elements
plt.show()
plt.close()


# Boxplot: City vs Price
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='City', y='Price')
plt.title('Boxplot: City vs Price')
plt.xlabel('City')
plt.ylabel('Price')
plt.tight_layout()
plt.show()
plt.close()