from program import hra, odeber_1_token
from program import odeber_2_tokeny
from program import odeber_3_tokeny
from program import pridej_1_token

def test_hra():
    vysledek = hra(15,
                   odeber_1_token, odeber_1_token)
    assert vysledek == 2

def test_hra_2t():
    vysledek = hra(15,
                   odeber_2_tokeny, odeber_2_tokeny)
    assert vysledek == 1

def test_hra_20():
    vysledek = hra(20,
                   odeber_2_tokeny, odeber_2_tokeny)
    assert vysledek == 1

def test_hra_20():
    vysledek = hra(20,
                   odeber_3_tokeny, pridej_1_token)
    assert vysledek == 2
