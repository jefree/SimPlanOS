from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

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

		nombre = self.txt_nombre.text
		tiempo = int(self.txt_tiempo.text)
		recursos = self.txt_recursos.text.replace(" ", "").split(",")
		
		if '' in recursos: 
			recursos.remove('')
		
		n_procesador = int(self.txt_procesador.text)

		self.sistema.agregar_proceso(nombre, tiempo, recursos, n_procesador)

		self.dismiss()

class RecursoPopup(Popup):
	
	def __init__(self, sistema):
		Popup.__init__(self)

		self.sistema = sistema

	def agregar(self):

		nombre = self.txt_nombre.text
		self.sistema.agregar_recurso(nombre)

		self.dismiss()

