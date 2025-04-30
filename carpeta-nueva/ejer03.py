class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1
        return True

# Pruebas
lista = LinkedList()
lista.insert_at_beginning(30)
lista.insert_at_beginning(20)
lista.insert_at_beginning(10)

# Verificación
print("Longitud:", lista.length)  # Debe imprimir 3
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
# Salida esperada: 10 -> 20 -> 30 -> None
