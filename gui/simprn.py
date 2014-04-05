from simpr import SimPlanPR
from logica.sistema import SistemaPRN
from simpr import TablaProcesosPR
from simpr import PrioridadPopup

class SimPlanPRN(SimPlanPR):

	def inicializar(self, n_procesadores):

		self.sistema = SistemaPRN(n_procesadores)
		self.tabla_procesos = TablaProcesosPR(self.sistema.procesos)

		self.popup_proceso = PrioridadPopup(self.sistema)