def hello(name):
    print('Hello, ' + name)

hello('Alice')

def num(num):
    return(num)

print('This is your number: ', num(1))


#function that returns the sum of two numbers, type casting the result to an integer
def add_numbers(num1, num2): 
    num1 = int(num1)
    num2 = int(num2)
    return(num1 + num2)
add_numbers(2, 2)
print('The sum is:', add_numbers(2, 2))

#function that returns the sum of two numbers, no type casting
def add_numbers(num1, num2): 
    return(num1 + num2)
add_numbers(2, 2)
print('The sum is:', add_numbers(2, 2))

#function that returns the sum of two numbers using Union
from typing import Union
def add_numbers(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]: 
    return(num1 + num2)
add_numbers(2.2, 2)
print(f'The sum is: {add_numbers(2.2, 2)}')


#function that checks if a number is even
def is_even(num):
   if num % 2 == 0:
       return True
   else:
       return False
print(is_even(10))

#function that checks if a number is odd
def is_odd(num):
   if num % 2 != 0:
       return True
   else:
       return False
print(is_odd(10))


"""function that concatenates two strings. It is not nessary to use Union here! 
Use Union when you want to specify that a parameter or return type can be one of several types"""
from typing import Union
def concatenate_string(string1: Union[str], string2: Union[str]) -> Union[str]: 
    return(string1 + string2)
concatenate_string('Hi', 'there')
print(concatenate_string('Hi ', 'there'))


#function that concatenates two strings using + operator
def concatenate_string(string1: str, string2: str) -> str:
    return string1 + string2
print(concatenate_string('Hi ', 'there'))


#function that concatenates two strings using f-string
def concatenate_string(string1: str, string2: str) -> str:
    return f'{string1} {string2}'
print(concatenate_string('Hi', 'there'))


