from sistema import Sistema
from logica.procesador import Procesador
from logica.planificador import SRJF

class SistemaSRJF(Sistema):

	def __init__(self, n_procesadores):
		Sistema.__init__(self)

		for n in range(n_procesadores):
			self.procesadores.append(Procesador("Procesador %d" % (n+1), SRJF()))
