import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (example: monthly sales trend)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
trend = [120, 150, 170, 160, 180, 200]

plt.figure(figsize=(10, 4))

# Bar chart subplot
plt.subplot(1, 2, 1)
plt.bar(categories, sales, color=['blue', 'green', 'orange'])
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')

# Line plot subplot
plt.subplot(1, 2, 2)
plt.plot(months, trend, marker='o', color='purple')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.tight_layout()
plt.show()
