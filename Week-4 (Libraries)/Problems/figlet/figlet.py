from pyfiglet import Figlet
import sys

figlet = Figlet()


prefix = ["-f", "--font"] # Criar prefixo

if len(sys.argv) >= 2 and sys.argv[1] in prefix and sys.argv[2] in figlet.getFonts(): # Verificar se contem mais de 2 elementos, se o segundo elemento está no prefixo e o terceiro faz parte das fontes
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2]) # Setar a font escolhida pelo usuario, que é o 3 elemento
    print(figlet.renderText(text)) # renderizar com a font nova e o texto
else:
    sys.exit("Invalid usage")