# Pregunta diferentes tipos de datos, sin validación.
# Importa el módulo requerido para usar datos de tipo Date.
import datetime
# Los datos se tienen, se preguntan o se calculan.
# y pueden ser de diferente tipo.
# Notación húngara utilizada:
#   str   string
#   i     int
#   f     float
#   dt    date


def ejemplo():
    # Los datos string se preguntan y procesan sin intermediación.
    strDato = input("Dame un dato string: ")
    # Los datos numéricos se preguntan por intermediación.
    _iDato = input("Dame un dato entero: ")
    iDato = int(_iDato)
    _fDato = input("Dame un dato float: ")
    fDato =float(_fDato)
    # Los datos date se preguntan por intermediación.
    _dtDato = input("Dame una fecha yyyy/mm/dd: ")
    # [n,m] Extrae de la posición n a la posición m,sin incluir m.
    # [-m:] Extrae desde la posición m, de atrás para adelante, hasta el final.

    anio=_dtDato[0:4]
    mes=_dtDato[5:7]
    dia=_dtDato[-2:]
    print(anio)
    print(mes)
    print(dia)

    dtDato = datetime.datetime(int(anio), int(mes), int(dia))

    print(strDato)
    print(type(strDato))
    print(iDato)
    print(type(iDato))
    print(fDato)
    print(type(fDato))
    print(dtDato)
    print(type(dtDato))

def main():
    strNombre = input("Dame tu nombre (string): ")

    intEdad = input("Dame tu edad (entero): ")
    intEdad = int(intEdad)

    fltEstatura = input("Dame tu estatura (float): ")
    fltEstatura = float(fltEstatura)

    dtfecha = input("Dame una fecha (yyyy/mm/dd): ")

    anio = dtfecha[0:4]
    mes = dtfecha[5:7]
    dia = dtfecha[-2:]
    print(anio)
    print(mes)
    print(dia)

    dtfechaFull = datetime.datetime(int(anio), int(mes), int(dia))

    print(f"Tu nombre es: {strNombre}")
    print(type(strNombre))
    print(f"Tu edad es: {intEdad}")
    print(type(intEdad))
    print(f"Tu estatura es: {fltEstatura}")
    print(type(fltEstatura))
    print(f"La fecha es: {dtfecha}")
    print(type(dtfecha))
    print(f"La fecha y hora: {dtfechaFull}")
    print(type(dtfechaFull))

# ejemplo()
main()