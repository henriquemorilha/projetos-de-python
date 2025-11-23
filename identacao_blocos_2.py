saldo = 500

def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")
    else:
        print("Saldo insuficiente.")

    print("Obrigado por ser nosso cliente!")

def depositar(valor):
    global saldo
    saldo += valor
    print("Depósito realizado com sucesso!")


sacar(100)
print("Saldo atual:", saldo)

