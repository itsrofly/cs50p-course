import requests
import pandas as pd
from tkinter import *
import os
from functions import MainWindow

def get_json(link):
    try:
        jsonfile = requests.get(link).json()
        print(f"✅ | Json found")
        return jsonfile

    except requests.RequestException as error:
        raise error("❌ | Json not found")


def get_verbs(verbs):
    try:
        verb = verbs["eng"]
        return verb
    except:
        raise ValueError


def list_status(file):
    try:
        v = pd.DataFrame(file)
        return v
    except:
        raise ValueError

def main():
    window = Tk()
    window.title("Tverbs")
    window.geometry("800x600")
    window.minsize(650, 400)
    window.iconbitmap("images/kitty.ico")

    filej = get_json("https://srrofly.github.io/IrregularVerbs/verbs.json")

    print(list_status(filej))
    verbs = get_verbs(filej)

    app = MainWindow(window, verbs)

    window.mainloop()


if __name__ == "__main__":
    main()