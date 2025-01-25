spam = 0
while spam < 5:
    print('Hello world')
    spam = spam + 1


name = ''
while name != 'Your name':
    print('Please type your name')
    name = input()
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is the password?')
    password = input()
    if password == 'fish':
        break
print('Access granted.')


while not name:
    print('Enter your name:')
    name = input()
print('How mane guests will you have?')
numofguests = int(input())
if numofguests:
    print ('Great!')
print('Done.')


print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


total = 0
for num in range(101):
    total = total + num
print(total)


for i in range(12, 16):
    print(i)

import random
for i in range(4):
    print(random.randint(1, 10))

spam = int(input('Enter a number: '))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')



number = 0
while number < 11:
    print(number)
    number = number + 1

number = 0
for i in range(11):
    print(i)