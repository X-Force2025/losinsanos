from collections import deque

# Función principal
def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []

    n = len(nums)
    result = []
    dq = deque()  # Deque almacena índices, no valores directamente

    for i in range(n):
        # Eliminar índices fuera de la ventana
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Eliminar del final los menores al actual
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Agregar índice actual
        dq.append(i)

        # Agregar el máximo al resultado (inicio de deque)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Caso 1: array creciente
nums1 = [1, 2, 3, 4, 5]
k1 = 3
print("Caso 1: creciente")
print("Entrada:", nums1)
print("Salida:", sliding_window_max(nums1, k1))  # Esperado: [3, 4, 5]
print()

# Caso 2: array decreciente
nums2 = [5, 4, 3, 2, 1]
k2 = 2
print("Caso 2: decreciente")
print("Entrada:", nums2)
print("Salida:", sliding_window_max(nums2, k2))  # Esperado: [5, 4, 3, 2]
print()

# Caso 3: valores repetidos
nums3 = [2, 2, 2, 2, 2]
k3 = 3
print("Caso 3: valores repetidos")
print("Entrada:", nums3)
print("Salida:", sliding_window_max(nums3, k3))  # Esperado: [2, 2, 2]
print()

# Caso original del enunciado
nums4 = [1, 3, -1, -3, 5, 3, 6, 7]
k4 = 3
print("Caso 4: original del enunciado")
print("Entrada:", nums4)
print("Salida:", sliding_window_max(nums4, k4))  # Esperado: [3, 3, 5, 5, 6, 7]
