import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# Create scatter plot
plt.scatter(study_hours, scores, color='blue', edgecolor='black')
plt.title('Study Hours vs Exam Scores')
plt.xlabel('Hours Spent Studying')
plt.ylabel('Exam Scores')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()