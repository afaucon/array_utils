import inspect
import os
import pytest

from pdttools import print_array
from pdttools import PdttoolsFunctionalException


def __generic_test_procedure(callback):

    test_name = inspect.currentframe().f_back.f_code.co_name

    out_file = "tests/" + test_name + ".out"
    exp_file = "tests/" + test_name + ".exp"

    callback(out_file)

    # If no out file exists, it means that nothing has been produced
    if not os.path.exists(out_file):
        with open(out_file, "w") as creating_new_csv_file:
            pass

    with open(out_file) as f:
        out = f.read()

    with open(exp_file) as f:
        exp = f.read()

    assert out == exp

    os.remove(out_file)


def test_array_01():
    array = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6},
    ]

    def callback(out_file):
        print_array(array, output_file=out_file, format="csv")

    __generic_test_procedure(callback)


def test_array_02():
    array = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "c": 6, "b": 5},
    ]

    def callback(out_file):
        print_array(array, output_file=out_file, format="pretty")

    __generic_test_procedure(callback)


def test_array_03():
    class Item:
        def __init__(self):
            self.a = 4
            self.b = 5
            self.c = 6

    i = Item()
    array = [
        {"a": 1, "b": 2, "c": 3},
        i,
    ]

    def callback(out_file):
        print_array(array, output_file=out_file, format="pretty")

    __generic_test_procedure(callback)


def test_array_04():
    array = []

    def callback(out_file):
        print_array(array, output_file=out_file, format="pretty")

    __generic_test_procedure(callback)


def test_array_05():
    array = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6, "d": 7},
    ]

    def callback(out_file):
        print_array(array, output_file=out_file, format="pretty")

    __generic_test_procedure(callback)


def test_array_06():
    array = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6, "d": 7},
    ]

    def callback(out_file):
        print_array(array, output_file=out_file, format="pretty", max_column_width=5)

    __generic_test_procedure(callback)


def test_array_not_homogene():
    array = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}, 42]

    with pytest.raises(PdttoolsFunctionalException):
        print_array(array)
