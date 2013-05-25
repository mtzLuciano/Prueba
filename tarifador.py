#!usr/bin/env python
# -*- coding: utf-8 -*-
def main () :
	"""El usuario ingresa la tarifa por segundo, cuántas
	comunicaciones se realizaron, y la duración de cada
	comunicación expresada en horas, minutos y segundos.
	Como resultado se informa la duración en segundos de
	cada comunicación y su costo."""
	
	f = input("¿Cuánto cuesta 1 segundo de comunicación?: ")
	n = input("¿Cuántas comunicaciones hubo?: ")
	costo_total = 0
	for x in range(n):
		hs = input("¿Cuántas horas?: ")
		min = input("¿Cuántos minutos?: ")
		seg = input("¿Cuántos segundos?: ")
		segcalc = asegundos(hs, min, seg)
		costo = segcalc*f
		costo_total = costo_total + costo
		print "Duración: ", segcalc, "Segundos. Costo:", int(costo), "pesos y", acentavos(costo), "centavos."
	print "Total a facturar:", int(costo_total), "pesos y ", acentavos(costo_total), "centavos."
	
def asegundos (horas, minutos, segundos) :
	segsal = 3600*horas + 60*minutos + segundos
	return segsal

def acentavos(cost) :
	centavos = round((cost%1)*100)
	return centavos

main ()