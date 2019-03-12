''' Modulo pilha utilizada na funcao quick nao recursivo '''

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

    def push (self, x):
        self._pilha.append(x)

    def pop (self):
        if self.is_empty():
            raise ValueError("Pilha vazia")
        return self._pilha.pop()
