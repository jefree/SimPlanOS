from kivy.uix.label import Label

from simplanos import SimPlanOS
from simplanos import ProcesadorGUI
from tablas import TablaProcesosGUI
from popups import ProcesoPopup

from logica.sistema import SistemaRR

class SimPlanRR(SimPlanOS):

	def inicializar(self, n_procesadores):
		
		self.sistema = SistemaRR(n_procesadores)
		self.tabla_procesos = TablaProcesosRR(self.sistema.procesos)
		self.procesadores = [ProcesadorRR(p, self.tabla_procesos) for p in self.sistema.procesadores]

class ProcesadorRR(ProcesadorGUI):

	def __init__(self, procesador, tabla):
		ProcesadorGUI.__init__(self, procesador, tabla)

		self.visores['cuanto'] = self.ids.cuanto

	def actualizar_info_proceso(self, proceso):
		ProcesadorGUI.actualizar_info_proceso(self, proceso)

		self.visores['cuanto'].text = str(proceso.cuanto)


class TablaProcesosRR(TablaProcesosGUI):

	def agregar(self, nombre):
		TablaProcesosGUI.agregar(self, nombre)

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