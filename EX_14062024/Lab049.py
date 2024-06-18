# For Loop

# for counter in range(1, 100):      # 0 to 99
#     print("99 =", counter)
#
# for counter in range(1, 101):      # 0 to 100
#     print("100 =", counter)
#
# for counter in range(0, 101, 2):      # even
#     print("even", counter)
#
# for counter in range(1, 101, 3):      # odd
#     print("odd", counter)

for counter in range(1, 101):  # 0 to 100
    print(counter)
    if counter == 5:
        break
print("Outside of the program")


for counter in range(10, 0, -1):
    print(counter)

for counter in reversed(range(0, 10)):
    print(counter)
