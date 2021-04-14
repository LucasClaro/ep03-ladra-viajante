from Classes import Item, Viagem
import random

itens = Item.buscarDados()
viagens = Viagem.buscarDados()

dicionarioViagens = Viagem.montarDicionario(viagens)

def faz_individuo_inicial():
    individuo = []
    aux = itens.copy()
    valores = [6, 7, 8]
    # for _ in range(random.choice(valores)):
    for _ in range(3):
        individuo.append(random.choice(aux))
        aux.remove(individuo[-1])
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

    print(f"Valor Gasto: {ValorGasto}\nTempo Gasto: {TempoGasto}\nValorRoubado: {ValorRoubado}\nPeso: {PesoCarregado}")

individuo = faz_individuo_inicial()
for gene in individuo:
    print(f"Item: {gene.nome}")
print()
fitness(individuo)




        
    