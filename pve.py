import time
from random import shuffle

mapa = ['', '', '', '', '', '', '', '', '']


def visual():
    print('\n\n\n\n\n\n\n----------------')
    print('| ', mapa[0], ' | ', mapa[1], ' | ', mapa[2], ' |')
    print('----------------')
    print('| ', mapa[3], ' | ', mapa[4], ' | ', mapa[5], ' |')
    print('----------------')
    print('| ', mapa[6], ' | ', mapa[7], ' | ', mapa[8], ' |')
    print('----------------')
    return


def Dcross():
    for i in range(0, 2):
        if i == 0:
            znak = 'O'
        else:
            znak = 'X'

        if mapa[0] == znak and mapa[4] == znak and mapa[8] == '':
            return 8
        if mapa[0] == znak and mapa[4] == '' and mapa[8] == znak:
            return 4
        if mapa[0] == '' and mapa[4] == znak and mapa[8] == znak:
            return 0
        if mapa[2] == '' and mapa[4] == znak and mapa[6] == znak:
            return 2
        if mapa[2] == znak and mapa[4] == znak and mapa[6] == '':
            return 6
        if mapa[2] == znak and mapa[4] == '' and mapa[6] == znak:
            return 4
    return 9


def Drow():
    for i in range(0, 2):
        if i == 0:
            znak = 'O'
        else:
            znak = 'X'

        if mapa[0] == znak and mapa[1] == znak and mapa[2] == '':
            return 2
        if mapa[0] == znak and mapa[1] == '' and mapa[2] == znak:
            return 1
        if mapa[0] == '' and mapa[1] == znak and mapa[2] == znak:
            return 0
        if mapa[3] == '' and mapa[4] == znak and mapa[5] == znak:
            return 3
        if mapa[3] == znak and mapa[4] == znak and mapa[5] == '':
            return 5
        if mapa[3] == znak and mapa[4] == '' and mapa[5] == znak:
            return 4
        if mapa[6] == '' and mapa[7] == znak and mapa[8] == znak:
            return 6
        if mapa[6] == znak and mapa[7] == znak and mapa[8] == '':
            return 8
        if mapa[6] == znak and mapa[7] == '' and mapa[8] == znak:
            return 7
    return 9


def Dcolumn():
    for i in range(0, 2):
        if i == 0:
            znak = 'O'
        else:
            znak = 'X'

        if mapa[0] == znak and mapa[3] == znak and mapa[6] == '':
            return 6
        if mapa[0] == znak and mapa[3] == '' and mapa[6] == znak:
            return 3
        if mapa[0] == '' and mapa[3] == znak and mapa[6] == znak:
            return 0
        if mapa[1] == '' and mapa[4] == znak and mapa[7] == znak:
            return 1
        if mapa[1] == znak and mapa[4] == znak and mapa[7] == '':
            return 7
        if mapa[1] == znak and mapa[4] == '' and mapa[7] == znak:
            return 4
        if mapa[2] == '' and mapa[5] == znak and mapa[8] == znak:
            return 2
        if mapa[2] == znak and mapa[5] == znak and mapa[8] == '':
            return 8
        if mapa[2] == znak and mapa[5] == '' and mapa[8] == znak:
            return 5
    return 9


def interweniuj():
    if Dcross() != 9:
        wynik = Dcross()
    elif Drow() != 9:
        wynik = Drow()
    elif Dcolumn() != 9:
        wynik = Dcolumn()
    elif (mapa[0] == 'X' and mapa[8] == 'X' and (mapa[2] == '' or mapa[6] == '')) or (mapa[2] == 'X' and mapa[6] == 'X' and (mapa[2] == '' or mapa[6] == '')):
        wynik = 9
        random = [1, 3, 5, 7]
        shuffle(random)
        while len(random) > 0:
            tmp = random.pop()
            if mapa[tmp] == '':
                wynik = tmp
                break
    else:
        wynik = 9
    return wynik


def podbijaj():
    if mapa[0] == 'O':
        if mapa[2] == '':
            mapa[2] = 'O'
        elif mapa[6] == '':
            mapa[6] = 'O'
        else:
            pass
    elif mapa[8] == 'O':
        if mapa[2] == '':
            mapa[2] = 'O'
        elif mapa[6] == '':
            mapa[6] = 'O'
        else:
            pass
    elif mapa[2] == 'O':
        if mapa[0] == '':
            mapa[0] = 'O'
        elif mapa[8] == '':
            mapa[8] = 'O'
        else:
            pass
    elif mapa[6] == 'O':
        if mapa[0] == '':
            mapa[0] = 'O'
        elif mapa[8] == '':
            mapa[8] = 'O'
        else:
            pass
    else:
        for i in range(8):
            if mapa[i] == '':
                mapa[i] = 'O'
                break


def strzel():
    if mapa[4] == '':
        mapa[4] = 'O'
    elif interweniuj() != 9:
        mapa[interweniuj()] = 'O'
    elif mapa[0] == 'O' or mapa[2] == 'O' or mapa[6] == 'O' or mapa[8] == 'O':
        podbijaj()
    else:
        random = [0, 2, 6, 8]
        shuffle(random)
        while len(random) > 0:
            tmp = random.pop()
            if mapa[tmp] == '':
                mapa[tmp] = 'O'
                break


def czyWygrana():
    gra = False
    for i in range(8):
        if mapa[i] != '':
            gra = True
    if mapa[0] == mapa[1] == mapa[2] != '':
        print('Wygrały: ', mapa[1])
        gra = False
    if mapa[3] == mapa[4] == mapa[5] != '':
        print('Wygrały: ', mapa[5])
        gra = False
    if mapa[6] == mapa[7] == mapa[8] != '':
        print('Wygrały: ', mapa[8])
        gra = False
    if mapa[0] == mapa[3] == mapa[6] != '':
        print('Wygrały: ', mapa[3])
        gra = False
    if mapa[1] == mapa[4] == mapa[7] != '':
        print('Wygrały: ', mapa[1])
        gra = False
    if mapa[2] == mapa[5] == mapa[8] != '':
        print('Wygrały: ', mapa[5])
        gra = False
    if mapa[0] == mapa[4] == mapa[8] != '':
        print('Wygrały: ', mapa[4])
        gra = False
    if mapa[2] == mapa[4] == mapa[6] != '':
        print('Wygrały: ', mapa[4])
        gra = False
    return gra


gra = True
while gra:
    pole = input('Wybierz pole 1-9 (0 kończy grę)\n')
    try:
        pole = int(pole)
        if pole == 0:
            gra = False
            break
        if pole > 9 or pole < 0 or mapa[pole - 1] != '':
            raise ValueError
    except:
        print('Złe dane!')
        continue

    mapa[pole - 1] = 'X'
    if mapa[0] != '' and mapa[1] != '' and mapa[2] != '' and mapa[3] != '' and mapa[4] != '' and mapa[5] != '' and mapa[6] != '' and mapa[7] != '' and mapa[8] != '':
        gra = False
        visual()
        print('Remis')
        break
    visual()
    gra = czyWygrana()
    if gra:
        time.sleep(1)
        strzel()
        visual()
        gra = czyWygrana()
