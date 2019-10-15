"""
	Dado un conjunto de palabras, filtrar todas aquellas que sean palindromas
	def palabra_palindroma(x):
	palindromo = join(reversed(x))
	if x == palindromo:
		return True
	else:
		return False
"""

palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

#usamos una funcion anonima que permita revertir las palabras y compararlas
resultado = filter(lambda a: a == "".join(reversed(a)), palabras)
print(list(resultado))