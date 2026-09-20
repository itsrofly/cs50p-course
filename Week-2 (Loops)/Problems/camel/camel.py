def main():
    text = input("cameCase: ")
    snake_case(text)

def snake_case(t):
    for c in t: # Loop, Contar todas as palavras
        if c.isupper():
            t = t.partition(c) # Dividir o t em 3 partições
            t = f"{t[0]}_{t[1].lower()}" + t[2] # Juntar a parte 0 com a letra maiuscula com snake case e deixar ela minuscula, Atualizar o t com snake_case, e depois volta e conta o resto
    print(f"snake_case: {t}") # Quando acabar de contar, print

main()

