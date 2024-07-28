#tuple is a collection data type that is ordered and immutable , 
#Difference between tuple and list is tuple element cannot changed once created
#It also allows duplicate elements like list

mytuple=("Max",28,"Boston")
print(mytuple)

print(type(mytuple))

#ways of defining tuple
my_tuple="max",28,"boston"
print(my_tuple)

my_l_tuple=tuple(["Max",28,"Boston"])
print(my_l_tuple)

#access elements from a tuple 
item=my_tuple[0]
item_last=my_tuple[-1]
print(item)#op:max
print(item_last)

#if we want to change element of tuple
# my_tuple[0]="Tim"
# print(my_tuple)

#iterating over one tuple
for i in my_tuple:
    print(i)
    
#checking element in tuple
if "max" in my_tuple:
    print("Yes")
else:
    print("No")
    
mytuple=['a','p','p','l','e']
print(len(mytuple))

#occurrence of any elements in a tuple
print(mytuple.count('p'))
print(mytuple.count('o'))

#first occurrence of elements
print(mytuple.index('p'))

#print(mytuple.index('o'))

#we can make list out of tuple
# mytuple=('a','p','p','l','e')
# mylist=list(mytuple)
# print(mylist)
# mytuple2=tuple(mylist)
# print(mytuple2)


mytuple=("Max",28,"Boston")
name,age,city=mytuple
print("My Name is",name,"My age is",age,"and"" I live in",city)

