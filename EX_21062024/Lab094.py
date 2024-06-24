set1 = set(['Ayushi', 'for', 'Ayushi..'])
print(len(set1))     # 3

for i in set1:
    print(i)

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(len(set1))     # 10
set1.remove(5)
print(set1)         # {1, 2, 3, 4, 6, 7, 8, 9, 10}
print(len(set1))

set1.add(10)
print(set1)         # {1, 2, 3, 4, 6, 7, 8, 9, 10}

# pop - remove a random element from the set. lets say 1st element. like push and pop
set1.pop()   # 1
print(set1)         # {2, 3, 4, 6, 7, 8, 9, 10}

