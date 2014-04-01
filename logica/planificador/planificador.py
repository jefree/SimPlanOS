
from logica.util import Cola
from logica.proceso import *

class Planificador():
	
	def __init__(self):

		self.listos = Cola()
		self.suspendidos = Cola()
		self.bloqueados = Cola()

		self.cuanto_suspendido = 3
		self.contador_suspendido = 3

	def planificar_pre(self, procesador):
		
		asignar_nuevo = False
		proceso_actual = procesador.proceso_asignado

		self.plan_bloqueados()
		self.plan_suspendidos()

		if proceso_actual:
			estado = proceso_actual.estado

			if estado == TERMINADO:
				asignar_nuevo = True

			elif estado == LISTO:

				asignar_nuevo = self.plan_listo(proceso_actual)

				if asignar_nuevo:
					proceso_actual.estado = SUSPENDIDO
					self.vista.informar_suspendido()
		else:
			asignar_nuevo = True

		if asignar_nuevo:

			procesador.proceso_asignado = self.obtener_proceso()
			procesador.proceso_asignado.estado = LISTO
			
			self.vista.informar_nuevo()

	def planificar_post(self, procesador):
		
		proceso_actual = procesador.proceso_asignado

		if proceso_actual:
			estado = proceso_actual.estado

			if estado == BLOQUEADO:

				self.vista.informar_bloqueado()

				self.bloqueados.insertar(proceso_actual)
				procesador.proceso_asignado = None

	def plan_bloqueados(self):

		if self.bloqueados.vacia():
			return

		cola = Cola()

		proceso = self.bloqueados.atender()

		while proceso:

			if proceso.solicitar_desbloqueo():
				self.listos.insertar(proceso)
				proceso.estado = LISTO

				self.vista.informar_desbloqueado(proceso.nombre)

			else:
				cola.insertar(proceso)

			proceso = self.bloqueados.atender()

		self.bloqueados = cola

	def asignar_vista(self, vista):
		self.vista = vista

	def obtener_proceso(self):
		pass

	def plan_suspendidos(self):
		pass

	def agregar_proceso(self):
		pass

	def plan_listo(self, proceso):
		pass
