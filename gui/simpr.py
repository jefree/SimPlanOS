from kivy.uix.label import Label

from simplanos import SimPlanOS
from simplanos import ProcesadorGUI
from tablas import TablaProcesosGUI
from popups import ProcesoPopup

from logica.sistema import SistemaPR

class SimPlanPR(SimPlanOS):

	def inicializar(self, n_procesadores):
		
		self.sistema = SistemaPR(n_procesadores)
		self.procesadores = [ProcesadorGUI(p) for p in self.sistema.procesadores]
		self.tabla_procesos = TablaProcesosPR(self.sistema.procesos)

		self.popup_proceso = PrioridadPopup(self.sistema)

class TablaProcesosPR(TablaProcesosGUI):

	def agregar(self, nombre):
		TablaProcesosGUI.agregar(self, nombre)

		proceso = self.procesos[nombre]

		caja = self.cajas[proceso.nombre]
		prioridad = Label(text=str(proceso.prioridad))

		caja.add_widget(prioridad)
		self.visores[proceso.nombre] = prioridad

	def actualizar(self):
		TablaProcesosGUI.actualizar(self)

		for proceso in self.procesos.values():

			visor = self.visores[proceso.nombre]
			visor.text = str(proceso.prioridad)

class PrioridadPopup(ProcesoPopup):

	def __init__(self, sistema):
		ProcesoPopup.__init__(self, sistema)

	def info_nuevo(self):
		prioridad = int(self.txt_prioridad.text)
		return {'prioridad':prioridad}

	def limpiar(self):
		ProcesoPopup.limpiar(self)
		self.txt_prioridad.text = ""
