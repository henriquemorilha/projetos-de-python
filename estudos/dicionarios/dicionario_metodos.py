# -------------------------------------------
# Dicionário base para os testes
# -------------------------------------------
pessoa = {
    "nome": "Henrique",
    "idade": 28,
    "cidade": "São Paulo"
}
print("Dicionário inicial:", pessoa)


# -------------------------------------------
# 1. copy() – cria uma cópia rasa do dicionário
# -------------------------------------------
pessoa_copia = pessoa.copy()
print("\nCópia do dicionário:", pessoa_copia)


# -------------------------------------------
# 2. fromkeys() – cria novo dict com chaves de um iterável
# -------------------------------------------
novo_dict = dict.fromkeys(["a", "b", "c"], 0)
print("\nDicionário criado com fromkeys:", novo_dict)


# -------------------------------------------
# 3. get() – obtém valor de forma segura
# -------------------------------------------
print("\nNome usando get:", pessoa.get("nome"))
print("Telefone usando get (com valor padrão):", pessoa.get("telefone", "não informado"))


# -------------------------------------------
# 4. items() – retorna pares (chave, valor)
# -------------------------------------------
print("\nitems():")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# -------------------------------------------
# 5. keys() – retorna apenas as chaves
# -------------------------------------------
print("\nkeys():", pessoa.keys())


# -------------------------------------------
# 6. values() – retorna apenas os valores
# -------------------------------------------
print("values():", pessoa.values())


# -------------------------------------------
# 7. pop() – remove uma chave específica
# -------------------------------------------
idade_removida = pessoa.pop("idade")
print("\nIdade removida com pop:", idade_removida)
print("Dicionário após pop:", pessoa)


# -------------------------------------------
# 8. popitem() – remove o último item inserido
# -------------------------------------------
ultimo_item = pessoa.popitem()
print("\nItem removido com popitem:", ultimo_item)
print("Dicionário após popitem:", pessoa)


# -------------------------------------------
# 9. setdefault() – retorna valor ou cria chave com valor padrão
# -------------------------------------------
valor_cpf = pessoa.setdefault("cpf", "000.000.000-00")
print("\nsetdefault (cpf criado):", valor_cpf)
print("Dicionário após setdefault:", pessoa)


# -------------------------------------------
# 10. update() – atualiza ou adiciona valores
# -------------------------------------------
pessoa.update({"nome": "Henrique Morilha", "idade": 29})
print("\nDicionário após update:", pessoa)


# -------------------------------------------
# 11. clear() – remove tudo do dicionário
# -------------------------------------------
pessoa.clear()
print("\nDicionário após clear:", pessoa)
