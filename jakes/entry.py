# Example of importing from other files in your program
from util import add_two_numbers, subtract_two_numbers # "go find these functions I want to use them"


def run_calculator():
    a = 1000
    b = 100

    result_from_addition = add_two_numbers("you ", "me")
    print(result_from_addition)
    more_addition = add_two_numbers(1, 10)
    print(more_addition)
    result_from_subtraction = subtract_two_numbers(a, b)
    print(result_from_subtraction)



if __name__ == '__main__':
    run_calculator()
    print(__name__)
