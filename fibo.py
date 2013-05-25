def fibo( n1, n2, l):
 if n2 <= l:
 	return str(n1) + "\n" + fibo( n2, n1 + n2, l )
 return str( n1 )