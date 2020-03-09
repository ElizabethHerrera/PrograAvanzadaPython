# Programa para la conversión de un número en un sistema númerico (X), a otro sistema númerico (Y)
# Bases aceptables: base2 a base35.

import re
import math

# --- Variables globales ---
# diccionario con índices literales.
dcabc = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21,
"M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35}

# diccionario con índices numericas.
dc123 = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J", 20:"K", 21:"L",
22:"M", 23:"N", 24:"O", 25:"P", 26:"Q", 27:"R", 28:"S", 29:"T", 30:"U", 31:"V", 32:"W", 33:"X", 34:"Y", 35:"Z"}

_opcion = ""
opcion = 0

_baseC = ""
baseC = 0

def pedirnumeros(opcion):
    # función para solicitar el número para la conversión.
    # -- variables locales --
    _cantidad = 0
    _cadenalist = []
    _charlist = []
    _numero = ""
    _base = 0
    _counter = 0

    # variables para almacenamiento del numero solicitado.
    x = "" # el numero en literales.
    cadenaX = [] # lista de los carácteres del número en str.
    charX = [] # lista con los numeros en int.

    bx = 0

    while True:
        _numero=input("Ingresa un número: ")
        if _numero:
            for _char in _numero:
                _cadenalist.append(_char.upper()) # agrega a la lista '_cadenalist' por carácteres, en mayús.
                char = chr(ord(_char.upper())) # identifica el número de la letra en el abecedario.

                if char in dcabc: # verifica si el carácter es una literal.
                    # agrega a la lista '_charlist' su valor númerico, dependiendo de su posición
                    # en el diccionario 'dcabc'.
                    _charlist.append(dcabc[char])
                else:
                    if re.findall("^\d+(\.\d+)?$", _char): # verifica que sea un valor númerico.
                        numero = int(char)
                        _charlist.append(numero) # agrega a la lista '_charlist' su valor númerico.

            _base = max(_charlist) + 1 # identifica el número mayor.

            while True:
                _b = input("ingresar base: ")
                if re.findall("^\d+(\.\d+)?$", _b):
                    b = int(_b)
                    if _base > b: # verifica que la base no sea menor al número mayor.
                        print("Base menor a valores en el numero")
                        print(f"Base minima requerida: {_base}")
                    else:
                        break
                else:
                    print("Ingrese un valor númerico")

            # agrega los valores correspondientes.
            cadenaX = _cadenalist
            charX = _charlist
            bx = b # sistema númerico del número, int

            _cadenalist = []
            _charlist = []
            break
        else:
            print("¡No se permiten valores vacios!\n")

    x = x.join([str(z) for z in cadenaX]) # concatena los valores de la lista str.
    print("---")
    print(f"Numero ingresado: {x} con base {bx}")

    dcX = {0:x, 1:bx, 2:charX} # agrega los valores de las variables a un diccionario 'dcX'.
    return dcX

