class Procesador():

	def __init__(self, nombre, planificador):

		self.nombre = nombre
		self.planificador = planificador
		self.proceso_asignado = None

	def ejecutar(self):

		self.planificador.planificar(self)
		
		if self.proceso_asignado:
			self.proceso_asignado.ejecutar()
		else:
			print "No hay proceso asignado"

	def agregar_proceso(self, nombre, tiempo, sistema, recursos):
		self.planificador.agregar_proceso(nombre, tiempo, sistema, recursos)
