
# n = int(input("Enter the two digit number: "))
# result = n % 10
# print(result)

################################# for reverse numbers
# def last_digit(n):
#     return n % 10
#
# result = last_digit(1234)
#
# for result in range(result, 0, -1):
#     print(result,  end="")


###########################String reverse
# def last_char(s):
#     return s[-1]
#
#
# s = "Hello"
# result = last_char(s)
#
# for i in range(len(s) - 1, -1, -1):
#     print(s[i], end="")


###########################String reverse

s = str(input("Enter the string: "))

def last_char(s):
    return s[-1]

result = last_char(s)
# print(result)

for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")
