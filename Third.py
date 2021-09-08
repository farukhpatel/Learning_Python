#list in python 
# list are used to store multiple values in single variable
# List items are ordered, changeable, and allow duplicate values.
# mylist = ["apple", "banana", "cherry","apple"] #allows dublicates vlues
# secondList=[1,2,3,4] 
# mylist[0]="apple updated version" #list are changeable   
# print(mylist[0])
# print(secondList)

# To add an item to the end of the list, use the append() method:
# secondList.append(5)
# print(secondList)  #append methode always added item at the end
# secondList.insert(1,'11')  #append item in specified index used insert methode instead of append methode
# print(secondList)

#remove del and pop in list
#remove
# mylist.remove("banana") #remove banana in the list
# print(mylist)
#pop
# mylist.pop(2) # 2 index value are poped in the list
#del
# print(mylist)
# del mylist[3]  # 3 index value are delete in the list
#del also used for completely delete the list
# del mylist
# print(mylist)
# listfirst=[1,2,3]
# del listfirst[1]
# listfirst.clear()
# print(listfirst)
thislist = ["apple", "banana", "cherry"]

#looping in list
for value in  thislist:
    print(value)
#length of the list
l=len(thislist)
print('lenghth', l)
for i in range(len(thislist)):
    print(i)