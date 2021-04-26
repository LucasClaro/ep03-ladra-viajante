from Classes import Item, Viagem
import random


popQtd = 10 # 15 -> ruim # 20 -> ok até # 40 -> ou bom ou ruim


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

    pontos = 0
    if (TempoGasto > 72):
        pontos -= 10_000_000_000
    if (PesoCarregado > 20):
        pontos -= 10_000_000_000
    pontos += ValorRoubado - ValorGasto

    print(f"Valor Gasto: {ValorGasto}\nTempoGasto: {TempoGasto}\nValor Roubado: {ValorRoubado}\nValor Liquido: {pontos}\nPeso Carregado: {PesoCarregado}")


def mutar(individuo):
    valores = [1, 1, 2, 2, 2, 2, 2, 2, 3, 4]
    tipoMutacao = random.choice(valores)

    if (len(individuo) < 2):
        tipoMutacao = 3

    if (len(individuo) == len(itens)):
        tipoMutacao = 4


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
    return nova_lista[0:popQtd]

def ehValido(individuo):
    if(len(individuo) == len(set(individuo))):
        return True
    return False

def crossover(populacao, mutada):
    populacao_crossover = []
    for ind1 in populacao:
        for ind2 in mutada:
            # geracao do cross_over
            i = random.randint(0, min(len(ind1),len(ind2)) - 1)

            cross = ind1[0:i] + ind2[i:]
            over = ind2[0:i] + ind1[i:]

            if (ehValido(cross)):
                populacao_crossover.append(cross)
            if (ehValido(over)):
                populacao_crossover.append(over)
    return populacao_crossover


def comparaIndividuos(ind1,ind2):
    if(ind1 == None or ind2 == None):
        return False
    
    #print(f"fit Maior: {fitness(maiorIndividuoGerecao)}; fit pop[0]: {fitness(populacao[0])}")
    if fitness(ind1) != fitness(ind2):
        return False
    return True


print('Iniciando...')
random.seed()

populacao = [faz_individuo_inicial() for _ in range(0,popQtd)]

geracoes = 0
maxGeracoes = 70000
patience = 100 # paciencia de quantas populações sem mudar (vimos no TensorFlow pra evitar Overfitting, achos interessante de implementar aqui para agilizar)
patienceCount = 0
maiorIndividuoGerecao = None 

# Looping principal
while True:
    pop_mutada = [mutar(individuo) for individuo in populacao]
    pop_crossover = crossover(populacao, pop_mutada)

    populacao = selecao(populacao + pop_mutada + pop_crossover)
    
    
    if comparaIndividuos(maiorIndividuoGerecao, populacao[0]):
        patienceCount += 1
    else:
        patienceCount = 0
        maiorIndividuoGerecao = populacao[0].copy()
    
    geracoes += 1

    if (geracoes % 1000 == 0):
        print(geracoes)

    # critério de parada
    if geracoes == maxGeracoes or patienceCount == patience:
        break

print('Finalizado!')

populacao = sorted(populacao, key=fitness, reverse=True)

print()
print(f"Gerações: {geracoes}")
for item in populacao[0]:
    print(item)
print()

fitnessComPrint(populacao[0])