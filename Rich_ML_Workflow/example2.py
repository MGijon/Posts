"""From pandas df to rich table."""
import pandas as pd
from rich import print as rprint
from rich import table
from rich import console
from seaborn import load_dataset

iris = load_dataset('iris')

print(iris.head())

print('----')

rprint(iris.head()) # very simplistic view

print('----')

def beautifulRichDataFrame(df, title, numberElements=10):
    """Print a table with teh data and highlight the values that are superior to the mean value for each variable."""
    rprint("[bold blue]" + title + "[/bold blue]")
    t = table.Table(show_lines=False, caption="Showed the first and the last " + str(numberElements) + " of the dataset")
    # Adding columns at the table
    for col in df.columns:
        t.add_column(col)
    
    # First elements in the dataset
    for i in range(numberElements):
        temp = []
        for j in range(len(df.columns)):
            temp.append(str(df.iloc[i, j]))
        t.add_row(*temp) 
    
    # Row to separate first from last displayed values
    temp = []
    for j in range(len(df.columns)):
        temp.append("...")
    t.add_row(*temp)

    # Last elements in the dataset
    for i in range(numberElements):
        temp = []
        for j in range(len(df.columns)):
            temp.append(str(df.iloc[-i, j]))
        t.add_row(*temp)

    con = console.Console()
    con.print(t)


beautifulRichDataFrame(df=iris, title='Iris Dataset')
