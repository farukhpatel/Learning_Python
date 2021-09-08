# name="farukh"
# print(name[::-1])
# print(reverse(name))
# str=""
# for i in name:
#    str=i+str 
# print(str)
# print(reverse(str))

# Another way to reverse a string
# for i in range(len(name)):
#     print(len(name)-i-1)
#     str+=name[len(name)-i-1]
# print(str)

# for i in range(1,11):
#     if(i==1):
#         print("nei")
#     elif(i%2==0):
#         print("is notna  prime number ",i)
#     else:
#         print("is number ",i)

# prime number between 10 to 20

# for num in range(10,21):
#     if(num>1):
#         for i in range(2,num):
#             if(num%i==0):
#                 break #if break else not work
#         else:
#             print('prime number',num)

# for i in range(5):
#     print(i)
# i=0;
# i1=1
# print('i0',i ,'i1',i1)
# print(true)
# name=str("farukh")
# y = 15

# # print(x)
# print(bool(y))
# x = str("farukh")
# name=str(" ")
# surname="patel"
# x=0
# x+=3
# print(x)

# Python Identity Operators
#check tha data as well memory location
x = ["apple", "banana"]
y = ["apple", "banana"]
# we do here shallow copy
z = x  

# print(x is y) #here data or memory location are not same ans:- False
# print(x is z) #here data or memory location are same ans:- True
# print(z is x) #here data or memory location are same ans:- True

print(True*10+1)

# Python Membership Operators
# "in" and "not in"