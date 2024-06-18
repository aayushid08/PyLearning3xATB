# NONE ka ex for revision
# with arg with ret

def f1(a, b, c):
    print(a, b, c)


result = f1(2, 3, 4)
print(result)  # None

# with arg without ret
def f2(a, b, c):
    return a + b + c


result2 = f2(2, 3, 4)
print(result2)  # 9