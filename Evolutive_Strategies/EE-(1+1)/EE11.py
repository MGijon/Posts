"""Implementation of an evolutive strategy based algorithm for solving optimization problems."""
## IMPORTS
## =======
import numpy as np
from random import gauss
import matplotlib.pyplot as plt
from test_functions import function_sphere, function_ackley, function_himmelblau, function_rastrigin

## PARAMETERS 
## ==========
DIMENSIONALITY = 2
NUMBER_OF_EXPERIMENTS = 10

sphere_a, sphere_b = -5.12, 5.12    # limits for the plot in the case of the sphere function
ackley_a, ackley_b = -32.77, 32.77  # limits for the plot in the case of the ackley´s function
himmelblau_a, himmelblau_b = -5.12, 5.12  # limits for the plot in the case of the himmelblau´s function
rastrigin_a, rastrigin_b = -5.12, 5.12    # limits for the plot in the case of the rastring´s function


def EE_11(function, boundaries, MaxNumber):
    """Function that performs the algorithm EE-(1+1).
    :param function: function to be optimized.
    :param boundaries: [(a1, b1), ...] n-dimensional array of tuples with the boundaries of the searching region.
    :param MaxNumber: max number of iteration (stop condition).
    :return path: array, n-dimensional, path follow for the algorithm.
    """
    # Init the variables
    g = 0
    path = []
    Xs = np.random.rand(len(boundaries))
    for i in range(len(boundaries)):
        Xs[i] = boundaries[i][0] + (boundaries[i][1] - boundaries[i][0]) * Xs[i]
  
    sigma = np.random.rand(1)[0]

    while g <= MaxNumber:
        # Update Ys
        Ys = [x + sigma * gauss(0, 1) for x in Xs]

        if function(vector=Xs) <= function(vector=Ys):
            path.append(Xs)
        else:
            path.append(Ys)
            Xs = Ys
        g += 1

    return path

def plots(function, boundaries, path):
    """Plot the path followd by the algorithm and evolution of the value of the function.
    :param function: function that has been optimized.
    :param boundaries: bounds for each axis.
    :param path: path obtained for the optimization algorithm.
    """
    fig = plt.figure()

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.set_xlim(left=boundaries[0][0])
    ax1.set_xlim(right=boundaries[0][1])
    ax1.set_ylim(bottom=boundaries[1][0])
    ax1.set_ylim(top=boundaries[1][1])

    ax1.set_title('Path')

    for i in path:
        ax1.scatter(i[0], i[1], color='black')
    ax1.scatter(path[-1][0], path[-1][1], color='red')

    ax2.plot(range(len(path)), [function(x) for x in path])
    ax2.set_title('Value of the function')

    plt.show()

def plot_paths(function, boundaries, paths):
    """Plot path along with the function in the space.
    :param function: function to be represented.
    :param boundaries: boundaries for the representation.
    :param paths: [array collection of paths], paths followed by the optimization algorithm.
    """
    number_points = 100
    x = np.linspace(boundaries[0][0], boundaries[0][1], number_points)
    y = np.linspace(boundaries[1][0], boundaries[1][1], number_points)
    X, Y = np.meshgrid(x, y)
    Z = function([X, Y])

    # Function
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Path in 3D 
    for path in paths:
        xs = [x[0] for x in path]
        ys = [y[1] for y in path]
        zs = [function(element) for element in path]
        ax.plot(xs, ys, zs)

    # show the figure
    plt.show()

# N-Dimensional!!
def progress_curves(function, boundaries, paths):
    """Plot progress curves.
    :param function: function to be represented.
    :param boundaries: boundaries for the representation.
    :param paths: [array collection of paths], paths followed by the optimization algorithm.
    """
    plt.figure(figsize=(7, 7))
    for exp in paths:
        plt.plot(range(0, len(paths[0])), [function(x) for x in exp], alpha=0.4)
    plt.title("Progress curves")
    plt.suptitle("")
    plt.xlabel("Number of generations")
    plt.ylabel("Fitness value")
    plt.show()


if __name__=='__main__':


    # Sphere ---------------------------------------------------------------- #
    bounds = [(sphere_a, sphere_b) for _ in range(DIMENSIONALITY)]

    experiments_results = []
    for _ in range(NUMBER_OF_EXPERIMENTS):
        experiments_results.append(EE_11(function=function_sphere,
                                         boundaries=bounds,
                                         MaxNumber=1000))

    if DIMENSIONALITY == 2:
        # Only works for DIMENSION 2 for obvious reasons
        plot_paths(function=function_sphere,
                   boundaries=bounds,
                   paths=experiments_results)

    # Progress curves
    progress_curves(function=function_sphere,
                    boundaries=bounds,
                    paths=experiments_results)


    # Ackley ---------------------------------------------------------------- #
    bounds = [(ackley_a, ackley_b) for _ in range(DIMENSIONALITY)]

    experiments_results = []
    for _ in range(NUMBER_OF_EXPERIMENTS):
        experiments_results.append(EE_11(function=function_ackley,
                                         boundaries=bounds,
                                         MaxNumber=1000))

    if DIMENSIONALITY == 2:
        # Only works for DIMENSION 2 for obvious reasons
        plot_paths(function=function_ackley,
                   boundaries=bounds,
                   paths=experiments_results)

    # Progress curves
    progress_curves(function=function_ackley,
                    boundaries=bounds,
                    paths=experiments_results)

    # Himmelblau ------------------------------------------------------------- #
    bounds = [(himmelblau_a, himmelblau_b) for _ in range(DIMENSIONALITY)]

    experiments_results = []
    for _ in range(NUMBER_OF_EXPERIMENTS):
        experiments_results.append(EE_11(function=function_himmelblau,
                                         boundaries=bounds,
                                         MaxNumber=1000))

    if DIMENSIONALITY == 2:
        # Only works for DIMENSION 2 for obvious reasons
        plot_paths(function=function_himmelblau,
                   boundaries=bounds,
                   paths=experiments_results)

    # Progress curves
    progress_curves(function=function_himmelblau,
                    boundaries=bounds,
                    paths=experiments_results)

    # Rastrigin -------------------------------------------------------------- #
    bounds = [(rastrigin_a, rastrigin_b) for _ in range(DIMENSIONALITY)]

    experiments_results = []
    for _ in range(NUMBER_OF_EXPERIMENTS):
        experiments_results.append(EE_11(function=function_rastrigin,
                                         boundaries=bounds,
                                         MaxNumber=1000))

    if DIMENSIONALITY == 2:
        # Only works for DIMENSION 2 for obvious reasons
        plot_paths(function=function_rastrigin,
                   boundaries=bounds,
                   paths=experiments_results)

    # Progress curves
    progress_curves(function=function_rastrigin,
                    boundaries=bounds,
                    paths=experiments_results)