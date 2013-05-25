#!usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ejercicio 5.1 Facturar el uso del un telefono dando la tarifa por segundo y
la duración de cada comunicación expresada en horas, minutos y segundos. 
Dando como resultado la duración en segundos de cada comunicación y su costo.
Resolver usando: 
1.Ciclo definido
2.Ciclo interactivo
3.Ciclo centinela
4.Ciclo "infinito" que se rompe"
'''

#Ciclo Centinela
def tarifa():
	opcion = raw_input("Ingrese 'si' para empezar o 'x' para terminar: ")
	while opcion<>'x':
		comunicacion = input("¿Cuántas comunicaciones son?: ")
		print "-"*20
		for x in range(comunicacion):
			#------- pedimos datos ---------	
			precioseg = input("¿Cuál es la tarifa por segundo?: ")
			horas = input("¿Cuántas horas?: ")
			minutos = input("¿Cuántos minutos?: ")
			segundos = input("¿Cuántos segundos?: ")
			#----- hacemos los calculos -----
			total_tiempo = asegundos(horas, minutos, segundos)
			total_costo = total_tiempo * precioseg
			#--------- imprimimos -----------
			print "La comunicación dura:",total_tiempo, "segundos."
			print "El precio total es de:", int(total_costo),"pesos con", acentavos(total_costo), "centavos."
			print "-"*20

		opcion = raw_input("Ingrese (si) para seguir o 'x' para terminar: ")	

def asegundos (hors, mins, segs) :
	segsal = 3600*hors + 60*mins + segs
	return segsal

def acentavos(cost) :
	centavos = int(round((cost%1)*100))
	return centavos

tarifa()