from random import randint

from logica.recurso import *

LISTO = 0
BLOQUEADO = 1
TERMINADO = 2
SUSPENDIDO = 3

class Proceso():

	"""
		Un proceso representa un programa en ejecucion, el cual
		necesita de un tiempo para terminar su ejecucion y de unos
		recursos para poder ejecutarse.
	"""

	def __init__(self, nombre, tiempo, sistema, recursos_necesarios):

		self.nombre = nombre
		self.tiempo = tiempo
		self.sistema = sistema

		self.estado = LISTO

		self.recursos_necesarios = dict()

		for r in recursos_necesarios:
			self.recursos_necesarios[r] = R_NO_USADO

	def solicitar_recursos_necesarios(self):

		solicitados = True

		for recurso, estado in self.recursos_necesarios.iteritems():

			if estado == R_NO_USADO:
				solicitados = solicitados and self.solicitar_recurso(recurso)

		return solicitados

	def solicitar_recurso(self, recurso):
		"""
			El proceso solicitara el recurso especificado, de no obtenerlo se bloqueara
			e informara que no pudo obtenerlo.
		"""

		obtenido = False

		if self.sistema.solicitar_recurso(recurso, self):

			self.recursos_necesarios[recurso] = R_USADO
			obtenido = True
		
		else:
			self.estado = BLOQUEADO

		return obtenido 

	def liberar_recurso(self, recurso):

		if self.recursos_necesarios[recurso] == R_USADO:
			self.sistema.liberar_recurso(recurso)
			self.recursos_necesarios[recurso] = R_NO_USADO

	def listar_recursos_usados(self):

		lista = []

		for recurso, estado in self.recursos_necesarios.iteritems():
			if estado == R_USADO:
				lista.append(recurso)

		return lista

	def liberar(self):

		for recurso in self.listar_recursos_usados():
			self.liberar_recurso(recurso)

	def ejecutar(self):

		self.tiempo -= 1

		if self.tiempo == 0:
			self.estado = TERMINADO
			self.liberar()
		
			
