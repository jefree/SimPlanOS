class Procesador():

	def __init__(self, nombre, planificador):

		self.nombre = nombre
		self.planificador = planificador
		self.proceso_asignado = None

	def ejecutar(self):

		self.planificador.planificar_pre(self)
		
		if self.proceso_asignado:
			self.proceso_asignado.ejecutar()

		self.planificador.planificar_post(self)

	def agregar_proceso(self, nombre, tiempo, sistema, recursos):
		return self.planificador.agregar_proceso(nombre, tiempo, sistema, recursos)
