import csv

file = open("students.csv", "r")
reader = csv.DictReader(file)

print(reader.fieldnames)   

print("Students who passed:")
for row in reader:
    if row["Status"] == "Pass":
        print(row["Name"])
file.close()
