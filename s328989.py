# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Notez bien: No need to include f0 -- it's just an example!

# for f0 x0 works perfect with lowest mse 0.012..
def f0(x: np.ndarray) -> np.ndarray:
    return (np.log(1.2) * x[1]) + x[1] 



def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
    return np.exp(12.36) * (x[1]+4.93*x[0] + x[2])


def f3(x: np.ndarray) -> np.ndarray:
    return (2.3 * x[0]*x[0])-(x[1]*x[1]*x[1]) #y=1.08 * 10^2


def f4(x: np.ndarray) -> np.ndarray: 
    return np.log(1.64 * x[0] * x[0]) #y= 26.09960298130464


def f5(x: np.ndarray) -> np.ndarray: 
    return np.sin(+6.349873083483724)  #y=0.004440670787932643


def f6(x: np.ndarray) -> np.ndarray: 
    return x[1] - x[0] #y=2.714350734283543


def f7(x: np.ndarray) -> np.ndarray: ...


def f8(x: np.ndarray) -> np.ndarray: ...
