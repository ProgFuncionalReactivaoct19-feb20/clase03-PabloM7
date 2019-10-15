"""
	Ejercicios de funciones de orden superior
	@pablom7
"""

def suma(a,b):
	return a+b
def producto(a,b):
	return a*b
def disparador(f,a,b):
	print(f(a,b))
disparador(suma, 1, 10)
disparador(producto, 3, 6)