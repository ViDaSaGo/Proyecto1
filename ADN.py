############################################################
# Proyecto1 version 1.0
############################################################


from ADNsimple import *


"""""""""""""""""""""""""""""""""""""""""""""
Clase ADN doble

"""""""""""""""""""""""""""""""""""""""""""""


class cadena_doble(object):
	def __init__(self,cadena):
		self._head = None
		self._size = 0










class ADN_doble(object):
	def __init__(self,cadenadoble):
		self._
		self._size = 0
	'''
	metodo zip:
		Descripcion: recibe una cadena simple la complementa y crea la
		cadena doble
	'''
	
	def azip(self,cadenasimple):
		cadenadoble = []                    
		compl = ADNsimple()
		compl.complementar(cadenasimple)
		for a in cadenasimple:
			if a == 'A':
				cadenadoble.append((str(a)+'T'))
			if a == 'T':
				cadenadoble.append((str(a)+'A'))
			if a == 'G':
				cadenadoble.append((str(a)+'C'))
			if a == 'C':
				cadenadoble.append((str(a)+'G'))

		print(cadenadoble)
		return cadenadoble

	def _unzip(self,cadenadoble):
		pass



		