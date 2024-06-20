# ✅ #4. Fibonaci series
# # 0,0+1, 0+1+1,
# # n = 7
# # 0, 1, 2, 3, 5, 8, 13

# x = (n-1) + (n-2) + (n-3) + (n-4) .....

# x = (7-1) + (7-2) + (7-3) + (7-4) + (7-5) + (7-6) + (7-7)
# print(x)

fact = 1
n = int(input("Enter a number: "))

while n > 0:
    x = (n-1) + x