from planificador import Planificador
from logica.proceso import ProcesoQuantum
from logica.proceso import LISTO
from logica.util import Cola
import os

class RoundRobin(Planificador):

	def agregar_listo(self, proceso):
		Planificador.agregar_listo(self, proceso)
		self.calcular_cuantos()
		self.vista.informar_entra_listo()

	def obtener_proceso(self):

		proceso = None	#proceso que se asignara

		if not self.listos.vacia():
			proceso_aux =  self.listos.atender()

			if proceso_aux.solicitar_recursos_necesarios():
				proceso = proceso_aux
			else:
				self.bloqueados.insertar(proceso_aux)
				
				self.vista.actualizar_todo()

				proceso = self.obtener_proceso()

		elif not self.suspendidos.vacia():

			self.contador_suspendido = self.cuanto_suspendido
			self.listos.insertar(self.suspendidos.atender())
			
			self.vista.informar_entra_listo()
			self.calcular_cuantos()

			proceso = self.obtener_proceso()			

		return proceso

	def plan_listo(self, proceso_actual):

		asignar_nuevo = False

		proceso_actual.cuanto -= 1

		if proceso_actual.cuanto == 0:
			asignar_nuevo = True

		return asignar_nuevo

	def plan_suspendidos(self):

		if not self.suspendidos.vacia():

			if self.contador_suspendido == 0:
				
				p = self.suspendidos.atender()
				p.estado = LISTO

				self.listos.insertar(p)
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

		self.agregar_listo(p)

		return p
