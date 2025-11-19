numero_positivos = 0 
numero = -1

while numero != 0:
    
    entrada = input("Digite um número (0 para parar):")
    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

    if numero > 0:
        soma_positivos = soma_positivos + numero
print(f"A soma dos números positivos digitados é: {soma_positivos}")            