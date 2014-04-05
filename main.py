import thread

from kivy.lang import Builder
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import *
from kivy.app import App

from gui.simrr import SimPlanRR
from gui.simpr import SimPlanPR
from gui.simprn import SimPlanPRN
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

		prn = SimPlanPRN(2, name='Prioridad No Apropiativa', archivo='gui/kv/pr.kv')
		Builder.unload_file('gui/kv/pr.kv')

		self.apps['RR'] = rr
		self.apps['PR'] = pr
		self.apps['SJF'] = sjf
		self.apps['SRJF'] = srjf
		self.apps['PRN'] = prn

		self.agregar_procesos_defecto()

		for app in self.apps.values():
			self.add_widget(app)

	def agregar_procesos_defecto(self):

		plan = self.apps['PRN']

		plan.sistema.agregar_proceso('Java', 7, ["pantalla"], 1, prioridad=2)
		plan.sistema.agregar_proceso('Firefox', 7, ["pantalla"], 1, prioridad=2)

		plan.sistema.agregar_recurso("pantalla")

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

