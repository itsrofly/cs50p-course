text = input("File name: ").strip().lower().replace(".jpg", ".jpeg")

def extensionhttp(i):
    # If is a image
    if i.endswith(".gif") or i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
        i = i.partition(".") # Dividir o i, com o ponto
        print(f"image/{i[2]}") # pegar só a 2 parte do i

    # if is a application.
    elif i.endswith(".pdf") or i.endswith(".zip"):
        i = i.partition(".")
        print(f"application/{i[2]}")

    elif i.endswith(".txt"):
        print("text/plain")

    else:
        print("application/octet-stream")

extensionhttp(text)

# Extensions HTTP header in the server