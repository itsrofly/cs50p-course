import random
import sys

def main():
    while True: # Repetir caso não seja um int, etç
        try:
            level = float(input("Level: ")) # Perguntar o nivel
            if level.is_integer(): # Se o nivel for inteiro
                number = random_number(level) # function para gerar um numero aleatorio entre 1 e o number
                break
        except:
            pass

    while True: # Repetir caso o guess não seja um int ou a resposta certa
        try:
            guess = float(input("Guess: ")) # Perguntar o guess
            if guess.is_integer(): # Se o guess é inteiro
                res = guess_number(guess, number) # function para dizer se está muito perto longe, ou etá certo
                if res == "Just right!": # Se estiver certo break
                    break
                else: # Se não dizer se está longe ou perto e repetir
                    print(res)
        except:
            pass

    sys.exit(res) # Print resposta certa


def random_number(n): # funcion numero aleatorio entre 1 e n
    return random.randint(1, n)

def guess_number(n, l): # function dizer se está perto ou longe
    if n < l:
        return "Too small!"
    elif n > l:
        return "Too large!"
    else:
        return "Just right!"

main()