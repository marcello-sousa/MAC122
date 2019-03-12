''' Marcelo de Sousa, nº USP: 4897669, Prof. MAnoel Marcilio '''

import pilha
from time import time

'''Funcao que compara item a item dois elementos da lista TAB, returndo True se i <= j, False caso contrario'''

def compara(i, j):
    if   i[0:40]  < j[0:40]:  return True  #nome
    elif i[0:40]  > j[0:40]:  return False
    if   i[44:48] < j[44:48]: return True  #ano
    elif i[44:48] > j[44:48]: return False
    if   i[42:44] < j[42:44]: return True  #mes
    elif i[42:44] > j[42:44]: return False  
    if   i[40:42] < j[40:42]: return True  #dia
    elif i[40:42] > j[40:42]: return False 
    if   i[48:57] < j[48:57]: return True  #ident
    elif i[48:57] > j[48:57]: return False
    return True

''' Função que particiona a lista '''

def particiona(lista, inicio, fim):
    i, j = inicio, fim
    pivo = lista[fim]
    while True:
        while i < j and compara(lista[i], pivo):
            i = i + 1
        if i < j:
            lista[i], lista[j] = pivo, lista[i]
        else: break
        while i < j and compara(lista[j], pivo) is False:
            j = j - 1
        if i < j: 
            lista[i], lista[j] = lista[j], pivo
        else: break
    return i

''' Funcao recursiva Quick Sort '''

def QuickRecursivo( TAB, inicio, fim):
    if inicio < fim:
        k = particiona( TAB, inicio, fim)
        QuickRecursivo( TAB, inicio, k-1)
        QuickRecursivo( TAB, k+1, fim)

''' Funcao que chama o metodo quick recursivo '''

def ClassQuickRecursivo( TAB):
    QuickRecursivo( TAB, 0, len(TAB)-1)

''' Funcao interativa Quick Sort, que utiliza o modulo pilha '''

def QuickNaoRecursivo( TAB, inicio, fim):
    p = pilha.Pilha()
    p.push((0, len(TAB) - 1))
    while not p.is_empty():
        inicio, fim = p.pop()
        if fim - inicio > 0:
            k = particiona( TAB, inicio, fim)
            p.push((inicio, k - 1))
            p.push((k + 1, fim))

''' Funcao que chama o metodo quick interativo'''

def ClassQuickNaoRecursivo( TAB):
    QuickNaoRecursivo( TAB, 0, len(TAB)-1)
  
'''Funcao que grava numa lista os itens do arquivo, retornando a lista com itens e o numero registro que
serao classificados, nessa funcao inclui na lista apenas as linhas do arquivos que possuiam tamanho igual
a 57, excluido tamanhos maiores e menores, pois como a funcao compara possui uma indexacao fixa ocasionaria
erro na ordenacao'''
  
def ArmazenaLista( ArquivoOrigem):
    arquivo = open( ArquivoOrigem, "r")
    registro, Tab = 0, []
    for linha in arquivo:
        if len(linha) == 57: 
            Tab.append(linha)
            registro += 1
    arquivo.close()
    return Tab, registro

''' Funcao que grava tabela em um arquivo txt '''
    
def GravaArquivo( ArquivoDestino, TAB):
    arquivo = open( ArquivoDestino, 'w')
    for linha in TAB:
        arquivo.write(linha)
    arquivo.close()

''' Funcao que verifica se a tabela esta ordenada '''

def VerifaClass(TAB):
    i, n  = 0, len(TAB)
    while i + 1 < n:
        if compara(TAB[i], TAB[i+1]) is False: return False
        i += 1
    return True

''' Funcao principal '''

def main():

    while True:
        entrada = input("Entre com o nome do arquivo de origem: ")
        if entrada == 'fim': break
        saida   = input("Entre com o nome do arquivo de destino: ")
        TAB, reg = ArmazenaLista(entrada)
        print("\nTotal de registros para classificar: ", reg)
        print("Tempo para classificar a tabela: \n")
        TABR = TAB[:]                           # Copia da tabela para classificacao do metodo recursivo
        inicio = time()
        ClassQuickRecursivo( TABR)
        fim = time()
        if VerifaClass(TABR):
            print("Metodo Quick Recursivo:     ", fim - inicio, "segundos")
        else:
            print("Erro na classificacao")      
        TABI = TAB[:]                           # Copia da tabela para classificacao do metodo interativo
        inicio = time()
        ClassQuickNaoRecursivo( TABI)
        fim = time()
        if VerifaClass(TABI):
            print("Metodo nao Quick Recursivo: ", fim - inicio, "segundos")
        else:
            print("Erro na classificacao")
        print("\n")
        GravaArquivo(saida, TABI)               # Entendendo que ambas as copias da tabela estarao classificadas,gravei no arquivo a TABI do metodo interativo '''

main()
