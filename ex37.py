numero_secreto = 42
palpite = 0

print("Tente adivinhar o número secreto entre 1 e 100.")

while palpite != numero_secreto:
    try:
        entrada = input("Seu palpit:")
        palpite = int(entrada)

        if palpite < numero_secreto:
            print(("Muito alto. Tente um número maior."))
        elif palpite > numero_secreto:
            print(("Muito alto. Tente um número menor."))
        else:
            print(f"Parabéns! Voce acertou o número secreto: {numero_secreto}!")
    except ValueError:
        print(f"Por favor, digite apenas números inteiros.")                    