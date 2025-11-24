itens = ["mouse", "teclado", "monitor"]

remover = input("Digite o item para remover: ")

if remover in itens:
    itens.remove(remover)
    print("Item removido:", remover)
else:
    print("Item não encontrado.")

print("Lista atual:", itens)
