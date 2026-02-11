import pandas as pd


grades = pd.Series([85, None, 92, 45, None, 78, 55])


print("Original grades:")
print(grades)


missing = grades.isnull()
print("\nMissing values:")
print(missing)


filled_grades = grades.fillna(0)
print("\nGrades after filling missing values:")
print(filled_grades)

filtered = filled_grades[filled_grades > 60]
print("\nScores greater than 60:")
print(filtered)
