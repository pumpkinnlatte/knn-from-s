# Implementación de K-Nearest Neighbors (KNN) desde Cero

Este proyecto contiene una implementación simple y didáctica del algoritmo de clasificación **K-Nearest Neighbors (KNN)** en Python, construido completamente desde cero para entender sus fundamentos.


## ¿Qué es KNN?

**K-Nearest Neighbors (KNN)** es un algoritmo de aprendizaje supervisado no paramétrico que se utiliza para tareas de **clasificación** y **regresión**. Su funcionamiento es bastante intuitivo:

1. **Memoriza los Datos de Entrenamiento**:  
   El algoritmo "aprende" simplemente memorizando todos los puntos de datos de entrenamiento y sus etiquetas de clase correspondientes.

2. **Clasifica Nuevos Puntos**:  
   Para clasificar un nuevo punto de datos, KNN:

   - Calcula la distancia (comúnmente la distancia **euclidiana**) entre el nuevo punto y todos los puntos en el conjunto de entrenamiento.
   - Identifica los **k puntos de datos más cercanos** (los "vecinos" más próximos) al nuevo punto. El valor de `k` es un número entero que se define previamente.
   - Asigna al nuevo punto la clase que sea **más frecuente entre esos k vecinos más cercanos**. Esto es una "votación" de mayoría.

> En resumen, los puntos de datos se clasifican según la mayoría de las clases de sus vecinos más cercanos.

---


- **`KNNClassificador.py`**: Contiene la clase `KNNClassificador` con la lógica central del algoritmo KNN, incluyendo el cálculo de distancias y la función de predicción.
- **`main.py`**: Script principal que carga un conjunto de datos (por defecto, el dataset Iris), inicializa el clasificador KNN y demuestra cómo hacer predicciones.
- **`data/`**: Carpeta diseñada para almacenar conjuntos de datos. Puedes agregar más datasets para experimentar con diferentes problemas de clasificación.



## Cómo Funciona Este Programa


### Inicialización (`KNNClassificador.__init__`)

- Al crear una instancia de `KNNClassificador`, le pasas el número de vecinos (`k_neighbors`) y tus datos (`DataFrame` de Pandas).
- Se asume que la **última columna** del conjunto de datos es la **etiqueta de clase** (`y_train`), y las demás son las **características** (`x_train`).

### Cálculo de Distancia (`distanciaEuclidiana`)

- Esta función calcula la **distancia euclidiana** entre dos puntos, es decir, la longitud de la línea recta que los conecta en un espacio multidimensional.

### Predicción (`predecir`)

- Al pasarle uno o varios `X_Nuevos` a la función `predecir`:

  1. Calcula la distancia de cada muestra nueva a todos los puntos de entrenamiento.
  2. Identifica los **k vecinos más cercanos**.
  3. Observa las etiquetas de clase de esos vecinos.
  4. Usa `collections.Counter` para contar la frecuencia de cada clase y elige la **más común** como predicción.

## Requisitos

Asegúrate de tener instaladas las siguientes librerías de Python:

- `numpy`
- `pandas`

Puedes instalarlas con:

```bash
pip install numpy pandas
```

## Uso

### Coloca tus Datos

Asegúrate de que tus archivos de datos (.csv, etc.) estén en la carpeta data/ o en una subcarpeta dentro de ella.
Este proyecto usa data/iris/iris.data como ejemplo.

### Ejecuta el Script

```bash
python main.py
```

El script cargará el dataset Iris, entrenará el clasificador KNN y realizará una predicción para una muestra de ejemplo.

## Experimenta
Cambia k_neighbors
Modifica el valor de k_neighbors en main.py para ver cómo afecta las predicciones.

## Añade Nuevos Datasets
Puedes agregar tus propios archivos .csv a la carpeta data/ y modificar main.py para cargarlos.
Recuerda que el programa espera que la última columna sea la etiqueta de clase.

## Prueba Nuevas Muestras
Cambia los valores en la lista nueva_muestra en main.py para experimentar con diferentes puntos a clasificar.