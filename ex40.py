def somar(a,b):
    return a + b

def subtrair(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
    if b != 0:
        a / b
    else:
        print("valor inválido")
escolha = ""
while escolha != "0":        
    escolha = input("digite uma opcao 0-parar, 1=soma, 2-subtrair, 3-mulitplicar, 4-dividir ")
    num1= int(input("digite o primeiro numero "))
    num2= int(input("digite o segundo numero "))
    if escolha == "1":
        x=somar(num1, num2)       
    elif escolha == "2":
        x=subtrair(num1, num2) 
    elif escolha == "3":
        x=mult(num1, num2)
    else:
        x=divi(num1, num2)

print(f"resultado da operacao: {x}")