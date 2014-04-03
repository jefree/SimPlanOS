R_NO_USADO = 0
R_USADO = 1
R_BLOQUEADO = 2

R_RETIRADO = 3
R_BLOQUEANDO = 4


class Recurso():

	def __init__(self, nombre):

		self.nombre = nombre
		self.estado = R_NO_USADO
		self.proceso = None

	def asignar(self, proceso):

		self.proceso = proceso
		self.estado = R_USADO

	def liberar(self):
		self.proceso = None
		self.estado = R_NO_USADO

	def bloquear(self, bloqueo):

		if bloqueo:
			self.estado = R_BLOQUEADO
		else:
			self.estado = R_NO_USADO
