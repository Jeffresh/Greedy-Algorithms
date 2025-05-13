# Greedy Algorithms (Algoritmos Devoradores)
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

# The Knapsack problem (El problema de la mochila)

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
 ### Función Solución:
 ```python
while capacidad != 0 ...:
```

### Función objetivo:
Especificada mediante la condición del bucle, y forma parte de la condición
de parada del algoritmo.
```python
def objetivo(mochila):
    valor_total = 0

    for objeto in mochila:
        valor_total += objeto.valor

    return valor_total
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

### Resolución mediante algoritmo devorador:

```python
def coinChange(conjunto_monedas, cambio):
    candidates_set = conjunto_monedas
    candidates_selected = []
    c = cambio
    candidate_selected = None

    while c != 0 and candidates_set:

        candidate = select(candidates_set)
        candidates_set.remove(candidate)
        candidate.cantidad = min(candidate.cantidad, c // candidate.valor)
        if candidate.cantidad > 0:
            candidates_selected.append(candidate)
            c = c - candidate.valor * candidate.cantidad

    return candidates_selected
```

### Función de selección:
```python
import math

def select(candidate_set):
    candidate_selected = None
    limit = -math.inf

    for candidate in candidate_set:
        if limit < candidate.valor:
            candidate_selected = candidate
            limit = candidate.valor

    return candidate_selected
```

### Función de factibilidad:
Se realiza mediante estas dos sentencias. Primero se obtiene el mínimo
número de esas monedas con las que se puede dar el cambio. Si es mayor
que 0 entonces se puede dar un cambio parcial o total con al menos
una moneda de ese valor.
```python
candidate.cantidad = min(candidate.cantidad, c // candidate.valor)
if candidate.cantidad > 0:
```

### Función Solución:
Especificada mediante la condición del bucle, y forma parte de la condición
de parada del algoritmo.
```python
while c != 0 ... :
```

### Función Objetivo:
```python
def objetivo(monedas):
    suma = 0
    for moneda in monedas:
        suma += moneda.cantidad

    return suma
```

## Árbol de expansión mínimo (Minimum spanning tree)

"Dado un grafo *G = <V,A>* siendo *V* los vértices y *A* las aristas que componen el grafo *G*" conexo y ponderado con valores no negativos
 en sus aristas, se trata de calcular un subgrafo *H = <V,S>* conexo y acíclico de
 forma que la suma de los valores de sus aristas sea mínima."
 
 ### Características:
 
 - Se demuestra que el subgrafo resultante es un árbol.
 - Un grafo puede tener más de un árbol de expansión mínimo.
 - La comprobación que se debe realizar al ir generando el subgrafo para mantenerlo acíclico es costosa,
 así que se simplifica manteniendo el subgrafo acíclico por construcción.
 - Supondremos un orden en *A* (aristas) inducido por la función de ponderación:
 *{i, j} <= {k, j} <=> p(i, j)*
 
 ### Elementos:
 
 - **Conjunto candidatos**: Las Aristas que componen el grafo.
 - **Función Solución**: Hemos conseguido unir todos los vertices sin ciclos.
 - **Función Selección**: Obtener la arista con menos valor.
 - **Función de factibilidad**: Comprobar si al introducir una nueva arista, genera un ciclo.
 - **Función objetio**: Suma total del valor de las aristas que conforman nuestro árbol de expansión mínimo.
 - **Objetivo**: Minimizar.
 
 
 
 
 
 
## Fuentes: 
 
A. Salguero, F. Palomo, I. Medina.<br>
Algoritmos Devoradores.
Universidad de Cádiz.

Brassard, Gilles & Bratley, Paul.<br>
Fundamentos de Algoritmia.
Prentice-Hall. 1997.

Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L. &
Stein, Cliord.<br>
Introduction to Algorithms.
MIT Press. 2001. 2a ed.

Manber, Udi.<br>
Introduction to Algorithms. A Creative Approach.
Addison-Wesley. 1989.
 
Sedgevick, Robert.<br>
Algorithms.
Addison-Wesley. 1988. 2a edición.
 
