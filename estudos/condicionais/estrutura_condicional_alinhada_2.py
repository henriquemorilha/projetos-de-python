conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    limite_total = saldo + cheque_especial

    if saque <= saldo:
        print("Saque realizado normalmente!")
    elif saque <= limite_total:
        print("Saque realizado usando cheque especial!")
    else:
        print("Saldo insuficiente mesmo com cheque especial.")

elif conta_universitaria:
    if saque <= saldo:
        print("Saque realizado normalmente!")
    else:
        print("Saldo insuficiente para conta universitária.")
        
else:
    print("Tipo de conta não identificado. Contate o gerente.")
