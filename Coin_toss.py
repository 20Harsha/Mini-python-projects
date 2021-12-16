#It is a simple virtual coin toss program
#Randomly it generates heads or tails for the user
import random
user = input('Hello, Enter your name : ')
userchoose = int(input('Choose 0 for heads and 1 for tails : '))
r1 = random.randint(0,1)
if r1 == 0:
    a = 0 # for heads
    s ='head'
else:
    a = 1 # for tails
    s = 'tail'
if a == userchoose:
    print(f'It\'s a {s}')
    print(f'{user} you won')
else:
    print(f'It\'s a {s}')
    print(f'{user} Oops your opponent won')

