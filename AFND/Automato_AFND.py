import json
import csv
import time
import sys

class AFND:
    def __init__(self, file_aut):
        initial_states = file_aut["initial"]
        if isinstance(initial_states, int):  # Verifica se é um único estado inicial (int) e converte em uma lista
            initial_states = [initial_states]
        self._initial_states = set(initial_states)
        self._final_states = file_aut["final"]
        self._transitions = file_aut["transitions"]
        self.result = []

    def operation(self, str_in_input):
        current_states = self._initial_states
        for word in str_in_input:
            current_states = self._get_next_states(current_states, word)
            if not current_states: # Adiciona esta condição para interromper a execução se não houver transição para a palavra lida
                break
        if any(state in self._final_states for state in current_states):
            return 'A'
        else:
          return 'R'

    def _get_next_states(self, current_states, word):
        next_states = []
        for transition in self._transitions:
            if transition["from"] == current_states and transition["read"] == word:
                if isinstance(transition["to"], int):
                    next_states.add(transition["to"])
                else:
                    next_states.update(transition["to"])        
        return list(next_states)

    def manipulating(self, string):
        self.result = [] # Limpa os resultados anteriores antes de executar o autômato
        self.current_states = []
        for word in string:
            next_states = []
            for state in self.current_states:
                state_transitions = self._get_next_states([state], word) #O |= atribuirá o valor após executar um OR entre duas variáveis, mas bit a bit
                next_states.update(state_transitions)
            if not self.current_states:
                break
        if any(state in self._final_states for state in self.current_states):
            return '1'
        else:
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
    automata = AFND(automata_file(file_aut_path))
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