"""positional arguments: matched to the parameters in the order they are defined"""


def substract(a, b):
    return a - b


print(f"The result is {substract(10, 4)}")


# fuction with positional arguments that return the full name
def full_name(first_name, last_name):
    return first_name + last_name


print(full_name("Your ", "Name"))


# fuction with positional arguments that return rectangle perimeter
def perimeter(length, width):
    return 2 * (length + width)


# print(perimeter(2, 4))
print(f"The perimeter is: {perimeter(2, 4)}")


"""Keyword arguments: allow you to call a function by explicitly naming the parameters
and assigning them values in the function call. This makes the code more readable 
and allows us to pass arguments in any order."""


# function with keyword args:
def greeting(name, age):
    print(f"Hello {name}, you are {age} years old.")


greeting(name="Lily", age=32)


# function with keyword args2:
def book(title, author, genre):
    print(f"The {author} is the author of the {title}. The genre is {genre}.")


book('"1984"', "George Orwell", "Dystopia")


# function with keyword args3:
def car(brand, model, year, color):
    print(f"You have {brand} {model} from {year}. The color is {color}.")


car("Toyota", "Yaris", 2016, "Grey")


"""Arbitrary Arguments(*args) allow you to pass a variable number of positional arguments 
to a function. This is done by using *args in the function definition. 
The *args collects all extra arguments passed into a tuple. 
Great for scenarios where you don’t know in advance how many arguments will be passed."""


def greet(*names):
    for name in names:
        print(f"Hello {name}")


greet("Lily", "Someone")


# function that accepts any number of numbers and returns their sum
def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 4))


# function that accepts any number of numbers and returns max number
def max_number(*args):
    return max(args)


print(max_number(1, 100, 8))


# function that takes any number of arguments and prints each one on a new line
def print_all(*args):
    for arg in args:
        print(arg)


print_all("Book", "Car", "Cat", 10)


# print on the same line, using coma as separator
def print_all(*args):
    print(*args, sep=", ")


print_all("Book", "Car", "Cat", 10)


# function that takes any number of string arguments and returns a single concatenated string
def concat_strings(*args):
    return " ".join(args)  # Explore more about join!!


print(concat_strings("This", "is", "fun"))


"""Arbitrary Keyword Arguments (**kwargs) allows us to pass a variable number of
keyword arguments (i.e., named arguments) to a function. It collects all the extra keyword 
arguments into a dictionary where the keys are the parameter names and the values are the 
corresponding arguments"""


def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


info(name="Lily", age=32)


# function that handles defolt value
def greeting(**kwargs):
    name = kwargs.get("name", "Guest")  # Default to "Guest" if no name is provided
    print(f"Hello, {name}")


greeting(name="Lily")
greeting()


# function that calculates total price:
def total_price(**kwargs):
    total = 0
    for item, price in kwargs.items():
        total += price
    print(f"Your total is {total}.")


total_price(milk=2.5, apples=4.8, otherstuff=15.45)

d = {"t0": 34}

print(d.get("name", "guest"))


def get(**kwargs):
    print(kwargs["key"])


get(key="gttt")


names = [["bla", "dfdg"], ["fdgd", "gdgd"]]


def concat(f, l):
    print(f"{f} {l}")


for l in names:
    concat(l[0], l[1])
