# #when an error occurs or exception as we call it , python will normally stop and generate an error message.
# try:
#     a=5/0
#     print(a)
# except ZeroDivisionError as e :
#     print(e)
    
# #file not found error
# try:
#     f=open('somefile.txt')
# except FileNotFoundError as e :
#     print(e)
    
#raising an exception
x =-5
# if x<0:
#     raise Exception ('x should be positive')
# if x<0:
#     #assert(x>=0)
#     assert(x>=0),'x has to be a positive number'
#handling exception
# try:
#     a=5/0
# except Exception as e :
#     print(e)
#we can add multiple except block with respect to one try block

# try:
#     a=5/1
#     b=a+'10'
# except ZeroDivisionError as e :
#     print(e)
# except TypeError as e :
#     print(e)
# else:
#     print('everything is good')
# finally :
#     print('cleaning up...')

#define our own exception- we can simply define our own error classes by sub classing from the base exception class

# class valueTooHighError(Exception):
#     pass

def test_value(x):
    if x <100:
        raise valueToosmallError('value is too small',x)

# try:
#     test_value(500)
# except valueTooHighError as e :
#     print(e)
class valueToosmallError(Exception):
    def __init__(self, message, value):
        self.message=message
        self.value=value
try:
    test_value(4)
except valueToosmallError as e :
    print(e.message,e.value)