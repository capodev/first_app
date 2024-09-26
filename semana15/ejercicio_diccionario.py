informacion_peronal = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "direccion": "Calle 123",
    "telefono": "1232837495",
    "ciudad": "Bogota"
}
# vamos a modificar el valor de nombre del diccionario informacin_personal
informacion_peronal["ciudad"] = "Cartagena"
# podriamos hacer que el valor de nombre sea una variable que ingrese por teclado

# vamos a ageregar un nuevo valor al diccionario informacion_personal este sera profesion
informacion_peronal["profesion"] = "Ingeniero"

# validamos si existe la clave telefono en el diccionario informacion_personal si existe no hacemos nada
# si no existe la agregamos con el valor 1234567890
if "telefono" not in informacion_peronal:
    informacion_peronal["telefono"] = "1234567890"

# aqui eliminaremos la clave edad del diccionario informacion_personal
del informacion_peronal["edad"]

# vamos a imprimir el diccionario informacion_personal
print(informacion_peronal)