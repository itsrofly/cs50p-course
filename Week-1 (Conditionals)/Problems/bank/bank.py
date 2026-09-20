def main():
    t = input("Greeting: ").strip().lower() # Remover espaço e deixar tudo minusculo
    greeting(t)


def greeting(text):
    if "hello" in text: # Se o text ou t for hello
        print("$0")
    elif text.startswith("h"): # Se o text começar com h
        print("$20")
    else: # Caso não a empresa te paga
        print("$100")

main()