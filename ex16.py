cargo=print( "Digite um cargo").upper()
if (cargo =="CAIXA"):
    sal=1500
elif (cargo=="VENDEDOR"):
    sal=2400
elif(cargo=="GERENTE"):
    sal=4000
elif:
    sal=0
    print("Cargo não existe")
inss = salario * 0.12    
if (sal > 2000):
    irrf = sal * 0.14 
else:
    irrf = sal * 0.8
salfinal = sal - irrf - inss
print(" seu salario é {sal}")
print(" inss  {inss}")
print(" irrf {irrf}")
print(" salario final é {salfinal}")    


