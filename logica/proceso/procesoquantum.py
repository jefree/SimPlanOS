from proceso import Proceso

class ProcesoQuantum(Proceso):

	def __init__(self, nombre, tiempo,  sistema, recursos):
		Proceso.__init__(self, nombre, tiempo, sistema, recursos)

		self.cuanto = 0