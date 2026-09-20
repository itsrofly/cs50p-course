def main():
    grocerylist = {} # Criar lista
    while True:
        try:
            item = input().upper() # Pegar item
            if item in grocerylist:
                grocerylist[item] += 1 # Somar 1 no item existente
            else:
                grocerylist[item] = 1 # Adicionar item na lista
        except EOFError:
            print("\n")
            grocerylist = sorted(grocerylist.items()) # Colocar em contagem de alfabeto, se tornou uma lista e deixou de ser uma dic
            grocery(grocerylist)
            break

def grocery(l):
    for i in l: # Fazer contagem
        print(f"{i[1]} {i[0]}") # Printar o valor e o item 0 = apple, 1 = numero

main()

# Sorted - https://docs.python.org/3/howto/sorting.html, New discovery, organize elements