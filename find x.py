from random import randint
import os
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
n = int(input(' Enter number of rows : '))
m = int(input(' Enter number of rows : '))
board_size = [n,m] # [row, col]
x_required = int(input("How many x's can u find : "))
times = 0


def x_s(board_size, n):
    x_all = []
    
    # inf loop if n > size of board 
    if n > board_size[0]*board_size[1]:
        n = board_size[0]*board_size[1]

    while (n > 0):
        a = randint(1,board_size[0])  # row
        b = randint(0,board_size[1]-1)  # col
        x_proposed = f'{chr(65+b)}{a}'
        
        if x_proposed not in x_all:
            x_all.append(x_proposed)
            n = n-1
    return x_all


x_hidden = x_s(board_size,x_required)
x_found = []
status = 0

# 65 : 90 :: 'A' : 'Z'
# chr(65) # will print "A"

def hr():
    print('-'*board_size[1]*5)


def display_board(board_size, x_found):
    col = [chr(x) for x in range(65, 65+board_size[1])]
    row = [x for x in range(1, board_size[0]+1)]
    hr()
    print('   ',end=' ')
    for col_name in col:
        print(col_name, end='   ')
    print('\n')

    for r in row:
        print(r, end='   ')
        for x in range(board_size[1]):
            cordinate = f'{chr(65+x)}{r}'
            if cordinate in x_found:
                print('X', end='   ')
            else:
                print('o', end='   ')
        print('\n')
    hr()

# placing x's
# find a row agn inside row find a col


def stats():
    status_message = ['In Proress' , 'Completed']
    print(f'Board size : {board_size[0]} X {board_size[1]}')
    print(f"X's found : {len(x_found)} out of {len(x_hidden)} ")
    print(f'Guessed {times} times')
    print(f'Game status : {status_message[status]}')


clear()
print(f'We have a board of size {board_size[0]} X {board_size[1]} \n and {len(x_hidden)} hidden "x" \n you have to guess all of them \n\n Example "Guess : A1" \n\n All the best !')
_ = input('Press any key to Continue....')


while len(x_found) != len(x_hidden):
    clear()
    stats()
    display_board(board_size, x_found)
    print(f'debug :{x_hidden}')
    hr()
    guess = input(r'Guess : ')
    times +=1
    if guess in x_hidden and guess not in x_found:
        x_found.append(guess)
        
        
if len(x_found) == len(x_hidden):
    clear()
    status = 1
    stats()
    display_board(board_size, x_found)
    print(' You Won ! :) \n')
