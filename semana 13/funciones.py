# Autor: Felix Jimenez
# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "New York": {
        "semana 1": [22, 25, 26, 24, 200],
        "semana 2": [22, 25, 26, 24, 80],
        "semana 3": [22, 25, 26, 24, 29],
        "semana 4": [22, 25, 26, 24, 50]


    },
    "los Angeles": {
        "semana 1": [28, 30, 29, 31, 215],
        "semana 2": [28, 30, 29, 31, 203],
        "semana 3": [28, 30, 29, 31, 300],
        "semana 4": [28, 30, 29, 31, 270]
    },
    "Chicago": {
        "semana 1": [21, 20, 22, 18, 110],
        "semana 2": [21, 20, 22, 18, 190],
        "semana 3": [21, 20, 22, 18, 186],
        "semana 4": [21, 20, 22, 18, 145]
    },
    "Miami": {
        "semana 1": [32, 33, 34, 30, 32],
        "semana 2": [32, 33, 34, 30, 32],
        "semana 3": [32, 33, 34, 30, 32],
        "semana 4": [32, 33, 34, 30, 32]
    },
    "Houston": {
        "semana 1": [30, 32, 31, 33, 32],
        "semana 2": [30, 32, 31, 33, 32],
        "semana 3": [30, 32, 31, 33, 32],
        "semana 4": [30, 32, 31, 33, 32]
    },
    "Phoenix": {
        "semana 1": [40, 42, 43, 41, 42],
        "semana 2": [40, 42, 43, 41, 42],
        "semana 3": [40, 42, 43, 41, 42],
        "semana 4": [40, 42, 43, 41, 42]
    },
    "Philadelphia": {
        "semana 1": [25, 26, 27, 24, 26],
        "semana 2": [25, 26, 27, 24, 26],
        "semana 3": [25, 26, 27, 24, 26],
        "semana 4": [25, 26, 27, 24, 26]
    },
    "San Antonio": {
        "semana 1": [31, 32, 33, 30, 390],
        "semana 2": [31, 32, 33, 30, 32],
        "semana 3": [31, 32, 33, 30, 32],
        "semana 4": [31, 32, 33, 30, 32]
    },
# aqui se puede agregar mas ciudades y el promgrama seguira funcionando
}


temperaturas_promedio = {}
# count = 0


def temperatura_promedio(ciudades_tempera):
    ciudades_index = 0
    for ciudad, semanas in ciudades_tempera.items():
        temperaturas_promedio[ciudad] = {}
        for semana, temperaturas in semanas.items():
            promedio_semana = sum(temperaturas) / len(temperaturas)
            temperaturas_promedio[ciudad][semana] = promedio_semana
        ciudades_index = ciudades_index + 1

    return temperaturas_promedio, ciudades_index

loco = temperatura_promedio(ciudades_temperaturas)

def jaja(locaso):
    option_number = 0
    print("Eligue una ciudad con un numero")
    cont = 0
    for citys in locaso[0].items():
        cont = cont + 1
        print(cont, ". ", citys[0])
    option_number = int(input("Eligue una ciudad:__ "))
    return option_number-1

city_selecte = {}


def dada(bla, contador):
    cont = 0
    for lo in bla[0].items():
        if int(cont) == int(contador):
            city_selecte = lo[0]
            break
        cont = cont + 1
    return city_selecte


citys_menu = {}


def menu(blablabla):
    for citys, temperatura in loco[0].items():
        for semana in temperatura.items():
            # citys_menu[semana] = semana, citys
            if blablabla == citys:
                print(f"La ciudad de :  {
                    citys} tiene la temperatura de: {semana}°C")



# estaba cansao y no estuve creativo con los nombres de  variables y funciones
chale = dada(loco, jaja(loco))
menu(chale)


#     for ciudad, semana, temperaturas in ciudades_temperaturas.items():
#         promedio = sum(temperaturas) / len(temperaturas)
#         temperaturas_promedio[ciudad] = promedio
#         print(temperaturas_promedio[ciudad])

#     return temperaturas_promedio

# Llamamos a la función para calcular las temperaturas promedio
# temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# # Mostramos los resultados
# print("Temperaturas Promedio por Ciudad:")
# for ciudad, promedio in temperaturas_promedio.items():
#     print(f"{ciudad}: {promedio:.2f}°C")

# print("Temperaturas Promedio por Ciudad:", temperaturas_promedio)
