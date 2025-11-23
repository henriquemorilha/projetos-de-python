valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra <= 0:
    print("Valor inválido.")
else:
    if valor_compra >= 500:
        print("Desconto aplicado: 20%")
    else:
        if valor_compra >= 300:
            print("Desconto aplicado: 10%")
        else:
            if valor_compra >= 100:
                print("Desconto aplicado: 5%")
            else:
                print("Sem desconto para compras abaixo de R$100.")
