numbers = [10, 20, 30, 40]

cordinates = (5, 10)
print(numbers)    
print(cordinates)


#######SLICING#########
num=[100,650,550,400,500,600,700,800,900]
print(num[1:4])
print(num[:5])
print(num[5:])
print(num[-3:-1])
print(num[1:9:2])
print(num[-2:-9:-2])

num.sort()
print(f"Sorted list :\n {num}")

num.reverse()
print(f"Reversed list :\n {num}")

num.append(750)
print(f"Appended list :\n {num}")  

num.insert(3, 375)
print(f"List after insertion :\n {num}")

num.remove(400)
print(f"List after removal :\n {num}")

num.pop()
print(f"List after popping last element :\n {num}")

num.pop(2)
print(f"List after popping element at index 2 :\n {num}")  








      
