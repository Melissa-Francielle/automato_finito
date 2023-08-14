import json 
import csv 
import time
import sys

class Simulador:
    def __init__(self):
        self.estados = []
        self.estado_inicial = ' '
        self.estados_finais = []
        self.transicoes = {}
        self.estados_atuais = []
        self.resultados = []
        self.transicoes_vazias = []
        self.tipo_automato = ''

    def gera_entrada(self, transicoes_vazias, estados_atuais, estado_inicial):
        self.estado_inicial = estado_inicial
        self.estados_atuais = []
        self.estados_atuais.append(self.estado_inicial)
        if " " in self.transicoes[self.estado_inicial - 1]:
            self.transicoes_vazias(self.estado_inicial)

    def delta(self, q, word):
        proximos_estado = set()

        if q in self.transicoes and word in self.transicoes[q]:
            proximos_estado.update(self.transicoes[q][word])

        if self.tipo_automato == 'AFND' or self.tipo_automato == 'AFND-epsilon':
            if q in self.transicoes and "" in self.transicoes[q]:
                proximos_estado.update(self.transicoes[q][''])

        return proximos_estado

    def program(self, q, word):
        if q == -1 or len(word) == 0:
            return q
        
        proximos_estados = set()

        for simbolo in word:
            if q in self._delta and simbolo in self.transicoes[q]:
                proximos_estados.update(self.transicoes[q][simbolo])
        
        novos_estados = set()

        for estados in proximos_estados:
            if '' in self.transicoes[estados]:
                novos_estados.update(self.transicoes[estados][''])

        for estados in proximos_estados:
            resultado = self.program(estados, word[1:])

            if resultado != -1:
                return resultado
        
        return -1

    def _get_next (self, atual, word, estado_atual):
        proximo_estado = set()

        for transicoes in self.delta(atual, word):
            proximo_estado.update(transicoes)
        
        if '' in self.transicoes[estado_atual]:
            for transicoes in self.transicoes[estado_atual]['']:
                proximo_estado.update(self.delta(transicoes, word))

        return [proximo_estado]

    def le_fita(self, transicao, s_inicial=0):
        if (s_inicial == 0):
            s_inicial = self._estado_inicial

        estados_finais = set()

        if self.tipo_automato == 'AFD':
            estados_finais.update(self._estados_finais)
        elif self.tipo_automato == "AFND" or self.tipo_automato == "AFND-epsilon":
            estados_finais.update(self._estados_finais)
            for estados in self.transicoes(s_inicial, ''):
                estados_finais.update(self.transicoes(estados, ''))

        proximos_estados = {s_inicial}    
        for simbolo in transicao:
            novo_estado = set()
            for estado in proximos_estados:
                novo_estado.update(self.transicoes(estado, simbolo))
            proximos_estados = novo_estado

        if(estados in estados_finais for estados in proximos_estados):
            self.resultados.append('Aceita')
        else:
            self.resultados.append('Reijeita')

    def manipulacao (self, string):
        self.le_fita(string)
        if'Aceita' in self.resultados:
            self.resultados = []
            return 1
        if 'Reijeita' in self.resultados:
            return 0
            self._resultados = []

def arquivo_automato(file_path):
        with open(file_path) as file:
            return json.load(file)

def cases(file_path):
    test = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for line in reader:
            if len(line) >= 2:
                str_in_input = line[0]
                expected_result = int(''.join(filter(str.isdigit, line[1].strip())))
                test.append((str_in_input, expected_result))
    return test

def main(file_aut_path, file_teste_path, file_out_path):
    automata = Simulador(arquivo_automato(file_aut_path))
    case_test = cases(file_teste_path)

    with open(file_out_path, 'w', newline='') as csv_file:
        writing = csv.writer(csv_file, delimiter=';')
        writing.writerow(["Palavra de entrada", "Resultado esperado", "Resultado obtido", "Tempo"])

        for testing in case_test:
            str_in_input, expected_result = testing
            start_time = time.perf_counter()
            result = automata.manipulacao(str_in_input)
            end_time = time.perf_counter()

            execution_time = "{:.5f}".format(end_time - start_time)  # Formatação com cinco casas decimais
            writing.writerow([str_in_input, expected_result, result, execution_time])
            csv_file.flush()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Ordem para acessar o arquivo: python arquivo tipo ->(.py) arquivo tipo ->(.json) arquivo do tipo-> (.csv) nome do arquivo de saida tipo -> (.out)")
        #python Automato_e_AFND.py aut_e_afnd.json entrada_AFND.csv saida.out
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
