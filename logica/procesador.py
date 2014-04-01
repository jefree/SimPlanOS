from collections import OrderedDict

class Procesador():

	def __init__(self, nombre, planificador):

		self.nombre = nombre
		self.planificador = planificador
		self.proceso_asignado = None

		self.procesos = {}
		self.gantt = OrderedDict()

	def ejecutar(self):

		self.planificador.planificar_pre(self)
		
		if self.proceso_asignado:
			self.proceso_asignado.ejecutar()

		self.actualizar_gantt()

		self.planificador.planificar_post(self)

	def actualizar_gantt(self):

		for p in self.procesos.values():

			if p == self.proceso_asignado:
				self.gantt[p.nombre].append('X')
			else:
				self.gantt[p.nombre].append('O')

	def agregar_proceso(self, nombre, tiempo, sistema, recursos, **kwargs):
		
		proceso = self.planificador.agregar_proceso(nombre, tiempo, sistema, recursos, **kwargs)
		self.procesos[proceso.nombre] = proceso
		self.gantt[proceso.nombre] = []

		return proceso
