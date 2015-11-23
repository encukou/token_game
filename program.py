from random import randrange

def odeber_token(stav):
    print('hráč odebírá 1 tokeny')
    stav = stav - 1
    return stav

def odeber_1_token(stav):
    print('hráč odebírá 1 tokeny')
    return -1

def odeber_2_tokeny(stav):
    print('hráč odebírá 2 tokeny')
    return -2

def odeber_3_tokeny(stav):
    print('hráč odebírá 3 tokeny')
    return -3

def pridej_1_token(stav):
    print('hráč přidává 1 token')
    return 1

def zeptej_se(stav):
    return int(input('Hraj: '))

def vyhodnot(stav, tah, predchozi_tah):
    if tah < -3 or tah > 1 or tah == 0:
        raise ValueError('Špatný tah')
    if tah == 1 and predchozi_tah != -3:
        raise ValueError('Špatný tah')
    return stav + tah

def hra(stav, strategie1, strategie2):
    predchozi_tah = 0
    while stav > 0:
        print('Stav je', stav, 'hraje hráč 1')
        tah = strategie1(stav)
        stav = vyhodnot(stav, tah,
                        predchozi_tah)
        predchozi_tah = tah
        if stav <= 0:
            print('vyhrál hráč 2')
            return 2
        print('Stav je', stav, 'hraje hráč 2')
        tah = strategie2(stav)
        stav = vyhodnot(stav, tah,
                        predchozi_tah)
        predchozi_tah = tah
        if stav <= 0:
            print('vyhrál hráč 1')
            return 1

