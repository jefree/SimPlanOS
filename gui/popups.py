from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class ProcesoPopup(Popup):
	
	def __init__(self, sistema):
		Popup.__init__(self)

		self.sistema = sistema
		self.lista_recursos = DropDown()

		self.btn_lista.bind(on_release=self.lista_recursos.open)
		self.lista_recursos.bind(on_select=self.usar_recurso)

		for recurso in self.sistema.recursos:
			self.agregar_recurso(recurso)

	def agregar_recurso(self, recurso):

		btn = Button(text=recurso, size_hint_y=None, height=44)
		btn.bind(on_release=lambda btn: self.lista_recursos.select(btn.text))

		self.lista_recursos.add_widget(btn)

	def usar_recurso(self, btn, recurso):
		self.txt_recursos.text = self.txt_recursos.text + recurso + ", "

	def agregar(self):
		self.dismiss()

class RecursoPopup(Popup):
	
	def __init__(self, sistema):
		Popup.__init__(self)

		self.sistema = sistema

	def agregar(self):

		nombre = self.txt_nombre.text
		self.sistema.agregar_recurso(nombre)

		self.dismiss()

class DiagramaGantt(Popup):

	def __init__(self, gantt, nombre):
		Popup.__init__(self, size_hint=(1.0, 0.5), title='Gantt para %s' % nombre)

		self.gantt = gantt
		self.tiempo = 0

		self.contenedor = BoxLayout(orientation='vertical', size_hint_x=None)
		self.procesos = {}

		scroll = ScrollView() 
		scroll.add_widget(self.contenedor)

		self.add_widget(scroll)

	def agregar_proceso(self, proceso):

		fila = GridLayout(rows=1, size_hint_y=None, height=25)
		self.procesos[proceso] = fila
		fila.add_widget(Label(size_hint_x=None, width=100, text=proceso))

		if self.tiempo > 0:
			for i in range(self.tiempo):
				fila.add_widget(Label(size_hint_x=None, width=25, text='-'))

		self.contenedor.add_widget(fila)

	def actualizar(self):
		
		for nombre, info in self.gantt.iteritems():
			if nombre not in self.procesos:
				self.agregar_proceso(nombre)

			fila = self.procesos[nombre]

			if info[self.tiempo] == 'X':
				color = (0,1,0,1)
			else:
				color = (1,0,1,1)

			fila.add_widget(Label(size_hint_x=None, width=25, text=info[self.tiempo], color=color))

		self.tiempo += 1

