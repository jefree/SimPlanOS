from planificador import Planificador
from logica.proceso import ProcesoPrioridad
from logica.util import Cola
from logica.proceso import LISTO

class PrioridadApropiativo(Planificador):

	def obtener_proceso(self):
		
		proceso = None

		if not self.listos.vacia():
			proceso =  self.listos.atender()

		elif not self.suspendidos.vacia():

			self.contador_suspendido = self.cuanto_suspendido
			self.listos.insertar(self.suspendidos.atender())

			proceso = self.listos.atender()

			self.vista.informar_entra_listo()

		return proceso


	def plan_listo(self, proceso_actual):
		
		asignar_nuevo = False

		if proceso_actual.tiempo == 0:
			self.suspendidos.insertar(proceso_actual)
			asignar_nuevo = True

		return asignar_nuevo


	def plan_suspendidos(self):
		
		if not self.suspendidos.vacia():

			if self.contador_suspendido == 0:
				
				p = self.suspendidos.atender()
				p.estado = LISTO
				
				self.agregar_ordenado(p)
				self.contador_suspendido = self.cuanto_suspendido

				self.vista.informar_entra_listo()

			else:
				self.contador_suspendido -= 1

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
