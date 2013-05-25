#!usr/bin/env python
"""Un programa sencillo, para calcular cuadrados de numeros"""
def main ():
	print 'Se calcularan los cuadrados de numeros'
	
	n1= input('Ingrese un numero entero: ')
	n2= input('Ingrese otro numero entero: ')
	
	for x in range(n1, n2):
		print x*x
	
	print 'esto es todo por ahora'
	print 'Este es otro cambio para el primer commit'
	
main ()
