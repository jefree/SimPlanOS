from planificador import Planificador
from logica.proceso import ProcesoPrioridad
from logica.util import Cola
from logica.proceso import LISTO

class PrioridadApropiativo(Planificador):

	def agregar_proceso(self, nombre, tiempo, sistema, recursos, **kwargs):

		p = ProcesoPrioridad(nombre, tiempo, sistema, recursos, kwargs['prioridad'])

		self.agregar_ordenado(p)
		self.vista.informar_entra_listo()

		return p

	def agregar_ordenado(self, proceso):

		cola = Cola()
		p = self.listos.atender()

		while p:
			if proceso.prioridad < p.prioridad:
				break

			cola.insertar(p)
			p = self.listos.atender()

		cola.insertar(proceso)

		while p:
			cola.insertar(p)
			p = self.listos.atender()

		self.listos = cola

class PrioridadNoApropiativo(PrioridadApropiativo):

	def plan_listo(self, proceso_actual):

		asignar_nuevo = False

		cola_aux = Cola()
		
		proceso = self.listos.atender()

		if proceso and (proceso.prioridad < proceso_actual.prioridad):
			asignar_nuevo = True

		while (proceso):
			cola_aux.insertar(proceso)
			proceso = self.listos.atender()

		self.listos = cola_aux

		return asignar_nuevo
