from kivy.app import App

from simplanos import SimPlanOS
from logica.sistema import SistemaRR

N_PROCESADORES  = 3

class MyApp(App):

	def build(self):
		
		self.sistema = SistemaRR(N_PROCESADORES)

		self.ejecutando = True

		gui = SimPlanOS(self.sistema)

		self.sistema.agregar_proceso("Juego", 25, ["pantalla"], 1)
		#self.sistema.agregar_proceso("Video", 12, ["pantalla", "mouse"], 3)

		self.sistema.agregar_recurso("pantalla")
		self.sistema.agregar_recurso("teclado")
		self.sistema.agregar_recurso("mouse")

		self.gui = gui
		return self.gui

	def actualizar(self):
		self.gui.actualizar()
	
	def on_stop(self):
		self.ejecutando = False