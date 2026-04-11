from service import exibirResultados
from service import calcularDistancia
import time

def buscaGulosa(tamanho, mapa):
    
    tempoInicio = time.time()
    nosExpandidos = 0
    pontoInicio = (0,0)
    pontoFinal = (tamanho - 1, tamanho -1)
    distanciaInicial = calcularDistancia(0, 0, pontoFinal[0], pontoFinal[1])  
    fila = [(distanciaInicial, pontoInicio)]
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
        distanciaAtual, v = fila.pop(0)

        nosExpandidos +=1
        linhaAtual = v[0]
        colunaAtual = v[1]

        if v == pontoFinal:
            break
            
        if colunaAtual + 1 < tamanho:
            if mapaNovo[linhaAtual][colunaAtual + 1] == 0 and mapa[linhaAtual][colunaAtual + 1 ] != -1:
                
                mapaNovo[linhaAtual][colunaAtual + 1] = 1

                distancia = calcularDistancia(linhaAtual, colunaAtual + 1, pontoFinal[0], pontoFinal[1])

                fila.append((distancia, (linhaAtual, colunaAtual + 1)))

                matrizPai[linhaAtual][colunaAtual + 1] = v


        if colunaAtual - 1 >= 0:
            if mapaNovo[linhaAtual][colunaAtual - 1] == 0 and mapa[linhaAtual][colunaAtual - 1] != -1:
                
                mapaNovo[linhaAtual][colunaAtual - 1] = 1

                distancia = calcularDistancia(linhaAtual, colunaAtual - 1, pontoFinal[0], pontoFinal[1])

                fila.append((distancia, (linhaAtual, colunaAtual - 1)))

                matrizPai[linhaAtual][colunaAtual - 1] = v


        if linhaAtual + 1 < tamanho:
            if mapaNovo[linhaAtual + 1][colunaAtual] == 0 and mapa[linhaAtual + 1][colunaAtual] != -1:
                
                mapaNovo[linhaAtual + 1][colunaAtual] = 1

                distancia = calcularDistancia(linhaAtual + 1, colunaAtual, pontoFinal[0], pontoFinal[1])

                fila.append((distancia, (linhaAtual + 1 , colunaAtual)))

                matrizPai[linhaAtual + 1][colunaAtual] = v


        if linhaAtual - 1 >= 0:
            if mapaNovo[linhaAtual - 1][colunaAtual] == 0 and mapa[linhaAtual - 1][colunaAtual] != -1:
                
                mapaNovo[linhaAtual - 1][colunaAtual] = 1

                distancia = calcularDistancia(linhaAtual - 1, colunaAtual, pontoFinal[0], pontoFinal[1])

                fila.append((distancia, (linhaAtual - 1, colunaAtual)))

                matrizPai[linhaAtual - 1][colunaAtual] = v

    tempoFim = time.time()
    tempoMs = (tempoFim - tempoInicio) * 1000

    if matrizPai[pontoFinal[0]][pontoFinal[1]] is not None:
        exibirResultados("Busca Gulosa", pontoFinal, nosExpandidos, tempoMs, matrizPai, mapa)
    else:
        print('Nenhum caminho encontrado ')
        print('Nós expandidos: ', nosExpandidos)
        print('Tempo de execução: ', tempoMs, ' milissegundos')