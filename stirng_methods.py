# String Methods 

# Write a program to convert a user input string to lowercase.

# s=input()
# print(s.lower())

# Accept a string and make it uppercase.

# s=input()
# print(s.upper())

# Convert a sentence into title case.

 # s="email is sunnny123@gmail.com"
# print(s.title())

# Capitalize only the first letter of a sentence.

# s="i am sunny"
# print(s.capitalize())

# Swap the case of all characters in a string.

# s='i am from InDia'
# print(s.swapcase())

# Check if a given string is all lowercase.

# s='i am Sunny'
# if s.islower():
#     print("all are lower case")


# Check if a string is all uppercase.

# s='i Am Sunny'
# if s.isupper():
#     print("all are uppercase")


# Verify if a string is in title case format.

# s='This Is Sunny'
# if s.istitle():
#     print("this is titlecase")


# Check if a string contains only alphabetic characters.

# s='my mail is sunny123@gmail.com'
# if s.isalpha():
#     print(s)

# Check if a string contains only digits.

# s='12345@'
# if s.isdigit():
#     print(s)

# Check if a string contains only alphanumeric characters.

# s='sunny123'
# if s.isdigit():
#     print(s)

# Check if a string has only whitespace characters.

# s=' hai python '
# if s.strip(' ',0,1):
#     print(s)

# Remove leading and trailing spaces from a user input string.

# s='I am Sunny '
# print(s.strip())

# Replace all spaces in a sentence with dashes.

# s='I am Learning Python Programming'
# print(s.replace(' ','_'))

# Split a sentence into words using spaces.

# s='I am Learning Python'
# print(s.split())

# Count how many times a specific word appears in a paragraph.

# s='A trailing space is defined as a space character at the end of a file or folder name'
# print(s.count('space',15))

# Find the first index of a word in a string.

# s='This is Sunny'
# print(s.index('This'))

# Find the last index of a substring in a string.

# s='I am from India'
# print(s.rindex('a'))

# Use find() to locate a word and check if it exists.

# s='I am Learning Python programming'

# if s.find('Python') != -1:
#     print("This word exists in sentence")
# else:
#     print("Not exists")


# Use startswith() and endswith() to validate email formatting

# s='sunny@gmail.com'
# if s.startswith('s') and s.endswith('m'):
#     print("validate email")
# else:
#     print("not validate")

# Format a string using variables (e.g., name and age).

# n='sunny'
# a='23'
# print(f'I am {n}. I am {a} years old')

# Join a list of strings into a sentence using " ".join().

# L=['sunny','python','learning']
# print("#".join(L))


# Write a program to reverse a string without using built-in reverse functions.

# s='sunny yadav'
# print(s[::-1])

# Check whether a string is a palindrome 

# s='level'
# if s==s[::-1]:
#     print('palindrome')
# else:
#     print('Not a palindrome')

# Write a program to count the number of vowels and consonants in a string.

# s='sunny@yadav'
# vowels=0
# conso=0
# for i in s:
#     if i in 'aeiouAEIOU':
#         vowels+=1
#     elif i.isalpha():
#         conso+=1
# print("vowels is ",vowels)
# print("consonants is ",conso)

# Take a string input and remove all duplicate characters.

# s = 'suuny yadav'
# res = ""
# for i in s:
#     if i not in res:
#         res += i
# print(res)

# Write a program that counts the frequency of each word in a paragraph.

# s='sunny yadav'
# for i in set(s):
#     print(i,s.count(i))

# Find the longest word in a given sentence.

# s = 'I am Learning Python'
# words = s.split()

# longest = ''
# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest word is:", longest)

# s = 'I am Learning Python'
# words = s.split()
# longest = max(words, key=len)
# print("Longest word is:", longest)


    
# Write a program to check if two strings are anagrams (same letters, different order).

# s='god'
# p='dog'
# if sorted(s)==sorted(p):
#     print('Anagrams')
# else:
#     print('not a anagrms')

# From a given input, count how many digits, alphabets, and special characters are present.

# s = 'sunny@yadav123'
# digits = 0
# alpha = 0
# special = 0
# for i in s:
#     if i.isalpha():
#         alpha+= 1
#     elif i.isdigit():
#         digits += 1
#     else:
#         special += 1

# print(alpha)
# print(digits)
# print(special)

# Strong Password Validator

# s = 'Sunnyy123@'

# has_lower = False
# has_upper = False
# has_digit = False
# has_special = False

# for char in s:
#     if char.islower():
#         has_lower = True
#     elif char.isupper():
#         has_upper = True
#     elif char.isdigit():
#         has_digit = True
#     elif not char.isalnum():
#         has_special = True

# if has_lower and has_upper and has_digit and has_special and len(s) >= 8:
#     print("Strong password")

# else:
#     print("Weak password")


# Remove All Punctuation

# s='I am learning python, programming.'
# print(s.replace('.','').replace(',',''))



















        


        
