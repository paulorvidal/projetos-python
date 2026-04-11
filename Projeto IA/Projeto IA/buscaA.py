from service import exibirResultados
from service import calcularDistancia
from service import avaliarVizinho
import time

def buscaA(tamanho, mapa):
    
    tempoInicio = time.time()
    nosExpandidos = 0
    pontoInicio = (0,0)
    pontoFinal = (tamanho - 1, tamanho -1)
    distanciaInicial = calcularDistancia(0, 0, pontoFinal[0], pontoFinal[1])  
    custoAcumulado = 0
    custoTotal = custoAcumulado + distanciaInicial
    fila = [(custoAcumulado, custoTotal, pontoInicio)]
    mapaNovo = []
    matrizPai = []

    for i in range(0, tamanho):
        matrizZeros = []
        for j in range (0, tamanho):
             matrizZeros.append(0)
        mapaNovo.append(matrizZeros)

    for i in range(0, tamanho):
        linhaPai = []
        for j in range(0, tamanho):
            linhaPai.append(None)
        matrizPai.append(linhaPai)
    
    nosExpandidos = 0

    mapaNovo[0][0] = 1

    while len(fila) > 0:
        fila.sort()
        custoTotal, custoAcumulado, v = fila.pop(0)

        nosExpandidos +=1
        linhaAtual = v[0]
        colunaAtual = v[1]

        if v == pontoFinal:
            break
            
        if colunaAtual + 1 < tamanho:
            avaliarVizinho(linhaAtual, colunaAtual + 1, custoAcumulado, v, pontoFinal, mapa, mapaNovo, matrizPai, fila)

        # ESQUERDA
        if colunaAtual - 1 >= 0:
            avaliarVizinho(linhaAtual, colunaAtual - 1, custoAcumulado, v, pontoFinal, mapa, mapaNovo, matrizPai, fila)

        # BAIXO
        if linhaAtual + 1 < tamanho:
            avaliarVizinho(linhaAtual + 1, colunaAtual, custoAcumulado, v, pontoFinal, mapa, mapaNovo, matrizPai, fila)

        # CIMA
        if linhaAtual - 1 >= 0:
            avaliarVizinho(linhaAtual - 1, colunaAtual, custoAcumulado, v, pontoFinal, mapa, mapaNovo, matrizPai, fila)

    tempoFim = time.time()
    tempoMs = (tempoFim - tempoInicio) * 1000

    if matrizPai[pontoFinal[0]][pontoFinal[1]] is not None:
        exibirResultados("Busca A*", pontoFinal, nosExpandidos, tempoMs, matrizPai, mapa)
    else:
        print('Nenhum caminho encontrado ')
        print('Nós expandidos: ', nosExpandidos)
        print('Tempo de execução: ', tempoMs, ' milissegundos')