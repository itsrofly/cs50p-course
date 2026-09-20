import re


def main():
    print(count(input("Text: ")))


def count(s):
    n = 0
    for _ in re.findall(r"\bum\b", s.lower()):
        n += 1
    return n


if __name__ == "__main__":
    main()