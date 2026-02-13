######## Plot ########

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 11]

plt.plot(x, y)
plt.show()

######## Scatter Plot ########

x1 = [1, 2, 3, 4, 5]
y1 = [5, 4, 3, 2, 1]

plt.scatter(x1, y1)
plt.show()

######## Bar Chart ########

categories = ['A', 'B', 'C']
values = [11, 20, 15]

plt.bar(categories, values)
plt.show()

######## Customizing Plots ########

plt.subplot(1, 2, 1)
plt.plot([1,2,3], [1,4,9])
plt.title("Line Plot")
plt.subplot(1, 2, 2)
plt.bar(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()
