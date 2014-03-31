
import gui
from gui import MyApp

import thread
from time import sleep

app = MyApp()

def ejecutar():

	while not hasattr(app, 'gui'):
		pass

	while app.ejecutando:
		app.actualizar()

def main():

	thread.start_new_thread(ejecutar, ())

	app.run()
		
if __name__ == '__main__':
	main()