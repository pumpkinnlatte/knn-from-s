
import numpy as np
from collections import Counter

class KNNClassificador:
    def __init__(self, k_neighbors, data):
        self.k_neighbors = k_neighbors
        self.x_train = data.iloc[:, :-1]   # atributos numericos
        self.y_train = data.iloc[:, -1]    # etiqueta de clase

    def distanciaEuclidiana(self, x1, x2):
        return np.sqrt(np.sum((np.array(x1) - np.array(x2))**2))
    
    def predecir(self, X_Nuevos):
        distancias = []
        mas_comun = []
        for punto_nuevo in X_Nuevos:
            #Calcular distancia del nuevo punto a todos los puntos de training
            distancias = [self.distanciaEuclidiana(punto_nuevo, punto_train) for punto_train in self.x_train.values]

            #Obtener los indices de los k vecinos mas cercanos
            k_indices_vecinos = np.argsort(distancias)[:self.k_neighbors]

            #Obtener las etiquetas de clase de los k vecinos mas cercanos
            k_clases_vecinas = [self.y_train[i] for i in k_indices_vecinos]

            #Predecir mediante votacion
            mas_comun.append(Counter(k_clases_vecinas).most_common(1)[0][0])

        return mas_comun




