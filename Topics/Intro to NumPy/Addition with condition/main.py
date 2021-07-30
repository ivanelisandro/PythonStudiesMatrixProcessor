import numpy as np


def custom_sum(arg1, arg2):
    arguments = (arg1, arg2)
    are_arrays = [isinstance(n, np.ndarray) for n in arguments]
    are_lists = [isinstance(n, list) for n in arguments]
    if all(are_arrays):
        return arg1 + arg2
    elif all(are_lists):
        return "Both arguments are lists, not arrays"

    return "One argument is a list"
