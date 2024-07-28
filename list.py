# # #ordered ,mutable , allows duplicate values

# # mylist=list(["banana","cherry","apple"])
# # # print(mylist)

# # # #accessing the elements , we can use index and it starts from 0

# # # print("First Element:" ,mylist[0])
# # # print("Second Element:",mylist[1])
# # # print("Third Element:" , mylist[2])
# # # #print("Fourth Element:" ,mylist[3])

# # # #accessing elements with negative index also , it starts from -1
# # # print("Last Element: ",mylist[-1])

# # #to iterate over the list
# # # for i in mylist:
# # #     print(i)
# # #If we need to check for any element whether it is present in the list or no
# # if "banana" in mylist:
# #     print('Yes')
# # else:
# #     print('No')
    
# # #To check the length of the list
# # length=len(mylist)
# # print("Length of the list is :",length)
# # #If I want to add one element

# # mylist.append("Lemon")
# # print(mylist)

# # #If i need to add element in a specific position
# # mylist.insert(3,"Orange")
# # print(mylist)

# # #I want to remove elements from list, and it will always remove the last element
# # mylist.pop()
# # print("After pop: ",mylist)

# # #now , If Need to remove one specific element
# # mylist.remove("Orange")
# # print(mylist)

# # #Reversing the list
# # mylist.reverse()
# # print(mylist)

# # #sorting the list
# # my_list=[7,10,-5,-90,78,80]
# # my_list.sort()
# # print("After sorting: ",my_list)
# # new_list=sorted(my_list)
# # print(new_list)


# mylist=[0]*5
# print(mylist)
# mylist2=[1,2,3,4,5,6,7,8,9]

# newlist=mylist+mylist2
# print(newlist)

# #slicing in the list
# a=mylist2[1:5]
# print(a)
# a=mylist2[:3]
# print(a)
# a=mylist2[::2]#steps to skip
# print(a)
# #to reverse a list
# print(mylist2[::-1]) #shortcut

#copying a list
# list_org=["banana","cherry","apple"]
# list_cp=list_org
# print(list_cp)
# list_cp.append("orange")
# print(list_org)
# #if we change in the copied variable it will reflect in the original one also
# #list_cp=list_org.copy() 
# #OR
# # list_cp=list(list_org)
# #OR
# list_cp=list_org[:]
# list_cp.append("Water")
# print("After slicing method in copy: ",list_cp)
# print("After slicing method in original: ",list_org)

#comprehensive in list
my_list=[1,2,3,4,5]
sq_list=[i*i for i in my_list]
print(sq_list)
