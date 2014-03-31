from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

class TablaProcesosGUI(BoxLayout):

	def __init__(self, procesos):
		BoxLayout.__init__(self)

		self.orientation = 'vertical'
		self.procesos = procesos

		self.tiempos = dict()
		self.cajas = dict()

		self.visores = dict()

	def agregar(self, nombre):

		proceso = self.procesos[nombre]

		caja = BoxLayout()

		nombre = Label(text=proceso.nombre)
		tiempo = Label(text=str(proceso.tiempo))

		caja.add_widget(nombre)
		caja.add_widget(tiempo)

		self.add_widget(caja)

		self.tiempos[proceso.nombre] = tiempo
		self.cajas[proceso.nombre] = caja

	def actualizar(self):

		for proceso in self.procesos.values():
			tiempo = self.tiempos[proceso.nombre]
			tiempo.text = str(proceso.tiempo)
			

class TablaRecursosGUI(BoxLayout):

	def __init__(self, recursos):
		BoxLayout.__init__(self)

		self.orientation = 'vertical'
		self.recursos = recursos
		self.visores = dict()

	def agregar(self, nombre):

		box = BoxLayout()

		bloqueado = CheckBox(active= False)
		bloqueado.bind(active= lambda inst, valor : self.recursos[nombre].bloquear(valor))
			
		usado = Label(text="-")

		box.add_widget(Label(text=nombre))
		box.add_widget(usado)
		box.add_widget(bloqueado)

		self.add_widget(box)
		self.visores[nombre] = usado

	def actualizar(self):

		for recurso in self.recursos.values():

			visor = self.visores[recurso.nombre]

			if recurso.proceso:
				visor.text = recurso.proceso.nombre
			else:
				visor.text = '-'

		