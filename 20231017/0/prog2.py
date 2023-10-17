import string
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = set(string.ascii_lowercase) - vowels
s = input()
print(len(set(s) & consonants), len(set(s) & vowels))
