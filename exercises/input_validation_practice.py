# Working with PyInputPlus
import os
from pathlib import Path

import pyinputplus as pyip

# response = pyip.inputNum()
# response = pyip.inputNum("Enter your number: ", min=4)

# Blank input isn’t allowed unless the blank keyword argument is set to True:
# response = pyip.inputNum("Enter your number: ", blank=True)

# The limit, timeout, and default Keyword Arguments
# response = pyip.inputNum(limit=2)     #limit the num of attempts
# response = pyip.inputNum(timeout=10)  #how many seconds user has to enter valid input4
# response = pyip.inputNum(limit=2, default='N/A') #instead of raising an error, we can pass a default keyword (ie"N/A")
# print(response)

print(Path.cwd())
print(Path.home())
print(os.path.abspath("."))
