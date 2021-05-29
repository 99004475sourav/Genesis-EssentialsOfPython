import pytest
from Assignment_3 import *

def test_correct_malformed_date():
    assert correct_malformed_date('5:70:65') ==('6:11:05')

def test_is_isogram():
    assert is_isogram('elephant')==False

def test_maxnumber():
    assert maxnumber(6385,1)==638

def test_maximumsuffle():
    assert maximumsuffle(1234)==4321