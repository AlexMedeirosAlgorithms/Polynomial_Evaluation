### CSC6013 - Coding Project 05 - Part 3
### Copyright Alexander Medeiros 11/27/2023
"""
This program is designed to evaluate a polynomial function. 

You provide the 'evaluate(A,x)' method an array of constants 'A', and the value of the variable 'x'

The program computes the power of the polynomial using the position of the constant associated to in within the array

A for loop is then run for each item in the array, the value of the polynomial is computed and added to a variable 'sum' which calculates the total sum of the function.

The asymptotic analysis is printed for the user at the end. 

Usage example:
    evaluate(A,x)

    # 3) Polynomial evaluation
    # A polynomial can be represented as an array in which the coefficient of the k’th power of the
    # variable is stored in array entry A[k]. For example, the array whose values are:

    # k 0 1 2 3 4 5 6
    # A[k] 12.3 40.7 -9.1 7.7 6.4 0 8.9

    # would represent the polynomial
    # 𝑓(𝑥) = 12.3 + 40.7𝑥 − 9.1𝑥** 2 + 7.7𝑥** 3 + 6.4𝑥** 4 + 8.9𝑥** 6.

    # To evaluate this function at x = 5.4 we would “plug in” 5.4 for each occurrence of the variable x
    # and perform the indicated arithmetic.

    # a) Calculating the p’th power of a real number
    # Write a Python function
    # power (x, p)
    # to calculate the value of 𝑥**𝑝 for any real number x and any non-negative integer p.
    # The brute-force function should use a for loop to repeatedly multiply the value of x.
    # Do not use Python’s exponentiation operator ** to evaluate x**p.

    # b) Evaluating a polynomial
    # Write a Python function
    # evaluate (A, x)
    # that determines the value of f(x) for the polynomial that is represented by the corresponding
    # array A of coefficients. For each term of the polynomial, this function should make a call to the
    # power() function that you wrote in part3a.

    # c) Run your code to evaluate the polynomial
    # 𝑓(𝑥) = 12.3 + 40.7𝑥 − 9.1𝑥** 2 + 7.7𝑥** 3 + 6.4𝑥** 4 + 8.9𝑥** 6.
    # at x = 5.4

    # d) Asymptotic analysis
    # Determine the maximum number of multiplications that are needed for any polynomial of degree
    # n (not just for this instance with a polynomial of degree 6). For your initial work, you can
    # identify a sum of terms. Be sure to include the work (number of multiplications) performed on
    # each call to the power() function. For your final answer, give a simple expression in terms of a
    # power of n (there should be no terms involving p and no summations Σ). What is the Big-Oh
    # class for this algorithm?
"""

# array 'A' of polynomial terms 
A = [12.3,40.7,-9.1,7.7,6.4,0,8.9]
# value of variable 'x'
x = 5.4

# a) Calculating the p’th power of a real number

# method to compute the power of a variable 'x', arguments are 'x' value and exponent 'p'
def power(x,p):
    
    f = 1 # initialize variable 'f'
    for i in range(p): # loop for i in range of exponent 'p'

        f = f*x # multiply 'f' times 'x' for each item in range 'p' to provide the equivalent of an exponent

    return f # return the value of 'f'

# b) Evaluating a polynomial
# method to evaluate a polynomial of order n
def evaluate(A,x):
    powers = [] # initialize an empty array 'powers' to store the calculated powers

    for index in range(len(A)): # for each index in range of array length
        powers.append(power(x,index))  # append the powers list with the power using the 'x' value and the index value from the given array
    #print(powers) # for development purposes, displays the calculated list of powers 

    sum = 0 # initialize a sum variable
    for index in range(len(A)): # for each index in the length of the array, 
        sum+=A[index-1]*powers[index-1] # compute the sum of the terms in the array using the given terms and calculated powers

    return sum # print the final sum value
   
# c) Run your code to evaluate the polynomial

print(f' f({x}) = {evaluate(A,x)}') # evaluate the polynomial function given the terms and the 'x' variable value

# d) Asymptotic analysis:

# display the asymptotic analysis for this method
print('The terms in the summation are, x**n, x**n-1, .... , x**1, x**0')

print('The total number of multiplications is therefore; M = n + (n-1) + .... + 1 + 0')

print('Which can be simplified to M = (n*(n+1))//2')

print('The complexity of M is therefore O(n**2)')