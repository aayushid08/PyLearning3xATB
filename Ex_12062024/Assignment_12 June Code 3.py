# ✅ Task - Fibonacci series and Factorial
# # 3. Factorial
# # n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24

fact = int(input("Enter a number: "))
for i in range(1, fact):
    fact = fact * i
print("Factorial is: ", fact)

########################################