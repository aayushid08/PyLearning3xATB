letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u


def vowel_giver(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


# yaha vo ek letter vovel hai ya nahi bata raha hai

# result = vowel_giver('i')
# print(result)


# yaha vo ek list me kitne vovel hai ye bata raha hai

filtered_words = filter(vowel_giver, letters_list)
print(list(filtered_words))