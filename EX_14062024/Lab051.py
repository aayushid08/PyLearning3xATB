# Break -> based on the condition, it will come out of the loop

# pass -> do nothing, just pass the statement - skip the code

for i in range(10):   # 0-9  agar range (10) bhi likha to vo 0 se he lene wala hai. ya (0,10) tab bhi same
    print(i)

for i in range(10):
    if i == 5:
        pass
    else:
        print("pass 5: ", i)

