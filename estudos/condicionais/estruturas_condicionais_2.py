MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade < 0:
    print("Idade inválida.")
else:
    if idade >= MAIOR_IDADE:
        print("Você é maior de idade e pode tirar a CNH.")
    else:
        if idade == IDADE_ESPECIAL:
            print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
        else:
            print("Ainda não pode tirar a CNH.")
