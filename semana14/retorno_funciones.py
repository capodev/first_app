# funcion para calcular el descuento de un monto total
# Autor: Felix Jimenez 1ro A

def calcular_descuento(monto_total, descuento):
    total_descuento = descuento / 100
    monto_descuento = monto_total * total_descuento
    final_price = monto_total - monto_descuento
    return "El total es de: ", final_price, " El descuento seria de: ", monto_descuento

#realizamos un do while para hacer multiples intentos, manipulado por el usuario
while True:
    #ingresamos los valores por teclado
    monto = float(input("Ingrese el monto total: "))
    descuentos = float(input("Ingrese el descuento: "))
    #llamamos a la funcion calcular_decuento que nos devolvera un string el cual contiene los valores rrequeridos
    print(calcular_descuento(monto, descuentos))
    if input("Desea calcular otro descuento? (s/n): ") == "n":
        break
