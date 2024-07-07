#explanation of arithmetic operations
def arithmetic_opera(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1/num2

    print(addition)
    print(subtraction)
    print(multiplication)
    print(division)
a= 10
b= 5
arithmetic_opera(a,b)




#explanation of increment and decrement
def increment_fun(value):
    value += 1
    print("incre the value", value)
    return value
def decrement_fun(value):
    value -= 1
    print("decre the value", value)
    return value
num = 10
num = increment_fun(num)  # output is 11
num = decrement_fun(num) # output is 10


#program to find equal or not
num1=int(input("enter first number"))
num2=int(input("enter second number"))
if num1==num2:
    print("it is equal")
else:
    print("it is not equal")



#relational operators
n1=3
n2=5
print("n1 equal to n2", n1 == n2)   #output is false 
print("n1 not equal to n2", n1 != n2)    #output is true
print("n1 is greater than n2", n1 > n2)  #output is false  
print("n1 is greater than n2", n1 < n2)   #output is true 
print("n1 is greater than or equal to n2", n1 >= n2)   #false
print("n1 is less than or equal to n2", n1 <= n2)  #true



#program for smaller and larger number
a1 = 50
a2= 60
if a1 > a2:
    print(f"the larger number is {a1}, and  the smaller number is {a2} ")
elif a1 < a2:
    print(f"the larger number is {a2}, and  the smaller number is {a1} ")
else:
    print("Both are equal")


