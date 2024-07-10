#printing a statement for 10 times
for i in range(10):
 print("Bright IT Career")



#printing numbers from 1 to 20 using a while loop
number = 1
while number <= 20:      
    print(number)
    number += 1   



#program to equal operator and not equal operators
a=50
b=60
print("a is equal to b", a == b)    
print("a is not equal to b", a != b) 



#checking odd and even numbers
num1=10
if num1%2==0:
   print("its an even number")
else:
   print("its an odd number")


#largest number among three numbers
f1 = 10
f2 = 20
f3 = 15
if f1 >= f2 and f1 >= f3:
    print(f"the largest number is {f1}")
elif f2 >= f1 and f2 >= f3:
    print(f"the largest number is {f2}")
else:
    print(f"the largest number is {f3}")



#program to print even numbers between 10 and 20 using while
n =10
while n <= 20:
    if n % 2 == 0:
        print(n)
    n += 1



#using do while to print 1 to 10 numbers
m = 1
while True:
    print(m)
    m += 1
    if m > 10:
        break



#program for armstorng number
def is_armstrong_number(num):
    original_num = number2
    num_digits = 0
    sum_of_powers = 0

    temp = number2
    while temp > 0:
        num_digits += 1
        temp //= 10

    temp = number2
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    return sum_of_powers == original_num
#checking
number2= 569
if is_armstrong_number(number2):
    print("it is an Armstrong number")
else:
    print("it is not an Armstrong number")





#prime or not
input_nummber= int(input("Enter a number: "))
if input_nummber<= 1:
    print("it is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(input_nummber ** 0.5) + 1):
        if input_nummber % i == 0:
            is_prime = False
            break

    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")



#palindrome or not
def is_palindrome(num):
    s = str(num)
    return s == s[::-1]
number = 12321
print(is_palindrome(number))  
number = 12345
print(is_palindrome(number))  




#check even or odd using switch
def check(num):
    switch = {
        0: "Even",
        1: "Odd"
    }
    return switch[num % 2]
def main():
    user_input = input("Enter a number to check if it is even or odd: ")
    
    try:
        number = int(user_input)
        result = check(number)
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()





def gender_check(input_char):
    switch = {
        'M': "Male",
        'F': "Female"
    }
    return switch.get(input_char.upper(), "Invalid input")

def main():
    user_input = input("Enter 'M' for Male or 'F' for Female: ")
    result = gender_check(user_input)
    print(result)

if __name__ == "__main__":
    main()