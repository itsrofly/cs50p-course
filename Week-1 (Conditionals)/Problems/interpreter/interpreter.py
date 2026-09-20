def main():
    x, y, z = input("Expression: ").split(" ")
    x = float(x)
    z = float(z)
    calculadora(y,x,z)

def calculadora(e,n1,n2):
    if e == "+":
        print(round(n1 + n2, 1))
    elif e == "-":
        print(round(n1 - n2, 1))
    elif e == "*":
        print(round(n1 * n2, 1))
    else:
        print(round(n1 / n2, 1))

main()

# Calculadora simples