# crea una matriz bidimecinoa de 3x3 con los valores del 1 al 9
matriz = [[2, 3, 1],
          [4, 5, 6],
          [7, 8, 9]]
# imprimimos la matriz original
print("Matriz original", matriz)
# ordenar la matriz con el metodo burbuja
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        for k in range(len(matriz[i])):
            if matriz[i][j] < matriz[i][k]:
                temp = matriz[i][j]
                matriz[i][j] = matriz[i][k]
                matriz[i][k] = temp
# impimimos la matriz ordenada
print("Matriz ordenada", matriz)
