# Simulador de automato_finito
Implementação de um simulador de automato finito feito em linguagem Python.
Os tipos de automatos simulados:
- AFD
- AFND
- AFND-e

## Funcionamento
Para seu funcionamento o simulador receber um arquivo.json que irá conter as transições, estados finais e estado inicial, também será recebido uma entrada.csv e o programa de deve devolver uma saída podendo ser um arquivo.txt. 
Na entrada CSV apresenta a seguinte ordem:
### Palavra de entrada, Resultado esperado, Resultado obtido, Tempo
Sendo 0 = REIJEITA
E 1 = ACEITA

## Arquivo.json 
# AFD   
Entrada CSV:  
aba;0  
cac;0  
abacac;1  
cacaba;1  

"initial": 0,
"final": [11],
"transitions": [  
{ "from": 0, "read": "a", "to": 1 },  
{ "from": 0, "read": "c", "to": 2 },  
[...]  
O restante do arquivo.json do AFD pode ser encontrado nesse link [JSON](https://github.com/Melissa-Francielle/automato_finito/blob/main/Simulador%20de%20Automato%20finito/automato_AFD.json)

