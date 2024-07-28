# #dictionary is a collection data type , it is unlike tuple , it is mutable and unordered , It consists element as a key value pair

# #creation of a dictionary
# mydict={"Name":'Anirban','Age':28,'city':'vienna'}
# print(mydict)

# print(type(mydict))

# mydict1=dict(name='anirban',age=28,city='vienna')
# print(mydict1)

# #access
# value=mydict1['age']
# print(value)

# #changing value
# mydict1['email']='anirban@gmail.com'
# print(mydict1)

# #deleting items
# del mydict1['email']
# print(mydict1)

# mydict1.pop('age')
# print(mydict1)

# mydict1.popitem()# will delete the last element in the dictionary
# print(mydict1)

# #checking element
# if "Name" in mydict:
#     print("Yes")
    
# try :
#     print(mydict["abc"])
# except:
#     print('Error')
    
# #looping over dictionary
# for key in mydict.keys():
#     print(key)
# for value in mydict.values():
#     print(value)
    
# for key,value in mydict.items():
#     print(key,":",value)
    
# mydict_cp=mydict
# print(mydict)
# mydict['age']=30
# print(mydict)
# print(mydict_cp)#It wll change in the original dictionary also


# mydict_cp=mydict.copy()
# mydict_cp['age']=12
# print(mydict)
# print(mydict_cp)

#merge and update
mydict={"name":"anirban","age":28,"city":"Vienna"}
mydict2=dict(name='Ananya',age=27,city='giessen',email='ananya@gmail.com')

mydict.update(mydict2)
print(mydict)

#link with tuple

mytuple=(8,7)
mydict2={mytuple:15}
print(mydict2)