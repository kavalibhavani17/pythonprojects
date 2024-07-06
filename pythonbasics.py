#this is single line comment
print("i'm kavali bhavani")

"""these are the data types of the python
.............................................................................
the multi comment is done like this
"""
integer_variable = 10
boolean_variable= True
char_variable= 'A'  
float_variable = 10.5
double_variable= 20.123456789 

print("the number is", integer_variable)
print("the boolean is", boolean_variable)
print("the character is", char_variable)
print("the float is", float_variable)
print("the double is", double_variable)


#scope of variables explanation

name = "bhavani" # global variable
def func_names():
    name = "kavali" # local variable
    print("my name is:", name)

func_names()

# global variable will be printed due to scope of the vaiable is global
print("my full name is:", name)