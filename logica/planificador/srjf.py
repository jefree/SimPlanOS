from sjf import SJF
from logica.util import Cola

class SRJF(SJF):

	def plan_listo(self, proceso_actual):
		
		asignar_nuevo = False

		cola_aux = Cola()
		
		proceso = self.listos.atender()

		if proceso and (proceso.tiempo < proceso_actual.tiempo):
			asignar_nuevo = True

		while (proceso):
			cola_aux.insertar(proceso)
			proceso = self.listos.atender()

		self.listos = cola_aux

		return asignar_nuevo
