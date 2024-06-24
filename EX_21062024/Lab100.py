# Type Conversions:

# Implicit Type  Conversion:-
# Python automatically converts one data  type to another data type. This is known as  Implicit Type Conversion.

# Explicit Type Conversion:-
# In this type conversion, the user has to do it manually. Here the user can convert the data type of a variable from one to another, depending on the requirement.


# Dictionary - Dictionary is unordered collection of key value pairs
# mutable

# Dict = {'a': 1, 'b': 2, 'c': 3}
# print(type(Dict.keys()))
# print(type(Dict.values()))

# eg: name -> "Ayushi"
# name -> key  // "Ayushi" -> value

dict = {'name': 'Ayushi',
        'age': 21,
        'marks': 90}

print(len(dict))    # 3
print(dict.keys())  #dict_keys(['name', 'age', 'marks'])
print(dict.values())    #dict_values(['Ayushi', 21, 90])
print(dict.items())     #dict_items([('name', 'Ayushi'), ('age', 21), ('marks', 90)])
print(dict.get('name')) # Ayushi
print(dict['name'])     # Ayushi
print(dict['marks'])    # 90
print(dict['age'])      #21


#change name:

dict['name'] = 'Anusha'
print(dict)      #{'name': 'Anusha', 'age': 21, 'marks': 90}
















