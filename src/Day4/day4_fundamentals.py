a={"key1":"value","key2":1}

print(a["key1"])
print(a["key2"])
print("\n")
#########Topic 1##########
student = {
    "name": "Amit", 
    "age": 21, 
    "courses": "MCA"
}

print(student["name"])
student["age"] = 22  
student["city"] = "Delhi"
print(student)
print("\n")


######### Topic 2 ##########

marks={"Maths":80,"Science":75,"English":85}
print(marks.get("Maths"))
print(marks.get("History", 0))
for subject, score in marks.items():
    print(subject, score)

marks.update({"Science": 78})
print(marks)

marks.pop("English")
print(marks)

marks["History"] = 90
print(marks)
print("\n")


########## Items ##########
purchase = {
    "Alice":250,
    "Bob":400,
    "Charlie":150
}

for name, amount in purchase.items():
    print(f"{name} made a purchase of Rs.{amount}")

print("Total Customers:", len(purchase))
print("\n")

########## Dynamic Data Collection ###########

n=int(input("Enter number of customers: "))
user_purchases = {}

for i in range(n):
    name = input(f"Enter customer name : ")
    amount = int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name] = amount

print("Customer Purchase Data:", user_purchases)

top_customer = max(user_purchases, key=user_purchases.get)
print("Top Spending Customer:", top_customer)

top_amount = max(user_purchases.values())
print("Top Spending Amount:", top_amount)

######## Sets ##########
fruits = {"apple", "banana", "cherry"}