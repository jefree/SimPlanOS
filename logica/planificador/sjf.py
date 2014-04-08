from planificador import Planificador
from logica.proceso import Proceso
from logica.util import Cola

class SJF(Planificador):

	def obtener_proceso(self, proceso_actual):

		proceso = None

		if not self.listos.vacia():

			if proceso_actual == None:
				proceso = self.listos.atender()
			
			else:

				if proceso_actual.tiempo == -1:
					proceso_actual = self.listos.atender()
				
				proceso = self.obtener_proceso_menor(proceso_actual)

		elif not self.suspendidos.vacia():

			self.contador_suspendido = self.cuanto_suspendido
			self.listos.insertar(self.suspendidos.atender())
			
			self.vista.informar_entra_listo()

			proceso = self.listos.atender()

		return proceso

	def obtener_proceso_menor(self, proceso_actual):

		cola_aux = Cola()

		proceso_aux = self.listos.atender()
		proceso_nuevo = proceso_actual

		while proceso_aux:

			if proceso_nuevo.tiempo < proceso_aux.tiempo:
				cola_aux.insertar(proceso_aux)

			else:
				cola_aux.insertar(proceso_nuevo)
				proceso_nuevo = proceso_aux
			
			proceso_aux = self.listos.atender()

		self.listos = cola_aux

		return proceso_nuevo
