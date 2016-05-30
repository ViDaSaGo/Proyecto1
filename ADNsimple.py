##################################################################
# Archivo con la implementacion de una cade simple de ADN
##################################################################



class ADNsimple:
	def complementar(self,cadenasimple):
		complemento = []
		for a in cadenasimple:
			if a == 'A':
				complemento.append('T')
			if a == 'T':
				complemento.append('A')
			if a == 'G':
				complemento.append('C')
			if a == 'C':
				complemento.append('G')
			return complemento
