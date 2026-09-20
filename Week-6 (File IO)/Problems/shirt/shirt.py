import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():

    ext = [".jpeg", ".jpg", ".png"]

    if len(sys.argv) == 3:
        if splitext(sys.argv[2])[1] not in ext:
            sys.exit("Invalid output")
        else:
            if splitext(sys.argv[1])[1] == splitext(sys.argv[2])[1]:
                update_image(sys.argv[1], sys.argv[2])
            else:
                sys.exit("Input and output have different extensions")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def update_image(item1, item2):
    shirt = Image.open("shirt.png")
    size = shirt.size
    try:
        image = Image.open(item1)
        image = ImageOps.fit(image, size) # Colocar na mesma size que a shirt
        image.paste(shirt,shirt) # A shir é colado na imagem
        image.save(item2) # Salvar imagem com o nome do item2
    except FileNotFoundError:
        sys.exit("Input does not exist")

main()