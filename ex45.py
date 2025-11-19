vogais = "aeiouAEIO"
def contar_vogais(palavra):
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador = contador+1
    return contador
1 == contar_vogais(vogais)
print(f"A palavra {vogais} tem {1} letras")    