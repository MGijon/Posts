"""Highlight something in the table as example."""
import pandas as pd
import numpy as np
from seaborn import load_dataset
from rich import print as rprint
from rich import table
from rich import console

iris = load_dataset('iris')

def hightlightSuperiorToMeanValues(df, title, numberElements=10):
    """Print a table with the data and highlight the values that are superior to the mean value for each variable."""
    rprint("[bold blue]" + title + "[/bold blue]")
    t = table.Table(caption = "The first and the last " + str(numberElements) + " values of the dataset. Values above the mean higlighted.")
    
    # We can define the logic that we wont here
    highlightOpen = "[bold green]"
    highlightClose = "[/bold green]"

    means = []
    for j in range(len(df.columns) - 1):
        means.append(np.mean(df.iloc[:, j]))
    
    # Adding columns to the table
    for col in df.columns:
        t.add_column(col)

    # First elements of the dataset
    for i in range(numberElements):
        temp = []
        for j in range(len(df.columns)):
            element = df.iloc[i, j]
            
            if j != len(df.columns)-1:
                if element > means[j]:
                    temp.append(highlightOpen + str(element) + highlightClose)
                else:
                    temp.append(str(element))
            
            else: # the last column
                temp.append(str(element))

        t.add_row(*temp)

    # Row to separate first and last group of elements
    temp = []
    for j in range(len(df.columns)):
        temp.append("...")
    t.add_row(*temp)

    # Last elements
    for i in range(numberElements):
        temp = []
        for j in range(len(df.columns)):
            element = df.iloc[-i, j]
            
            if j != len(df.columns) - 1:
                if element > means[j]:
                    temp.append(highlightOpen + str(element) + highlightClose)
                else:
                    temp.append(str(element))
            
            else: # the last columns
                temp.append(str(element))

        t.add_row(*temp)

    con = console.Console()
    con.print(t)


hightlightSuperiorToMeanValues(df=iris, title="Iris Dataset")
