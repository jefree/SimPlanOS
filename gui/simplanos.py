from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from time import sleep

from tablas import *
from popups import *

TIEMPO_SLEEP = 1

class SimPlanOS(FloatLayout):
	
	def __init__(self, sistema):
		FloatLayout.__init__(self)

		self.sistema = sistema
		self.procesadores = [ProcesadorGUI(p) for p in sistema.procesadores]
		
		self.tabla_procesos = TablaProcesosRR(sistema.procesos)
		self.tabla_recursos = TablaRecursosGUI(sistema.recursos)

		self.ejecutando = False
		self.paso = False

		for p in self.procesadores:
			self.ids.procesadores.add_widget(p)

		self.c_procesos.add_widget(self.tabla_procesos)
		self.c_recursos.add_widget(self.tabla_recursos)

		self.sistema.asignar_vista(self)

	def actualizar(self):

		global TIEMPO_SLEEP

		if self.paso:
			self.ejecutando = True

		if not self.ejecutando:
			return

		self.sistema.ejecutar()

		for p in self.procesadores:
			p.actualizar()

		self.tabla_procesos.actualizar()
		self.tabla_recursos.actualizar()

		self.l_info.text = '-'

		sleep(TIEMPO_SLEEP*2)

		if self.paso:
			self.paso = False
			self.ejecutando = False
			TIEMPO_SLEEP = 1

	def iniciar(self):
		global TIEMPO_SLEEP

		TIEMPO_SLEEP = 1
		self.ejecutando = True

	def pausar(self):
		self.ejecutando = False

	def hacer_paso(self):
		self.paso = True

	def mostrar_popup_proceso(self):
		ProcesoPopup(self.sistema).open()

	def mostrar_popup_recurso(self):
		RecursoPopup(self.sistema).open()

	def informar_nuevo_proceso(self, nombre):
		self.tabla_procesos.agregar(nombre)

	def informar_nuevo_recurso(self, nombre):
		self.tabla_recursos.agregar(nombre)

	def informar_solicitud(self, proceso, recurso):
		self.l_info.text = "%s solicita %s" % (proceso, recurso)

		sleep(TIEMPO_SLEEP)

	def informar_liberacion(self, proceso, recurso):

		self.tabla_recursos.actualizar()
		self.l_info.text = "%s libera %s" % (proceso, recurso)

		sleep(TIEMPO_SLEEP)
		
class ProcesadorGUI(BoxLayout):
	
	def __init__(self, procesador):
		BoxLayout.__init__(self)

		self.procesador = procesador

		self.ids.id_procesador.text = self.procesador.nombre

		self.listos = ListaProcesosListos(self.ids.listos)
		self.suspendidos = ListaProcesosSuspendidos(self.ids.suspendidos)
		self.bloqueados = ListaProcesosBloqueados(self.ids.bloqueados)

		self.procesador.planificador.asignar_vista(self)

	def actualizar(self):

		proceso = self.procesador.proceso_asignado

		if proceso:
			self.ids.nombre.text = proceso.nombre
			self.ids.tiempo.text = str(proceso.tiempo)
			self.ids.cuanto.text = str(proceso.cuanto)

		self.ids.c_suspendido.text = str(self.procesador.planificador.contador_suspendido)

		self.ids.l_info.text = "-"

		self.listos.actualizar(self.procesador.planificador.listos)
		self.suspendidos.actualizar(self.procesador.planificador.suspendidos)
		self.bloqueados.actualizar(self.procesador.planificador.bloqueados)

	def informar_nuevo(self):

		global TIEMPO_SLEEP

		self.suspendidos.actualizar(self.procesador.planificador.suspendidos)
		
		proceso = self.procesador.proceso_asignado

		if proceso:
			self.ids.nombre.text = proceso.nombre
			self.ids.tiempo.text = str(proceso.tiempo)
			self.ids.cuanto.text = str(proceso.cuanto)
		else:
			self.limpiar_info_proceso()

	def informar_suspendido(self):

		if not self.procesador.proceso_asignado:
			self.limpiar_info_proceso()

		self.suspendidos.actualizar(self.procesador.planificador.suspendidos)

		sleep(TIEMPO_SLEEP)

	def informar_entra_listo(self):
		self.listos.actualizar(self.procesador.planificador.listos)
		self.suspendidos.actualizar(self.procesador.planificador.suspendidos)

		sleep(TIEMPO_SLEEP)

	def informar_bloqueado(self):

		nombre = self.procesador.proceso_asignado.nombre
		bloqueando = ', '.join(self.procesador.proceso_asignado.listar_recursos_bloqueando())

		self.ids.l_info.text = "proceso %s bloqueado por %s" % (nombre, bloqueando)

		self.limpiar_info_proceso()

		sleep(TIEMPO_SLEEP)

	def limpiar_info_proceso(self):
		self.ids.nombre.text = '-'
		self.ids.tiempo.text = '-'
		self.ids.cuanto.text = '-'

	def informar_desbloqueado(self, proceso):

		self.bloqueados.actualizar(self.procesador.planificador.bloqueados)
		self.suspendidos.actualizar(self.procesador.planificador.suspendidos)

		self.ids.l_info.text = "proceso %s desbloqueado" % proceso

		sleep(TIEMPO_SLEEP)

class ListaProcesos():

	def __init__(self, layout):
		self.layout = layout
		
	def actualizar(self):
		self.layout.clear_widgets()


class ListaProcesosListos(ListaProcesos):
		
	def actualizar(self, procesos):
		ListaProcesos.actualizar(self)
			
		for proceso in procesos.listar():
			self.layout.add_widget(Label(text=proceso.nombre))

class ListaProcesosSuspendidos(ListaProcesos):	

	def actualizar(self, procesos):
		ListaProcesos.actualizar(self)
			
		for proceso in procesos.listar():
			self.layout.add_widget(Label(text=proceso.nombre))

class ListaProcesosBloqueados(ListaProcesos):

	def actualizar(self, procesos):
		ListaProcesos.actualizar(self)
			
		for proceso in procesos.listar():

			bloqueando = ', '.join([r for r in proceso.listar_recursos_bloqueando()])

			self.layout.add_widget(Label(text=proceso.nombre + ": " + bloqueando ))
