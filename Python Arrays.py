import numpy as np

# random numpy array
a2D_array = np.random.randint(0, 25, (5, 5))
print(a2D_array)

# printing the 2nd row on the third column
print('2nd row on the 3rd column:', a2D_array[1,2])

# finding and printing the total sum of the array
sum_a2D = np.sum(a2D_array)
print(sum_a2D)

# printing the mean of each row
print(np.mean(a2D_array, axis=1))

# finding and printing the max of each row
x = np.amax(a2D_array, axis=1)
print(x)
