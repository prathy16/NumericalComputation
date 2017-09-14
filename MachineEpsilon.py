# numpy is the fundamental package for scientific computing in python
import numpy as np


def machine_epsilon(func):
    """
    Returns:
         Machine Epsilon
    Arguments:
        func -- function converts a floating number to float32, float64
        float32 - Single Precision float
        float64 - Double Precision float
    """
    x = func(0)
    # Single Precision
    if func is np.float32:
        min_x = func(-126)  # least possible value of power, x, for a 32-bit system
    # Double Precision
    elif func is np.float64:
        min_x = func(-1023)  # least possible value of power, x, for a 64-bit system

    while func(1)+func(2**x) > func(1) and min_x <= x:
        # When loop breaks, prev_x stores the smallest power of x for which
        # 1+2**x > 1, and x stores a value such that 1+2**x  = 1
        prev_x = func(x)
        x += func(-1)

    return func(2**prev_x)


print("Machine Epsilon for single precision = ", machine_epsilon(np.float32))

print("Machine Epsilon for Double precision = ", machine_epsilon(np.float64))
