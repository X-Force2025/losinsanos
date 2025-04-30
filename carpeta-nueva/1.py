class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def display(self):
        """Return a string representation of the linked list."""
        if self.head is None:
            return "Empty list"
        
        current = self.head
        result = ""
        
        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()
        
        return result + "None"
    
    # Método auxiliar para añadir elementos rápidamente durante las pruebas
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        
        self.length += 1
        return True

# CASOS DE PRUEBA

def test_empty_list():
    """Caso de prueba 1: Lista vacía"""
    print("Caso de prueba 1: Lista vacía")
    my_list = LinkedList()
    result = my_list.display()
    expected = "Empty list"
    
    print(f"Resultado: {result}")
    print(f"Esperado: {expected}")
    print(f"Prueba pasada: {result == expected}")
    print("-" * 40)

def test_single_element():
    """Caso de prueba 2: Lista con un solo elemento"""
    print("Caso de prueba 2: Lista con un solo elemento")
    my_list = LinkedList()
    my_list.insert_at_end(42)
    
    result = my_list.display()
    expected = "42 -> None"
    
    print(f"Resultado: {result}")
    print(f"Esperado: {expected}")
    print(f"Prueba pasada: {result == expected}")
    print("-" * 40)

def test_multiple_elements():
    """Caso de prueba 3: Lista con múltiples elementos"""
    print("Caso de prueba 3: Lista con múltiples elementos")
    my_list = LinkedList()
    elements = [10, 20, 30, 40, 50]
    
    for item in elements:
        my_list.insert_at_end(item)
    
    result = my_list.display()
    expected = "10 -> 20 -> 30 -> 40 -> 50 -> None"
    
    print(f"Resultado: {result}")
    print(f"Esperado: {expected}")
    print(f"Prueba pasada: {result == expected}")
    print("-" * 40)

# Ejecutamos los casos de prueba
if __name__ == "__main__":
    test_empty_list()
    test_single_element()
    test_multiple_elements()
