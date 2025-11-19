def calculadora():
    try:
        a = float(input("digite o primeiro numero:"))
        b = float(input("digite o segundo numero:"))
        op = input("digite a operacao (+,-,*,/):")

        match op:
              case '+':
                  resultado = a + b  
              case '-':88
                  resultado = a - b
              case '*':
                  resultado = a * b
              case '/':
                  resultado = a / b
              case _:               
                raise ValueError("operação inválida")

    except ZeroDivisionError:
        print("Erro: divisão por zero!") 
    except ValueError as e:
        print(f"{e}")
    else:
        print(f"resultado: {resultado}") 
    finally:
        print("calculo encerrado.")  
calculadora()             