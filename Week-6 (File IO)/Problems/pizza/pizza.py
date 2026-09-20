import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        table = get_tabulate(sys.argv[1])
        print(tabulate(table[1:], table[0], tablefmt="grid")) # Printar em tabela
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

def get_tabulate(item):
    try:
        tabulate = []
        if item.endswith("csv"):
            with open(item) as file:
                file = csv.reader(file)
                for lines in file:
                    tabulate.append([lines[0],lines[1],lines[2]]) # Pegar os elementos dos arquivos csv
                return tabulate
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

main()