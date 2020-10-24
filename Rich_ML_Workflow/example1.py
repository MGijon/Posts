"""Example: how easy is to use Rich and how useful it can be."""
import rich
import seaborn as sns
import matplotlib.pyplot as plt
from random import seed
from random import gauss
from random import uniform
from random import gammavariate
from random import lognormvariate
from random import paretovariate
from random import weibullvariate
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy.stats import shapiro

seed(32)
SAMPLES = 1000
SL = 0.05 # Significance Level

# Generate the values
normal_values = [gauss(mu=0, sigma=1) for _ in range(SAMPLES)]
normal_values2 = [gauss(mu=1, sigma=1.5) for _ in range(SAMPLES)]
uniform_values = [uniform(a=-3, b=3) for _ in range(SAMPLES)]
gamma_values = [gammavariate(alpha=10, beta=.5) for _ in range(SAMPLES)]
lognorm_values = [lognormvariate(mu=0, sigma=1) for _ in range(SAMPLES)]
pareto_values = [paretovariate(alpha=1.2) for _ in range(SAMPLES)]
weibull_values = [weibullvariate(alpha=1, beta=1) for _ in range(SAMPLES)]

data_sets = [normal_values, uniform_values, gamma_values, lognorm_values, normal_values2, pareto_values, weibull_values]
labels = ["feature_" + str(i) for i in range(1, len(data_sets) + 1)]
means = [np.round(np.mean(data_sets[i]), 4) for i in range(len(data_sets))]
stds = [np.round(np.std(data_sets[i]), 4) for i in range(len(data_sets))]
kurtosiss = [np.round(kurtosis(data_sets[i]), 4) for i in range(len(data_sets))]
skews = [np.round(skew(data_sets[i]), 4) for i in range(len(data_sets))]

def shapiroWilkTest(arr):
    """Performs the Shapiro-Wilk test.
    :param arr: 1-Dimensional array.
    :return: statistic, p-value.
    """
    return shapiro(arr)

# Print the information
for index in range(len(data_sets)):
    rich.print("Name of the variable: [bold white]" + labels[index] + "[/bold white]")
    rich.print("Mean: [green]" + str(means[index]) + "[/green]")
    rich.print("Std: [blue]" + str(stds[index]) + "[/blue]")
    rich.print("Kurtosis: [purple]" + str(kurtosiss[index]) + "[/purple]")
    rich.print("Skew: [yellow]" + str(skews[index]) + "[/yellow]")
    rich.print("Shapiro-Wilk test (statistic): [bold]" + str(np.round(shapiroWilkTest(data_sets[index]).statistic, 4)) + "[/bold]")
    rich.print("Shapiro-Wilk test (p-value): [bold]" + str(np.round(shapiroWilkTest(data_sets[index]).pvalue, 4)) + "[/bold]")
    print("---- ---- ---- ---")
print("\n")

# Create a table
table = rich.table.Table(title='Mean, Std and Shapiro-Wilk test results for Significance Level ' + str(SL), show_lines=False)

table.add_column("Feature", justify="right", style="cyan", no_wrap=True)
table.add_column("#samples", style="magenta")
table.add_column("Mean", justify="right", style="green")
table.add_column("Std")
table.add_column("Shapiro-Wilk statistic")
table.add_column("Shapiro-Wilk p-value")

for i in range(len(data_sets)):
    if np.round(shapiroWilkTest(data_sets[i]).pvalue, 4) < SL:
        table.add_row(labels[i],
                      str(len(data_sets[i])),
                      str(means[i]),
                      str(stds[i]),
                      str(np.round(shapiroWilkTest(data_sets[i]).statistic, 4)),
                      "[green]" + str(np.round(shapiroWilkTest(data_sets[i]).pvalue, 4)) + "[/green] :heavy_check_mark:")
    else:
        table.add_row(labels[i],
                      str(len(data_sets[i])),
                      str(means[i]),
                      str(stds[i]),
                      str(np.round(shapiroWilkTest(data_sets[i]).statistic, 4)),
                      "[red]" + str(np.round(shapiroWilkTest(data_sets[i]).pvalue, 4)) + "[/red] :heavy_exclamation_mark:")


console = rich.console.Console()
console.print(table)


# Plot the distributions
'''
plt.title('Comes this samples from a Normal Distrubuted SOMETHING?')
sns.distplot(normal_values, label='Normal')
sns.distplot(uniform_values, label='Uniform')
sns.distplot(gamma_values, label='Gamma')
sns.distplot(lognorm_values, label='Log Norm')
plt.legend()
plt.show()
'''
