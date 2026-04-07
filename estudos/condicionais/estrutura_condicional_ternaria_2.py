saldo = 5000
saque = 2130

novo_saldo = saldo - saque if saldo >= saque else saldo
mensagem   = "Saque aprovado" if saldo >= saque else "Saque negado"

print(mensagem)
print("Saldo final:", novo_saldo)
