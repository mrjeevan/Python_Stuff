# import time //time.sleep(100)
sec = 'python'
d = list(set(list(sec)))
trys = 0
trys = int(input('How many tries do u want to guess the word:'))
used = []
if trys < len(sec):
    print(f'''You won't be able to guess the word in {trys} Chances....''')
    trys = int(input('How many tries do u want to guess the word : '))
    if trys <len(sec):
        trys = len(sec)
flag = False
while (trys):
    for k in sec:
        if k not in used:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        print(' Awsome , You won The Game In Advance!')
        exit(0)
    print(f'{trys} Chances left .')
    c = input('\n guess a letter : ')
    if len(c) > 1 or len(c) == 0:
        print('No cheating!')
    else:
        if c[0] in sec:
            print(' Good ')
            used.append(c[0])
            for i in sec:
                if i in used:
                    print(i, end='.')
                else:
                    print('_', end='.')
        else:
            print(' Hmmmm , Nope ')
            for i in sec:
                if i in used:
                    print(i, end='.')
                else:
                    print('_', end='.')
    trys -= 1

for k in sec:
    if k not in used:
        flag = False
        break
    else:
        flag = True


if flag == True:
    print('Good , You Win!')
else:
    print('Sorry, Better luck Next Time.')
