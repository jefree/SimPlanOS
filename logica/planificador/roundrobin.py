from logica.proceso import *
from logica.util import Cola
from logica.proceso import *

class RoundRobin():
	
	def __init__(self):

		self.listos = Cola()
		self.suspendidos = Cola()
		self.bloqueados = Cola()

		self.cuanto_suspendido = 3
		self.contador_suspendido = 0

	def planificar(self, procesador):
		
		asignar_nuevo = False
		proceso_actual = procesador.proceso_asignado

		self.plan_bloqueados()
		self.plan_suspendidos()
		
		if proceso_actual:

			estado = proceso_actual.estado

			if estado == TERMINADO:
				asignar_nuevo = True

			elif estado == BLOQUEADO:
				self.bloqueados.insertar(proceso_actual)
				asignar_nuevo = True

			elif estado == EJECUTANDO:

				if proceso_actual.cuanto == 0:
					self.suspendidos.insertar(proceso_actual)
					asignar_nuevo = True
				
				else:
					proceso_actual.cuanto -= 1
		else:
			asignar_nuevo = True

		if asignar_nuevo:
			procesador.proceso_asignado = self.obtener_proceso()

		print ""
		print ""
		print "BLOQUEADOS"
		
		for p in self.bloqueados.listar():
			print p.nombre, p.recurso_bloqueado

		print "-------------"

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

	def plan_bloqueados(self):

		if self.bloqueados.vacia():
			return

		cola = Cola()

		proceso = self.bloqueados.atender()

		while proceso:

			if proceso.solicitar_recurso_bloqueado():
				self.suspendidos.insertar(proceso)
			else:
				print proceso.nombre, "no obtuvo bloqueado", proceso.recurso_bloqueado
				cola.insertar(proceso)

			proceso = self.bloqueados.atender()

		self.bloqueados = cola

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
