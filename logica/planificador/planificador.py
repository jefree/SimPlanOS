
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

		if proceso_actual == None:
			self.asignar_nuevo(procesador)

	def planificar_post(self, procesador):
		
		proceso_actual = procesador.proceso_asignado

		if proceso_actual == None:
			return

		if proceso_actual and proceso_actual.estado == LISTO:

			suspender = self.plan_listo(proceso_actual)
			self.vista.actualizar_info_proceso(proceso_actual)

			if suspender:

				proceso_actual.estado = SUSPENDIDO
				proceso_actual.liberar()

				self.suspendidos.insertar(proceso_actual)
				self.vista.actualizar_todo()
				self.vista.limpiar_info_proceso()

				procesador.proceso_asignado = None

		elif proceso_actual.estado == TERMINADO:
			self.vista.limpiar_info_proceso()

			procesador.proceso_asignado = None

	def plan_bloqueados(self):

		if self.bloqueados.vacia():
			return

		cola = Cola()

		proceso = self.bloqueados.atender()

		while proceso:

			if proceso.solicitar_recursos_necesarios():

				self.vista.informar_desbloqueado(proceso.nombre)

				self.agregar_listo(proceso)
				proceso.estado = LISTO

				self.vista.informar_desbloqueado(proceso.nombre)

			else:
				cola.insertar(proceso)

			proceso = self.bloqueados.atender()

		self.bloqueados = cola

	def plan_suspendidos(self):
		
		if not self.suspendidos.vacia():

			if self.contador_suspendido == 0:
				
				p = self.suspendidos.atender()
				p.estado = LISTO
				
				self.listos.insertar(p)
				self.contador_suspendido = self.cuanto_suspendido

				self.vista.informar_entra_listo()

			else:
				self.contador_suspendido -= 1

	def asignar_nuevo(self, procesador):

		self.vista.informar_removido_actual()

		procesador.proceso_asignado = self.obtener_proceso()

		if procesador.proceso_asignado: 
			procesador.proceso_asignado.estado = LISTO
			self.vista.informar_nuevo()

	def agregar_listo(self, proceso):
		self.listos.insertar(proceso)
		self.vista.informar_entra_listo()

	def obtener_proceso(self):
		
		proceso = None	#proceso que se asignara

		if not self.listos.vacia():
			proceso_aux =  self.listos.atender()

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

	def plan_listo(self, proceso_actual):
		return False

	def asignar_vista(self, vista):
		self.vista = vista

	def agregar_proceso(self, nombre, tiempo, sistema, recursos, **kwargs):

		p = Proceso(nombre, tiempo, sistema, recursos)

		self.agregar_listo(p)

		return p

	