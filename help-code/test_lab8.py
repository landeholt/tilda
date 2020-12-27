#!python
#-*- coding: utf-8 -*-
# Author: John Landeholt [TA]
from YOUR_FILE import YOUR_FUNCTION as f
# from lab8 import formula as f
import pytest

@pytest.mark.parametrize('formula, expected', [
    ('Na', 'Formeln är syntaktiskt korrekt'),
    ('H2O', 'Formeln är syntaktiskt korrekt'),
    ('Si(C3(COOH)2)4(H2O)7', 'Formeln är syntaktiskt korrekt'),
    ('Na332', 'Formeln är syntaktiskt korrekt'),
    ('C(Xx4)5', 'Okänd atom vid radslutet 4)5'),
    ('C(OH4)C', 'Saknad siffra vid radslutet C'),
    ('C(OH4C', 'Saknad högerparentes vid radslutet'),
    ('H2O)Fe', 'Felaktig gruppstart vid radslutet )Fe'),
    ('H0', 'För litet tal vid radslutet'),
    ('H1C', 'För litet tal vid radslutet C'),
    ('H02C', 'För litet tal vid radslutet 2C'),
    ('Nacl', 'Saknad stor bokstav vid radslutet cl'),
    ('a', 'Saknad stor bokstav vid radslutet a'),
    ('(Cl)2)3', 'Felaktig gruppstart vid radslutet )3'),
    (')', 'Felaktig gruppstart vid radslutet )'),
    ('2', 'Felaktig gruppstart vid radslutet 2'),
    ('', 'Formeln är syntaktiskt korrekt'),
    ('H111', 'Formeln är syntaktiskt korrekt'),
    ('H110', 'Formeln är syntaktiskt korrekt')
])

def test_formulas(formula, expected):
    cert = f(formula)
    assert cert == expected