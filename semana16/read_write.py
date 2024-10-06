# abrimos en modo lectura y escritura nuestro archivo my_notes.txt con encoding utf-8 y r+
# y lo guardamos en la variable ar
# vamos a manejarlo con funciones
def write_File():
    with open("my_notes.txt", 'r+', encoding="utf-8") as ar:
        # agregamos la palabra Hola en la primera linea del archivo
        ar.write("Hola\n")

# aqui abrimos en modo lectura para imprimir luego de agrgar el texto
def read_file():
    with open("my_notes.txt", 'r', encoding="utf-8") as ar:
        # leemos el archivo y lo retornamos
        return ar.read()


# llamamos a la funcion write_File
write_File()
# llamamos a la funcion read_file y lo imprimimos
print(read_file())
# ar.close()
# al usar el with open, no es necesario cerrar el archivo con ar.close()
# como esta comentado en la linea 20

