from simplanos import SimPlanOS
from logica.sistema import SistemaSJF

class SimPlanSJF(SimPlanOS):

	def inicializar(self, n_procesadores):
		self.sistema = SistemaSJF(n_procesadores)