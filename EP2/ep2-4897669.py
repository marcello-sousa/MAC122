'''Nome: Marcelo de Sousa, n° USP 4897669
   MAC0122 - Professor: Manoel Marcilio'''

#Implementacao da classe pilha
class Pilha:
    def __init__ (self):
        self._pilha = []

    def __len__ (self):
        return len(self._pilha)
        
    def is_empty (self):
        return len(self._pilha) == 0
        
    def top (self):
        if self.is_empty():
            raise ValueError("Pilha vazia")
        return self._pilha[-1]

    def  push (self, x):
        self._pilha.append(x)

    def pop (self):
        if self.is_empty():
            raise ValueError("Pilha vazia")
        return self._pilha.pop()

'''Funcao que verifica se ha excesso de parênteses ou 
falta, retorna True ou False '''

def VerificaParentesis (Expr):
    p = Pilha()
    for i in Expr:
        if prioridade(i) == 6:
            if p.is_empty(): return False
            c = p.pop()     
        elif prioridade(i) == 5: 
            p.push(i)          
    return p.is_empty()

'''Funcao que devolve a prioridade dos operadores e operandos,
nessa funcao achei necessario colocar os dois operadores de divisao,
pois estava dando conflito na leitura da lista, na funcao controi lista, 
para a operacao utilizei apenas o operador de divisao para inteiros.'''
    
def prioridade (x):
    if   x == '+' : return 1
    elif x == '-' : return 1
    elif x == '*' : return 2
    elif x == '/' : return 2
    elif x == '//': return 2
    elif x == '%' : return 2
    elif x == '#' : return 3
    elif x == '_' : return 3
    elif x == '**': return 4
    elif x == '√' : return 4
    elif x == '(' : return 5
    elif x == ')' : return 6
    else: return 0
    
'''Dic que retorna o valor da operacao para dois valores a e b,
assiciando um metodo lamba. Neste caso utilizei uma dic porque achei
interessante e bem compacto'''

operadores = {
    "+" : lambda a, b: a +  b,
    "#" : lambda a, b: a +  b,
    "-" : lambda a, b: a -  b,
    "_" : lambda a, b: a -  b,
    "*" : lambda a, b: a *  b,
    "//": lambda a, b: a // b,
    "%" : lambda a, b: a %  b,
    "**": lambda a, b: a ** b
}

'''Funcao que recebe uma string e constroi a lista com as operacoes, 
nesta funcao percorro a string verificando intervalos contendo operadores
e operandos guardando na lista, e por fim retorna a lista'''
def ConstroiLista(Expr):
    exp, i = [], 0
    if VerificaParentesis(Expr):
        while i < len(Expr):
            if prioridade(Expr[i]) != 0:
                if Expr[i] == '/':
                    valor = Expr[i:i+2]
                    exp.append(valor)
                    i += 2
                elif Expr[i] == '*' and Expr[i+1] == '*':
                    valor = Expr[i:i+2]
                    exp.append(valor)
                    i += 2
                else:
                    exp.append(Expr[i])
                    i += 1
            elif Expr[i] != ' ' and prioridade(Expr[i]) == 0:
                j = i
                while i < len(Expr) and Expr[i] != ' ' and prioridade(Expr[i]) == 0:            
                    i += 1
                valor = Expr[j:i]
                exp.append(valor)              
            else: i += 1
    else: raise ValueError('Experessao nao balanceada')
    return exp
 
'''Funcao que verifica a existencia de opreadores unarios, 
alterando a expressao, retornando o proprio vetor''' 
def VerificaUnarios (infix):
    for i in range(len(infix)):
        if prioridade(infix[i]) == 1 and (prioridade(infix[i-1]) != 0 or i - 1 < 0):
        	    if   infix[i] == '+': infix[i] = '#'
        	    elif infix[i] == '-': infix[i] = '_' 
    return infix
 
'''Funcao que traduz para posfixa, basicamente segui o pseudocodigo apresentado
pelo professor, sem novidades'''
    
def TraduzPosf (infix):
    p, posfix = Pilha(), []
    infix = VerificaUnarios (infix)
    for i in range(len(infix)):
        if prioridade(infix[i]) == 0: 
            posfix.append(infix[i])
        elif prioridade(infix[i]) < 5:
            if not p.is_empty():
                x = p.pop()
                if prioridade(infix[i]) <= prioridade(x) and prioridade(x) < 5:
                    posfix.append(x)               
                else: p.push(x)
            p.push(infix[i])
        elif prioridade(infix[i]) == 5:
            p.push(infix[i])
        elif prioridade(infix[i]) == 6:
            x = p.pop()
            while prioridade(x) != 5:
                posfix.append(x)  
                x = p.pop()
    while not p.is_empty():
        posfix.append(p.pop())
    return posfix
 
'''Funcao que recebe uma lista com a exoressao posfixa e calcula o valor da 
expressao posfixa, tambem, como funcao anterior, segui as instrucoes apresentadas 
pelo professor'''
    
def calculaPosf (posfix):
    p = Pilha()
    for i in posfix:
        if prioridade(i) == 0:
            p.push(int(i))
        elif i == '#' or i == '_':
            x = p.pop()
            p.push(operadores[i](0, x))
        elif prioridade(i) < 5:
            x, y = p.pop(), p.pop()
            p.push(operadores[i](y, x))
    return p.top()

'''Funcao principal que recebe exoressao digitada pelo usuario e imprime
a valor das expressoes, ate que o usuario digite fim'''
def main():
    Expr = []
    while True:
        Expr = input('\nDigite a expressao: ')
        if Expr != 'fim':
            L_Expr = ConstroiLista(Expr)
            Expr_Posf = TraduzPosf(L_Expr)
            k = calculaPosf(Expr_Posf)
            print('Valor = ', k)
        else: break
main()
