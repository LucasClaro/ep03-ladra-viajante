import csv

class Item():

    def __init__(self, nome, peso, tempo, valor, cidade):
        self.nome = nome
        self.peso = peso
        self.tempo = tempo
        self.valor = valor
        self.cidade = cidade

    @staticmethod
    def buscarDados():
        itens = []
        with open('itens.csv', 'r', encoding='utf-8') as f:
            dados = csv.reader(f)
            for dado in dados:
                itens.append(Item(dado[0], dado[1], dado[2], dado[3], dado[4]))
            return itens


class Viagem():

    def __init__(self, origem, destino, tempo, preco):
        self.origem = origem
        self.destino = destino
        self.tempo = tempo
        self.preco = preco

    @staticmethod
    def buscarDados():
        viagens = []
        with open('cidades.csv', 'r', encoding='utf-8') as f:
            dados = csv.reader(f)
            for dado in dados:
                viagens.append(Viagem(dado[0], dado[1], dado[2], dado[3]))
            return viagens

    @staticmethod
    def montarDicionario(viagens):
        dicionario = {}
        for viagem in viagens:
            tupla = (viagem.origem, viagem.destino)
            dicionario[tupla] = viagem
        return dicionario