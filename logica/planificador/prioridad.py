from planificador import Planificador
from logica.proceso import ProcesoPrioridad
from logica.util import Cola
from logica.proceso import LISTO

class PrioridadApropiativo(Planificador):

	def obtener_proceso(self):

		proceso = None	#proceso que se asignara

		if not self.listos.vacia():
			proceso_aux = self.obtener_proceso_menor()

			if proceso_aux.solicitar_recursos_necesarios():
				proceso = proceso_aux
			else:
				self.bloqueados.insertar(proceso_aux)
				proceso = self.obtener_proceso()

				self.vista.actualizar_todo()

		elif not self.suspendidos.vacia():

			self.contador_suspendido = self.cuanto_suspendido
			self.listos.insertar(self.suspendidos.atender())
			
			self.vista.informar_entra_listo()

			proceso = self.obtener_proceso()			

		return proceso

	def obtener_proceso_menor(self):

		cola_aux = Cola()
		proceso = self.listos.atender()

		if proceso == None:
			return None

		while not self.listos.vacia():

			proceso_aux = self.listos.atender()

			if proceso_aux.prioridad < proceso.prioridad:
				cola_aux.insertar(proceso)
				proceso = proceso_aux
			
			else:
				cola_aux.insertar(proceso_aux)

		self.listos = cola_aux

		return proceso


	def agregar_proceso(self, nombre, tiempo, sistema, recursos, **kwargs):
		
		p = ProcesoPrioridad(nombre, tiempo, sistema, recursos, kwargs['prioridad'])

		self.agregar_listo(p)

		return p

class PrioridadNoApropiativo(PrioridadApropiativo):

	def plan_listo(self, proceso_actual):

		cola_aux = Cola()
		proceso = self.listos.atender()

		asignar_nuevo = False

		while proceso:
			if proceso.prioridad < proceso_actual.prioridad:
				asignar_nuevo = True
			
			cola_aux.insertar(proceso)
			proceso = self.listos.atender()

		self.listos = cola_aux

		return asignar_nuevo
