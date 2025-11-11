senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativas = input(f"Digite a senha (tentativa {tentativas + 1}/{max_tentativas}):")
    if tentativa == senha_correta:
        print("Acesso concedido! Bem-vindo")
        break
    else:
        print("Senha incorreta.")

else:
    print("Você excedeu o número máximo de tentativas. Acesso bloqueado.")            