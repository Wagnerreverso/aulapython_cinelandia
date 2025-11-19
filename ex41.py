def saudar(nome):
    return f"olá, {nome}! Seja bem-vindo(a) ao mundo python!!!"

nome_usuario = input("digite seu nome: ")

mensagem = saudar(nome_usuario)
print(mensagem)