import random
from collections import deque

class Vehiculo:
    def __init__(self, llegada):
        self.llegada = llegada

class Semaforo:
    def __init__(self, duracion_ciclo):
        self.duracion = duracion_ciclo
        self.tiempo = 0
        self.estado = 'NS'  # NS = norte-sur, EO = este-oeste

    def actualizar(self):
        self.tiempo += 1
        if self.tiempo >= self.duracion:
            self.estado = 'EO' if self.estado == 'NS' else 'NS'
            self.tiempo = 0

class Interseccion:
    def __init__(self, prob_vehiculo=0.3, duracion_semaforo=30, tiempo_simulacion=300):
        self.cola_norte = deque(maxlen=1000)
        self.cola_sur = deque(maxlen=1000)
        self.cola_este = deque(maxlen=1000)
        self.cola_oeste = deque(maxlen=1000)
        self.prob_vehiculo = prob_vehiculo
        self.semaforo = Semaforo(duracion_semaforo)
        self.tiempo_total = tiempo_simulacion
        self.estadisticas = {
            "esperas": [],
            "max_colas": {
                "N": 0, "S": 0, "E": 0, "O": 0
            }
        }

    def generar_vehiculos(self, tiempo):
        if random.random() < self.prob_vehiculo:
            self.cola_norte.append(Vehiculo(tiempo))
        if random.random() < self.prob_vehiculo:
            self.cola_sur.append(Vehiculo(tiempo))
        if random.random() < self.prob_vehiculo:
            self.cola_este.append(Vehiculo(tiempo))
        if random.random() < self.prob_vehiculo:
            self.cola_oeste.append(Vehiculo(tiempo))

    def actualizar_estadisticas_colas(self):
        self.estadisticas["max_colas"]["N"] = max(self.estadisticas["max_colas"]["N"], len(self.cola_norte))
        self.estadisticas["max_colas"]["S"] = max(self.estadisticas["max_colas"]["S"], len(self.cola_sur))
        self.estadisticas["max_colas"]["E"] = max(self.estadisticas["max_colas"]["E"], len(self.cola_este))
        self.estadisticas["max_colas"]["O"] = max(self.estadisticas["max_colas"]["O"], len(self.cola_oeste))

    def avanzar_vehiculos(self, tiempo):
        # Avanzan 1 vehículo por segundo por carril si tienen luz verde
        if self.semaforo.estado == 'NS':
            for cola in [self.cola_norte, self.cola_sur]:
                if cola:
                    vehiculo = cola.popleft()
                    self.estadisticas["esperas"].append(tiempo - vehiculo.llegada)
        else:
            for cola in [self.cola_este, self.cola_oeste]:
                if cola:
                    vehiculo = cola.popleft()
                    self.estadisticas["esperas"].append(tiempo - vehiculo.llegada)

    def simular(self):
        for t in range(self.tiempo_total):
            self.generar_vehiculos(t)
            self.avanzar_vehiculos(t)
            self.actualizar_estadisticas_colas()
            self.semaforo.actualizar()

        espera_promedio = (sum(self.estadisticas["esperas"]) / len(self.estadisticas["esperas"])
                           if self.estadisticas["esperas"] else 0)

        print("📊 Estadísticas de la simulación:")
        print(f"- Tiempo promedio de espera: {espera_promedio:.2f} segundos")
        print(f"- Longitud máxima de cola por dirección:")
        for dir, val in self.estadisticas["max_colas"].items():
            print(f"  • {dir}: {val} vehículos")


# Ejecutar la simulación
if __name__ == "__main__":
    interseccion = Interseccion(prob_vehiculo=0.4, duracion_semaforo=30, tiempo_simulacion=300)
    interseccion.simular()
