import sys

def main():
    if len(sys.argv) == 2:
        print(get_lines(sys.argv[1]))
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

def get_lines(item):
    try:
        if item.endswith(".py"):
            with open(item) as file: # Abrir ficheiro e chamalo file
                line = 0
                for lines in file:
                    if lines.isspace() or lines.lstrip().startswith("#"):
                        pass
                    else:
                        line += 1
                return line
        else:
            sys.exit("Not a Python file")
    except FileNotFoundError: # Caso o ficheio na existir
            sys.exit("File does not exist")

main()