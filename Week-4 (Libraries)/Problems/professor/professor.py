import random


def main():
    errors = 0
    score = 0
    round = 10
    level = get_level()

    for n in range(round):
        x, y = generate_integer(level), generate_integer(level)
        r = x + y
        while True:
            q = input(f"{x} + {y} = ")
            if q != str(r):
                errors += 1
                print("EEE")
                if errors == 3:
                    errors = 0
                    print(f"{x} + {y} = {r}")
                    break
            else:
                score += 1
                break
    print(f"Score: {score}")

    # solicita (e, se necessário, solicita novamente) ao usuário um nível e retorna 1, 2, ou 3
def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return level


    # generate_integer retorna um inteiro não negativo gerado aleatoriamente
def generate_integer(level):
    if level == "1":
        return random.randint(0, 9)
    elif level == "2":
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()