def main():
    t = input("Greeting: ").strip() # Remover espaço
    print(f"${value(t)}")


def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting: # Se o greeting ou t for hello
        return 0
    elif greeting.startswith("h"): # Se o greeting começar com h
        return 20
    else: # Caso não a empresa te paga
        return 100

if __name__ == "__main__":
    main()