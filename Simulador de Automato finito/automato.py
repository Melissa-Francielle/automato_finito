import json
import csv
import time

class AutomatoNFA:
    def __init__(self, transitions):
        self.transitions = transitions
        self.current_states = set()

    def operation(self, input_str):
        self.current_states = set([0])  # Inicializa com o estado inicial
        for char in input_str:
            self.step(char)
        return 1 if any(state in self.transitions['final'] for state in self.current_states) else 0

    def step(self, char):
        next_states = set()
        for state in self.current_states:
            for transition in self.transitions['transitions']:
                if transition['from'] == state and (transition['read'] == char or transition['read'] is None):
                    next_states.add(transition['to'])
        self.current_states = next_states

def automata_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            automaton_data = json.load(json_file)
        return automaton_data
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON {file_path}. Verifique o formato.")
        return None

def cases(file_path):
    test_cases = []
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader)  # Pula a linha de cabeçalho
            for row in csv_reader:
                input_str = row[0]
                expected_result = int(row[1])
                test_cases.append((input_str, expected_result))
        return test_cases
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return []
    except csv.Error:
        print(f"Erro ao ler o arquivo CSV {file_path}. Verifique o formato.")
        return []

def main():
    file_aut_path = 'arquivo.json'
    file_teste_path = 'entrada.csv'
    file_out_path = 'saida.csv'

    automata = AutomatoNFA(automata_file(file_aut_path))
    case_test = cases(file_teste_path)

    with open(file_out_path, 'w', newline='') as csv_file:
        writing = csv.writer(csv_file, delimiter=';')
        writing.writerow(["Palavra de entrada", "Resultado esperado", "Resultado obtido", "Tempo"])

        for str_in_input, expected_result in case_test:
            start_time = time.perf_counter()
            result = automata.operation(str_in_input)
            end_time = time.perf_counter()

            execution_time = "{:.5f}".format(end_time - start_time)  # Formatação com cinco casas decimais
            writing.writerow([str_in_input, expected_result, result, execution_time])
            csv_file.flush()

if __name__ == "__main__":
    main()
