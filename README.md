<body>
    <h1>Simulador de Autômato Finito</h1>
    <p>Este é um trabalho referente a disciplina de Teoria da Computação do curso de Ciência da Computação pela Universidade Estadual do Norte do Paraná. </p>
  <p>Foi desenvolvido um simulador de autômatos finitos implementado em Python. O simulador é capaz de trabalhar com três tipos diferentes de autômatos:</p>
    <ol>
        <li>AFD (Autômato Finito Determinístico)</li>
        <li>AFND (Autômato Finito Não Determinístico)</li>
        <li>AFND-ε (Autômato Finito Não Determinístico com Transições Vazias)</li>
    </ol>
    <h2>Funcionamento</h2>
    <p>O simulador recebe três arquivos:</p>
    <ol>
        <li><strong>arquivo.json:</strong> Este arquivo contém as definições do autômato, incluindo estados, transições, estados finais e estado inicial.</li>
        <li><strong>entrada.csv:</strong> Este arquivo contém uma lista de palavras de entrada juntamente com os resultados esperados.</li>
        <li><strong>saida.csv:</strong> (opcional) Este arquivo será gerado pelo simulador e conterá os resultados da simulação.</li>
    </ol>
    <h3>Formato de entrada.csv</h3>
    <p>O arquivo de entrada deve seguir o seguinte formato:</p>
    <pre>
        Palavra de entrada;Resultado esperado
        aba;0
        cac;0
        abacac;1
        cacaba;1
    </pre>
    <p>Onde "0" representa REJEIÇÃO e "1" representa ACEITAÇÃO.</p>
    <h3>Formato de arquivo.json</h3>
    <p>O formato do arquivo JSON varia dependendo do tipo de autômato, mas geralmente inclui informações sobre estados iniciais, estados finais e transições. Abaixo está um exemplo simplificado de um arquivo JSON para um AFD:</p>
    <pre>
        {
            "initial": 0,
            "final": [11],
            "transitions": [
                { "from": 0, "read": "a", "to": 1 },
                { "from": 0, "read": "c", "to": 2 },
                // ...
            ]
        }
    </pre>
    <p>Para formatos específicos de JSON de diferentes tipos de autômatos, consulte os arquivos JSON de exemplo fornecidos.</p>
    <h2>Execução</h2>
    <p>Para executar o simulador, você pode utilizar o seguinte comando:</p>
    <pre>
        python simulador.py arquivo.json entrada.csv saida.csv
    </pre>
    <p>Onde:</p>
    <ul>
        <li><code>arquivo.json</code> é o arquivo JSON contendo as definições do autômato.</li>
        <li><code>entrada.csv</code> é o arquivo CSV com as palavras de entrada e resultados esperados.</li>
        <li><code>saida.csv</code> (opcional) é o arquivo de saída onde os resultados da simulação serão gravados.</li>
    </ul>
    <p>Certifique-se de ajustar os nomes dos arquivos de acordo com sua configuração específica.</p>
    <h2>Tipos de Autômatos Suportados</h2>
    <h3>AFD (Autômato Finito Determinístico)</h3>
    <p>O simulador é capaz de simular autômatos finitos determinísticos (AFD). Para configurar um AFD, você pode seguir o formato de arquivo JSON fornecido no exemplo.</p>
    <h3>AFND (Autômato Finito Não Determinístico)</h3>
    <p>O simulador também é capaz de simular autômatos finitos não determinísticos (AFND). Os detalhes da configuração do AFND podem ser encontrados no arquivo JSON de exemplo correspondente.</p>
    <h3>AFND-ε (Autômato Finito Não Determinístico com Transições Vazias)</h3>
    <p>Para autômatos finitos não determinísticos com transições vazias (AFND-ε), você pode configurar o arquivo JSON de acordo com as especificações correspondentes.</p>
    <h2>Exemplos de Configuração</h2>
    <p>Exemplos de arquivos JSON para cada tipo de autômato estão disponíveis nos seguintes links:</p>
    <ul>
        <li><a href="https://github.com/Melissa-Francielle/automato_finito/blob/main/Simulador%20de%20Automato%20finito/automato_AFD.json">JSON para AFD</a></li>
        <li><a href="https://github.com/Melissa-Francielle/automato_finito/blob/main/Simulador%20de%20Automato%20finito/Automato_AFND_e.json">JSON para AFND</a></li>
        <li><a href="https://github.com/Melissa-Francielle/automato_finito/blob/main/Simulador%20de%20Automato%20finito/Automato_AFND_e.json">JSON para AFND-ε</a></li>
    </ul>
    <p>Certifique-se de ajustar a configuração do arquivo JSON conforme necessário para representar o seu autômato específico.</p>
  <p>Exemplos de arquivos de ENTRADA para cada tipo de autômato estão disponíveis nos seguintes links:</p>
    <ul>
        <li><a href="https://github.com/Melissa-Francielle/automato_finito/blob/main/Simulador%20de%20Automato%20finito/entrada_AFD.csv">ENTRADA para AFD</a></li>
        <li><a href="https://github.com/Melissa-Francielle/automato_finito/blob/main/Simulador%20de%20Automato%20finito/entrada_AFND.csv">ENTRADA para AFND</a></li>
        <li><a href="https://github.com/Melissa-Francielle/automato_finito/blob/main/Simulador%20de%20Automato%20finito/entradaVazio.csv">ENTRADA para AFND-ε</a></li>
    </ul>
    <p>Certifique-se de ajustar a configuração do arquivo de ENTRADA conforme necessário para representar o seu autômato específico.</p>
    <p>Agora você está pronto para usar este simulador de autômato finito para testar diferentes autômatos e verificar se eles aceitam ou rejeitam palavras de entrada específicas.</p>
</body>

</html>
