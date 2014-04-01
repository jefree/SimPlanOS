from kivy.app import App

from simrr import SimPlanRR
from simpr import SimPlanPR

import simplanos

class SimApp(App):

	def __init__(self):
		App.__init__(self)

		self.ejecutando = True

	def actualizar(self):
		self.gui.actualizar()
	
	def on_stop(self):
		self.ejecutando = False

class RRApp(SimApp):

	def build(self):

		self.ejecutando = True

		gui = SimPlanRR()

		simplanos.TIEMPO_SLEEP = 1

		self.gui = gui
		return self.gui


class PRApp(SimApp):

	def build(self):

		gui = SimPlanPR()

		simplanos.TIEMPO_SLEEP = 1

		self.gui = gui
		return self.gui

	def actualizar(self):
		self.gui.actualizar()
	
	def on_stop(self):
		self.ejecutando = False