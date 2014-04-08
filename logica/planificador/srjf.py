from sjf import SJF
from logica.util import Cola

class SRJF(SJF):

	def plan_listo(self, proceso_actual):
		return True