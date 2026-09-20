def main():
    text = shorten(input("Input: "))
    print(f"Output: {text}")

def shorten(t):
    for c in t: # Loop, contar todas as char
        if c in "aeiouAEIOU": # As char do aeiouAEIOU tem que estár no c
            t = t.replace(c, "")
    return t

if __name__ == "__main__":
    main()