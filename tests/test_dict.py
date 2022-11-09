import inspect
import os

from pdttools import print_dict


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


def test_dict_01():
    the_dict = {"a": 1, "b": 2, "c": 3}

    def callback(out_file):
        print_dict(the_dict, output_file=out_file)

    __generic_test_procedure(callback)
