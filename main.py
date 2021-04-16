from Classes import Item, Viagem
import random

itens = Item.buscarDados()
viagens = Viagem.buscarDados()

dicionarioViagens = Viagem.montarDicionario(viagens)

def faz_individuo_inicial():
    individuo = []
    itensNaoRoubados = itens.copy()
    valores = [6, 7, 8]
    for _ in range(random.choice(valores)):
        individuo.append(random.choice(itensNaoRoubados))
        itensNaoRoubados.remove(individuo[-1])
    return individuo

    
def fitness(individuo):
    TempoGasto = 0
    PesoCarregado = 0
    ValorGasto = 0
    ValorRoubado = 0

    roubo = individuo[0]
    ValorGasto += int(dicionarioViagens[("Escondidos", roubo.cidade)].preco) if ("Escondidos", roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, "Escondidos")].preco)
    TempoGasto += int(dicionarioViagens[("Escondidos", roubo.cidade)].tempo) if ("Escondidos", roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, "Escondidos")].tempo)
    TempoGasto += int(roubo.tempo)
    ValorRoubado += int(roubo.valor)
    PesoCarregado += int(roubo.peso)

    rouboAnterior = roubo

    for roubo in individuo[1:-1]:
        ValorGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].preco) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].preco)
        TempoGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].tempo) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].tempo)
        TempoGasto += int(roubo.tempo)
        ValorRoubado += int(roubo.valor)
        PesoCarregado += int(roubo.peso)
        rouboAnterior = roubo

    roubo = individuo[-1]
    ValorGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].preco) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].preco)
    TempoGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].tempo) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].tempo)
    TempoGasto += int(roubo.tempo)
    ValorRoubado += int(roubo.valor)
    PesoCarregado += int(roubo.peso)

    ValorGasto += int(dicionarioViagens[(roubo.cidade, "Escondidos")].preco) if (roubo.cidade, "Escondidos") in dicionarioViagens else int(dicionarioViagens[("Escondidos", roubo.cidade)].preco)
    TempoGasto += int(dicionarioViagens[(roubo.cidade, "Escondidos")].tempo) if (roubo.cidade, "Escondidos") in dicionarioViagens else int(dicionarioViagens[("Escondidos", roubo.cidade)].tempo)

    pontos = 0
    if (TempoGasto > 72):
        pontos -= 10_000_000_000
    if (PesoCarregado > 20):
        pontos -= 10_000_000_000
    pontos += ValorRoubado - ValorGasto
    return pontos

def fitnessComPrint(individuo):
    TempoGasto = 0
    PesoCarregado = 0
    ValorGasto = 0
    ValorRoubado = 0

    roubo = individuo[0]
    ValorGasto += int(dicionarioViagens[("Escondidos", roubo.cidade)].preco) if ("Escondidos", roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, "Escondidos")].preco)
    TempoGasto += int(dicionarioViagens[("Escondidos", roubo.cidade)].tempo) if ("Escondidos", roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, "Escondidos")].tempo)
    TempoGasto += int(roubo.tempo)
    ValorRoubado += int(roubo.valor)
    PesoCarregado += int(roubo.peso)

    rouboAnterior = roubo

    for roubo in individuo[1:-1]:
        ValorGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].preco) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].preco)
        TempoGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].tempo) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].tempo)
        TempoGasto += int(roubo.tempo)
        ValorRoubado += int(roubo.valor)
        PesoCarregado += int(roubo.peso)
        rouboAnterior = roubo

    roubo = individuo[-1]
    ValorGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].preco) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].preco)
    TempoGasto += int(dicionarioViagens[(rouboAnterior.cidade, roubo.cidade)].tempo) if (rouboAnterior.cidade, roubo.cidade) in dicionarioViagens else int(dicionarioViagens[(roubo.cidade, rouboAnterior.cidade)].tempo)
    TempoGasto += int(roubo.tempo)
    ValorRoubado += int(roubo.valor)
    PesoCarregado += int(roubo.peso)

    ValorGasto += int(dicionarioViagens[(roubo.cidade, "Escondidos")].preco) if (roubo.cidade, "Escondidos") in dicionarioViagens else int(dicionarioViagens[("Escondidos", roubo.cidade)].preco)
    TempoGasto += int(dicionarioViagens[(roubo.cidade, "Escondidos")].tempo) if (roubo.cidade, "Escondidos") in dicionarioViagens else int(dicionarioViagens[("Escondidos", roubo.cidade)].tempo)

    print(f"Valor Gasto: {ValorGasto}\nTempoGasto: {TempoGasto}\nValor Roubado: {ValorRoubado}\nPeso Carregado: {PesoCarregado}")


def mutar(individuo):
    valores = [1, 2, 3, 4]
    tipoMutacao = random.choice(valores)

    if (len(individuo) < 2):
        tipoMutacao = 3

    if (len(individuo) == len(itens)):
        tipoMutacao = 4

    # print(len(individuo), tipoMutacao)

    if tipoMutacao == 1:
        #Inserir um item novo no início
        item = None
        while (True):
            item = random.choice(itens)
            if (item not in individuo):
                break

        individuo.insert(0, item)
    elif tipoMutacao == 2:
        #Substitue um elemento
        item = None
        while (True):
            item = random.choice(itens)
            if (item not in individuo):
                break

        posicao = random.choice(range(len(individuo)-1))

        individuo[posicao] = item
    elif tipoMutacao == 3:
        #Insere um item novo no fim
        item = None
        while (True):
            item = random.choice(itens)
            if (item not in individuo):
                break

        individuo.append(item)
    else:
        #Remove um elemento
        posicao = random.choice(range(len(individuo)-1))
        item = individuo[posicao]
        individuo.remove(item)
    return individuo

def selecao(lista):
    nova_lista = sorted(lista, key=fitness, reverse=True)
    return nova_lista[0:10]

# def crossover(populacao, mutada):
#     populacao_crossover = []
#     for ind1 in populacao:
#         for ind2 in mutada:
#             # geracao do cross_over
#             i = random.randint(0, len(meta) - 1)
#             populacao_crossover.append(ind1[0:i] + ind2[i:])
#             populacao_crossover.append(ind2[0:i] + ind1[i:])
#     return populacao_crossover

print('Iniciando...')
random.seed()

populacao = [faz_individuo_inicial() for _ in range(0,10)]

geracoes = 0
while True:
    pop_mutada = [mutar(individuo) for individuo in populacao]
    # pop_crossover = crossover(populacao, pop_mutada)

    # populacao = selecao(populacao + pop_mutada + pop_crossover)
    populacao = selecao(populacao + pop_mutada)
    
    geracoes += 1
    # if geracoes % 50 == 0:
    #     print(''.join(populacao[0]), geracoes)
    # critério de parada
    if geracoes == 1000:
        break
print('Finalizado!')

populacao = sorted(populacao, key=fitness, reverse=True)
for item in populacao[0]:
    print(item)
print()

fitnessComPrint(populacao[0])

# individuo = faz_individuo_inicial()
# for gene in individuo:
#     print(f"Item: {gene.nome}")
# print()
# fitness(individuo)




        
    