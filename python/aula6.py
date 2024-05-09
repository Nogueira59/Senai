import random

def gerar_senha(tamanho=8):
    caracteres = '0123456789'
    senha = ''.join(random.choice(caracteres) for _ in range(4))
    return senha

def adivinhar_senha():
    senha = gerar_senha()
    tentativas = 3
    while tentativas > 0:
        tentativa = input("Digite a senha ({} tentativas restantes): ".format(tentativas))
        if tentativa == senha:
            print("Parabéns! Você acertou a senha.")
            return
        else:
            print("Senha incorreta. Tente novamente.")
            tentativas -= 1
    print("Suas tentativas acabaram. A senha era:", senha)

adivinhar_senha()
