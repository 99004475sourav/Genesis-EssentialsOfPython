import pytest
from Assignment_2 import *

def test_occurence():
    assert occurrence([8, 3, 6, 4, 6, 8, 4, 3, 6, 8, 4, 4, 8 ],13)==8

def test_near_mean():
    assert near_mean([1,2,3,4,5,6,7,8,9,10])==1

def test_missing_no():
    assert missing_no([1, 2, 3, 5, 6])==4

def test_number_of_elements():
    assert number_of_elements([8, 3, 6, 4, 6, 8, 4, 3, 6, 8, 4, 4, 8 ])==6