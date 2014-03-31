from kivy.app import App

from simrr import SimPlanRR

class RRApp(App):

	def build(self):

		self.ejecutando = True

		gui = SimPlanRR()

		gui.sistema.agregar_proceso("Juego", 25, ["pantalla"], 1)
		#self.sistema.agregar_proceso("Video", 12, ["pantalla", "mouse"], 3)

		gui.sistema.agregar_recurso("pantalla")
		gui.sistema.agregar_recurso("teclado")
		gui.sistema.agregar_recurso("mouse")

		self.gui = gui
		return self.gui

	def actualizar(self):
		self.gui.actualizar()
	
	def on_stop(self):
		self.ejecutando = False