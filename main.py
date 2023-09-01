#Nome: Bryan Strey, Tiago de Brito Follador, Ricardo Vinicius Viana
conjuntos = []
conjuntos2 = []
aux1 = {0}
aux2 = {0}
aux1.clear()
aux2.clear()
sm = []
with open('TrabalhoNatureza.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        conjuntos.append(linha.split(","))
    for i in range(len(conjuntos)):
        set(conjuntos[i])
for i in range(len(conjuntos)):
    if conjuntos[i] == ['U']:
        aux1 = set(conjuntos[i+1])
        aux2 = set(conjuntos[i+2])
        print(f"União: conjunto 1 {aux1}, conjunto 2 {aux2}. Resultado: {aux1 | aux2}")
    elif conjuntos[i] == ['I']:
        aux1 = set(conjuntos[i + 1])
        aux2 = set(conjuntos[i + 2])
        print(f"Intersecção: conjunto 1 {aux1}, conjunto 2 {aux2}. Resultado: {aux1 & aux2}")
    elif conjuntos[i] == ['D']:
        aux1 = set(conjuntos[i + 1])
        aux2 = set(conjuntos[i + 2])
        print(f"Diferença: conjunto 1 {aux1}, conjunto 2 {aux2}. Resultado: {aux1 - aux2}")
    elif conjuntos[i] == ['C']:
        compl = {0}
        compl.clear()
        sm = []
        aux1 = set(conjuntos[i + 1])
        aux2 = set(conjuntos[i + 2])
        print(f"")
        for j in range(len(conjuntos[i+1])):
            for k in range(len(conjuntos[i+2])):
                sm.append(f"{conjuntos[i+1][j]} X {conjuntos[i+2][k]}")
                compl = set(sm)
        print(f"Produto cartesiano: conjunto 1 {aux1}, conjunto 2 {aux2}. Resultado {compl}")