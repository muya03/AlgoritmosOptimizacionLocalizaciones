import csv
import random
from time import time

def elimina_comas(ListaTrimeada):

	nueva = []
	for dato in ListaTrimeada:
		if dato != ",":
			nueva.append(int(dato))
	return nueva

tINI = time()

for i in range(1):
	numCont = 0
	free_loc_param = 0
	numLocTotales = 0
	posIO_Tierra = []
	posIO_Mar = []
	listaContenedores = []
	listaLocalizaciones = []
	solucionAlgoritmo = []
	tTotal_Localizacion = 0

	with open("") as datos:

		for linea in datos:
			
			if linea.startswith("number of containers"):
			
				instanciaNumCont = next(datos).strip()
				instanciaNumCont = instanciaNumCont.replace("\t",",")
				numCont = instanciaNumCont

			if linea.startswith("Free Locations Parameter"):
				
				instanciaFL = next(datos).strip()
				instanciaFL = instanciaFL.replace("\t",",")
				free_loc_param = instanciaFL

			if linea.startswith("Crane"):

				isntanciaPosGrua = next(datos).strip()
				isntanciaPosGrua = isntanciaPosGrua.replace("\t",",")
				isntanciaPosGrua = list(isntanciaPosGrua)
				isntanciaPosGrua = elimina_comas(isntanciaPosGrua)
				posGrua = isntanciaPosGrua
				pass   

			if linea.startswith("I/0 Land"):

				instanciaIO_tierra = next(datos)
				instanciaIO_tierra = next(datos).strip()
				instanciaIO_tierra = instanciaIO_tierra.replace("\t",",")
				instanciaIO_tierra = list(map(int,instanciaIO_tierra.split(",")))
				posIO_Tierra = instanciaIO_tierra
				pass

			if linea.startswith("I/O Sea"):

				instanciaIO_mar = next(datos)
				instanciaIO_mar = next(datos).strip()
				instanciaIO_mar = instanciaIO_mar.replace("\t",",")
				instanciaIO_mar = list(map(int,instanciaIO_mar.split(",")))
				posIO_Mar = instanciaIO_mar
				pass

			if linea.startswith("#Type"):

				for veces in range(int(numCont)):

					instanciaCont = next(datos).strip()
					instanciaCont = instanciaCont.replace("\t",",")
					instanciaCont = list(map(int, instanciaCont.split(",")))
					listaContenedores.append(instanciaCont)
					pass 
				pass

			if linea.startswith("Free Locations:"):

				instanciaLoc = next(datos)
				numLocTotales = int(numCont)*int(free_loc_param)

				for veces in range(numLocTotales):

					instanciaLoc = next(datos).strip()
					instanciaLoc = instanciaLoc.replace("\t",",")
					instanciaLoc = list(map(int,instanciaLoc.split(",")))
					listaLocalizaciones.append(instanciaLoc)
					listaLocalizaciones[veces].append(0)
					pass

				pass

			pass

	Max_IT = 1;		
			
	def seleccionarRj(elem):
		return elem[1]

	def calculoTij(contenedor,locT):
			
		fase1 = 0
		fase2 = 0
		fase3 = 0
		fase4 = 0
		nuevaPosGrua = 0

		if contenedor[0] == 1:
			fase1 = abs(posGrua[2]-posIO_Mar[2]) + abs(posGrua[2]-posIO_Mar[2]) 
			pass
		else:
			fase1 = abs(posGrua[1]-posIO_Tierra[1]) + abs(posGrua [2]-posIO_Tierra[2]) + abs(posGrua [2]-posIO_Tierra [2])
		
		if contenedor[0] == 1:
			fase2 = max(abs(posGrua [0] - locT [0]) ,abs(posGrua [1] - locT [1]) )
			pass
		else:
			nuevaPosGrua = [5,43,5]
			fase2 = max(abs(nuevaPosGrua [0] - locT [0]) ,abs(nuevaPosGrua [1] - locT [1]))

		fase3 = abs(posGrua[2]-locT[2]) + abs(posGrua[2]-locT[2])
		fase4 = max(abs(locT [0] - posIO_Mar [0]) ,abs(locT [1] - posIO_Mar [1]) )

		return fase1 + fase2 + fase3 + fase4
		pass

	tiempo_inicial = time()

	listaContenedores.sort(key=seleccionarRj)
	listaContOrndenada = listaContenedores

	for contenedor in listaContOrdenada:
		if tTotal_Localizacion < contenedor[1]:
			tTotal_Localizacion = contenedor[1]-tTotal_Localizacion
			pass
		listaLocalizaciones = listaLocalizaciones
		locAsignada = 0
		localizacionAleatoria = random.choice(listaLocalizaciones)

		while localizaciónAleatoria[3] != 0:

			localizacionAleatoria = random.choice(listaLocalizaciones)
		else:
			tTotal_Localizacion = tTotal_Localizacion + calculoTij(contenedor, localizacionAleatoria)
			solucionAlgoritmo.append([contenedor,localizacionAleatoria,tTotal_Localizacion])
			localizacionAleatoria[3] = 1
			locAsignada = 1

		pass

	print(solucionAlgoritmo)

	tLocal = 0
	tOptimo = 0
	for k in range(Max_IT):
		for contenedor in listaContOrdenada:
			indice = listaContenedores.index(contenedor)

			tOptimo = solucionAlgoritmo[indice][2]
			print("Esto es el tOptimo del contenedor ", contenedor, ": ", tOptimo)

			localizacionAleatoria = random.choice(listaLocalizaciones)
			locAsingada = 0

			while localizaciónAleatoria[3] != 0:

				localizacionAleatoria = random.choice(listaLocalizaciones)

			else: 
				tLocal = calculoTij(contenedor, localizacionAleatoria)

				if tLocal <= tOptimo:

					solucionAlgoritmo[indice] = [contenedor,localizacionAleatoria,tLocal]

					print("Solución del algritmo actualizada: ", solucionAlgoritmo)
					localizacionAleatoria[3] = 1
					pass
				locAsignada = 1
				pass
			pass

	tiempoTotal_interactivo = 0
	
	for lista in solucionAlgoritmo:
		
		tiempoTotal_interactivo = tiempoTotal_interactivo + solucionAlgoritmo[solucionAlgoritmo.index(lista)][2]
		pass

	# print ( posGrua [:])
	# print ( posIO_Tierra )
	# print ( listaContOrdenada )
	# print (" Tiempo de llegada : " , int( listaContenedores [3][1]) )
	# print ( calculoTij ( listaContOrdenada [0] , listaLocalizaciones [0]) )
	# print ("\nLocalizacion aleatoria : " , random . choice ( listaLocalizaciones ),"\n")

	tiempo_final = time()
	tiempo_total = float(tiempo_final) - float(tiempo_inicial)

	# print ("\nEl tiempo de ejecucion del algoritmo ha sido de " ,tiempo_inicial )
	# print ("\nEl tiempo de ejecucion del algoritmo ha sido de " , tiempo_final)
	# print ("\nEl tiempo de ejecucion del algoritmo ha sido de " , tiempo_total)

pass

tFIN = time()

t_X_iteraciones = tFIN - tINI

archivoEscritura = open("","a")
archivoEscritura.write(str(tiempoTotal_interactivo)+ "\t" + str(t_X_iteraciones ) )
archivoEscritura . write ("\n")

archivoEscritura.close() 