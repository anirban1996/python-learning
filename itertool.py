from itertools import product #will return a cartesian product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count,cycle,repeat

# a=[1,2]
# b=[3,4]
# prod=product(a,b)
# print(prod)#o/p: <itertools.product object at 0x000001C15786EA00>
# print(list(prod))
# prod=product(a,b,repeat=2)
# print(list(prod))

# a=[1,2,3]
# perm=permutations(a,2)
# print(list(perm))

# comb=combinations(a,2)#need to specify the repeat
# print(list(comb))#numbers are not combining self , so to self combination

# comb_wr=combinations_with_replacement(a,2)
# print(list(comb_wr))

# acc=accumulate(a)
# print(a)
# print(list(acc))
# #to multiply
# import operator

# acc=accumulate(a,func=operator.mul)
# print(a)
# print(acc)
# a=[1,2,5,3,4]
# #for max replacement
# acc=accumulate(a,func=max)
# print(a)
# print(list(acc))

def smaller_than_4(x):
    return x<4

a=[1,2,3,4]
#group_obj=groupby(a,key=smaller_than_4)#replace this with lambda function

group_obj=groupby(a,key=lambda x: x<4)
for key,value in group_obj:
    print(key,list(value))
    
    
persons=[{'name':'anirban','age':28},{'name':'akash','age':26},{'name':'abir','age':27}]
group_obj=groupby(persons,key=lambda x: x['age'])
for key,value in group_obj:
    print(key,list(value))
    

for i in count(10):
    print(i)
    if i ==15:
        break
a=[1,2,3]    
for i in cycle(a):
    print(i)
    if i==2:
        break

for i in repeat(1,4):
    print(i)