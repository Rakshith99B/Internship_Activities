name=input("Enter your name: ")
goal=input("Enter your goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Goal: {goal}\n")
    file.close()