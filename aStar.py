from ast import AST
from cmath import pi
import numpy as np

class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo #Nome
        self.visitado = False #se o vertice foi visitado
        self.distancia_objetivo = distancia_objetivo #a distância do vertice do objetivo
        self.adjacentes = [] #vertices vizinhos a este vertice

    def add_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_astar = vertice.distancia_objetivo + self.custo

class Grafo:
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)  

    arad.add_adjacente(Adjacente(zerind, 75))
    arad.add_adjacente(Adjacente(sibiu, 140))
    arad.add_adjacente(Adjacente(timisoara, 118))
    
    zerind.add_adjacente(Adjacente(arad, 75))
    zerind.add_adjacente(Adjacente(oradea, 71))

    oradea.add_adjacente(Adjacente(zerind, 71))
    oradea.add_adjacente(Adjacente(sibiu, 151))

    sibiu.add_adjacente(Adjacente(oradea, 151))
    sibiu.add_adjacente(Adjacente(arad, 140))
    sibiu.add_adjacente(Adjacente(fagaras, 99))
    sibiu.add_adjacente(Adjacente(rimnicu, 80))

    timisoara.add_adjacente(Adjacente(arad, 118))
    timisoara.add_adjacente(Adjacente(lugoj, 111))
    
    lugoj.add_adjacente(Adjacente(timisoara, 111))
    lugoj.add_adjacente(Adjacente(mehadia, 70))

    mehadia.add_adjacente(Adjacente(lugoj, 70))
    mehadia.add_adjacente(Adjacente(dobreta, 75))
    
    dobreta.add_adjacente(Adjacente(mehadia, 75))
    dobreta.add_adjacente(Adjacente(craiova, 120))
    
    craiova.add_adjacente(Adjacente(dobreta, 120))
    craiova.add_adjacente(Adjacente(pitesti, 138))
    craiova.add_adjacente(Adjacente(rimnicu, 146))
    
    rimnicu.add_adjacente(Adjacente(craiova, 146))
    rimnicu.add_adjacente(Adjacente(sibiu, 80))
    rimnicu.add_adjacente(Adjacente(pitesti, 97))
    
    fagaras.add_adjacente(Adjacente(sibiu, 99))
    fagaras.add_adjacente(Adjacente(bucharest, 211))

    pitesti.add_adjacente(Adjacente(craiova, 138))
    pitesti.add_adjacente(Adjacente(bucharest, 101))

    bucharest.add_adjacente(Adjacente(sibiu, 211))
    bucharest.add_adjacente(Adjacente(pitesti, 101))
    bucharest.add_adjacente(Adjacente(giurgiu, 90))

    giurgiu.add_adjacente(Adjacente(bucharest, 90))

grafo = Grafo()

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #Mudança no tipo de dados
        self.valores = np.empty(self.capacidade, dtype=object)
    
    #Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1): #percorre o vetor
            posicao = i
            if self.valores[i].distancia_astar > adjacente.distancia_astar:
                break
            if i == self.ultima_posicao: #atualiza a última posição
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x] #desloca o valor para a inserir
            x-=1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, '; ',
                self.valores[i].custo, ' - ',
                self.valores[i].vertice.distancia_objetivo, ' - ',
                self.valores[i].distancia_astar)

class AStar:
    def __init__(self, objetivo):
        self.objetivo = objetivo # self.parametro -> atributo
        self.encontrado = False
    def buscar(self, atual): #função de teste de objetivo
        print('-----------------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True #marca o atual como visitado

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes)) #cria um vetor ordenado com o tamanho da quantidade de ajdacentes
            for adjacente in atual.adjacentes: #percorre a lista de vizinhos do grafo atual
                if adjacente.vertice.visitado == False: # se o vizinho ainda não foi visitado
                    adjacente.vertice.visitado = True #marcar como visitado
                    vetor_ordenado.insere(adjacente) #inserir dentro do vetor ordenado como um vizinho do nó atual
            vetor_ordenado.imprime() #mostra os vizinhos do nó atual

            if vetor_ordenado.valores[0] != None: #se o vetor ordenado tiver algum objeto no início
                self.buscar(vetor_ordenado.valores[0].vertice) #busca pelo início do vetor ordenado

busca_astar = AStar(grafo.bucharest)
busca_astar.buscar(grafo.dobreta)