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

	def agregar(self):
		ProcesoPopup.agregar(self)

		nombre = self.txt_nombre.text
		tiempo = int(self.txt_tiempo.text)
		recursos = self.txt_recursos.text.replace(" ", "").split(",")
		prioridad = int(self.txt_prioridad.text)
		
		if '' in recursos: 
			recursos.remove('')
		
		n_procesador = int(self.txt_procesador.text)

		self.sistema.agregar_proceso(nombre, tiempo, recursos, n_procesador, prioridad=prioridad)

		self.prioridad.text = ""