from kivy.uix.label import Label

from simplanos import SimPlanOS
from simplanos import ProcesadorGUI
from tablas import TablaProcesosGUI

from logica.sistema import SistemaRR

class SimPlanRR(SimPlanOS):

	def inicializar(self):
		
		self.sistema = SistemaRR(3)
		self.procesadores = [ProcesadorRR(p) for p in self.sistema.procesadores]
		self.tabla_procesos = TablaProcesosRR(self.sistema.procesos)


class ProcesadorRR(ProcesadorGUI):

	def __init__(self, procesador):
		ProcesadorGUI.__init__(self, procesador)

		self.visores['cuanto'] = self.ids.cuanto

	def actualizar_info_proceso(self, proceso):
		ProcesadorGUI.actualizar_info_proceso(self, proceso)

		self.visores['cuanto'].text = str(proceso.cuanto)


class TablaProcesosRR(TablaProcesosGUI):

	def agregar(self, nombre):
		TablaProcesosGUI.agregar(self, nombre)

		print "procesos hijo",self.procesos

		proceso = self.procesos[nombre]

		caja = self.cajas[proceso.nombre]
		cuanto = Label(text=str(proceso.cuanto))

		caja.add_widget(cuanto)
		self.visores[proceso.nombre] = cuanto

	def actualizar(self):
		TablaProcesosGUI.actualizar(self)

		for proceso in self.procesos.values():

			visor = self.visores[proceso.nombre]
			visor.text = str(proceso.cuanto)