"""
	Ejercicios de funciones de orden superior
	@pablom7
"""
# Aplicacion de funcion filter

def es_vocal(x):
	vocales = ["a", "e", "i", "o", "u"]
	if x in vocales:
		return True
	else:
		return False

datos = ["e", "c", "u", "a", "d", "o", "r"]

resultado = filter(es_vocal, datos)
print(resultado)
print(list(resultado))