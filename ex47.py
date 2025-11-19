def ler_inteiro():
    try:
        numero = int(input("Digite um numero inteiro:"))
    except ValueError:
        print("Erro: voce deve digitar apenas numeros inteiros!") 
    else:
        print(f"numero digitado com sucesso: {numero}")
    finally:
        print("Fim do programa de conversão.")

ler_inteiro()