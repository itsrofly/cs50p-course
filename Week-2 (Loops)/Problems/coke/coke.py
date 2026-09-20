def main():
    price = 50
    sell = cokemachine(price)
    print(f"Change Owed: {sell * -1}") # Troco, converter para positivo

def cokemachine(p):
    while p > 0: # Loop, se o preço for maior que zero
        print(f"Amount Due: {p}") # Quanto tens que pagar
        coin = int(input("Insert Coin: ")) # Pedir moedas
        if coin == 25 or coin == 10 or coin == 5: # Só aceita essas moedas
            p = p - coin # Subtrair moedas no preço
    return p # Devolver preço

main()