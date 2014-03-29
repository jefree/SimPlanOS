from random import randint

from logica.recurso import *

EJECUTANDO = 0
BLOQUEADO = 1
TERMINADO = 2

class Proceso():

	def __init__(self, nombre, tiempo, sistema, recursos_necesarios):

		self.nombre = nombre
		self.tiempo = tiempo
		self.sistema = sistema

		self.estado = EJECUTANDO
		self.recurso_bloqueado = None

		self.recursos_necesarios = dict()

		for r in recursos_necesarios:
			self.recursos_necesarios[r] = R_NO_USADO

	def bloquear_por_recurso(self):

		bloquear = False

		for recurso, estado in self.recursos_necesarios.iteritems():

			if estado == R_NO_USADO:

				if randint(0, 2) == 0:
					if not self.solicitar_recurso(recurso):
						print self.nombre, "no obtuvo", recurso

						self.recursos_necesarios[recurso] = R_BLOQUEADO
						self.recurso_bloqueado = recurso
						bloquear = True

			else:

				if randint(0, 1) == 0:
					self.liberar_recurso(recurso)

		return bloquear

	def solicitar_recurso(self, recurso):

		print self.nombre, "solicitando recurso:", recurso

		if self.sistema.solicitar_recurso(recurso, self):
			self.recursos_necesarios[recurso] = R_USADO
			return True

		return False

	def liberar_recurso(self, recurso):

		print self.nombre, "liberando:", recurso

		self.sistema.liberar_recurso(recurso)
		self.recursos_necesarios[recurso] = R_NO_USADO

	def solicitar_recurso_bloqueado(self):

		print self.nombre, "solicitando bloqueado:", self.recurso_bloqueado

		return self.solicitar_recurso(self.recurso_bloqueado)

	def terminar(self):

		for recurso in self.recursos_necesarios:
			if self.recursos_necesarios[recurso] == R_BLOQUEADO:
				self.liberar_recurso(recurso)

	def ejecutar(self):

		self.estado = EJECUTANDO

		print self.nombre, self.tiempo

		self.tiempo -= 1

		if self.tiempo > 0:
			if self.bloquear_por_recurso():
				self.estado = BLOQUEADO
		else:
			self.estado = TERMINADO

			self.terminar()
