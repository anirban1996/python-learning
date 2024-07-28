#The collection module implements special containers data type , and provide alternatives with some additional functionality compared to the general bert and containers

from collections import Counter#counter is a container that stores the element as dictionary key and their count as value
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a ='aaaaaabbcccddddddddddddd'
count=Counter(a)
print(count)#Counter({'a': 6, 'b': 6, 'c': 6, 'd': 5})

print(count.items())#o/p: dict_items([('a', 6), ('b', 6), ('c', 6), ('d', 5)])

print(count.keys())#o/p: dict_keys(['a', 'b', 'c', 'd'])
print(count.values())#o/p: dict_values([6, 6, 6, 5])

#to see most common element
print(count.most_common())#It will return an ordered list count wise, and position starts with 1
print(count.most_common(1)[0])#to get the first pair of key and values
print(count.most_common(1)[0][0])#to get the first element

print(count.elements())#o/p: <itertools.chain object at 0x0000023F0A0EB5E0>
print(list(count.elements()))#o/p: ['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']

#Namedtuple -> It is an easy to create and lightweight object type similar to a struct
point = namedtuple('point','x,y')
pt = point(3,2)
print(pt)
print(pt.x,pt.y)


#ordered Dict-> acts like a dictionary but in a ordered format

ordered_dict=OrderedDict()
ordered_dict['c']=1
ordered_dict['b']=2
ordered_dict['a']=3

print(ordered_dict)

#defaultdict -> It is similar to the usual dictionary container , it will have a default value if the key has not been set yet

d=defaultdict(float)
print(d)
d['a']=1
d['b']=2
print(d)
print(d['c'])


d=defaultdict(dict)
print(d['c'])

#deque -> double ended queue , it can be used to add or remove elements from both side of the queue
d= deque()
d.append(1)
d.append(2)
d.append(3)
print(d)

d.appendleft(3)#deque([3, 1, 2, 3])
print(d)

d.pop()
print(d)

d.popleft()
print(d)

#d.clear()
print(d)

d.extend([4,5,6])
print(d)

d.extendleft([1,2,3,4])#deque([4, 3, 2, 1, 1, 2, 4, 5, 6])
print(d)

d.rotate(-1)#this will rotate all the elements one place to the right and if passing -1 then will rotate to the left by one place 
print(d)