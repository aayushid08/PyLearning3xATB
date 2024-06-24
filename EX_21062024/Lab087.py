# tuple within tuple - or combining 2 tuple

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince", "W")

new_tuple = (hero1, hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[0][1]) # 2nd element of 1st tuple
print(new_tuple[1][1]) # 2nd element of 2nd tuple
print(len(new_tuple)) # 2
print(len(new_tuple[0])) # 2
print(len(new_tuple[1])) # 3
