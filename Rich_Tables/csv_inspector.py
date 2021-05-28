"""
This script is written for printing a fast visualization of a .csv file.
"""
import sys
import csv

def help() -> None:
    """Prints help menu."""
    print("\n                           CSV INSPECTOR") 
    print("This script is written for printing a fast visualization of a .csv file.")
    print("                               -·-")
    print("COMMANDS:")
    print("\b-h        print help")
    print("\b-f        filepath (mandatory). Does not need ''")
    print("\b-d        csv delimiter (, by default)")
    print("\b-r        if present use the library Rich")
    print("\b-l        number of lines to be shown from the top and the bottom of the file")
    print("                               -·-")
    print("IMPORTANT: this version support only arguments passed in this order.")
    print("                               -·-")
    print("EXAMPLES:")
    print("\b    0) python csv_inspector.py -h")
    print("\b    1) python csv_inspector.py -f Iris.csv")
    print("\b    2) python csv_inspector.py -f Iris.csv -r")
    print("\b    3) python csv_inspector.py -f Iris.csv -l 4")
    print("\b    4) python csv_inspector.py -f Iris.csv -d ';' -l 4")
    print("\b    5) python csv_inspector.py -f Iris.csv -l 4 -r")
    print("                               -·-")
    print("\n")

ops = [opt for opt in sys.argv[1:] if opt.startswith("-")]
arg = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# Extract the user's options
ops_arg = dict(zip(ops, arg))

# Add values by default
if "-d" not in ops:
    ops_arg["-d"] = ","

if "-r" not in ops:
    ops_arg["-r"] = False
else:
    ops_arg["-r"] = True

if "-l" not in ops:
    ops_arg["-l"] = 0

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

            if ops_arg["-l"] == 0:
                for row in data:
                    row_str = "    "
                    for element in row:
                        row_str += str(element) + " | "
                    print(row_str)
                    print(subheader_str)
            else: 
                for row in data[:int(ops_arg["-l"])]:
                    row_str = "    "
                    for element in row:
                        row_str += str(element) + "  ·  "
                    print(row_str)
                
                for j in range(int(ops_arg["-l"]), 0, -1):
                    row_str = "    "
                    for element in data[len(data) - j]:
                        row_str += str(element) + "  ·  "
                    print(row_str)
        
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
            if ops_arg["-l"] == 0:
                for row in data:
                    table.add_row(*row)
            else: 
                for row in data[:int(ops_arg["-l"])]:
                    table.add_row(*row)
                
                for j in range(int(ops_arg["-l"]), 0, -1):
                    row = data[len(data) - j]
                    table.add_row(*row)

            console.print(table)
             

