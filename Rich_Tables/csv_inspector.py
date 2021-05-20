"""
"""
import sys
import csv
from rich.console import Console
from rich.table import Table


def help() -> None:
    """Prints help menu."""
    print("This script is written for printing a fast visualization of a .csv file.")
    print("\b-h        print help")
    print("\b-f        filepath (mandatory)")
    print("\b-d        csv delimiter (, by default)")


ops = [opt for opt in sys.argv[1:] if opt.startswith("-")]
arg = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# Extract the user's options
ops_arg = dict(zip(ops, arg))

# Add values by default
if "-d" not in ops:
    ops_arg["-d"] = ","

# Starts the process
if "-h" in ops:
    help()
else:
    if "-f" not in ops:
        print("Please, specify the file with the flag -f [filepath]")

    else:
        print("The file to read is: ", ops_arg["-f"])

        with open(arg[0]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=ops_arg["-d"])
            line_count = 0
            data = []
            for row in csv_reader:
                if line_count == 0:
                    header = row
                else:
                    data.append(row)
                line_count += 1

            #print(header)
            #print(data)


            table = Table(show_footer=False)
            console = Console()
            
            # Adding the header
            for element in header:
                table.add_column(element)
            
            # Adding the data
            for row in data:
                table.add_row(*row)
            
            

            console.print(table, justify="center")


