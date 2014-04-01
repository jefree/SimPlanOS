
import gui
from gui import *

import thread
from time import sleep

app = RRApp()

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