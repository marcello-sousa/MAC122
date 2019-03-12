'''Nome: Marcelo de Sousa, n° USP 4897669
   MAC0122 - Professor: Manoel Marcilio'''

'''Variavel global que criei para contar o 
numero de solucoes'''
contador = 0

from time import time

#Cria matrix 9 x 9 zerada
def Cria_Matriz ():
    m = [9 * [0] for k in range(9)]
    return m

'''Funcao que lê matriz de um arquivo texto. Da
funcao passada pelo professor, fiz duas
alteracao, a primeira verifica se o valor eh 
numerico, caso esteja preenchida com letras e 
encerrando o programa, pois nao eh possivel 
converter uma letra em numero inteiro, e a 
segunda que verifica se a matriz tem as 
dimensoes 9 x 9, tratei os casos de negativos ou
 valores maiores que dez numa funcao abaixo,
para nao mexer demais na funcao original e 
eventualmente encerrar precocemente o programa'''

def LeiaMatriz(Mat):
    arquivo = input("Digite o arquivo: ")
    try:
        arq = open(arquivo, "r")
    except:
        return False
    
    i = 0
    for linha in arq:
        v = linha.split()
        if len(v) == 9:
            for j in range(len(v)):
                try:
                    Mat[i][j] = int(v[j])
                except:
                    raise ValueError("Matriz Inconsistente - Valor nao numerico")  
        
        else: 
            print("\nMatriz Inconsistente, fora das dimensoes 9 x 9\n")  
            return False      
        i = i + 1
             
    arq.close()
    
    if TestaMatrizLida(Mat):
        return True
    
#Funcao que imprime a matriz    
def ImprimaMatriz (Mat):

    for lin in range(len(Mat)):
        for col in range(len(Mat[0])):
            print ("%2d" %Mat[lin][col], end = " ")
        print("\t")

#Funcao que procura elemento na linha
def ProcuraElementoLinha(Mat, L, d):
 
    for i in range(len(Mat)):
        if d == Mat[L][i]: return i
    return -1	

#Funcao que procura elemento na coluna
def ProcuraElementoColuna(Mat, C, d):

    for i in range(len(Mat)):
        if d == Mat[i][C]: return i
    return -1	

