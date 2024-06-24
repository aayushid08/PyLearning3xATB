pramod_details = {
    "name": "pramod",
    "age": 21,
    "hobbies": ["reading", "coding", "traveling"],
    "favorite_color": "green"
}

print(pramod_details["hobbies"])
print(pramod_details.get("hobbies"))
print(pramod_details.keys())
print(pramod_details.values())
print(len(pramod_details))


# values can be duplicate - keys should be unique
mydict = {'a': 11,  'b': 24, 'c': 366,  'd': 45, 'e': 55}
print(mydict)
print(len(mydict))
print(list(mydict.keys()))
print(list(mydict.values()))
# for one by one
for i in mydict:
    print(i)
##################
for i in mydict:
    print(i, mydict[i])
####################
for k, v in mydict.items():
    print(k, v)
