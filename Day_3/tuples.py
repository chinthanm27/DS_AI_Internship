# Tuples are immutable: their values cannot be changed after creation.

# Create a tuple for screen resolution
screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")

# The Experiment: Try to change the width
# This will cause a TypeError because tuples are immutable
# Uncomment the next line to see the error
# screen_res[0] = 1280

# The Fix: Comment out the error-causing line and explain
print("Tuples cannot be modified!")
