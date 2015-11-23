from random import randrange

def odeber_token(stav):
    print('hráč odebírá 1 tokeny')
    stav = stav - 1
    return stav

def odeber_1_token(stav):
    print('hráč odebírá 1 tokeny')
    stav = stav - 1
    return stav

def odeber_2_tokeny(stav):
    print('hráč odebírá 2 tokeny')
    stav = stav - 2
    return stav

def odeber_3_tokeny(stav):
    print('hráč odebírá 3 tokeny')
    stav = stav - 3
    return stav

def pridej_1_token(stav):
    print('hráč přidává 1 token')
    stav = stav + 1
    return stav

def hra(stav, strategie1, strategie2):
    while stav > 0:
        print('Stav je', stav, 'hraje hráč 1')
        stav = strategie1(stav)
        if stav <= 0:
            print('vyhrál hráč 2')
            return 2
        print('Stav je', stav, 'hraje hráč 2')
        stav = strategie2(stav)
        if stav <= 0:
            print('vyhrál hráč 1')
            return 1

hra(randrange(10, 21),
    odeber_1_token,
    odeber_2_tokeny)
