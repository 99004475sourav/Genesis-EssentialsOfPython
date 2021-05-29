import pytest

from Assignment_3 import correct_malformed_date


def test_correct_malformed_date():
    assert correct_malformed_date('5:70:65')== '6:11:05'