from proceso import Proceso

class ProcesoPrioridad(Proceso):
	
	def __init__(self, nombre, tiempo,  sistema, recursos, prioridad):
		Proceso.__init__(self, nombre, tiempo, sistema, recursos)

		self.prioridad = prioridad
