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

	def agregar_recurso(self, recurso):

		btn = Button(text=recurso, size_hint_y=None, height=44)
		btn.bind(on_release=lambda btn: self.lista_recursos.select(btn.text))

		self.lista_recursos.add_widget(btn)

	def usar_recurso(self, btn, recurso):
		self.txt_recursos.text = self.txt_recursos.text + recurso + ", "

	def info_nuevo(self):
		return {}

	def limpiar(self):

		self.txt_nombre.text = ""
		self.txt_tiempo.text = ""
		self.txt_recursos.text = ""
		self.txt_procesador.text= ""

		self.dismiss()

	def agregar(self):

		nombre = self.txt_nombre.text
		tiempo = int(self.txt_tiempo.text)
		recursos = self.txt_recursos.text.replace(" ", "").split(",")
		
		if '' in recursos: 
			recursos.remove('')
		
		n_procesador = int(self.txt_procesador.text)

		self.sistema.agregar_proceso(nombre, tiempo, recursos, n_procesador, **self.info_nuevo())

		self.limpiar()
		

class RecursoPopup(Popup):
	
	def __init__(self, sistema):
		Popup.__init__(self)

		self.sistema = sistema

	def agregar(self):

		nombre = self.txt_nombre.text
		self.sistema.agregar_recurso(nombre)

		self.dismiss()

class DiagramaGantt(Popup):

	def __init__(self, procesador):
		Popup.__init__(self, size_hint=(1.0, 0.5), title='Gantt para %s' % procesador.nombre)

		self.procesador = procesador
		self.gantt = self.procesador.gantt

		self.contenedor = BoxLayout(orientation='vertical', size_hint_x=None)
		self.procesos = {}

		scroll = ScrollView() 
		scroll.add_widget(self.contenedor)

		self.add_widget(scroll)

	def agregar_proceso(self, proceso):

		fila = GridLayout(rows=1, size_hint_y=None, height=25)
		self.procesos[proceso] = fila
		fila.add_widget(Label(size_hint_x=None, width=100, text=proceso))

		for i in self.gantt[proceso][:-1]:
			fila.add_widget(Label(size_hint_x=None, width=25, text=i))

		self.contenedor.add_widget(fila)

	def actualizar(self):

		for nombre, info in self.gantt.iteritems():
			if nombre not in self.procesos:
				self.agregar_proceso(nombre)

			fila = self.procesos[nombre]

			if info[self.procesador.tiempo -1] == 'X':
				color = (0,1,0,1)
			
			elif info[self.procesador.tiempo -1] == 'S':
				color = (1,0,1,1)

			elif info[self.procesador.tiempo -1] == 'B':
				color = (1,0,0,1)

			elif info[self.procesador.tiempo -1] == 'L':
				color = (1,1,1,1)

			elif info[self.procesador.tiempo -1] == 'T':
				color = (1,1,0,1)

			fila.add_widget(Label(size_hint_x=None, width=25, text=info[self.procesador.tiempo -1], color=color))
