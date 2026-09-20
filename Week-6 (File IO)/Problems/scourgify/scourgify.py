import sys
import csv

def main():
    if len(sys.argv) == 3:
        update_data(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

def update_data(item, item2):
    try:
        data = []
        if item.endswith(".csv"):
            with open(item) as file:
                file = csv.DictReader(file) # ler
                for line in file:
                    last, first = line["name"].split(',')
                    house = line["house"]
                    data.append([first.strip(), last, house])
                with open(item2, "w") as file: # permissão de escrever
                    file = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                    file.writeheader()
                    for i in data:
                        file.writerow({"first": i[0], "last": i[1], "house": i[2]})
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit(f"Could not read {item2}")


main()