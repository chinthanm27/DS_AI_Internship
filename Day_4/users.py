# Step 1: Create the raw logs list with duplicates
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# Step 2: Convert to a set for unique users
unique_users = set(raw_logs)

# Step 3: Membership test for 'ID05'
is_id05_present = "ID05" in unique_users
print(f"Is 'ID05' a unique visitor? {is_id05_present}")

# Step 4: Compare counts
print(f"Total log entries: {len(raw_logs)}")
print(f"Unique visitors: {len(unique_users)}")

# Step 5: Output the unique set of IDs
print(f"Unique User IDs: {unique_users}")
