
from logica.sistema import SistemaRR

def main():
	
	sistema = SistemaRR(1)

	sistema.agregar_proceso("test", 5, ["pantalla"], 1)
	sistema.agregar_proceso("juego", 10, ["pantalla"], 1)

	sistema.agregar_recurso("pantalla")
	sistema.agregar_recurso("teclado")
	sistema.agregar_recurso("mouse")

	sistema.ejecutar()


if __name__ == '__main__':
	main()