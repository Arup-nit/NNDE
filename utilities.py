import numpy as np
# ---------------------------------------------------------------------------------------------------------
# -----Activation Functions--------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# Sigmoid activation function
# ---------------------------------------------------------------------------------------------------------


def sigmoid(x, n):
    '''
    Sigmoid activation function and its first three derivatives.
    @params:
    1. x - float, the argument,
    2. n - non-negative integer, n-th derivative
    @returns: float
    '''
    x = x.astype('float64')
    temp_sig = np.exp((-x).round(7), dtype="float64")
    temp_sig = 1 / (temp_sig + 1)
    if n == 0:
        return temp_sig
    elif n == 1:
        return temp_sig * (1 - temp_sig)
    elif n == 2:
        return temp_sig * (1 - temp_sig) * (1 - 2 * temp_sig)
    elif n == 3:
        return temp_sig * (1 - temp_sig) * (1 - 6 * temp_sig * (1 - temp_sig))
    else:
        raise Exception(
            f'Parameter n should be non-negative integer, but n = {n}')
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# Linear activation function
# ---------------------------------------------------------------------------------------------------------


def linear(x, n):
    '''
    Linear activation function and its derivatives.
    @params:
    1. x - float, the argument,
    2. n - non-negative integer, n-th derivative
    @returns: float
    '''
    if n == 0:
        return x
    elif n == 1:
        return 1
    elif n > 1:
        return 0
    else:
        raise Exception(
            f'Parameter n should be non-negative integer, but n = {n}')
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# ReLu activation function
# ---------------------------------------------------------------------------------------------------------


def ReLu(x, n):
    '''
    Relu function f(x)=max(0, x) and its derivatives.
    @params:
    1. x - float, the argument,
    2. n - non-negative integer, n-th derivative
    @returns: float
    '''
    if n == 0:
        return np.max(0, x)
    elif n == 1:
        return 0 if x < 0 else 1
    elif n > 1:
        return 0
    else:
        raise Exception(
            f'Parameter n should be non-negative integer, but n = {n}')
# ---------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------
# Kronecker delta function
# ---------------------------------------------------------------------------------------------------------
def kronecker_delta(i, j):
    '''
    Kronecker delta function.
    @params:
    i, j - non-negative integers
    @returns: boolean
    '''
    if isinstance(i, int) and isinstance(j, int) and i >= 0 and j >= 0:
        return i == j
    else:
        raise Exception(
            f'The arguments should be non-negative integers, but i = {i} and j = {j}.')
# ---------------------------------------------------------------------------------------------------------