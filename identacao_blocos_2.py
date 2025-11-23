saldo = 500  # saldo global do cliente

def sacar(valor):
    global saldo

    if valor <= 0:
        print("Valor inválido para saque.")
        return False

    if saldo >= valor:
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
        print("Retire o seu dinheiro no caixa.")
        return True
    else:
        print("Saldo insuficiente para realizar o saque.")
        return False

def depositar(valor):
    global saldo

    if valor <= 0:
        print("Valor inválido para depósito.")
        return False

    saldo += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    return True


# Exemplo de uso
sacar(100)
print("Saldo atual:", saldo)
