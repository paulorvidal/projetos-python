import os
import random
import sys
import time

def criarLabirinto(tamanho, parede):
    mapa = []
    for i in range(0, tamanho):
        x = []
        for j in range (0, tamanho):
             num1 = random.randint(0, 1)
             if num1 == 1:
                x.append(5)
             else: 
                x.append(2)
        mapa.append(x)
    
    paredesColocadas = 0
    while paredesColocadas < parede:
        aleatoriolinha = random.randint(0, tamanho-1)
        aleatoriocoluna = random.randint(0, tamanho-1)
        
        if (aleatoriolinha, aleatoriocoluna) != (0, 0) and (aleatoriolinha, aleatoriocoluna) != (tamanho - 1, tamanho - 1):
            if mapa[aleatoriolinha][aleatoriocoluna] != -1:
                mapa[aleatoriolinha][aleatoriocoluna] = -1
                
                paredesColocadas += 1

    mapa[0][0] = 'A' 
    mapa[tamanho - 1][tamanho - 1] = 'B'

    print('Labirinto') 

    for i in range(0, tamanho):
         for j in range (0, tamanho):
            valor = mapa[i][j]
            if valor == -1:
                print(f"{'■':>3}", end='') 
            else:
                print(f"{str(valor):>3}", end='')
         print()
    # mapa[tamanho -1][tamanho -1] = 'B'
    return mapa


def animarCaminho(nomeBusca, mapa, tamanho, caminho, matrizPai):
    os.system('') 
    time.sleep(1) 
    
    rastro = [] 
    linhas_do_grid = tamanho + 1 
    
    print("\n" * linhas_do_grid)
    sys.stdout.write(f"\033[{linhas_do_grid}A")
    sys.stdout.flush()
    
    for passo_atual in caminho:
        rastro.append(passo_atual)
        
        frame = f"Passo atual do {nomeBusca}: {passo_atual} \033[K\n"
        
        for linha in range(tamanho):
            for coluna in range(tamanho):
                
                if (linha, coluna) == (0,0):
                    frame += f"{'A':>3}"
                elif (linha, coluna) == (tamanho - 1, tamanho - 1):
                    frame += f"{'B':>3}"
                
                elif (linha, coluna) == passo_atual:
                    frame += f"{'X':>3}"
                    
                elif (linha, coluna) in rastro:
                    frame += f"{'*':>3}"
                    
                elif matrizPai[linha][coluna] is not None:
                    frame += f"{'-':>3}"
                    
                else:
                    valor = mapa[linha][coluna]
                    if valor == -1:
                        frame += f"{'■':>3}"
                    else:
                        frame += f"{str(valor):>3}"
            frame += "\n" 
            
        sys.stdout.write(frame)
        sys.stdout.flush()
        
        time.sleep(0.1) 

        sys.stdout.write(f"\033[{linhas_do_grid}A")
        sys.stdout.flush()
        
    sys.stdout.write(f"\033[{linhas_do_grid}B")
    print(f" {nomeBusca} concluída com sucesso!\n")
    
def calcularDistancia(linhaAtual, colunaAtual, proximaLinha, proximaColuna):
        diferencaLinha = linhaAtual - proximaLinha
        diferencaColuna = colunaAtual - proximaColuna

        if diferencaLinha < 0:
            diferencaLinha = diferencaLinha * -1

        if diferencaColuna < 0:
            diferencaColuna = diferencaColuna * -1

        return diferencaLinha + diferencaColuna

def avaliarVizinho(novaLinha, novaColuna, custoAcumulado, noPai, pontoFinal, mapa, mapaNovo, matrizPai, fila):
    terreno = mapa[novaLinha][novaColuna]
    
    if terreno == -1:
        return
        
    if terreno == 'B' or terreno == 'A':
        custoDoPasso = 0
    else:
        custoDoPasso = terreno 
        
    novoCustoAcumulado = custoAcumulado + custoDoPasso

    nunca_visitado = (mapaNovo[novaLinha][novaColuna] == 0 and (novaLinha, novaColuna) != (0,0))
    caminho_mais_barato = (mapaNovo[novaLinha][novaColuna] != 0 and novoCustoAcumulado < mapaNovo[novaLinha][novaColuna])
    
    if nunca_visitado or caminho_mais_barato:
        
        mapaNovo[novaLinha][novaColuna] = novoCustoAcumulado
        matrizPai[novaLinha][novaColuna] = noPai
        
        estimativa = calcularDistancia(novaLinha, novaColuna, pontoFinal[0], pontoFinal[1])
        
        custoTotal = novoCustoAcumulado + estimativa
        
        fila.append((custoTotal, novoCustoAcumulado, (novaLinha, novaColuna)))

def exibirResultados(nomeBusca, pontoFinal, nosExpandidos, tempoMs, matrizPai, mapa):
    caminho = []
    atual = pontoFinal
    while atual is not None:
        caminho.append(atual)
        atual = matrizPai[atual[0]][atual[1]]
      
    caminho.reverse()
    custoTotal = 0
    
    custoAcumulado = 0
    for coordenada in caminho:  
        linha = coordenada[0]
        coluna = coordenada[1]
        valorTerreno = mapa[linha][coluna]

        if isinstance(valorTerreno, int) and valorTerreno != -1:
            custoAcumulado += valorTerreno


    print(f"\nDeseja ver o caminho percorrido da {nomeBusca}? (s/n)")
    resposta = input().strip().lower() 
    if resposta == 's':
        animarCaminho(nomeBusca, mapa, len(mapa), caminho, matrizPai)
        print('Caminhos encontrados: ', caminho)
        print ('Nós expandidos: ', nosExpandidos)
        print('Tempo de execução:', tempoMs, 'milissegundos')
        print('Custo Acumulado: ', custoAcumulado)

   