friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

shared = friend_a & friend_b
print("Shared interests:", shared)

all_interests = friend_a | friend_b
print("All interests:", all_interests)

unique_to_a = friend_a - friend_b
print(" Unique Interests:", unique_to_a)