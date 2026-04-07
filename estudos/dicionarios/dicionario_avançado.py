def saudacao():
    return "Olá! Eu sou uma função dentro de um dicionário."

pessoa = {
    "nome": "Henrique",              # string
    "idade": 28,                     # int
    "altura": 1.78,                  # float
    "ativo": True,                   # bool
    "hobbies": ["programar", "praia", "filosofia"],  # lista
    "habilidades": ("Python", "Git", "DevOps"),      # tupla
    "certificados": {"Python", "GitHub", "Linux"},   # conjunto (set)
    "endereco": {                    # outro dicionário
        "cidade": "São Paulo",
        "estado": "SP",
        "pais": "Brasil"
    },
    "nota_final": None,              # tipo None
    2025: "Ano atual",               # chave inteira
    (1, 2): "chave em forma de tupla",  # tupla também pode ser chave
    "funcao": saudacao               # função como valor
}

print(pessoa)
print(pessoa["funcao"]())  # chamando a função guardada no dicionário
