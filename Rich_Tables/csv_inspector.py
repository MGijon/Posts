"""
"""
import sys
import csv

def help() -> None:
    """Prints help menu."""
    print("\n                           CSV INSPECTOR") 
    print("This script is written for printing a fast visualization of a .csv file.")
    print("\b-h        print help")
    print("\b-f        filepath (mandatory)")
    print("\b-d        csv delimiter (, by default)")
    print("\b-r        if presesnt use the library Rich")
    print("\b-l        number of lines to be shown from the top and the bottom of the file")
    print("\n")

ops = [opt for opt in sys.argv[1:] if opt.startswith("-")]
arg = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# Extract the user's options
ops_arg = dict(zip(ops, arg))

print(ops_arg)

# Add values by default
if "-d" not in ops:
    ops_arg["-d"] = ","

if "-r" not in ops:
    ops_arg["-r"] = False
else:
    ops_arg["-r"] = True

if "-l" not in ops:
    ops_arg["-l"] = None


print(ops_arg)

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


        # Print without Rich
        if not ops_arg["-r"]:
            header_str = "    "
            for element in header:
                header_str += element + " | "
            
            print(header_str[:-3])
            subheader_str = "    "
            for element in range(len(header_str[:-7])):
                subheader_str += "-"
            print(subheader_str)

            #for element in data:


        # Print using Rich 
        if ops_arg["-r"]:

            from rich.console import Console
            from rich.table import Table
    
            table = Table(show_footer=False)
            console = Console()
                
            # Adding the header
            for element in header:
                table.add_column(element)
                
            # Adding the data
            for row in data:
                table.add_row(*row)
            
            console.print(table, justify="center")
            # 

