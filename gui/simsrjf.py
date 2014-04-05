from simplanos import SimPlanOS
from logica.sistema import SistemaSRJF

class SimPlanSRJF(SimPlanOS):

	def inicializar(self, n_procesadores):
		self.sistema = SistemaSRJF(n_procesadores)
		