

def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/") # Repartir em x e y usando o / como referencia, ou seja, (1/4) para "1", "4"
            x = int(x) # converter para int
            y = int(y)
            if x <= y: # O x tem que ser menor ou igual ao y
                fuel(x,y) # function fuel
                break # parar loop
        except (ValueError, ZeroDivisionError) as error:
            return error

def fuel(p,s):
    fuel = round(((p / s) * 100)) # Converter em percentagem
    if fuel >= 99: # Se o fuel for 99 ou mais
        print("F")
    elif fuel <= 1: # Se o fuel for 1 ou menos
        print("E")
    else:
        print(f"{fuel}%") # Caso não printa a percentagem

main()