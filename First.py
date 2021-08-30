print("Hello python");
# casting in python
name=str("Farukh Patel")
roll_number=int(23)
percantage=float(7.78)
print("name "+name)
a_a="Farukh"
A="Farukh Patel"
print(a_a)
print(A)
# Assign multiple values
x,y=10,20
p1="Python is "
p2="Awesome"
p=p1+p2
print(p)

# p3=786
# p4="Awesome"
# p5=p3+p4
# print(p5)  it gives error

# Global variable in python
global_variable="Global variable"
def myFirstFunc():
    global global_variable_in_function
    global_variable_in_function="global variable in function with the help of global keyword"
    print("Access global variable in function "+global_variable)
    function_variable="function_variable"
    print("funcion var "+function_variable)
myFirstFunc()
print("global_variable_in_function " +global_variable_in_function)
# print(function_variable) you can't access function variable outside the function

#check the type of a variable in python
a=10j
print(type(global_variable_in_function)) 
print(type(a))

# string in python
name="farukh"
print(name[2])
# name[2]="R" TypeError: 'str' object does not support item assignment
# print(name) 
# Looping in string
for x in name:
    print(x)

if("f" in name):
    print("f not present")
if("s" not in name):
    print("s not present")
# f a r u k h
# 1 2 3 4 5 6
# -6-5-4-3-2-1
# slicing in string in python
print(name[:len(name)]) #slice from the start
print(name[2:])  #slice from the 2 to end
print('- '+name[-6:-4])  #last index not included in slicing
name="farukh"
name2=name.split(" ")
print(name2)
# name2[0]="shahrukh"
# print(name2)

# conccatenate a string
firstName="farukh"
lastName="patel"
fullName=firstName + " " +lastName
print(fullName)

# insert dynamic value in string
about="my name is {}"
print(about)
about2=about.format(fullName)
print(about)
print(about2)

print(fullName.find('z'))  #not found -1 found give index