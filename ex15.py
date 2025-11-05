#estudo de caso:
anonasc=int(input("digite o ano de nascimento "))
genero=input("Digite o sexo M ou F ").upper()
#print(anonasc)
#print(genero)
idade=2025-anonasc
if (idade >=18 and genero == "M"):
    print(" apto a se alistar")
else:
    print("Não apto")    
 