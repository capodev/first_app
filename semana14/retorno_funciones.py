# funcion para calcular el descuento de un monto total
# Autor: Felix Jimenez 1ro A

def calcular_descuento(monto_total, descuento):
    total_descuento = descuento / 100
    monto_descuento = monto_total * total_descuento
    final_price = monto_total - monto_descuento
    return "El total es de: ", final_price, " El descuento seria de: ", monto_descuento


while True:
    monto = float(input("Ingrese el monto total: "))
    descuentos = float(input("Ingrese el descuento: "))
    print(calcular_descuento(monto, descuentos))
    if input("Desea calcular otro descuento? (s/n): ") == "n":
        break
