import pytest
from Assignment_1 import BiggestNum
from Assignment_1 import ArmstrongNo
from Assignment_1 import ReverseNum
from Assignment_1 import Sumofdigit
from Assignment_1 import myhcf
from Assignment_1 import compute_lcm
from Assignment_1 import primerange
from Assignment_1 import triangularsum
from Assignment_1 import nCr

def test_BiggestNumber():
    assert BiggestNum(4,5,6)==6

def test_ArmstrongNo():
    assert ArmstrongNo(153)==1
    assert ArmstrongNo(150)==0

def test_ReverseNum():
    assert ReverseNum(123)==321
    assert ReverseNum(456)==654

def test_Sumofdigit():
    assert Sumofdigit(1234)==10

def test_myhcf():
    assert myhcf(8,4)==4

def test_compute_lcm():
    assert compute_lcm(6,9)==18

def test_primerange():
    assert primerange(100)==25

def test_triangularsum():
    assert triangularsum(7)==84

def test_nCr():
    assert nCr(5,3)==10