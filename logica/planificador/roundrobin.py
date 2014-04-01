from planificador import Planificador
from logica.proceso import ProcesoQuantum
from logica.util import Cola
import os

class RoundRobin(Planificador):

	def obtener_proceso(self):

		proceso = None

		if not self.listos.vacia():
			proceso =  self.listos.atender()

		elif not self.suspendidos.vacia():

			self.contador_suspendido = self.cuanto_suspendido
			self.listos.insertar(self.suspendidos.atender())

			self.vista.informar_entra_listo()

			self.calcular_cuantos()

			proceso = self.listos.atender()
			
		if proceso:
			proceso.cuanto -= 1

		return proceso

	def plan_listo(self, proceso_actual):

		asignar_nuevo = False

		if proceso_actual.cuanto == 0:
			self.suspendidos.insertar(proceso_actual)
			asignar_nuevo = True

		else:	
			proceso_actual.cuanto -= 1

		return asignar_nuevo

	def plan_suspendidos(self):

		if not self.suspendidos.vacia():

			if self.contador_suspendido == 0:
				
				self.listos.insertar(self.suspendidos.atender())
				self.contador_suspendido = self.cuanto_suspendido

				self.calcular_cuantos()

				self.vista.informar_entra_listo()

			else:
				self.contador_suspendido -= 1

	def calcular_cuantos(self):

		cola = Cola()
		lista = self.listos.listar()

		medio = sum(p.tiempo for p in lista) / len(lista)

		proceso = self.listos.atender()

		while proceso:

			dist = proceso.tiempo - medio
			cuanto = medio

			if dist > 0:

				if dist > medio * 0.5:
					cuanto = medio * 1.3
				else:
					cuanto = medio
			else:

				if dist < medio*-0.5:
					cuanto = proceso.tiempo
				else:
					cuanto = proceso.tiempo*0.8

			proceso.cuanto = int(round(cuanto))

			cola.insertar(proceso)
			proceso = self.listos.atender()

		self.listos = cola

	def agregar_proceso(self, nombre, tiempo, sistema, recursos):
		p = ProcesoQuantum(nombre, tiempo, sistema, recursos)

		self.listos.insertar(p)
		self.calcular_cuantos()

		self.vista.informar_entra_listo()

		return p
