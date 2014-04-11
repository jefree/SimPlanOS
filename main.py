from collections import OrderedDict
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

		self.apps = OrderedDict()

		rr = SimPlanRR(3, name='RoundRobin', archivo='gui/kv/rr.kv')
		Builder.unload_file('gui/kv/rr.kv')

		pr = SimPlanPR(3, name='Prioridad Apropiativa', archivo='gui/kv/pr.kv')
		Builder.unload_file('gui/kv/pr.kv')

		sjf = SimPlanSJF(3, name='Short Job First', archivo='gui/kv/sjf.kv')
		Builder.unload_file('gui/kv/sjf.kv')

		srjf = SimPlanSRJF(3, name='Short Remaining Job First', archivo='gui/kv/sjf.kv')
		Builder.unload_file('gui/kv/sjf.kv')

		prn = SimPlanPRN(3, name='Prioridad No Apropiativa', archivo='gui/kv/pr.kv')
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

		plan = self.apps['RR']

		plan.sistema.agregar_proceso('Java', 1, ["pantalla"], 1)
		plan.sistema.agregar_proceso('Firefox', 3, ["pantalla"], 1)
		plan.sistema.agregar_proceso('Word', 1, ["pantalla"], 1)
		
		plan.sistema.agregar_proceso('Excel', 3, ["pantalla"], 2)
		#plan.sistema.agregar_proceso('video', 3, ["mouse"], 2)

		plan.sistema.agregar_proceso('Eclipse', 2, ["pantalla"], 3)
		#plan.sistema.agregar_proceso('voz', 3, ["mouse"], 3)

		plan.sistema.agregar_recurso("pantalla")
		plan.sistema.agregar_recurso("teclado")
		plan.sistema.agregar_recurso("mouse")
		plan.sistema.agregar_recurso("impresora")

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

