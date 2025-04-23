from collections import deque

class PlanificadorRR:
    def __init__(self, quantum):
        self.cola = deque()
        self.quantum = quantum 
        self.tiempo_actual = 0
        self.metricas = {
            'respuesta': {},
            'espera': {},
            'total': {}
        }
    def agregar_proceso(self, pid, tiempo_cpu):
        self.cola.append({
            'pid': pid,
            'tiempo_restante': tiempo_cpu, 
            'llegada': self.tiempo_actual,
            'primera_vez': True
         })
        # Inicializar métricas
        self.metricas['respuesta'][pid] = 0
        self.metricas['espera'][pid] = 0
        self.metricas['total'][pid] = 0
    def ejecutar(self):
        print("\nPlanificador Round Robin (Quantum={self.quantum})")
        print("="*40)
        while self.cola:
            proceso = self.cola.popleft()
            pid = proceso['pid']
            # Registrar tiempo de respuesta si es la primera vez que se ejecuta el proceso
            if proceso['primera_vez']:
                self.metricas['respuesta'][pid] = self.tiempo_actual - proceso['llegada']
                proceso['primera_vez'] = False

            # Tiempo de ejecución real
            tiempo_ejec = min(self.quantum, proceso['tiempo_restante'])
            print(f"T={self.tiempo_actual}: Ejecutando P{pid} (Restante: {proceso['tiempo_restante']})")

            # Actualizar tiempo de espera para otros procesos
            for p in self.cola:
                self.metricas['espera'][p['pid']] += tiempo_ejec

            # Ejecutar proceso
            self.tiempo_actual += tiempo_ejec
            proceso['tiempo_restante'] -= tiempo_ejec

            # Verificar si el proceso terminó o vuelve a la cola
            if proceso['tiempo_restante'] > 0:
                self.cola.append(proceso)
                print(f"T={self.tiempo_actual}: P{pid} vuelve a cola")
            else:
                self.metricas['total'][pid] = self.tiempo_actual - proceso['llegada']
                print(f"T={self.tiempo_actual}: P{pid} completado")

        # Mostrar métricas
        print("\n--- Métricas ---")
        print("Respuesta:", self.metricas['respuesta'])
        print("Espera:", self.metricas['espera'])
        print("Total:", self.metricas['total'])
# Casos de prueba
if __name__ == "__main__":
    pruebas = [
        {"quantum": 2, "procesos": [(1, 5), (2, 3), (3, 4)]},
        {"quantum": 3, "procesos": [(1, 7)]},
        {"quantum": 4, "procesos": [(1, 6), (2, 2)]}
    ]

    for i, prueba in enumerate(pruebas, 1):
        print(f"\nPrueba {i}: Quantum = {prueba['quantum']}")
        rr = PlanificadorRR(prueba['quantum'])
        for pid, tiempo in prueba['procesos']:
            rr.agregar_proceso(pid, tiempo)
        rr.ejecutar()

