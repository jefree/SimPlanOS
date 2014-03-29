
from logica.sistema import SistemaRR

def main():
	
	sistema = SistemaRR(2)

	sistema.agregar_proceso("test", 5, ["mouse", "pantalla"], 1)
	sistema.agregar_proceso("navegador", 5, ["pantalla", "teclado"], 1)

	sistema.agregar_proceso("editor", 5, ["teclado", "mouse"], 2)
	sistema.agregar_proceso("juego", 5, ["pantalla", "mouse", "teclado"], 2)

	sistema.agregar_recurso("pantalla")
	sistema.agregar_recurso("teclado")
	sistema.agregar_recurso("mouse")

	sistema.ejecutar()


if __name__ == '__main__':
	main()