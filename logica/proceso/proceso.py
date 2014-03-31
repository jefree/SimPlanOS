from random import randint

from logica.recurso import *

LISTO = 0
BLOQUEADO = 1
TERMINADO = 2

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

	def plan_recursos_necesarios(self):

		for recurso, estado in self.recursos_necesarios.iteritems():

			if estado == R_NO_USADO:

				if True: #randint(0, 2) == 0:
					self.solicitar_recurso(recurso)
						
			elif estado == R_USADO:

				if self.solicitar_recurso(recurso):

					if False:#randint(0, 1) == 0:
						self.liberar_recurso(recurso)

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

			self.recursos_necesarios[recurso] = R_BLOQUEANDO
			self.estado = BLOQUEADO

		return obtenido 

	def liberar_recurso(self, recurso):

		if self.recursos_necesarios[recurso] == R_USADO:
			self.sistema.liberar_recurso(recurso)
			self.recursos_necesarios[recurso] = R_NO_USADO

	def retirar_recurso(self, recurso):
		"""
			Si un proceso se bloquea el sistema llamara este metodo
			para retirar un recurso que este usando.

			Cuando el proceso se reanude debera solicitar de nuevo 
			los recursos retirados.
		"""

		self.recursos_necesarios[recurso] = R_RETIRADO

	def solicitar_recursos_bloqueando(self):
		""" El proceso solictara todos aquellos recursos que hayan 
			bloqueado su ejecucion
		"""
		
		r_bloqueando = self.listar_recursos_bloqueando()
		obtenidos = True

		for recurso in r_bloqueando:
			
			resultado = self.solicitar_recurso(recurso)
			
			obtenidos = obtenidos and resultado

		return obtenidos

	def recuperar_recursos(self):

		"""
			El proceso solicitara al sistema todos aquellos recursos
			que le fueron quitados cuando entro en estado de bloqueo 
		"""

		recuperados = True

		for recurso in self.listar_recursos_retirados():

			resultado = self.solicitar_recurso(recurso)
			recuperados = recuperados and resultado

		return recuperados

	def solicitar_desbloqueo(self):
		"""
			Un proceso bloqueado debera solicitar al sistema todos los recursos
			que necesita para su ejecucion para pasar a estado de LISTO
		"""

		if self.solicitar_recursos_bloqueando() and self.recuperar_recursos():
			self.estado = LISTO

		return self.estado == LISTO


	def listar_recursos_bloqueando(self):

		lista = []

		for recurso, estado in self.recursos_necesarios.iteritems():

			if estado == R_BLOQUEANDO:
				lista.append(recurso)

		return lista

	def listar_recursos_retirados(self):

		lista = []

		for recurso, estado in self.recursos_necesarios.iteritems():
			if estado == R_RETIRADO:
				lista.append(recurso)

		return lista


	def terminar(self):

		for recurso in self.recursos_necesarios:
			self.liberar_recurso(recurso)

	def ejecutar(self):

		self.tiempo -= 1

		if self.tiempo > 0:
			self.plan_recursos_necesarios()

		else:
			self.estado = TERMINADO
			self.terminar()
