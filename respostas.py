import json
"""
1 - Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
    Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
    Imprimir(SOMA);
    Ao final do processamento, qual será o valor da variável SOMA?
    R: 91
"""


INDICE = 13
SOMA = 0
K = 0
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

"""
2-  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
    (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a
    sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

def isNumberInFibonacci(x):
    fibonacci = [0, 1]

    while fibonacci[-1] < x:
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)

    if x in fibonacci:
        return f"{x} pertence à sequência de Fibonacci."
    else:
        return f"{x} não pertence à sequência de Fibonacci."
    


"""
3 - Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
    • O menor valor de faturamento ocorrido em um dia do mês; R: 373,78
    • O maior valor de faturamento ocorrido em um dia do mês; R: 48.924,24
    • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal; R: 10

    Obs.: As respostas são sobre o json localizado na pasta db.
"""

def billingAnalyze(path_json):
    with open(path_json, "r") as file:
        data = json.load(file)
    
    faturamento = [dia['valor'] for dia in data if dia['valor'] > 0]

    menor_faturamento = min(faturamento)

    maior_faturamento = max(faturamento)

    media_mensal = sum(faturamento) / len(faturamento)

    dias_acima_da_media = [{"dia": faturamento['dia'], "valor": faturamento['valor']} for faturamento in data if faturamento['valor'] > media_mensal]


    return f"""
Menor valor de faturamento: {menor_faturamento:.2f}
Maior valor de faturamento: {maior_faturamento:.2f}
Número de dias com faturamento acima da média: {len(dias_acima_da_media)}.
Detalhamento dias acima da média:
{json.dumps(dias_acima_da_media, indent=4)}
    """


"""
5 - Escreva um programa que inverta os caracteres de um string.

    IMPORTANTE:
    a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
    b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def reverse_string(string):
    inverted_string = ""

    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]

    return inverted_string


# Utilizando as funções para gerar as respostas:
print(SOMA) # 91

numero = int(input("Informe um número: "))
print(isNumberInFibonacci(numero)) # Você deve testar com o número que desejar

print(billingAnalyze("db/dados.json")) # Menor valor de faturamento: 373.78 ; Maior valor de faturamento: 48924.24 ; Número de dias com faturamento acima da média: 10.


print(reverse_string("Werricsson")) # nosscirreW