# Greedy Algorithms (Algoritmos Devoradores.)
Repositorio sobre los algoritmos devoradores. 
Se presentará un esquema general, descripición, 
elementos que lo componen y ejemplos de uso. Para ello se
ha realizado un resumen y modificado las partes que he creido pertinentes
del temario dado en la asignatura **"Diseño de Algoritmos "** añadiendo
y traduciendo los algoritmos del temario a código *python*.

### Elementos:

- **Conjunto de candidatos**: *candidates_set*
- **Conjunto de candidatos selecionados**: *candidates_selected_set*
- **Función solución**: Comprueba si un conjunto de candidatos
 seleccionados es una solución válida. Represetada mediante *is_solution()*
- **Función selección**: Selecciona el candidato más prometedor del conjunto 
de candidatos. Representada mediante: *select()*
- **Función de factibilidad**: Comprueba que el conjunto de candidatos seleccionados
 se puede expandir añadiendo un candidato seleccionado. Representada mediante:
 *feasible()*
- **Función objetivo**: Función que asocia un valor a una solución de nuestro
algoritmo devorador, y que queremos minimizar o maximizar (optimizar)
según nuestro objetivo.
- **Objetivo**: Minimizar, maximizar.


### Características
- El candidato más prometedor, puede ser no único.
- Una vez elegido un candidato, nunca más vuelve a ser procesado.
- Puede que la solución no exista o no pueda ser encontrada.
- Aunque se encuentre una solución, puede que no sea la más óptima.
- Se emplean normalmente en problemas de optimización.


### Esquema general:
```python
def greedy(candidates_set):

    candidates_selected_set = None

    while not is_solution(candidates_selected_set) and candidates_set:
        
        candidate_selected = select(candidates_set)
        candidates_set.remove(candidate_selected)
        
        if feasible(candidates_selected_set, candidate_selected):
            
            candidates_selected_set.append(candidate_selected)
     
    return candidates_selected_set   
    
```

# The Knapsack problem (El problema de la mochila.)

"Dado un cojunto *O* de objetos, cada uno con un valor *v* y un peso
 *p*, y una mochila con una capacidad  *c*, que limita el peso total que puede transportar,
 se desea hallar la composición de la mochila que maximiza el valor de la carga."
 
 - En su versión continua, donde los objetos pueden fraccionarse, puede
 resolverse con un algoritmo devorador de forma óptima, usando la 
 estrategia correcta para la selección de objetos. Esta estrategia
 se implementa dentro de la **función de selección**.
 
 - **Estrategia**: Se seleccionaran los objetos en orden decreciente de relación
 de *valor/peso*.
 
 ### Elementos
 
 - **Conjunto de candidatos**:  Los objetos que queremos meter en la mochila.
 
 - **Función Solución**: Comprobar si la mochila está llena.
 
 - **Función Selección**: Elegir el objeto con mayor ratio *valor/peso*
 
 - **Función de factibilidad**: Que el objeto se pueda introducir en la 
 mochila sin exceder la capacidad de esta.
 
 - **Función objetivo:** La suma de los valores de los objetos que hay
 en la mochila.
 
 - **Objetivo**: Maximizar.
 
 ### Resolución mediante algoritmo devorador:
 
 ```python
def knapsack_problem(objetos, capacidad):

    candidates_set = objetos[:]
    candidates_selected = []

    while capacidad != 0 and candidates_set:
        candidato = select(candidates_set)
        candidates_set.remove(candidato)

        if candidato.peso <= capacidad:
            capacidad = capacidad-candidato.peso
            candidates_selected.append(candidato)
        else:
            candidato.peso = capacidad
            candidato.valor = candidato.valor * capacidad / candidato.peso
            candidates_selected.append(candidato)
            capacidad = 0

    return candidates_selected


```

### Función de Selección:
 
 ```python
import math

def select(candidates_set):
    limit = -math.inf
    best_candidate = None

    for candidate in candidates_set:
        if candidate.valor/candidate.peso > limit:
            best_candidate = candidate
            limit = candidate.valor/candidate.peso

    return best_candidate


 ```
 ### Función de Factibilidad:
 Implementada directamente en el código del algoritmo principal mediante
 la sentencia: 
 ```python
if candidato.peso <= capacidad:  
```
 
# The Coin Change problem (El problema del cambio de moneda.)

"Sea *M* un conjunto de monedas y *c* una cantidad a devolver. Por cada
tipo de moneda de valor *v* se dispone de un suministro  de *k* unidades
. Se desea hallar la composición del cambio  que posee el menor número de
monedas."

- En general, esta aproximación no produce una solución óptima,
solo para un conjunto determinados de monedas, como por ejemplo
si se dispondría de un número de un número suficiente de monedas de
1, 5, 10, 15, 25, 50, 100, 200 y 500 unidades.

- **Estrategia**: Elegir, de las que quedan, la de mayor valor y si es posible
seleccionar todas las monedas del mismo valor de una vez.

### Elementos:

- **Conjunto de candidatos**: Monedas.

- **Función solución**: El cambio a devolver es igual a 0.

- **Función de selección**: Elegir las monedas de mayor valor.

- **Función de factibilidad**: Valor de las monedas no supera el valor a devolver.

- **Función objetivo**: Número de monedas devueltas.

- **Objetivo**: Minimizar. 
 
 
 
 
 
 
 
 Fuentes: "Algoritmos Devoradores", por A. Salguero, F. Palomo, I. Medina
Universidad de Cádiz.
 
 