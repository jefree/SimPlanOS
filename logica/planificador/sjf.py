from planificador import Planificador
from logica.util import Cola

class SJF(Planificador):

	def obtener_proceso(self):

		proceso = None	#proceso que se asignara

		if not self.listos.vacia():
			proceso_aux = self.obtener_proceso_menor()

			if proceso_aux.solicitar_recursos_necesarios():
				proceso = proceso_aux
			else:
				self.bloqueados.insertar(proceso_aux)
		
				self.vista.actualizar_todo()

				proceso = self.obtener_proceso()

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

			if proceso_aux.tiempo < proceso.tiempo:
				cola_aux.insertar(proceso)
				proceso = proceso_aux
			
			else:
				cola_aux.insertar(proceso_aux)

		self.listos = cola_aux

		return proceso
