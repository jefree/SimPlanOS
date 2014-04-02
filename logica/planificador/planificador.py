
from logica.util import Cola
from logica.proceso import *

class Planificador():
	
	def __init__(self):

		self.listos = Cola()
		self.suspendidos = Cola()
		self.bloqueados = Cola()

		self.cuanto_suspendido = 3
		self.contador_suspendido = 3

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

		if proceso_actual.estado == TERMINADO:
			self.suspendidos.insertar(proceso_actual)
			return True

		return False

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

		p = Proceso(nombre, tiempo, sistema, recursos)

		self.listos.insertar(p)
		self.vista.informar_entra_listo()

		return p

	