# ✅ Task - Fibonacci series and Factorial
# # 3. Factorial
# # n = 5
# # 5! -> 5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24

import math

n = int(input("Enter a number: "))
fact = 1    # factorial avribale will not be availbe so somewhere we have to store the value
# result = math.factorial(n)
# print(result)


# using for loop
#
# for i in range(1, n+1):     # n+1 isliye liya kyuki agar sirf n daalte to vo value 1 2 3 4 aise leta. agar n+1 dalege to 5 value lega vo chahiye
#     fact = fact * i
#
#
# print(fact)


###############
# i   F
# 1   1=1*1
# 2   2=2*1
# 3   6=3*2
# 4   24=4*6
# 5   120=5*24

#################

while n > 0:
    fact = fact * n
    n = n - 1
print(fact)
















