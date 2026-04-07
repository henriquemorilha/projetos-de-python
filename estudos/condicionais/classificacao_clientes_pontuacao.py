pontos = int(input("Informe sua pontuação no sistema de fidelidade: "))

if pontos < 0:
    print("Pontuação inválida.")

else:
    if pontos >= 1000:
        print("Cliente categoria DIAMOND!")
        if pontos >= 3000:
            print("Bônus extra: acesso VIP e 20% de desconto.")
        else:
            print("Benefícios: 10% de desconto e suporte prioritário.")

    elif pontos >= 500:
        print("Cliente categoria GOLD!")
        if pontos >= 700:
            print("Benefício adicional: frete grátis.")
        else:
            print("Benefício: 5% de desconto.")

    elif pontos >= 200:
        print("Cliente categoria SILVER!")
        print("Benefício: cupom de R$10.")

    else:
        print("Cliente categoria BRONZE!")
        print("Sem benefícios adicionais.")
