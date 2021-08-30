name="farukh"
# print(name[::-1])
# print(reverse(name))
str=""
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

for num in range(10,21):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break #if break else not work
        else:
            print('prime number',num)
