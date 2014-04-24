from time import sleep
import os

from logica.recurso import *
from logica.procesador import *
from logica.proceso import *
from logica.planificador import RoundRobin
class Sistema():

	def __init__(self):

		self.procesadores = []
		self.procesos = OrderedDict()
		self.recursos = {}

		self.contador_procesador = 0

	def ejecutar(self):
		
		for procesador in self.procesadores:
			procesador.ejecutar()

		self.plan_recursos()

	def dar_permiso_ejecucion(self, proceso):
		return True

	def agregar_a_cola(self, proceso):

		#insercion por FIFO 
		self.procesos[proceso.nombre] = proceso
	
	def agregar_proceso(self, nombre, tiempo, recursos, n_procesador, **kwargs):

		n = self.contador_procesador
		self.contador_procesador = (self.contador_procesador+1) % len(self.procesadores)
		n_procesador -= 1

		if n_procesador >= 0 and n_procesador < len(self.procesadores):
			n = n_procesador

		proceso = self.procesadores[n].agregar_proceso(nombre, tiempo, self, recursos, **kwargs)

		self.agregar_a_cola(proceso)

		self.vista.informar_nuevo_proceso(proceso.nombre)

	def agregar_recurso(self, nombre):

		self.recursos[nombre] = Recurso(nombre)
		self.vista.informar_nuevo_recurso(nombre)

	def plan_recursos(self):
		""" Retira los recursos a los procesos bloqueados. """

		for nombre, recurso in self.recursos.iteritems():

			if recurso.estado == R_USADO and recurso.proceso.estado == BLOQUEADO:

				recurso.proceso.retirar_recurso(nombre)
				recurso.estado = R_NO_USADO

	def solicitar_recurso(self, nombre, proceso):		

		self.vista.informar_solicitud(proceso.nombre, nombre)

		if nombre not in self.recursos:
			return False

		recurso = self.recursos[nombre]
		disponible = False

		if recurso.estado != R_BLOQUEADO:

			if recurso.estado == R_NO_USADO:
				
				recurso.asignar(proceso)
				disponible = True

			elif proceso == recurso.proceso:
				disponible = True

		return disponible

	def liberar_recurso(self, nombre):
		
		if nombre not in self.recursos:
			return

		self.vista.informar_liberacion(self.recursos[nombre].proceso.nombre, nombre)

		recurso = self.recursos[nombre]

		if recurso:
			recurso.liberar()

	def asignar_vista(self, vista):
		self.vista = vista
