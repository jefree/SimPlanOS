import thread

from kivy.lang import Builder
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import *
from kivy.app import App

from gui.simrr import SimPlanRR
from gui.simpr import SimPlanPR
from gui.simsjf import SimPlanSJF
from gui.simsrjf import SimPlanSRJF

def ejecutar():

	for app in apps:
		app.actualizar()

class Screnear(ScreenManager):

	def __init__(self):
		ScreenManager.__init__(self)

		self.apps = []

		rr = SimPlanRR(3, name='RoundRobin', archivo='gui/kv/rr.kv')
		Builder.unload_file('gui/kv/rr.kv')

		pr = SimPlanPR(1, name='Prioridad Apropiativa', archivo='gui/kv/pr.kv')
		Builder.unload_file('gui/kv/pr.kv')

		sjf = SimPlanSJF(2, name='Short Job First', archivo='gui/kv/sjf.kv')
		Builder.unload_file('gui/kv/sjf.kv')

		srjf = SimPlanSRJF(5, name='Short Remainnig Job First', archivo='gui/kv/sjf.kv')
		Builder.unload_file('gui/kv/sjf.kv')

		self.apps.append(rr)
		self.apps.append(pr)
		self.apps.append(sjf)
		self.apps.append(srjf)

		srjf.sistema.agregar_proceso("Java", 10, [],1)
		srjf.sistema.agregar_proceso("Word", 8, [], 1)

		srjf.sistema.agregar_proceso("Geany", 5, [], 1)
		srjf.sistema.agregar_proceso("Excel", 12, [], 1)

		#srjf.sistema.agregar_recurso("pantalla")
		#srjf.sistema.agregar_recurso("mouse")

		for app in self.apps:
			self.add_widget(app)

class SimApp(App):

	def __init__(self):
		App.__init__(self)

		self.screaner = Screnear()
		self.ejecutando = True

		thread.start_new_thread(self.iniciar_sim, ())

	def build(self):
		return self.screaner

	def iniciar_sim(self):
		
		while self.ejecutando:
			for app in self.screaner.apps:
				app.actualizar()

	def on_stop(self):
		self.ejecutando = False

SimApp().run()

