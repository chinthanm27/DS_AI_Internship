import numpy as np
scores = np.random.randint(50, 101, size=(5, 3))
subject_means = scores.mean(axis=0)
centered_scores = scores - subject_means  

print("Original scores:")
print(scores)
print("\nCentered scores (normalized):")
print(centered_scores)