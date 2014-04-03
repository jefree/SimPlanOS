from simplanos import SimPlanOS
from simplanos import ProcesadorGUI
from tablas import TablaProcesosGUI
from popups import ProcesoPopup
from logica.sistema import SistemaSJF

class SimPlanSJF(SimPlanOS):

	def inicializar(self, n_procesadores):
		
		self.sistema = SistemaSJF(n_procesadores)
		self.procesadores = [ProcesadorGUI(p) for p in self.sistema.procesadores]
		self.tabla_procesos = TablaProcesosGUI(self.sistema.procesos)

		self.popup_proceso = ProcesoPopup(self.sistema)