from proceso import *
from collections import OrderedDict

class Procesador():

	def __init__(self, nombre, planificador):

		self.nombre = nombre
		self.planificador = planificador
		self.proceso_asignado = None

		self.procesos = {}
		self.gantt = OrderedDict()
		self.tiempo = 0

	def ejecutar(self):

		self.tiempo += 1
		self.planificador.planificar_pre(self)
		
		if self.proceso_asignado:
			self.proceso_asignado.ejecutar()

		self.actualizar_gantt()

		self.planificador.planificar_post(self)

	def actualizar_gantt(self):

		for p in self.procesos.values():

			if p.nombre == self.proceso_asignado.nombre:
				self.gantt[p.nombre].append('X')
			
			elif p.estado == SUSPENDIDO:
				self.gantt[p.nombre].append('S')

			elif p.estado == BLOQUEADO:
				self.gantt[p.nombre].append('B')

			elif p.estado == LISTO:
				self.gantt[p.nombre].append('L')

			elif p.estado == TERMINADO:
				self.gantt[p.nombre].append('T')

	def agregar_proceso(self, nombre, tiempo, sistema, recursos, **kwargs):
		
		proceso = self.planificador.agregar_proceso(nombre, tiempo, sistema, recursos, **kwargs)
		self.procesos[proceso.nombre] = proceso
		self.gantt[proceso.nombre] = ['-']*self.tiempo

		return proceso
