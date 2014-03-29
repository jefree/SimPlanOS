
from logica.util import Cola
from logica.proceso import *

class Planificador():
	
	def __init__(self):

		self.listos = Cola()
		self.suspendidos = Cola()
		self.bloqueados = Cola()


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

	def obtener_proceso(self):
		pass

	def plan_suspendidos(self):
		pass

	def agregar_proceso(self):
		pass