mapa = ['','','','','','','','','']

def visual():
    print('\n\n\n\n\n\n\n----------------')
    print('| ', mapa[0], ' | ', mapa[1], ' | ', mapa[2], ' |')
    print('----------------')
    print('| ', mapa[3], ' | ', mapa[4], ' | ', mapa[5], ' |')
    print('----------------')
    print('| ', mapa[6], ' | ', mapa[7], ' | ', mapa[8], ' |')
    print('----------------')

gra = True
tura = True
while gra:
    pole = input('Wybierz pole 1-9 (0 kończy grę)\n')
    try:
        pole = int(pole)
        if pole > 9 or pole < 0 or mapa[pole-1] != '':
            raise ValueError
    except:
        print('Złe dane!')
        continue
    if pole == 0:
        gra = False
    elif tura:
        mapa[pole-1] = 'X'
        tura = False
    else:
        mapa[pole-1] = 'O'
        tura = True
    visual()
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