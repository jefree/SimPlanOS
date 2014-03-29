from planificador import Planificador
from logica.proceso import *
from logica.util import Cola

class RoundRobin(Planificador):
	
	def __init__(self):
		Planificador.__init__(self)
		
		self.cuanto_suspendido = 3
		self.contador_suspendido = 0

	def obtener_proceso(self):

		proceso = None

		if not self.listos.vacia():
			proceso =  self.listos.atender()

		elif not self.suspendidos.vacia():

			self.contador_suspendido = self.cuanto_suspendido
			self.listos.insertar(self.suspendidos.atender())

			self.calcular_cuantos()

			proceso = self.listos.atender()
			
		if proceso:
			proceso.cuanto -= 1

		return proceso

	def plan_suspendidos(self):

		if not self.suspendidos.vacia():

			if self.contador_suspendido == 0:
				
				self.listos.insertar(self.suspendidos.atender())
				self.contador_suspendido = self.cuanto_suspendido

				self.calcular_cuantos()

			else:
				self.contador_suspendido -= 1

	def calcular_cuantos(self):

		cola = Cola()
		proceso = self.listos.atender()

		while proceso:

			proceso.cuanto = 3
			cola.insertar(proceso)
			proceso = self.listos.atender()

		self.listos = cola

	def agregar_proceso(self, nombre, tiempo, sistema, recursos):
		self.listos.insertar(ProcesoQuantum(nombre, tiempo, sistema, recursos))
		self.calcular_cuantos()
