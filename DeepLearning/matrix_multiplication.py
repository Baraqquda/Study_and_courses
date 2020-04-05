import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param first: list of "size" lists, each contains "size" floats
    """

    first_list =[]
    zz = list(zip(*second))
    for i in range(len(first)):
      second_list = []
      for j in range(len(second)):
        ff = first[i]
        ss = zz[j]
        uu = [a * b for a, b in zip(ff, ss)]
        second_list.append(sum(uu))
      first_list.append(second_list)
    result = first_list
    return result


def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """

    a = np.array(first)
    b = np.array(second)
    total = a.dot(b)

    result = total
    return result
