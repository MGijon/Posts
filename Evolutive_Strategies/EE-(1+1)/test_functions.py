"""Test functions. Functions to be minimized."""
import numpy as np

def function_sphere(vector):
    """Return the value of the sphere function for the given vector.
    :param vector: n-dimensional array.
    :return value: value of the function at this point in the n-dimensional space.
    """
    return sum([x*x for x in vector])

def function_ackley(vector):
    """Implementations of the Ackley function.
    :param vector: n-dimensional array of floats.
    :return value: value of the Ackley function for the given point in the space.
    """
    n = len(vector)               # dimension of the vector
    sv = function_sphere(vector)  # value of the sphere function

    a = -0.2 * np.sqrt( 1/n * sv)
    b = 1/n * sum([np.cos( 2 * np.pi * x) for x in vector])
    value = -20 * np.exp(a) - np.exp(b) + 20 + np.e

    return value

def function_himmelblau(vector):
    """Compute the value of the Himmelblau's function for a given 2d point in R^2.
    :param vector: 2D array of floats.
    :return value: value of the function at the given point.
    """
    value = np.power(np.power(vector[0], 2) + vector[1] - 11, 2)
    value += np.power(vector[0] + np.power(vector[1], 2) - 7, 2)

    return value

def function_rastrigin(vector):
    """Computes the rastrigin function.
    :param vector: n-dimensional array of floats, vector of dimension n.
    :return value: value of the function at that point.
    """
    A = 10
    An = A * len(vector) # A * n, where n is the dimension of the space
    v = sum([np.power(x, 2) - A * np.cos(2 * np.pi * x) for x in vector])

    value = An + v
    return value 
