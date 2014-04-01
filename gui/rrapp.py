from kivy.app import App

from simrr import SimPlanRR
import simplanos

class RRApp(App):

	def build(self):

		self.ejecutando = True

		gui = SimPlanRR()

		gui.sistema.agregar_proceso("Juego", 25, ["pantalla"], 1)
		gui.sistema.agregar_proceso("Java", 25, ["pantalla"], 1)
		gui.sistema.agregar_proceso("System", 25, ["pantalla"], 1)
		gui.sistema.agregar_proceso("Dota", 25, ["pantalla"], 1)
		gui.sistema.agregar_proceso("LoL", 25, ["pantalla"], 1)

		gui.sistema.agregar_proceso("Firefox", 25, ["pantalla"], 2)
		gui.sistema.agregar_proceso("Word", 25, ["pantalla"], 2)

		gui.sistema.agregar_proceso("Excel", 25, ["pantalla"], 3)
		gui.sistema.agregar_proceso("GIMP", 25, ["pantalla"], 3)

		gui.sistema.agregar_recurso("pantalla")
		gui.sistema.agregar_recurso("teclado")
		gui.sistema.agregar_recurso("mouse")

		simplanos.TIEMPO_SLEEP = 1

		self.gui = gui
		return self.gui

	def actualizar(self):
		self.gui.actualizar()
	
	def on_stop(self):
		self.ejecutando = False