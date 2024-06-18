# ✅ #4. Fibonaci series
# # 0,0+1, 0+1+1,
# # n = 7
# # 0, 1, 2, 3, 5, 8, 13

# x = (n-1) + (n-2) + (n-3) + (n-4) .....

# x = (7-1) + (7-2) + (7-3) + (7-4) + (7-5) + (7-6) + (7-7)
# print(x)


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1nm
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Input: number of terms
n = int(input("Enter the number of terms: "))
fib_sequence = [fibonacci_recursive(i) for i in range(n)]
print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")