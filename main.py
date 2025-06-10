import pandas as pd
import KNNClassificador as KNN

def main():
    
    columnas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    datos = pd.read_csv('datasets/iris/iris.data', names=columnas)

    knn_clasificador = KNN.KNNClassificador(k_neighbors=3, data=datos)

    # Predecir una nueva muestra
    nueva_muestra = [[5.9,3.0,5.1,1.8], 
                     [5.0,3.5,1.3,0.3], 
                     [6.7,3.1,4.4,1.4]]

    prediccion = knn_clasificador.predecir(nueva_muestra)

    print(f"La clase predicha para la nueva muestra {nueva_muestra} es: {prediccion}")

if __name__ == "__main__":
    main()