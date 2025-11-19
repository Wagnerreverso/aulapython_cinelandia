def dividir(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:

         print("Erro; divisão por zero não é permitido!") 
    except ValueError:
         print("Erro: valor inválido informado!")
    else:

          print(f"resultado sa divisão: {resultado}")
    finally:

          print("Operação finalizada (com ou sem erro).")
try:

    num1 = float(input("Digite o numerador:"))
    num2 = float (input("Digite odenominado:"))
    dividir(num1, num2)
except ValueError:
    print("Voce deve digitar apenas numeros:")