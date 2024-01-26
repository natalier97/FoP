
letters_dict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def count_letters (str):
    str = str.lower()
    for char in str:
        if char in alphabet:
            if char in letters_dict:
                letters_dict[char] += 1
            if char not in letters_dict:
                letters_dict[char] = 1
    return letters_dict

print(count_letters('natalie rivero561615632321'))