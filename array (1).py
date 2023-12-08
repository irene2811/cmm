# import libraries
import numpy as np
import random

# Basic Array Types
zeros_array = np.zeros(5)  # Array of 5 zeros
ones_array = np.ones(10)   # Array of 10 ones
empty_array = np.empty(3)  # Creates an array with 3 uninitialized elements

# Arrays with a Range of Numbers
range_array = np.arange(1, 10)  # Array with values from 1 to 9

# Array with Specific Values
specific_array = np.array([1, 2, 3, 4, 5])  # Array with specified values

# Multi-Dimensional Arrays
matrix_array = np.zeros((3, 3))  # 3x3 matrix of zeros

# Array with Random Numbers
random_array = np.random.rand(4)  # Array with 4 random numbers

# Filling an Array with Random Numbers
n = 20
x = np.zeros(n)
for i in range(n):
    x[i] = np.random.uniform(0, 10)
    

#Array example 
# Array of n values
n_values = np.array([10, 100, 1000])

# Define the approximation function
def approx(n):
    return n * 3  # Example approximation function

# Calculate approximations
approximations = []
for n in n_values:
    approximation = approx(n)
    approximations.append(approximation)

# Define a true value for pi for error calculation (use numpy's pi if applicable)
true = np.pi

# Calculate errors
errors = [abs(true - a)/abs(true) for a in approximations]

# Display the data in a table format
print("{:<10} {:<20} {:<10}".format('n Value', 'Approximation', 'Error')) #Header for table 
for n, approx_val, error in zip(n_values, approximations, errors): #Create a for loop with new names 
    print("{:<10} {:<20} {:<10}".format(n, approx_val, error))
