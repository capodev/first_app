# crea una matriz de 3x3 con los valores del 1 al 9
matriz = [1, 2, 3,
          4, 5, 6,
          7, 8, 9]
 # definire un numero al que deseo buscar en la matriz
numero = 5
# busco el numero en la matriz
if numero in matriz:
    print("El numero", numero,
          "se encuentra en la matriz en la posicion", matriz.index(numero))
