from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import *

from gui.simrr import SimPlanRR
from gui.simpr import SimPlanPR

apps = []

class Manager(Accordion):

	def __init__(self):
		Accordion.__init__(self)

		self.item1 = AccordionItem(title="Primero")
		self.item2 = AccordionItem(title="Segundo")

		self.item1.add_widget(SimPlanRR())
		self.item2.add_widget(SimPlanRR())

		self.add_widget(self.item1)
		self.add_widget(self.item2)


class Screnear(ScreenManager):

	def __init__(self):
		ScreenManager.__init__(self)

		apps.append(SimPlanRR(name='RoundRobin', archivo='gui/kv/rr.kv'))
		Builder.unload_file('gui/kv/rr.kv')

		apps.append(SimPlanPR(name='Prioridad Apropiativa', archivo='gui/kv/pr.kv'))
		Builder.unload_file('gui/kv/pr.kv')

		for app in apps:
			self.add_widget(app)

runTouchApp(Screnear())
