# Simulación de Sistemas Cuánticos

Este proyecto simula un sistema cuántico básico donde una partícula está confinada a un conjunto discreto de posiciones en una línea. Se implementa en Python utilizando la biblioteca NumPy para realizar cálculos matriciales y vectoriales.

## Contenido

1. Descripción del Sistema
2. Instalación
3. Uso
4. Ejemplos
5. Ejercicios y Discusión
6. Funciones Implementadas
7. Contribuciones

## 1. Descripción del Sistema

El sistema permite especificar:
- El número de posiciones disponibles.
- Un vector *ket* que representa el estado de la partícula y asigna las amplitudes de probabilidad.

### Funcionalidades

- Calcular la probabilidad de encontrar la partícula en una posición particular.
- Calcular la probabilidad de transición de un vector *ket* a otro.

## 2. Instalación

Asegúrate de tener Python y NumPy instalados. Puedes instalar NumPy utilizando pip:

```bash
pip install numpy

3. Uso
import numpy as np

# Definir el número de posiciones y el vector ket
numberOfPositions = 3
ketVector = np.array([1, 0])

# Calcular la norma del ket
ketVectorNorm = np.linalg.norm(ketVector)
ketVector = ketVector / ketVectorNorm

# Calcular la probabilidad en una posición específica
position = 1  
print("Probabilidad en esa posición", position)
probabilityPosition = ketVector[position] ** 2
print(probabilityPosition)

# Calcular la probabilidad de transición entre vectores ket
ketVector2 = np.array([1, 1])  
ketVector2Norm = np.linalg.norm(ketVector2)
ketVector2 = ketVector2 / ketVector2Norm

transitionProbability = np.dot(np.conjugate(ketVector2.T), ketVector)
print("La probabilidad de transición entre el vector", ketVector, "y el vector", ketVector2)
print(transitionProbability)

4. Ejemplos
A continuación, se incluyen ejemplos de problemas implementados:

Ejemplo 4.3.1
Calcular la probabilidad de transición del vector ket al vector base 
𝑒
1
e 
1
​
 :


Ket = [1, 0]
matrix = [[0, 1], [1, 0]]
probabilidades, valoresPropios, vectoresPropios = calculateTransitionOfEigenvectors(matrix, Ket)
print("Estados:")
print(vectoresPropios)
Ejemplo 4.3.2
Calcular el valor medio:


media = probabilidades[0] * int(np.int32(valoresPropios[0])) 
media += probabilidades[1] * int(np.int32(valoresPropios[1])) 
print(media)
Ejemplo 4.4.1
Verificar si una matriz es unitaria:


isUnitary = np.allclose(a3U, Imatrix)
if isUnitary:
    print("Es unitaria")
Ejemplo 4.5.2
Calcular la probabilidad en cualquier punto:


num = 1 + 1j
p = 2 / (2 * 6)
print("La probabilidad en cualquier punto =:", p)
5. Ejercicios y Discusión
Este proyecto incluye ejercicios como:

4.3.1
4.3.2
4.4.1
4.4.2
4.5.2
4.5.3
Para cada ejercicio, se ha proporcionado un análisis y discusión en el código y se espera que los usuarios puedan explorar y modificar los ejemplos.

6. Funciones Implementadas
transitionAmplitude(vector1, vector2): Calcula la amplitud de transición entre dos vectores.
calculaMedia(matrix, ket): Calcula el valor esperado para un estado dado.
calculateVariance(matrix, ket): Calcula la varianza para un operador dado.
calculateTransitionOfEigenvectors(matrix, ket): Calcula la transición entre los vectores propios de una matriz.
finalState(initialState, matrices): Calcula el estado final dado un estado inicial y una lista de matrices de transición.
7. Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios.

