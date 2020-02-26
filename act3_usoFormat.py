# Utiliza la función format de un string, para incrustar valores
# en una salida.

def main():
  intBase = 10
  intAltura = 6
  fltAreaTriangulo=(intBase*intAltura)/2
  txt = "Area: {2:0.2f} ( {0} por {1} entre dos )"
  print(txt.format(intBase, intAltura, fltAreaTriangulo))

  intDistanciaKm = 1750
  fltTiempo = 3.2
  fltVelocidad=(intDistanciaKm/fltTiempo)
  txt2 = "La velocidad promedio fue de: {2:0.2f} ({0} entre {1})"
  print(f"{txt2.format(intDistanciaKm, fltTiempo, fltVelocidad)}")

main()

# El orden de los parámetros proporcionados a format es de base cero.
# {2:0,0f} es un flotante sin decimales.