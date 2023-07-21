import json
import csv
import time
import sys

class AutomatoFinito:
    def __init__(self, aut_file):
        self.initial = aut_file["initial"]
        self.final = aut_file["final"]
        self.transitions = aut_file["transitions"]
    
    def run(self, input_str):
        current_state = self.initial
        
        for char in input_str:
            next_state = self._get_next_state(current_state, char)
            if next_state is None:
                return False
            current_state = next_state
        
        return current_state in self.final

    def _get_next_state(self, current_state, char):
        for transition in self.transitions:
            if transition["from"] == current_state and (transition["read"] == char or transition["read"] is None):
                return transition["to"]
        return None

def load_automato_from_file(file_path):
    with open(file_path) as f:
        return json.load(f)

def load_test_cases(file_path):
    test_cases = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Pula a primeira linha (cabeçalhos)cd
        for row in reader:
            if len(row) >= 2:  # Verifica se a linha tem pelo menos dois elementos
                test_cases.append((row[0], int(row[1])))
    return test_cases

def main(aut_file_path, test_file_path, output_file_path):
    automato = AutomatoFinito(load_automato_from_file(aut_file_path))
    test_cases = load_test_cases(test_file_path)
    
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["palavra de entrada", "resultadoesperado", "resultadoobtido", "tempo"])
        
        for test_case in test_cases:
            input_str, expected_result = test_case
            start_time = time.time()
            result = automato.run(input_str)
            end_time = time.time()
            execution_time = round(end_time - start_time, 3)
            writer.writerow([input_str, expected_result, int(result), execution_time])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python automato.py arquivo_do_automato.aut arquivo_de_testes.in arquivo_de_saida.out")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
