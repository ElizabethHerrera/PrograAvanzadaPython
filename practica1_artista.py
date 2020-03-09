#Importamos 're' para poder usar expresiones regulares.
import re

# Funcion para calcular si la aportacion dada
# es menor o igual a 1000.
def calcularia(valor):
	valorfijo=300
	valorvariable= valor*0.20
	if valor >= 1000:
		return valorvariable
	else:
		return valorfijo

# definicion de variables
_aportacion = ""
aportacion=0.00
minimo= 500.00

# ciclo infinito, que finaliza una vez que
# se ha introducido un valor nu15merico y que sea mayor a 500
while True:
	_aportacion=input("Aportacion: ")
    # validacion sobre si es un valor numerico
	if re.search("^\d+(\.\d+)?$",_aportacion):
		aportacion=float(_aportacion)
		if aportacion < 500:
			print("Aportacion minima 500")
		else:
			break
			# se utiliza para cortar un ciclo
	else:
		print("se requiere una cantidad")

# Se imprimen los valores dados por la funcion 'calcularia()' con formato monetario.
txt= "Aportacion al artista ${:,.2f}"
print(txt.format(calcularia(aportacion)))