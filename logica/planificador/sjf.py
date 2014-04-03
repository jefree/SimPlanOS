from planificador import Planificador
from logica.proceso import Proceso
from logica.util import Cola

class SJF(Planificador):

	def agregar_proceso(self, nombre, tiempo, sistema, recursos, **kwargs):

		p = Proceso(nombre, tiempo, sistema, recursos)

		self.agregar_ordenado(p)
		self.vista.informar_entra_listo()

		return p

	def agregar_ordenado(self, proceso):

		cola = Cola()

		cola = Cola()
		p = self.listos.atender()

		while p:
			if proceso.tiempo < p.tiempo:
				break

			cola.insertar(p)
			p = self.listos.atender()

		cola.insertar(proceso)

		while p:
			cola.insertar(p)
			p = self.listos.atender()

		self.listos = cola




