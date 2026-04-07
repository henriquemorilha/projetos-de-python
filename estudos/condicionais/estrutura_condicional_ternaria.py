saldo = 5000
saque = 2150

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")