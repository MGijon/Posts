"""Graphical representation of the test functions."""
import numpy as np    # No sure if it is necessary
import matplotlib.pyplot as plt
from test_functions import function_sphere, function_ackley, function_himmelblau, function_rastrigin

sphere_a, sphere_b = -5.12, 5.12    # limits for the plot in the case of the sphere function
ackley_a, ackley_b = -32.77, 32.77  # limits for the plot in the case of the ackley´s function
himmelblau_a, himmelblau_b = -5.12, 5.12  # limits for the plot in the case of the himmelblau´s function
rastrigin_a, rastrigin_b = -5.12, 5.12    # limits for the plot in the case of the rastring´s function

def simple3D_plot(function, a, b, title):
    """Create a simple 3d-plot.
    :param function: function used to compute the value for the z-axis.
    :param a: lower limit for each one of the components.
    :param b: higher limit for each one of the components.
    """
    number_points = 500
    x = np.linspace(a, b, number_points)
    y = np.linspace(a, b, number_points)
    X, Y = np.meshgrid(x, y)
    Z = function([X, Y])

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_title(title)
    ax.contour3D(X, Y, Z, 50, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)
    ax.contour(X, Y, Z, 10, lw=3, cmap="autumn_r", linestyles="solid", offset=-1)
    ax.contour(X, Y, Z, 10, lw=3, colors="k", linestyles="solid")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

if __name__ == "__main__":
    
    # 3D Plots 
    simple3D_plot(function=function_sphere, a=sphere_a, b=sphere_b, title="Sphere function")
    simple3D_plot(function=function_ackley, a=ackley_a, b=ackley_b, title="Ackley´s function")
    simple3D_plot(function=function_himmelblau, a=himmelblau_a, b=himmelblau_b, title="Himmelblau´s function")
    simple3D_plot(function=function_rastrigin, a=rastrigin_a, b=rastrigin_b, title="Rastrigin´s function")