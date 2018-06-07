# 10x480.00
# 10x169.00

def checaChaves(exp):
    chaves = {"(":")", "{":"}", "[":"]"}
    # a pilha não pode estar vazia para não
    # levantar erro caso tenha um elemento
    # sem fechamento e tente dar .pop()
    pilha = [""]
    for b in exp:
        # se b estiver em chaves o fechamento é adicionado à pilha
        if b in chaves:
            pilha.append(chaves[b])
        # se b está entre os valores de brackets e não aparece
        # no topo da pilha o resultado é falso
        elif b in chaves.values() and b != pilha.pop():
            return False
    return pilha == [""]

print(checaChaves("{{()[}]}"))

