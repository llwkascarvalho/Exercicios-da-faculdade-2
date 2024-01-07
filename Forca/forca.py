# forca.py

import random

def escolher_palavra():
    palavras = ["python", "java", "javascript", "html", "css", "ruby"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    palavra_mostrada = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra + " "
        else:
            palavra_mostrada += "_ "
    return palavra_mostrada.strip()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(mostrar_palavra(palavra_secreta, letras_corretas))

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")

        palavra_atual = mostrar_palavra(palavra_secreta, letras_corretas)
        print(palavra_atual)

        if "_" not in palavra_atual:
            print("Parabéns! Você venceu!")
            break

    if "_" in palavra_atual:
        print(f"Fim de jogo! A palavra era '{palavra_secreta}'.")
