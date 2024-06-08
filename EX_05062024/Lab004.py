print("Hello", "World", "One", end="        ")
print("Hello", "World", "Two")
# for end by default there will be new line. When you will run it like that only or with end="", output will be one below the other.
# if end="\t" \t is tab. It will give a tab between two hello worlds
print("Hello", "World", "One", sep="=", end="\t")
print("Hello", "World", "Two")

# sep="", end ="", file=None will always come at the end.
