#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:56:27 2023

@author: eiriniretsou
"""

# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                # y as the sine of x

# Example 1: Simple Line Plot
plt.figure()                 # Create a new figure
plt.plot(x, y)               # Plot y vs. x
plt.title("Simple Line Plot")# Adding a title
plt.xlabel("x-axis")         # X-axis label
plt.ylabel("y-axis")         # Y-axis label
plt.show()                   # Display the plot

# Example 2: Scatter Plot
plt.figure()                 # Create another new figure
plt.scatter(x, y)            # Scatter plot of y vs. x
plt.title("Scatter Plot")    # Adding a title
plt.xlabel("x-axis")         # X-axis label
plt.ylabel("y-axis")         # Y-axis label
plt.show()                   # Display the plot

plt.plot(x[0, 300], y)
plt.title("new")
plt.show()

# Example data 3: Two y values for same graph 
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y1 = np.sin(x)               # y1 as the sine of x
y2 = np.cos(x)               # y2 as the cosine of x

# Create a new figure
plt.figure()

# Plot y1 vs. x with a blue line
plt.plot(x, y1, label='sin(x)', color='blue')

# Plot y2 vs. x with a red line
plt.plot(x, y2, label='cos(x)', color='red')

# Adding a title
plt.title("Line Plot with Multiple Datasets")

# Adding labels
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Adding a legend to differentiate datasets
plt.legend()

# Display the plot
plt.show()