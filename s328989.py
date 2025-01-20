# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Notez bien: No need to include f0 -- it's just an example!

# for f0 x0 works perfect with lowest mse 0.012..
def f0(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5



def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
    return np.exp(12.36) * (x[1]+4.93*x[0] + x[2])


def f3(x: np.ndarray) -> np.ndarray:
    return ((((x[0] * x[0]) - x[2]) + np.exp(-0.074069 - x[1])) - x[2]) + ((((0.78765 - x[1]) + ((x[0] * x[0]) + (1.0216 - np.exp(x[1])))) + 3.2687) - x[2]) #y=1.08 * 10^2


def f4(x: np.ndarray) -> np.ndarray: 
    return (((((x[0]*3) + -0.39527) * -0.004329) + 0.46678) + np.cos(x[1])) * 7 


def f5(x: np.ndarray) -> np.ndarray: 
    return np.sin((x[1] * 5.3851e-14) * x[1]) * (((x[1] * np.exp(x[1])) + 1.1635) - np.exp(x[0] + x[1]))  #y=2.00395


def f6(x: np.ndarray) -> np.ndarray: 
    return (x[1]*2) - ((((x[0] * 0.69452) + 0.097928) - 0.11889) +((x[1] * 0.30548) - -0.020958))


def f7(x: np.ndarray) -> np.ndarray: 
    return (np.exp((x[0] * x[1]) + (np.cos(np.cos(x[1])) + np.cos(np.sin(x[1] * ((x[1] - x[0]) * x[0])) * (x[1]*2)))) * (1.3267 + 0.26225)) + -1.2431


def f8(x: np.ndarray) -> np.ndarray: 
    return (((np.exp(x[5] * -1.0831) * (x[5] + -62.992)) + np.exp(x[5] + 4.6193)) - 268.02) + -360.77 
