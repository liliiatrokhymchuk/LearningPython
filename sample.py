def printsmth(smth = 'this is defolt'):
    print(smth)


h = "hello"
w = "world"


def hi():
    print('hi')


def say_hi_n_times(times_to_say: int = 2):
    times_said = 0
    while times_said < times_to_say:
        hi()
        times_said = times_said + 1



def say_hi_forever():
    #while True:
    #while 1=1
    #while 100=100
    #while 1 < 100
    #while "hi" == "hi"
    while True:
        hi()


"""
;kjasdf;lkjasdf

;lkjasdf;lkjasdf
;kjlasd;lfkjasdf
;kljads;flkjsad
"""

"""
TODO -> WRite a function that prints "hi", N times, using a for loop
"""

def xyc(n:int):
    """This is a function that prints 'hi' N times using a for loop but not using the range(n) or range(0, n) function. Do not use range."""
    for i in range(n):
        h()


printsmth("hello")

say_hi_n_times(5)

#say_hi_forever()
