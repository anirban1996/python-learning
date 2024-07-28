# #string is an ordered and immutable collection data type that is used for text representation.
# my_string="Hello World"
# print(my_string)

# #slicing
# substring=my_string[1:5]
# print(substring)#ello

# my_string1="    Hello World   "
# print(my_string1)
# print(len(my_string1))
# separated_string=my_string1.strip()
# print(len(separated_string))
# print(separated_string)

# #startswith and endswith
# print(my_string.startswith("Hello"))#True
# print(my_string.endswith("world"))#False

# #Finding element in a string
# print(my_string.find("H"))#will return the position of the word and if the case is for string then the position of first word in that string will get return
# print(my_string.find("World"))#o/p:6
# print(my_string.find("abcd"))#if the word or string is not there in the string then it will return -1

# #count of characters
# print(my_string.count('o'))#2

# #replace
# print(my_string.replace("World","Universe"))#it will replace the world with universe

#string to list
# my_string="how are you doing"
# my_list=my_string.split()
# print(my_list)#['how', 'are', 'you', 'doing']

# #to string
# new_string=' '.join(my_list)
# print(new_string)#o/p: how are you doing


# my_list=['a']*6
# print(my_list)

# my_string_new=' '

# for i in my_list:
#     my_string_new+=i
# print(my_string_new)
# print(type(my_string_new))

# my_string=" ".join(my_list)
# print(my_string)

#Format method for string
var="Tom"
my_string ='the variable is %s'%var #o/p: the variable is Tom
print(my_string)

value=5.5
my_string='the variable is %.2f'%value
print(my_string)

value='3.123456'
my_string="the value of pi is {}".format(value)
print(my_string)

#f string
my_string=f'the value is {var} and {value}'
print(my_string)