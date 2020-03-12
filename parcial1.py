import re

lugaresdisponibles = 60
lugaresocupados = 0

def entero2d(x):
    try:
        valorInt = int(x)
        return True
    except ValueError:
        print(f"Introducir solo valores númericos enteros.")
        return False

def reservacion(ld, lo):
    while True:
        if ld != 0:
            print("---")
            txt = "Lugares disponibles: {0}. Lugares ocupados: {1}."
            print(txt.format(ld, lo))
            _cantidad = input("¿Cuántos lugares desea reservar?: ")
            if _cantidad:
                _i = entero2d(_cantidad)
                if _i == True:
                    cantidad = int(_cantidad)
                    if cantidad > 10:
                        print("Sólo se puede reservar un máximo de 10 lugares.")
                    else:
                        if cantidad > ld or cantidad < 1:
                            print("No hay lugares disponibles para esa reservación.")
                        else:
                            print("Reserva exitosa.")
                            print(f"Reservación de {cantidad} asientos.")
                            ld = ld - cantidad
                            lo = lo + cantidad
                            txt = "Lugares disponibles: {0}. Lugares ocupados: {1}."
                            print(txt.format(ld, lo))
                            return ld, lo
                            break
                else:
                    print("Ese dato no tiene el formato requerido.")
            else:
                print("Debe ingresar una cantidad.")
        else:
            print("---")
            print("No hay más lugares.")
            return ld, lo
            break

while True:
    print("---- MENÚ ----")
    print("1) Realizar una reserva -- 2) Salir")
    _opcion=input("Seleccione una opción: ")
    if _opcion:
        _i = entero2d(_opcion)
        if _i == True:
            opcion = int(_opcion)
            if opcion == 1:
                lugaresdisponibles, lugaresocupados = reservacion(lugaresdisponibles, lugaresocupados)
            elif opcion == 2:
                print("Fin de la sesión.")
                break
            else:
                print("Opción no encontrada.")
    else:
        print("Debe ingresar una opción disponible.")