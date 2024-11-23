# Programa de Análise de Dados em JSON

## Descrição
Este programa em Python é uma aplicação simples que lê dados armazenados em um arquivo no formato JSON, realiza cálculos sobre os dados e exibe informações processadas. Ele foi projetado para processar informações de funcionários, como nome, cidade, idade e salário, permitindo calcular a média salarial e visualizar os dados de forma clara.

---

## Funcionalidades
- **Leitura de dados de um arquivo JSON**: Os dados são armazenados no arquivo `dados.txt` e convertidos para uma estrutura Python para processamento.
- **Cálculo da média salarial**: O programa calcula a média dos salários registrados no arquivo.
- **Exibição de dados**: Exibe a lista completa de informações de cada funcionário.

---

## Benefícios
- **Automatização**: Permite processar dados estruturados de maneira eficiente.
- **Flexibilidade**: O programa pode ser adaptado para trabalhar com outros conjuntos de dados JSON com atributos similares.
- **Legibilidade**: Exibe informações de forma clara e organizada, ideal para análises rápidas.
- **Facilidade de manutenção**: Código simples e modular que permite fácil modificação e expansão.

---

## Requisitos
- Python 3.x
- Biblioteca `json` (nativa do Python)

---

## Como Usar
1. Certifique-se de que o arquivo `dados.txt` contém dados no formato JSON válido. Aqui está um exemplo de como o arquivo deve ser estruturado:
    ```json
    [
        {"nome": "Jenifer", "cidade": "Aracaju", "idade": 25, "salario": 3500},
        {"nome": "Pedro", "cidade": "Aracaju", "idade": 32, "salario": 4200},
        {"nome": "Carlos", "cidade": "Salvador", "idade": 28, "salario": 2900},
        {"nome": "Maria", "cidade": "Recife", "idade": 41, "salario": 5000}
    ]
    ```

2. Execute o programa:
    ```bash
    python nome_do_programa.py
    ```

3. O programa exibirá a média salarial e a lista de funcionários diretamente no terminal.

---

## Estrutura do Código
- **`bancoFunc`**: Lê e converte o conteúdo do arquivo JSON para um objeto Python.
- **`calcMedia`**: Calcula a média dos salários com base nos dados fornecidos.
- **`imprimeLista`**: Exibe cada item da lista JSON.

---

## Exemplos de Saída
### Entrada:
```json
[
    {"nome": "Jenifer", "cidade": "Aracaju", "idade": 25, "salario": 3500},
    {"nome": "Pedro", "cidade": "Aracaju", "idade": 32, "salario": 4200}
]
