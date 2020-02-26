# Pregunta un dato hasta que sea correcto, haciendo validaciones usando
# expresiones regulares.

# Importa el módulo requerido para usar Regular Expressions.
import re

def ejemplo():
  # Infinty Loop - Itera hasta que se presenta un break
  # Estará preguntando el dato, mientras no cumpla con el patrón de la
  # expesión regular.
  while True:
    strRFC = input("Dame el RFC: ")
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      print("RFC Correcto!")
      break
    else:
      print("RFC incorrecto. Intenta de nuevo.")
   

def main():
    while True:
        strCURP = input("Dame el CURP: ")
        coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z]{6}-[0-9]{2}$", strCURP)
        if (coincide):
            print("CURP Correcto!")
            break
        else:
            print("CURP incorrecto. Intenta de nuevo.")

# ex. ABCD-123456-AA9
# ejemplo()

# ex. ASDF-123456-QWERTY-05
main()