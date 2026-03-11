# more than 100

# a=int(input())
# if a>100:
#     print(a)

# even number of character

# a=input()
# L=len(a)
# if L%2==0:
#     print(a)

# if given str having one 'a' character

# a=input()
# c=a.count('a')
# if c==1:
#     print(a)

# positive,negative,zero

# a=int(input())
# if a>0:
#     print('positive')
# elif a<0:
#     print('negative')
# else:
#     print('zero')

# # Even,odd

# a=int(input())
# if a%2==0:
#     print('even')
# else:
#     print('odd')

# # check voter 

# a=int(input())
# if a>=18:
#     print('eligible for voting')
# else:
#     print('Not eligible for voting')


# # compare two numbers

# a=int(input())
# b=int(input())
# if a>b:
#     print('a is greater')
# elif b>a:
#     print('b is greater')
# else:
#     print('both are equal')

# # leap year

# a=int(input())
# if (a%4==0 and a%100!=0) or (a%400==0):
#     print('leap year')
# else:
#     print('not a leap year')

# # multiple of 5

# a=int(input())
# if a%5==0:
#     print('divisible 5')
# else:
#     print('not divisible')

# # grade calculator

# a=int(input())
# if a>=90 and a<=100:
#     print(' A grade')
# elif a>=80 and a<90:
#     print('B grade')
# elif a>=70 and a<80;
#     print('c grade')
# else:
#     print('Fail')

# # vowel or consonent

# a=input()
# if a in'AEIOUaeiou':
#     print('vowel')
# else:
#     print('consonant')

# # 3 number max finder

# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print('a is max')
# elif b>c:
#     print('b is max')
# else:
#     print('c is max')

# # number range checker (1-100)

# a=int(input())
# if 1<=a<=100:
#     print('range 1-100')
# else:
#     print('out of range')

# built in  methods of string 

# anagrams checker

# a=input().lower().replace(" ","")
# b=input().lower().replace(" ","")

# if sorted(a)==sorted(b):
#     print('a b are anagrams')
# else:
#     print('a b are not anagrams')

# count consonents,vowels,digits,spaces

# text=input()
# vowels_c=consonents_c=digits_c=spaces_c=0

# for i in text:
#     if i.isalpha():
#         if i in 'AEIOUaeiou':
#             vowels_c+=1
#         else:
#             consonents_c+=1
#     elif i.isdigit():
#         digits_c+=1
#     elif i.isspace():
#         spaces_c+=1

# print('vowels ',vowels_c)
# print('consonents ',consonents_c)
# print('digits ',digits_c)
# print('spaces ',spaces_c)

# censor bad words

# a=input()
# L=['bad','stupid']

# for word in L:
#     a=a.replace(word,"*"*len(word)-1)
# print(a)

# built in  methods of list

# Find Duplicates
# Ask for a list of numbers and print only the duplicates using .count().

# L=[10,20,30,40,20,30]
# p=set()
# for i in L:
#     if L.count(i)>1 and i not in p:
#         print(i)
#         p.add(i) # set method 
# Remove All Odd Numbers
# Input a list of numbers. Use a loop to remove all odd numbers using .remove().

# L=[11,22,33,44,55]
# for i in L:
#     if i%2==1:
#         L.remove(i)
# print(L)

# Sort and Reverse
# Ask for a list of words. Sort alphabetically, then reverse the order using .sort() and .reverse().

# L=['apple','zebra','king','mango','banana','rat']

# L.sort()
# print(L)
# L.sort(reverse=True)
# print(L)



# s=input()

# for i in s:
#     if i.isdigit() and int(i)%2==0:
#         print(i)

    
# s=input()
# c=0
# for i in s:
#     if i.isalnum()==False:
#         c+=1
# print(c)

# set and count method

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

# chess number based that output was black or white

# s=input()
# col=(ord -ord(s[0]))+1
# row=s[1]
# if (row+col)%2==0:
#     print("black")
# else:
#     print("white")

# def isEven(num):
#   return not num&1

# if __name__ == "__main__":
#   num = 13
#   if isEven(num):
#     print('Even')
#   else:
#     print('Odd')


s={"name":"suneel","age":24,"name":"sai"}
print(s["name"])














    
























    


