#Set is a collection data type that is unordered and mutable unlike tuple . but it does not allow duplicate value

# myset={1,2,3}
# print(type(myset))

# #if we define a black set then the data type of that will be dict as it is defined with curly braces like dictionary
# myset={}
# print(type(myset))#<class 'dict'>

# myset={1,2,2,2,2,3,3,3,33,4,4,4,4,4,4,}
# print(myset)

# myset=set("Hello")
# print(myset)#{'l', 'e', 'o', 'H'} as unordered

#adding element in a set

myset=set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4) 
myset.add(5)
print(myset)

#removing elements from a set
myset.remove(4)
print(myset)

#outside the set of values
#myset.remove(6)
#print(myset)#KeyError: 6

myset.discard(6)
print(myset)#no error message

#clearing one set 
# myset.clear()
# print(myset)

#poop method

myset.pop()
print(myset)#randomly remove elements from a set

#iterate over a set
for i in myset:
    print(i)
    
#checking element in a set
if 5 in myset:
    print("No")#o/p: Yes
if 4 in myset:
    print("Yes")#No output
    
#union and intersection
odds={1,3,5,7,9}
evens={2,4,6,8}
primes={2,3,5,7}

union=odds.union(evens)#combine element from two sets of numbers without duplication
print(union)

intersection=odds.intersection(evens)#Will take out all the common / or which are present in both the sets
print(intersection)#returns nothing 

intersection1=odds.intersection(primes)
print(intersection1)#will return odd primes numbers

#difference of two sets
#this will return a set that are not present in the second set

setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}

diff=setA.difference(setB)
print(diff)#{4, 5, 6, 7, 8, 9}
diff=setB.difference(setA)
print(diff)#{10,11,12}

#symmetric difference

diff=setA.symmetric_difference(setB)
print(diff)#will return a set with all the elements from setA and setB but not which are present in both the sets
#o/p:{4, 5, 6, 7, 8, 9, 10, 11, 12}

#-> These operations will not change the original object it will always return a new set object
#if we want to change our set in place , then we need to use below functions
#setA.update(setB)
print(setA)#it will combine all the elements 

#keep the elements which are found in both the sets
#setA.intersection_update(setB)
print(setA)#{1,2,3}

#difference update
#setA.difference_update(setB)#it updates the set by removing elements found in another set
print(setA)

#symmetric difference update
setA.symmetric_difference_update(setB)##will return a set with all the elements from setA and setB but not which are present in both the sets
print(setA)

#subset & superset
setA={1,2,3,4,5,6}
setB={1,2,3}

print(setA.issubset(setB))
print(setA.issuperset(setB))

#disjoint -> will return false if both sets have same elements
print(setA.isdisjoint(setB))
setC={7,8}
print(setA.isdisjoint(setC))

#for copy it is same as list if we change in the copied version the change will reflect in original also
setB=setA.copy()#actual Copy
#or
setB=set(setA)

#frozen set
A=frozenset([1,2,3,4,5])#immutable set
print(A)#frozenset({1, 2, 3, 4, 5})
A.add(1)#AttributeError: 'frozenset' object has no attribute 'add'
print(A)