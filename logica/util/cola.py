class Nodo():

	def __init__(self, _valor):
		self.valor = _valor
		self.sig = None
	
class Cola():
	
	def __init__(self):

		self.cabeza = None
		self.prox = None

	def atender(self):

		valor = None

		if self.cabeza: 

			valor = self.cabeza.valor
			self.cabeza = self.cabeza.sig

		return valor

	def insertar(self, nuevo):

		if (self.cabeza):
			aux = self.cabeza

			while aux.sig:
				aux = aux.sig

			aux.sig = Nodo(nuevo)

		else:
			self.cabeza = Nodo(nuevo)
			self.prox = self.cabeza

	def proximo(self, begin=False):

		valor = None

		if (begin):
			self.prox = self.cabeza

		if (self.prox):

			valor = self.prox.valor
			self.prox = self.prox.sig

		return valor

	def vacia(self):
		return self.cabeza == None

	def listar(self):

		lista = []
		aux = self.cabeza

		while aux:

			lista.append(aux.valor)
			aux = aux.sig

		return lista
