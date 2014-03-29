from time import sleep
import os

from logica.recurso import *
from logica.procesador import *
from logica.planificador import RoundRobin

class SistemaRR():

	def __init__(self, n_procesadores):

		self.procesadores = []
		self.recursos = {}

		for n in range(n_procesadores):
			self.procesadores.append(Procesador("Procesador %d" % (n+1), RoundRobin()))

	def ejecutar(self):

		while True:

			os.system('cls')
			
			for procesador in self.procesadores:

				print "--- PROCESADOR:", procesador.nombre, "----"

				procesador.ejecutar()


			print "\n"
			for k in self.recursos:

				if self.recursos[k].proceso:
					print k, "usado:", self.recursos[k].proceso.nombre
				else: 
					print k, "esta libre"

			raw_input()
	
	def agregar_proceso(self, nombre, tiempo, recursos, n_procesador):
		self.procesadores[n_procesador-1].agregar_proceso(nombre, tiempo, self, recursos)
		

	def agregar_recurso(self, nombre):
		self.recursos[nombre] = Recurso(nombre)

	def solicitar_recurso(self, nombre, proceso):		
		
		if nombre not in self.recursos:
			return

		recurso = self.recursos[nombre]
		disponible = False

		if recurso.estado == R_NO_USADO:
			
			recurso.asignar(proceso)
			disponible = True

		return disponible

	def liberar_recurso(self, nombre):
		
		if nombre not in self.recursos:
			return

		recurso = self.recursos[nombre]

		if recurso:
			recurso.liberar()