def conversion(bc, _num, bx, _anum):
    # variables locales
    n = 0 # cantidad de veces a realizar 2^n.
    fn = -1 # cantidad de veces a realizar 2^n-1.
    i = 0 # cantidad de decimas finales.

    # variables para la parte entera, multiplicación/división.
    iproducto = 0
    iresiduo = 0.00
    icociente = 0.00
    iresultado = []

    # variables para la parte decimal, multiplicación/división.
    fproducto = 0
    fdecimals = 0.00
    finteger = 0.00
    fresultado = []

    # variables para mostrar el resultado.
    istrnumero = ""
    fstrnumero = ""

    # variables para el manejo de números con base > 10.
    _ihex = []
    _fhex = []

    _numt = _num.find('.' ) # identifica la posición del punto decimal.
    _inum = _num[0:_numt] # separa la parte entera apartir del indice encontrado en '_numt'.

    _fnum = _num[::-1] # invierte el orden de la cadena.
    _numt = _fnum.find('.') # identifica la posición del punto decimal.
    _fnum = _fnum[0:_numt] # separa la parte entera apartir del indice encontrado en '_numt'.

    fnum = _fnum[::-1] # Se invierte el orden de la cadena a su estado original.
    inum = _inum[::-1] # Se invierte el orden de la cadena.

    if bx > 10:
        for _alphanumber in inum:
            if _alphanumber in dcabc: # se identifica si el carácter se encuentra en 'dcabc'
                alphanumber = dcabc[_alphanumber]
                _ihex.append(alphanumber)
            else:
                # se agrega 'alphanumber' a la lista '_ihex'
                # convirtiendo su valor a int.
                _ihex.append(int(_alphanumber))

        # mismo procedimiento pero para la parte decimal.
        for _alphanumber in fnum:
            if _alphanumber in dcabc:
                alphanumber = dcabc[_alphanumber]
                _fhex.append(alphanumber)
            else:
                _fhex.append(int(_alphanumber))

        for char in _ihex: # se realiza la operación [número*(base^n)] / 2^n
            _iproducto = char
            _iproducto = _iproducto * (bx ** n)
            iproducto = iproducto + _iproducto
            n = n + 1

        for char in _fhex: # se realiza la operación [número*(base^n-1)] / 2^n-1
            _fproducto = char
            _fproducto = int(_fproducto)
            _fproducto = _fproducto * (bx ** fn)
            fproducto = fproducto + _fproducto
            fn = fn - 1

    else:
        for char in inum: # se realiza la operación [número*(base^n)] / 2^n [enteros]
            _iproducto = char
            _iproducto = int(_iproducto)
            _iproducto = _iproducto * (bx ** n)
            iproducto = iproducto + _iproducto
            n = n + 1

        for char in fnum: # se realiza la operación [número*(base^n-1)] / 2^n-1 [decimales]
            _fproducto = char
            _fproducto = int(_fproducto)
            _fproducto = _fproducto * (bx ** fn)
            fproducto = fproducto + _fproducto
            fn = fn - 1

    while iproducto > 0: # se realizan las divisiones de la parte entera.
        icociente, iresiduo = divmod(iproducto, bc)
        iproducto = icociente
        _icociente = str(icociente)
        iresultado.append(iresiduo)

    while i < 4: # se realizan las multiplicaciones de la parte fraccionaria.
        fproducto = fproducto * bc
        fdecimals, finteger = math.modf(fproducto)
        fresultado.append(finteger)
        fproducto = fdecimals
        i = i + 1

    # Si base final es diferente de 10, se realizan las conversiones necesarias
    # para remplazar valores > 10 por sus literales correspondientes.
    if bc != 10:
        for _numero in iresultado:
            numero = int(_numero)
            if numero in dc123:
                numero = dc123[numero]
                istrnumero = istrnumero + str(numero)
            else:
                istrnumero = istrnumero + str(numero)
    if bc != 10:
        for _numero in fresultado:
            numero = int(_numero)
            if numero in dc123:
                numero = dc123[numero]
                fstrnumero = fstrnumero + str(numero)
            else:
                fstrnumero = fstrnumero + str(numero)

    # se imprime el resultado final.
    istrnumero = istrnumero[::-1]
    txt = "Resultado final: {0}.{1} en base {2}"
    print(txt.format(istrnumero, fstrnumero, bc))
    print("\b")

# MENU ---
while True:
    print("---- Operaciones ----")
    print("1) Conversión -- 2) Salir")
    _opcion=input("Seleccione una opción: ")

    if re.findall("^\d+(\.\d+)?$", _opcion):
        opcion=int(_opcion)
        if opcion <= 3 and opcion >= 1:
            if opcion == 1:
                # llama la función para solicitar un número.
                numeroX = pedirnumeros(opcion)
                while True:
                    _baseC = input("Base a convertir: ")
                    if re.findall("^\d+(\.\d+)?$", _baseC):
                        baseC = int(_baseC)
                        if baseC >= 2 and baseC <= 35 and baseC != numeroX[1]:
                            # llama la función para realizar la conversión de sistemas númericos.
                            conversion(baseC, numeroX[0], numeroX[1], numeroX[2])
                            break
                        else:
                            print("Base fuera de parámetros o es la misma base en la que se encuentra actualmente")
                    else:
                        print("Ingrese un valor númerico")
            elif opcion == 2:
                print("Fin del programa")
                break
        else:
            print("Opción no encontrada\n")
    else:
	    print("Se requiere un número entre las opciones\n")
print("Adios")