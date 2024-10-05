"""
TECH2 mandatory assignment - Part A / AJS
"""
import numpy as np

from math import sqrt

# Part A1

def std_loops(x):
    # Create a function using for loops to find the standard deviation of a list x
   
    n = 0 # Create an empty value for N
    ts = 0 # Create an empty value for total sum
    tss = 0 # Create an empty value for total sum of squares

    #Find N, total sum (ts) and total sum of squares (tss) for list x
    for i in x:
        n += 1
        ts += i
        tss += i**2

    #Find the mean (m) and the mean of squares (ms)
    mean = ts/n
    meansquares = tss/n

    #Find variance s2 and standard deviation s
    s2 = meansquares - mean**2
    s = sqrt(s2)

    return s

num_lst = [1, 2, 3, 4, 5]
sd_loops = std_loops(num_lst)
print(f"Standard Deviation using loops: {sd_loops}")

# Part A2

def std_builtin(x):
  # Create a function using built in functions to find the standard deviation of a list x
    n = len(x) # Find the lenght (n()) of the list x
    ts = sum(x) # Find the total sum (ts) of the list x
    tss =  sum(i**2 for i in x) # Find the total sum of squares (tss) of the list x

    #Find the mean (m) and the mean of squares (ms)
    mean = ts/n
    meansquares = tss/n

    #Find variance (s2) and standard deviation (s)
    s2 = meansquares - mean**2
    s = sqrt(s2)

    #Function should return standard deviation s of list x
    return s

print(f"Standard Deviation using built in functions: {sd_loops}")

# Part A3
 
# Find the standard deviation of list x, using NumPy
s = np.std(num_lst)
print("Standard Deviation Using NumPy:", s)


