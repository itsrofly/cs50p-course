def main():
    text = shorten(input("Input: "))
    print(f"Output: {text}")

def shorten(word):
    for c in word: # Loop, contar todas as char
        if word in "aeiouAEIOU": # As char do aeiouAEIOU tem que estár no c
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()