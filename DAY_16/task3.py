import numpy as np
import matplotlib.pyplot as plt

# Heavily skewed dataset: log-normal (like income)
np.random.seed(42)
data = np.random.lognormal(mean=2, sigma=1.5, size=10000)

sample_means = []
for _ in range(1000):
    sample = np.random.choice(data, size=30, replace=False)
    sample_means.append(np.mean(sample))

plt.figure(figsize=(8,5))
plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black', density=True)
plt.title('Distribution of Sample Means (n=30, 1000 samples)')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.show()

print("Original data is heavily skewed, but the distribution of sample means is approximately normal. This demonstrates the Central Limit Theorem.")
