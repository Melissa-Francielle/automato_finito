import json 
import csv 
import time
import sys

class Simulador:
    def __init__(self):
        self.estados = []
        self._estado_inicial = ''
        self._estado_final = []
        self.transicao = {}
        self._lista_resultados= []

    def Gerando_da_entrada(self, estados, estado_inicial, estado_final, delta, current, word):
        self._estado_inicial = estado_inicial
        #Ainda tentando como fazer essa parte

    def delta (self, q, states, word):
        for state in self.transicao[q][states]:
            self.fita(word, state)
        else:
            return -1
        
    def program(self, q, word):
        if (q == -1 or len(word) == 0):
            return q
        else:
            return self.program(self.transicao(q, word[0], word[1::]))
        
    def fita(self, transicoes, estadoInicial = 0):
        if (estadoInicial == 0):
            estadoInicial = self._estado_inicial
            
    def operacao (self, string_entrada):
        current = self._estado_inicial
        for word in string_entrada:
            current = self.next(current, word)
            if current is None:
                break
        if current in self._estado_final:
            return 'Aceita'
        else:
            return 'Rejeita'
        
    def _get_next (self, atual, word, estado_atual):
        for transicao in self.transicao:
            if transicao['from'] == atual and transicao['read'] == word:
                return transicao['to']
            if transicao ['from'] == estado_atual and transicao ['read'] == word or transicao['read'] == '&':
                if isinstance(transicao ['to'], int):
                    next.add(transicao['to'])
                else:
                    next.update(transicao['to'])
        return list(next)
    
    def manipulando(self, string):
        self.fita(string)
        if ("Aceita" in self._lista_resultados):
            self._lista_resultados = []
            return '1'
        if ("Rejeita" in self._lista_resultados):
            self._lista_resultados = []
            return '0'
        
    def automata_file(file_path):
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
    automata = Simulador.automata_file(file_aut_path)
    case_test = cases(file_teste_path)

    with open(file_out_path, 'w', newline='') as csv_file:
        writing = csv.writer(csv_file, delimiter=';')
        writing.writerow(["Palavra de entrada", "Resultado esperado", "Resultado obtido", "Tempo"])

        for testing in case_test:
            str_in_input, expected_result = testing
            start_time = time.perf_counter()
            result = automata.manipulating(str_in_input)
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
