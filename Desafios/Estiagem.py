"""
Devido às constantes estiagens que aconteceram nos últimos tempos em algumas regiões do Brasil, 
o governo federal criou um órgão para a avaliação do consumo destas regiões com finalidade de verificar 
o comportamento da população na época de racionamento. Este órgão responsável irá pegar algumas cidades (por amostragem) 
e verificará como está sendo o consumo de cada uma das pessoas da cidade e o consumo médio de cada cidade por habitante.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*106), 
indicando a quantidade de imóveis. As N linhas contém um par de valores X (1 ≤ X ≤ 10) e Y (1 ≤ Y ≤ 200), 
indicando a quantidade de moradores de cada imóvel e o respectivo consumo total de cada imóvel (em m3). 
Com certeza, nenhuma residência consome mais do que 200 m3 por mês. 
O final da entrada é representado pelo número zero.

Saída
Para cada entrada, deve-se apresentar a mensagem “Cidade# n:”, 
onde n é o número da cidade seguindo a sequência (1, 2, 3, ...) e em seguida deve-se listar, 
por ordem ascendente de consumo, a quantidade de pessoas seguido de um hífen e o consumo destas pessoas, 
arredondando o valor para baixo. Na terceira linha da saída deve-se mostrar o consumo médio por pessoa da cidade, 
com 2 casas decimais sem arredondamento, considerando o consumo real total. 
Imprimir uma linha em branco entre dois casos de teste consecutivos. No fim da saída não deve haver uma linha em branco.
"""

from math import floor
import math

cidade = 1
while True:
    
    N = int(input("Quantidade de moveis: "))
    if N == 0:
        break

    consumos = {}
    total_pessoas = 0
    total_consumo = 0

    for i in range(N):
        moradores, consumo = map(int, input().split())

        consumo_por_pessoa = consumo // moradores
        if consumo_por_pessoa not in consumos:
            consumos[consumo_por_pessoa] = moradores
        else:
            consumos[consumo_por_pessoa] += moradores

        total_pessoas += moradores
        total_consumo += consumo

    ordenar = sorted(consumos.items())

    print(f"Cidade# {cidade}:")
    print(' '.join([f"{v}-{k}" for k, v in ordenar]))
    media = total_consumo / total_pessoas
    print(f"Consumo medio: {math.floor(media * 100) / 100:.2f} m3")
    cidade +=1
   
    




    


