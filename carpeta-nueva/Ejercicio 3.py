class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
    
   
    
# Inicialización
ms = MinStack()

# Secuencia de operaciones
ms.push(5)       # stack=[5], min_stack=[5]
ms.push(2)       # stack=[5,2], min_stack=[5,2]
ms.push(7)       # stack=[5,2,7], min_stack=[5,2]
print(ms.getMin())   # Devuelve 2
print(ms.top())      # Devuelve 7
print(ms.pop())      # Devuelve 7, stack=[5,2], min_stack=[5,2]
print(ms.getMin())   # Devuelve 2

# Inicialización
ms = MinStack()

# Secuencia de operaciones
ms.push(3)       # stack=[3], min_stack=[3]
ms.push(1)       # stack=[3,1], min_stack=[3,1]
ms.push(1)       # stack=[3,1,1], min_stack=[3,1,1]
print(ms.getMin())   # Devuelve 1
ms.pop()         # stack=[3,1], min_stack=[3,1]
print(ms.getMin())   # Devuelve 1
ms.pop()         # stack=[3], min_stack=[3]
print(ms.getMin())   # Devuelve 3

# Inicialización
ms = MinStack()

# Secuencia de operaciones
print(ms.getMin())   # Devuelve None (pila vacía)
print(ms.top())      # Devuelve None (pila vacía)
print(ms.pop())      # Devuelve None (pila vacía)
ms.push(10)      # stack=[10], min_stack=[10]
print(ms.getMin())   # Devuelve 10
ms.pop()         # stack=[], min_stack=[]
print(ms.getMin())   # Devuelve None (pila vacía nuevamente)
