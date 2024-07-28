#a lambda function is a small anonymous function , which can take any number of arguments but will have only one single expression

add10=lambda x: x+10

print(add10(5))#o/p:15

def add_func(x):
    print(x+10)

add_func(5)


#lambda for sorted operation

points2d=[(1,2),(15,1),(5,-1),(10,4)]
points2d_sorted=sorted(points2d)
print(points2d)
print(points2d_sorted)#it will the list with the x argument-> [(1, 2), (5, -1), (10, 4), (15, 1)]
#now if we want to sort that with the y argument
points2d_sorted=sorted(points2d,key=lambda x : x[1])
print(points2d_sorted)#o/p: [(5, -1), (15, 1), (1, 2), (10, 4)]



#sort the list by sum of each
a=[(1,2),(15,1),(5,-1),(10,4)]

b = sorted(a,key=lambda x: x[0]+x[1])
print(a) #[(1, 2), (15, 1), (5, -1), (10, 4)]
print(b) #[(1, 2), (5, -1), (10, 4), (15, 1)]


#map function -> this is a built-in function , where one function will be applied to all the elements of the iterable object passed to the map function

a=[1,2,3,4,5]#we want to every element to be multiplied by 2 
b=map(lambda x: x*2,a)

print(list(b))

#with list comprehension
c = [x*2 for x in a]
print(c)

#filter function -> it will only the output of the condition matches to be true 

a=[1,2,3,4,5]
b= filter(lambda x: x%2==0,a)#to get only the even numbers
print(list(b))

#with list comprehension
c=[x for x in a if x%2==0]
print(list(c))

#reduce function-> It also a function which takes one function and one sequence , the function will be applied to each elements and return a single value

from functools import reduce

a=[1,2,3,4]

b = reduce(lambda a ,b: a*b,a)
print((b))

