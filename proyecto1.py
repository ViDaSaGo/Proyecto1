#
# Archivo: ej_archivo.py
#
# Descripcion: Ejemplo de lectura de un archivo con formato
#

import sys
from ADN import*

def procesar_archivo(nombre_archivo):
	linea_adn_simple = []                       	# Se crea una lista de tuplas vacias
	with open(nombre_archivo, "r") as fd:   # Se abre el archivo para lectura
		for line in fd:                    # Se lee linea por linea
			line = line.rstrip()       # Se elimina el salto-de-linea al final de la linea
			tok = line.split("\t")     # Se parte la linea en el caracter tabulador [TAB]
			nombre = tok[0]            # Se obtiene el nombre
			t = nombre 
			linea_adn_simple.append(t)          # Se agrega la tupla a la lista de tuplas
			print(linea_adn_simple)

	cadenas = []
	for i in linea_adn_simple:
		lista = list(i)
		cadenas.append(lista)
	print(cadenas)

	for i in cadenas:
		q = ADN_doble()
		q.azip(i)

	return cadenas                          # Se retorna la lista de tuplas


####################
####################
#      Main
####################
####################

if __name__ == "__main__":
	lm = procesar_archivo(sys.argv[1])
