
######## Day 8: NumPy Fundamentals ########
import statistics as stats
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print("result:\n", result)

arr = np.random.rand(100)
print("Random Number:\n", arr)


squared = arr ** 2
print("squared:\n", squared)

########## Creating Arrays ##########

zeros_array = np.zeros((3, 4))
print( "zeros_array:\n", zeros_array)

ones_array = np.ones((2, 5))
print("ones_array:\n", ones_array)  


two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("two_d_array:\n", two_d_array)
  
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("three_d_array:\n", three_d_array)

##########Reshaping Arrays##########

arr = np.arange(12)
reshaped = arr.reshape(4, 3)
print("reshaped:\n", reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])

print("V stacked:")
vstacked = np.vstack((a, b))
print(vstacked)

print("H stacked:")
hstacked = np.hstack((a, b))
print(hstacked)

######## Statistics with NumPy ########
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print("Mean:",np.mean(data, axis=0))


######### Matrx multiplication #########
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.multiply(A, B)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix C (A * B):\n", C)



