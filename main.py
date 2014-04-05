import thread

from kivy.lang import Builder
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import *
from kivy.app import App

from gui.simrr import SimPlanRR
from gui.simpr import SimPlanPR
from gui.simsjf import SimPlanSJF
from gui.simsrjf import SimPlanSRJF

class Screnear(ScreenManager):

	def __init__(self):
		ScreenManager.__init__(self)

		self.apps = {}

		rr = SimPlanRR(3, name='RoundRobin', archivo='gui/kv/rr.kv')
		Builder.unload_file('gui/kv/rr.kv')

		pr = SimPlanPR(1, name='Prioridad Apropiativa', archivo='gui/kv/pr.kv')
		Builder.unload_file('gui/kv/pr.kv')

		sjf = SimPlanSJF(2, name='Short Job First', archivo='gui/kv/sjf.kv')
		Builder.unload_file('gui/kv/sjf.kv')

		srjf = SimPlanSRJF(5, name='Short Remainnig Job First', archivo='gui/kv/sjf.kv')
		Builder.unload_file('gui/kv/sjf.kv')

		self.apps['RR'] = rr
		self.apps['PR'] = pr
		self.apps['SJF'] = sjf
		self.apps['SJRJF'] = srjf

		self.agregar_procesos_defecto()

		for app in self.apps.values():
			self.add_widget(app)

	def agregar_procesos_defecto(self):

		rr = self.apps['RR']

		rr.sistema.agregar_proceso('Java', 10, [], 1)
		rr.sistema.agregar_proceso('Firefox', 5, [], 1)

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
			for app in self.screaner.apps.values():
				app.actualizar()

	def on_stop(self):
		self.ejecutando = False

SimApp().run()

