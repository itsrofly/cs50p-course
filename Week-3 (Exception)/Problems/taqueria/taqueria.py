def main():
    Total = 0
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }


    while True:
        try:
            Item = input("Item: ").title()
            if Item in menu: # Se o item tiver na lista
                Total += menu[Item] # Somar o total mais o valor do item
                print(f"Total: ${Total:.2f}") # Arredondar em duas casas
        except EOFError: # Ctrl-d, fecha aplicação
            print("\n") # Para enviar o usuario para outra linha
            break

main()
