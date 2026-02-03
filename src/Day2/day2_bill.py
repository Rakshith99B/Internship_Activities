total_bill = float(input("Enter the Total Bill Amount: "))
num_people = int(input("Enter the Number of People: "))

share_per_person = total_bill / num_people


print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")

print("\nData Types:")
print(f"total_bill type: {type(total_bill)}")
print(f"num_people type: {type(num_people)}")
print(f"share_per_person type: {type(share_per_person)}")
