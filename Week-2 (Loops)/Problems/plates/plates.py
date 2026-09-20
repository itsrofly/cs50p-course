def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum() and 2 <= len(s) <= 6 and s[0:2].isalpha(): # Primeiro ver se é um texto com apenas abecedario e numeros, depois verificar o maximo e o minimo de strings, por fim as 2 primeiras char têm de ser letras, caso não retorna como invalido
        middle = False # Meio
        for c in s[2:]: # Apartir das duas primmeiras char
            if c.isdigit(): # Se for um numero
                if c == "0" and middle == False: # E for 0, retorna como invalido
                    return
                else: # caso não, retorna como meio true, para verificar se um numero ja foi digitado
                    middle = True
            else: # se um numero ja foi digitado retorna como invalido
                if middle == True:
                    return
        return True # Caso não retorna como true
    else:
        return

        # len(s) - https://docs.python.org/3/library/functions.html#len, New discovery, count the chars

main()