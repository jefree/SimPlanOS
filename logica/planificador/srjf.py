from sjf import SJF
from logica.util import Cola

class SRJF(SJF):

	def plan_listo(self, proceso_actual):

		cola_aux = Cola()
		proceso = self.listos.atender()

		asignar_nuevo = False

		while proceso:
			if proceso.tiempo < proceso_actual.tiempo:
				asignar_nuevo = True
			
			cola_aux.insertar(proceso)
			proceso = self.listos.atender()

		self.listos = cola_aux

		return asignar_nuevo