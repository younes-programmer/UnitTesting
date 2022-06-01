import pytest
from app import *


def test_equation_degre_one_1():
    assert equation_resolve(2, -6) == 3
    assert equation_resolve(4, -8) == 2
    assert equation_resolve(0, -8) == "non"


def test_equation_degree_two():
    assert equation_resolve_second_degree(1, 3, 10) == []
    assert equation_resolve_second_degree(2, -3, 9/8) == [3/4]
    assert equation_resolve_second_degree(2, -1, -6) == [-3/2, 2]
