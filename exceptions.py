
def divide(numerator, denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError as e:
        print(e)
        print('You cant divide by zero. Use a non-zero demoninator')
    except ValueError as e:
        print('You entered strings. Enter only numbers.')
        print(e)
    except TypeError as e:
        print('You entered strings. Enter only numbers.')
        print(e)
    except Exception as e:
        print('Something went wrong.')
        print(e)
    else:
        print(result)


divide(10,0)
divide("you", "me")