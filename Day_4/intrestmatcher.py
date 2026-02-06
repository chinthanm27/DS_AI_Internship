# Step 1: Create sets for each friend's interests
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

# Step 2: Intersection (shared interests)
shared_interests = friend_a & friend_b

# Step 3: Union (all unique interests)
all_interests = friend_a | friend_b

# Step 4: Difference (interests friend_a has but friend_b does not)
unique_to_a = friend_a - friend_b

# Step 5: Output results
print(f"Shared Interests: {shared_interests}")
print(f"All Interests: {all_interests}")
print(f"Unique to Friend A: {unique_to_a}")
