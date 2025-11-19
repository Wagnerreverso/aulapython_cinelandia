def maior(a, b):
    if a > b:
        return a 
    else:
        return b

n1 = int(input("digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:")) 

maior_numero = maior(n1, n2)
print(f" o maior numero entre {n1} e {n2} é : {maior_numero}")



   