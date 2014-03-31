import math

def main():

	procesos = {'test':1,}

	tiempos = procesos.values()

	suma = sum(tiempos)
	n = len(procesos)
	
	medio = 1.0 * suma / n

	print "medio:", int(medio)

	for p, t in procesos.iteritems():

		dist = t - medio
		cuanto = medio

		if dist > 0:

			if dist > medio * 0.5:
				cuanto = medio * 1.3
		else:

			if dist < medio*-0.5:
				cuanto = t
			else:
				cuanto = t*0.8

		cuanto = int(round(cuanto))

		print cuanto, "para", t

main()