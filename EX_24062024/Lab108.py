# Recursion : It's a programing technique where a function calls itself inorder to solve a problem.

# Recursion

# Key Concepts
# 1. Base Case
# 2. Recursive Case

# Factorial

def factorial(n):
    # Base Case:
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n - 1)

print(factorial(5))