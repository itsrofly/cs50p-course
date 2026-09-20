import inflect

p = inflect.engine()
name = []

while True:
    try:
        name.append(input("name: "))
    except EOFError:
        print("\nAdieu, adieu, to", p.join(name))
        break