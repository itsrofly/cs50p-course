import pytest

def main():
    fuel = gauge(convert(input("Fraction: ")))
    print(fuel)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        return round((x / y) * 100)
    except (ValueError, ZeroDivisionError) as error:
        raise error # Para o pytest

def gauge(percentage):
    try:
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        else:
            return f"{percentage}%"
    except:
        pass

if __name__ == "__main__":
    main()