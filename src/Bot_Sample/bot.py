import random

print("🤖 Welcome to RoboController 1.0 🤖")

# --- User Inputs ---
robot_name = input("Enter robot name: ")
target_distance = int(input("Enter distance to target (in meters): "))
obstacle_ahead = input("Is there an obstacle ahead? (yes/no): ").lower()

# --- Decision Making ---
speed = 0
movement = ""

if obstacle_ahead == "yes":
    if target_distance > 50:
        speed = 5
        movement = "Slow forward with caution"
    else:
        speed = 2
        movement = "Very slow movement"
else:
    if target_distance > 100:
        speed = 20
        movement = "Fast forward"
    elif target_distance > 50:
        speed = 12
        movement = "Moderate speed"
    else:
        speed = 6
        movement = "Slow and precise"

# --- Journey Checkpoints ---
checkpoints = ["Start Point"]

# Simulate journey checkpoints
for i in range(1, 4):
    direction = random.choice(["Left", "Right", "Straight"])
    checkpoint = f"Checkpoint {i} - Turn {direction}"
    checkpoints.append(checkpoint)

# Add final destination
checkpoints.append("Destination Reached")

# Optional update (remove a checkpoint randomly)
removed_checkpoint = random.choice(checkpoints[1:-1])
checkpoints.remove(removed_checkpoint)

# --- Distance Calculation ---
distance_travelled = target_distance - random.randint(0, 10)

# --- Trip Summary ---
print("\n📊 TRIP SUMMARY 📊")
print(f"Robot Name        : {robot_name}")
print(f"Target Distance   : {target_distance} meters")
print(f"Distance Travelled: {distance_travelled} meters")
print(f"Obstacle Ahead    : {'Yes' if obstacle_ahead == 'yes' else 'No'}")
print(f"Chosen Speed      : {speed} m/s")
print(f"Movement Strategy : {movement}")
print(f"Removed Checkpoint: {removed_checkpoint}")
print(f"Final Checkpoints : {checkpoints}")

print("\n✅ Mission Completed Successfully!")
