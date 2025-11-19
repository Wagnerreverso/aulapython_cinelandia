def calcular_media():
    try:
        nota1 = float (input("digite a primeira nota:"))
        nota2 = float (input("digite a segunda nota:"))    
        media = (nota1 + nota2) / 2
    except ValueError:
        print("Erro: digite apenas numeros válidos;")
    else:
        print(f"Média calculada: {media:.2f}")
    finally:
        print("Fim do calculo de média.")

calcular_media()             