'''Funcao que procura elemento no quadrado 
internoneste funcao usei o operador de divisao
 de inteiros // para que a a linha e a coluna 
 sempre iniciem no primeiro elemento do quadrad 
interno '''
def ProcuraElementoQuadrado (Mat, L, C, d): 
    l, c = 0, 0    
    l = (L // 3) * 3   
    c = (C // 3) * 3
    
    for i in range(l, l + 3): 
       for j in range(c, c + 3):        
           if Mat[i][j] == d: return (i, j)
    return (-1, -1)  
    
'''Funcao testa matriz lida: Nesta funcao, optei
 por utilizar filtros nos laços, no primeiro 'if
 ', testo se a matriz encontra-se no intervalo 0
 <= x <= 9 (preferi verificar valores fora do
intervalo nesta funcao, ao inves da funcao 
leiaMatriz, pois como minha condicao da leitura
 dos arquivos na funcao main so se encerra 
 quando o usuario aperta crtl + c, e na funcao 
 leiaMatriz encerrei as inconsistencias 
 numericas num except, o que da menos dinamica
 ao programa, ja esta funcao informa a 
 inconsistencia e ja solicita uma nova entrada 
 de arquivo), que sao valores do jogo, 
 informando ao usuario, se inconsistente, a 
 linha e a coluna em que o valor fora do 
 intervalo foi localizado;no segundo 'if' 
 verifico se o valor encontado na matriz nao 
 esta repetido, nas regras do jogo, neste trecho
  utilizei uma variavel auxiliar 'd' que retira
  o valor momentaneamente, adicionando zero,
 pois as funcoes procura elemento na linha e 
 coluna nao me dao a informaco necessaria sobre 
 a posicao, e sempre me informaria que a matriz 
 eh inconsistente, no fim, se nao atendida, 
retorna a linha e coluna em que enontra-se o 
valor repetido; se as condicoes forem
 consistentes, retorna true '''
def TestaMatrizLida(Mat):
    d = 0
    for lin in range(len(Mat)):
        for col in range(len(Mat[0])):
            if 0 <= Mat[lin][col] <= 9: 
                if 1 <= Mat[lin][col] <= 9:
                    d, Mat[lin][col] = Mat[lin][col], 0
                    if ProcuraElementoColuna(Mat, col, d) != -1 or ProcuraElementoLinha(Mat, lin, d) != -1 or ProcuraElementoQuadrado (Mat, lin, col, d) != (-1, -1):
                        Mat[lin][col] = d
                        print("\nMatriz Inconsistente (Linha %d, Coluna %d, valor = %d), valores repetidos\n" %(lin, col, Mat[lin][col]))
                        return False
                    else: 
                        Mat[lin][col] = d
            else: 
                print("\nMatriz inconsistente (Linha %d, Coluna %d, valor = %d) Fora do intervalo 0 <= valor <= 9.\n" %(lin, col, Mat[lin][col]))
                return False       
    return True 
    
'''Esta funcao verifica se a possivel candidato
 atente ou nao as regras de repeticao do jogo '''
def VerificaCandidato(Mat, L, C, d):

    if ProcuraElementoColuna(Mat, C, d) != -1 or ProcuraElementoLinha(Mat, L, d) != -1 or ProcuraElementoQuadrado (Mat, L, C, d) != (-1, -1): return False
    else: return True

'''Funcao que verifica se matriz preencida eh
 consistente, nesta funcao utilizei uma variavel
  auxiliar 'd', conforme explicao acima. '''  
def TestaMatrizPreenchida(Mat):
    d = 0
    for lin in range(len(Mat)):
        for col in range(len(Mat[0])):
            if Mat[lin][col] != 0:
                d, Mat[lin][col] = Mat[lin][col], d
                if ProcuraElementoLinha (Mat, lin, d) != -1 or ProcuraElementoColuna (Mat, col, d) != -1 or ProcuraElementoQuadrado (Mat, lin, col, d) != (-1, -1): return False
                Mat[lin][col], d = d, 0
            else: return False
    return True

'''Funcao procura casas, retorna a linha e a 
coluna que ainda nao foram preenchidas e retorna
 -1, -1, caso contrario: optei por procurar as
 casas para preenchimento fora da funcao sudoku
, pois esta funcao ficaria mais limpa'''
def ProcuraCasas (Mat):
    for lin in range(0, 9):
        for col in range(0, 9):
            if Mat[lin][col] == 0: return lin, col
    return -1, -1
    
'''Funcao sudoku que preenche as casas da matriz
recursivamente. Basicamente segui as instruções 
descritas em sala de aula. A funcao busca casas,
 preenchendo com seu candidato, quando 
totalmente preenchida, verifica se esta 
correto o preenchimento, informando um possível 
preenchimento incorreto, alem de incrementar o 
contador do numero de solucoes, sempre buscando
 um possivel nova solucao'''
def Sudoku(Mat, lin, col):  
    global contador
    lin, col = ProcuraCasas(Mat)  
       
    if lin == -1 and col == -1:
        if TestaMatrizPreenchida(Mat):
            print("Matriz completa e consistente\n")
            ImprimaMatriz(Mat)
            contador += 1
            print("\t")
        else: print("Preenchimento incorreto")    
    else:
        for candidato in range (1, 10):
            if VerificaCandidato (Mat, lin, col, candidato) is True:
                Mat[lin][col] = candidato     
                Sudoku(Mat, lin, col)           
        Mat[lin][col] = 0        

'''Funcao principal. Funcao cria uma matriz 
zerada, apos entra num laco verificando se a
 funcao retorna matriz retorna True, apos inicia
  a funcao sudoku, contado o tempo de solucao,
  usando a funcao time, por fim imprime o tempo 
 e o numero denumero de solucoes'''  
   
def main():
    global contador 
    tempo1, tempo2, tempo_decorrido = 0, 0, 0
    Mat = Cria_Matriz() 
    while (1): 
        if LeiaMatriz(Mat):       
            print("\nMatriz Inicial\n")
            ImprimaMatriz(Mat)
            print("\t")
            tempo1 = time()
            contador = 0
            Sudoku (Mat, 0, 0)
            tempo2 = time()
            tempo_decorrido = tempo2 - tempo1
            print("Tempo decorrido: ", tempo_decorrido, "segundos\n")
            print("solucoes possiveis para essa matriz = ", contador)
            print("\t")
    
main()