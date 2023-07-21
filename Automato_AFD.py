class Automato: #cria uma classe para que depois seja chamada em outros programas
    def _init_ (self): #utilizando a função para iniciar os objetos, utilizando o método init
     self.aut_estados = [] #lista
     self.aut_alfabeto = [] #lista
     self.aut_transicao = {} #dicionario
     self.estado_inicial = "" #string
     self.estado_finais = []  #lista
    #função self para referenciar o objeto e os atributos do objeto 


    def estados_repetidos (self, armazena):
        vetor = [] #cria um vetor para armazenar os dados de armazena
        for i in armazena: #a função for para percorrer por armazena
           if (i not in vetor): #com a condição caso i não esteja em vetor
              vetor.append(i) #então utiliza-se o método append para fazer um "linkagem" do valor aos outro dentro daquela lista de valores
        return vetor #retornar vetor sendo um novo conjunto
    
    def set_estados (self, aut_estados):
       self.aut_estados = self.estados_repetidos(aut_estados) #chama a função para verificar se existem estados repetidos 
       self.aut_estados.sort() #e utiliza a método sort para alterar a lista 

    def entrada (self, aut_estados, estado_inicial, estado_finais, delta):
        self.aut_estados = aut_estados(', ')
        self.estado_finais = estado_finais.split(', ')

    def initial_states(self, state): #verificação para ver se o estado inicial colocado faz parte do conjunto de estados   
        if state in self.aut_estado: #verifica se estado está nos estados e armazena no estado inicial 
            self.estado_inicial = state #esse estado armazenado a variavel estado inicial
        else:
            print("O estado inicial é inválido") #caso contrário o estado selecionado como inicial será dito como inválido

    def final_states (self, finais):
       finais = self.estados_repetidos(finais) #chama a função para verificar se há estados finais repetidos    
       for f in finais: #Com a função for percorre os estados 
            if f in finais: #Condição se f esta em finais
                if f in self.aut_estados: #Esta em estados finais
                    if f not in self.estado_final: #mas não esta em estado final
                        #então ele será adicionado com o método append de lista para ser armazenado nos estados finais
                        self.estado_final.append(f)
                    
    def delta (self, states, q, w):
        if states in self.t[q][w]:
            self.fita_automato 
    