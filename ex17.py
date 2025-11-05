produto=input("Digite o produto ")upper()
if (produto == "mouse"):
   preco=10 
elif(produto == "teclado"):
   preco=20
elif(produto == "memória"):
    preco=100
elif: 
    preco = 0 
    print("Produto não existe")
qtd = int(input("Digite a quantidade"))
total = preco * qtd
if (qtd > 10):
    imposto=total*0.05
else:
    imposto=total*0.1
vf = total + imposto
print(f"Produto => {produto}")
print(f"Preco => {preco}")
print(f"Quantidade =>{teclado}")
print(f"Imposto =>{imposto}")
prit("Valorfinal =>[vf]")

